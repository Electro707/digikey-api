# coding: utf-8

"""
    Barcoding

    Retrieve package information from the barcode.  # noqa: E501

    OpenAPI spec version: v3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from e707_digikey.v3.barcode.api_client import ApiClient


class BarcodingApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def pack_list2_d_barcode(self, barcode, authorization, x_digikey_client_id, **kwargs):  # noqa: E501
        """Converts a pack list 2D barcode to information about the order. The barcode this takes in is a two-dimensional  barcode located in the upper right corner of the pack list. This is not for individual line item barcodes. The 2D  barcode contains special symbols. These MUST be URL encoded to be sent through the API.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pack_list2_d_barcode(barcode, authorization, x_digikey_client_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str barcode: Pack list barcode located on the pack list in the upper right corner. (required)
        :param str authorization: OAuth Bearer Token. Please see<a href= \"https://developer.digikey.com/documentation/oauth\" target= \"_blank\" > OAuth 2.0 Documentation </a > page for more info. (required)
        :param str x_digikey_client_id: The Client Id for your App. (required)
        :param str includes: Comma separated list of fields to return. Used to customize response to reduce bandwidth by  selecting fields that you wish to receive. For example: \"Salesorder\"
        :return: PackListBarcodeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.pack_list2_d_barcode_with_http_info(barcode, authorization, x_digikey_client_id, **kwargs)  # noqa: E501
        else:
            (data) = self.pack_list2_d_barcode_with_http_info(barcode, authorization, x_digikey_client_id, **kwargs)  # noqa: E501
            return data

    def pack_list2_d_barcode_with_http_info(self, barcode, authorization, x_digikey_client_id, **kwargs):  # noqa: E501
        """Converts a pack list 2D barcode to information about the order. The barcode this takes in is a two-dimensional  barcode located in the upper right corner of the pack list. This is not for individual line item barcodes. The 2D  barcode contains special symbols. These MUST be URL encoded to be sent through the API.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pack_list2_d_barcode_with_http_info(barcode, authorization, x_digikey_client_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str barcode: Pack list barcode located on the pack list in the upper right corner. (required)
        :param str authorization: OAuth Bearer Token. Please see<a href= \"https://developer.digikey.com/documentation/oauth\" target= \"_blank\" > OAuth 2.0 Documentation </a > page for more info. (required)
        :param str x_digikey_client_id: The Client Id for your App. (required)
        :param str includes: Comma separated list of fields to return. Used to customize response to reduce bandwidth by  selecting fields that you wish to receive. For example: \"Salesorder\"
        :return: PackListBarcodeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['barcode', 'authorization', 'x_digikey_client_id', 'includes']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method pack_list2_d_barcode" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'barcode' is set
        if ('barcode' not in params or
                params['barcode'] is None):
            raise ValueError("Missing the required parameter `barcode` when calling `pack_list2_d_barcode`")  # noqa: E501
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `pack_list2_d_barcode`")  # noqa: E501
        # verify the required parameter 'x_digikey_client_id' is set
        if ('x_digikey_client_id' not in params or
                params['x_digikey_client_id'] is None):
            raise ValueError("Missing the required parameter `x_digikey_client_id` when calling `pack_list2_d_barcode`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'barcode' in params:
            path_params['barcode'] = params['barcode']  # noqa: E501

        query_params = []
        if 'includes' in params:
            query_params.append(('includes', params['includes']))  # noqa: E501

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501
        if 'x_digikey_client_id' in params:
            header_params['X-DIGIKEY-Client-Id'] = params['x_digikey_client_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKeySecurity', 'oauth2AccessCodeSecurity']  # noqa: E501

        return self.api_client.call_api(
            '/PackList2DBarcodes/{barcode}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PackListBarcodeResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def pack_list_barcode(self, barcode, authorization, x_digikey_client_id, **kwargs):  # noqa: E501
        """Converts a pack list barcode to information about the order. The barcode this takes in is a one-dimensional barcode  located in the lower left corner of the pack list.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pack_list_barcode(barcode, authorization, x_digikey_client_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str barcode: Pack list barcode located on the pack list in the lower left corner. (required)
        :param str authorization: OAuth Bearer Token. Please see<a href= \"https://developer.digikey.com/documentation/oauth\" target= \"_blank\" > OAuth 2.0 Documentation </a > page for more info. (required)
        :param str x_digikey_client_id: The Client Id for your App. (required)
        :param str includes: Comma separated list of fields to return. Used to customize response to reduce bandwidth by  selecting fields that you wish to receive. For example: \"Salesorder\"
        :return: PackListBarcodeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.pack_list_barcode_with_http_info(barcode, authorization, x_digikey_client_id, **kwargs)  # noqa: E501
        else:
            (data) = self.pack_list_barcode_with_http_info(barcode, authorization, x_digikey_client_id, **kwargs)  # noqa: E501
            return data

    def pack_list_barcode_with_http_info(self, barcode, authorization, x_digikey_client_id, **kwargs):  # noqa: E501
        """Converts a pack list barcode to information about the order. The barcode this takes in is a one-dimensional barcode  located in the lower left corner of the pack list.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pack_list_barcode_with_http_info(barcode, authorization, x_digikey_client_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str barcode: Pack list barcode located on the pack list in the lower left corner. (required)
        :param str authorization: OAuth Bearer Token. Please see<a href= \"https://developer.digikey.com/documentation/oauth\" target= \"_blank\" > OAuth 2.0 Documentation </a > page for more info. (required)
        :param str x_digikey_client_id: The Client Id for your App. (required)
        :param str includes: Comma separated list of fields to return. Used to customize response to reduce bandwidth by  selecting fields that you wish to receive. For example: \"Salesorder\"
        :return: PackListBarcodeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['barcode', 'authorization', 'x_digikey_client_id', 'includes']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method pack_list_barcode" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'barcode' is set
        if ('barcode' not in params or
                params['barcode'] is None):
            raise ValueError("Missing the required parameter `barcode` when calling `pack_list_barcode`")  # noqa: E501
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `pack_list_barcode`")  # noqa: E501
        # verify the required parameter 'x_digikey_client_id' is set
        if ('x_digikey_client_id' not in params or
                params['x_digikey_client_id'] is None):
            raise ValueError("Missing the required parameter `x_digikey_client_id` when calling `pack_list_barcode`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'barcode' in params:
            path_params['barcode'] = params['barcode']  # noqa: E501

        query_params = []
        if 'includes' in params:
            query_params.append(('includes', params['includes']))  # noqa: E501

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501
        if 'x_digikey_client_id' in params:
            header_params['X-DIGIKEY-Client-Id'] = params['x_digikey_client_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKeySecurity', 'oauth2AccessCodeSecurity']  # noqa: E501

        return self.api_client.call_api(
            '/PackListBarcodes/{barcode}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PackListBarcodeResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def product2_d_barcode(self, barcode, authorization, x_digikey_client_id, **kwargs):  # noqa: E501
        """Converts a product 2D barcode to Digi-Key and Manufacturer part number and quantity. The barcode this takes in QR  Code located on the label on the anti-static bag. The QR Code contains special ASCII symbols. These MUST be encoded  to be sent through the API. Please ensure the Record Separator character is encoded as \\u241E and the Group  Separator character is encoded as \\u241D  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.product2_d_barcode(barcode, authorization, x_digikey_client_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str barcode: QR Code from a Digi-Key product label. The QR Code contains special ASCII symbols. These MUST be  encoded to be sent through the API. Please ensure the Record Separator character is encoded as \\u241E and the Group  Separator character is encoded as \\u241D (required)
        :param str authorization: OAuth Bearer Token. Please see<a href= \"https://developer.digikey.com/documentation/oauth\" target= \"_blank\" > OAuth 2.0 Documentation </a > page for more info. (required)
        :param str x_digikey_client_id: The Client Id for your App. (required)
        :param str includes: Comma separated list of fields to return. Used to customize response to reduce bandwidth by  selecting fields that you wish to receive. For example: \"DigiKeyPartNumber,Quantity\"
        :return: Product2DBarcodeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.product2_d_barcode_with_http_info(barcode, authorization, x_digikey_client_id, **kwargs)  # noqa: E501
        else:
            (data) = self.product2_d_barcode_with_http_info(barcode, authorization, x_digikey_client_id, **kwargs)  # noqa: E501
            return data

    def product2_d_barcode_with_http_info(self, barcode, authorization, x_digikey_client_id, **kwargs):  # noqa: E501
        """Converts a product 2D barcode to Digi-Key and Manufacturer part number and quantity. The barcode this takes in QR  Code located on the label on the anti-static bag. The QR Code contains special ASCII symbols. These MUST be encoded  to be sent through the API. Please ensure the Record Separator character is encoded as \\u241E and the Group  Separator character is encoded as \\u241D  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.product2_d_barcode_with_http_info(barcode, authorization, x_digikey_client_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str barcode: QR Code from a Digi-Key product label. The QR Code contains special ASCII symbols. These MUST be  encoded to be sent through the API. Please ensure the Record Separator character is encoded as \\u241E and the Group  Separator character is encoded as \\u241D (required)
        :param str authorization: OAuth Bearer Token. Please see<a href= \"https://developer.digikey.com/documentation/oauth\" target= \"_blank\" > OAuth 2.0 Documentation </a > page for more info. (required)
        :param str x_digikey_client_id: The Client Id for your App. (required)
        :param str includes: Comma separated list of fields to return. Used to customize response to reduce bandwidth by  selecting fields that you wish to receive. For example: \"DigiKeyPartNumber,Quantity\"
        :return: Product2DBarcodeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['barcode', 'authorization', 'x_digikey_client_id', 'includes']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method product2_d_barcode" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'barcode' is set
        if ('barcode' not in params or
                params['barcode'] is None):
            raise ValueError("Missing the required parameter `barcode` when calling `product2_d_barcode`")  # noqa: E501
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `product2_d_barcode`")  # noqa: E501
        # verify the required parameter 'x_digikey_client_id' is set
        if ('x_digikey_client_id' not in params or
                params['x_digikey_client_id'] is None):
            raise ValueError("Missing the required parameter `x_digikey_client_id` when calling `product2_d_barcode`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'barcode' in params:
            path_params['barcode'] = params['barcode']  # noqa: E501

        query_params = []
        if 'includes' in params:
            query_params.append(('includes', params['includes']))  # noqa: E501

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501
        if 'x_digikey_client_id' in params:
            header_params['X-DIGIKEY-Client-Id'] = params['x_digikey_client_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKeySecurity', 'oauth2AccessCodeSecurity']  # noqa: E501

        return self.api_client.call_api(
            '/Product2DBarcodes/{barcode}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Product2DBarcodeResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def product_barcode(self, barcode, authorization, x_digikey_client_id, **kwargs):  # noqa: E501
        """Converts a legacy product barcode to Digi-Key and Manufacturer part number and quantity. The barcode this takes in  is a one-dimensional barcode that was previously located on the label on the anti-static bag. This barcode can  still be found on older products.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.product_barcode(barcode, authorization, x_digikey_client_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str barcode: Product barcode located on the product's anti-static bag. (required)
        :param str authorization: OAuth Bearer Token. Please see<a href= \"https://developer.digikey.com/documentation/oauth\" target= \"_blank\" > OAuth 2.0 Documentation </a > page for more info. (required)
        :param str x_digikey_client_id: The Client Id for your App. (required)
        :param str includes: Comma separated list of fields to return. Used to customize response to reduce bandwidth by  selecting fields that you wish to receive. For example: \"DigiKeyPartNumber,Quantity\".
        :return: ProductBarcodeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.product_barcode_with_http_info(barcode, authorization, x_digikey_client_id, **kwargs)  # noqa: E501
        else:
            (data) = self.product_barcode_with_http_info(barcode, authorization, x_digikey_client_id, **kwargs)  # noqa: E501
            return data

    def product_barcode_with_http_info(self, barcode, authorization, x_digikey_client_id, **kwargs):  # noqa: E501
        """Converts a legacy product barcode to Digi-Key and Manufacturer part number and quantity. The barcode this takes in  is a one-dimensional barcode that was previously located on the label on the anti-static bag. This barcode can  still be found on older products.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.product_barcode_with_http_info(barcode, authorization, x_digikey_client_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str barcode: Product barcode located on the product's anti-static bag. (required)
        :param str authorization: OAuth Bearer Token. Please see<a href= \"https://developer.digikey.com/documentation/oauth\" target= \"_blank\" > OAuth 2.0 Documentation </a > page for more info. (required)
        :param str x_digikey_client_id: The Client Id for your App. (required)
        :param str includes: Comma separated list of fields to return. Used to customize response to reduce bandwidth by  selecting fields that you wish to receive. For example: \"DigiKeyPartNumber,Quantity\".
        :return: ProductBarcodeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['barcode', 'authorization', 'x_digikey_client_id', 'includes']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method product_barcode" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'barcode' is set
        if ('barcode' not in params or
                params['barcode'] is None):
            raise ValueError("Missing the required parameter `barcode` when calling `product_barcode`")  # noqa: E501
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `product_barcode`")  # noqa: E501
        # verify the required parameter 'x_digikey_client_id' is set
        if ('x_digikey_client_id' not in params or
                params['x_digikey_client_id'] is None):
            raise ValueError("Missing the required parameter `x_digikey_client_id` when calling `product_barcode`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'barcode' in params:
            path_params['barcode'] = params['barcode']  # noqa: E501

        query_params = []
        if 'includes' in params:
            query_params.append(('includes', params['includes']))  # noqa: E501

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501
        if 'x_digikey_client_id' in params:
            header_params['X-DIGIKEY-Client-Id'] = params['x_digikey_client_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKeySecurity', 'oauth2AccessCodeSecurity']  # noqa: E501

        return self.api_client.call_api(
            '/ProductBarcodes/{barcode}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ProductBarcodeResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
