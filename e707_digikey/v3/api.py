import os
import logging
from distutils.util import strtobool
import e707_digikey.oauth.oauth2
import e707_digikey.configfile
from e707_digikey.exceptions import DigikeyError
from e707_digikey.v3.productinformation import (KeywordSearchRequest, KeywordSearchResponse, ProductDetails, DigiReelPricing,
                                           ManufacturerProductDetailsRequest)
from e707_digikey.v3.productinformation.rest import ApiException
from e707_digikey.v3.ordersupport import (OrderStatusResponse, SalesOrderHistoryItem)
from e707_digikey.v3.batchproductdetails import (BatchProductDetailsRequest, BatchProductDetailsResponse)
from e707_digikey.v3.barcode import (Product2DBarcodeResponse)

logger = logging.getLogger(__name__)


class DigikeyAPI:
    class DigikeyApiWrapper(object):
        apinames = {
            e707_digikey.v3.productinformation: 'Search',
            e707_digikey.v3.ordersupport: 'OrderDetails',
            e707_digikey.v3.batchproductdetails: 'BatchSearch',
            e707_digikey.v3.barcode: 'Barcoding'
        }

        apiclasses = {
            e707_digikey.v3.productinformation: e707_digikey.v3.productinformation.PartSearchApi,
            e707_digikey.v3.ordersupport: e707_digikey.v3.ordersupport.OrderDetailsApi,
            e707_digikey.v3.batchproductdetails: e707_digikey.v3.batchproductdetails.BatchSearchApi,
            e707_digikey.v3.barcode: e707_digikey.v3.barcode.BarcodingApi,
        }

        def __init__(self, config_file: e707_digikey.configfile.DigikeyBaseConfig, is_sandbox: bool = False):
            self.sandbox = is_sandbox
            self.apiname = None
            self._api_instance = None
            self.wrapped_function = None
            self.x_digikey_client_id = None
            self.config = config_file

            # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            # configuration.api_key_prefix['X-DIGIKEY-Client-Id'] = 'Bearer'

            self._digikeyApiToken = None
            self.authorization = None

        def get_authorization(self):
            """
                Function that get Oauth2 authorization. This is not implement in __init__ to give the user
                a chance to set the client secret and client id if it's not in the config file already
            """
            # Configure OAuth2 access token for authorization: oauth2AccessCodeSecurity
            self._digikeyApiToken = digikey.oauth.oauth2.TokenHandler(self.config, version=3, sandbox=self.sandbox).get_access_token()

            # Populate reused ids
            self.authorization = self._digikeyApiToken.get_authorization()

        def change_api(self, wrapped_function, module):
            apiname = self.apinames[module]
            apiclass = self.apiclasses[module]
            # Only change the API when it's different than the current API
            if self.apiname != apiname:

                if self.config.get('client-id') is None or self.config.get('client-secret') is None:
                    raise DigikeyError('Please provide a valid DIGIKEY_CLIENT_ID and DIGIKEY_CLIENT_SECRET in your env setup')

                if self._digikeyApiToken is None:
                    self.get_authorization()

                self.apiname = apiname
                self.x_digikey_client_id = self.config.get('client-id')

                # Configure API key authorization: apiKeySecurity
                configuration = module.Configuration()
                configuration.api_key['X-DIGIKEY-Client-Id'] = self.config.get('client-id')

                # Use normal API by default, if DIGIKEY_CLIENT_SANDBOX is True use sandbox API
                configuration.host = 'https://api.digikey.com/' + apiname + '/v3'
                try:
                    if self.sandbox:
                        configuration.host = 'https://sandbox-api.digikey.com/' + apiname + '/v3'
                except (ValueError, AttributeError):
                    pass

                configuration.access_token = self._digikeyApiToken.access_token

                # create an instance of the API class
                self._api_instance = apiclass(module.ApiClient(configuration))
            self.wrapped_function = wrapped_function

        @staticmethod
        def _remaining_requests(header, api_limits):
            try:
                rate_limit = header['X-RateLimit-Limit']
                rate_limit_rem = header['X-RateLimit-Remaining']

                if api_limits is not None and type(api_limits) == dict:
                    api_limits['api_requests_limit'] = int(rate_limit)
                    api_limits['api_requests_remaining'] = int(rate_limit_rem)

                logger.debug('Requests remaining: [{}/{}]'.format(rate_limit_rem, rate_limit))
            except (KeyError, ValueError) as e:
                logger.debug(f'No api limits returned -> {e.__class__.__name__}: {e}')
                if api_limits is not None and type(api_limits) == dict:
                    api_limits['api_requests_limit'] = None
                    api_limits['api_requests_remaining'] = None

        @staticmethod
        def _store_api_statuscode(statuscode, status):
            if status is not None and type(status) == dict:
                status['code'] = int(statuscode)
            logger.debug('API returned code: {}'.format(statuscode))
        def call_api_function(self, *args, **kwargs):
            try:
                # If optional api_limits, status mutable object is passed use it to store API limits and status code
                api_limits = kwargs.pop('api_limits', None)
                status = kwargs.pop('status', None)

                func = getattr(self._api_instance, self.wrapped_function)
                logger.debug(f'CALL wrapped -> {func.__qualname__}')
                api_response = func(*args, self.authorization, self.x_digikey_client_id, **kwargs)
                self._remaining_requests(api_response[2], api_limits)
                self._store_api_statuscode(api_response[1], status)

                return api_response[0]
            except ApiException as e:
                logger.error(f'Exception when calling {self.wrapped_function}: {e}')
                self._store_api_statuscode(e.status, status)

    def __init__(self, config_constructor: e707_digikey.configfile.DigikeyBaseConfig, is_sandbox: bool = False):
        self.config = config_constructor
        self.client = self.DigikeyApiWrapper(self.config, is_sandbox)

    def needs_client_id(self) -> bool:
        if self.config.get('client-id') is None:
            return True
        return False

    def needs_client_secret(self) -> bool:
        if self.config.get('client-secret') is None:
            return True
        return False

    def set_client_info(self, client_id=None, client_secret=None):
        if client_id is not None:
            self.config.set('client-id', client_id)
        if client_secret is not None:
            self.config.set('client-secret', client_secret)
        self.config.save()

    def keyword_search(self, *args, **kwargs) -> KeywordSearchResponse:
        self.client.change_api('keyword_search_with_http_info', e707_digikey.v3.productinformation)

        if 'body' in kwargs and type(kwargs['body']) == KeywordSearchRequest:
            logger.info(f'Search for: {kwargs["body"].keywords}')
            logger.debug('CALL -> keyword_search')
            return self.client.call_api_function(*args, **kwargs)
        else:
            raise DigikeyError('Please provide a valid KeywordSearchRequest argument')

    def product_details(self, *args, **kwargs) -> ProductDetails:
        self.client.change_api('product_details_with_http_info', e707_digikey.v3.productinformation)

        if len(args):
            logger.info(f'Get product details for: {args[0]}')
            return self.client.call_api_function(*args, **kwargs)

    def digi_reel_pricing(self, *args, **kwargs) -> DigiReelPricing:
        self.client.change_api('digi_reel_pricing_with_http_info', e707_digikey.v3.productinformation)

        if len(args):
            logger.info(f'Calculate the DigiReel pricing for {args[0]} with quantity {args[1]}')
            return self.client.call_api_function(*args, **kwargs)

    def suggested_parts(self, *args, **kwargs) -> ProductDetails:
        self.client.change_api('suggested_parts_with_http_info', e707_digikey.v3.productinformation)

        if len(args):
            logger.info(f'Retrieve detailed product information and two suggested products for: {args[0]}')
            return self.client.call_api_function(*args, **kwargs)

    def manufacturer_product_details(self, *args, **kwargs) -> KeywordSearchResponse:
        self.client.change_api('manufacturer_product_details_with_http_info', e707_digikey.v3.productinformation)

        if 'body' in kwargs and type(kwargs['body']) == ManufacturerProductDetailsRequest:
            logger.info(f'Search for: {kwargs["body"].manufacturer_product}')
            return self.client.call_api_function(*args, **kwargs)
        else:
            raise DigikeyError('Please provide a valid ManufacturerProductDetailsRequest argument')

    def status_salesorder_id(self, *args, **kwargs) -> OrderStatusResponse:
        self.client.change_api('status_salesorder_id_get_with_http_info', e707_digikey.v3.ordersupport)

        if len(args):
            logger.info(f'Get order details for: {args[0]}')
            return self.client.call_api_function(*args, **kwargs)

    def salesorder_history(self, *args, **kwargs) -> [SalesOrderHistoryItem]:
        self.client.change_api('history_get_with_http_info', e707_digikey.v3.ordersupport)

        if 'start_date' in kwargs and type(kwargs['start_date']) == str \
                and 'end_date' in kwargs and type(kwargs['end_date']) == str:
            logger.info(f'Searching for orders in date range ' + kwargs['start_date'] + ' to ' + kwargs['end_date'])
            return self.client.call_api_function(*args, **kwargs)
        else:
            raise DigikeyError('Please provide valid start_date and end_date strings')

    def batch_product_details(self, *args, **kwargs) -> BatchProductDetailsResponse:
        self.client.change_api('batch_product_details_with_http_info', e707_digikey.v3.batchproductdetails)

        if 'body' in kwargs and type(kwargs['body']) == BatchProductDetailsRequest:
            logger.info(f'Batch product search: {kwargs["body"].products}')
            logger.debug('CALL -> batch_product_details')
            return self.client.call_api_function(*args, **kwargs)
        else:
            raise DigikeyError('Please provide a valid BatchProductDetailsRequest argument')

    def barcode_2d(self, *args, **kwargs) -> Product2DBarcodeResponse:
        self.client.change_api('product2_d_barcode_with_http_info', e707_digikey.v3.barcode)

        if len(args):
            logger.info(f'Get barcode details for: {args[0].encode("utf-8")}')
            # Barcode encoding, converting ASCII characters to Unicode as per the API's request
            args = list(args)
            args[0] = args[0].encode("utf-8")
            args[0] = args[0].replace(u"\u001E".encode('utf-8'), u"\u241E".encode('utf-8'))
            args[0] = args[0].replace(u"\u001D".encode('utf-8'), u"\u241D".encode('utf-8'))
            args[0] = args[0].decode("utf-8")
            args = tuple(args)
            print(args[0])
            return self.client.call_api_function(*args, **kwargs)
