# coding: utf-8

"""
 Copyright 2023 TikTok Pte. Ltd.

 This source code is licensed under the MIT license found in
 the LICENSE file in the root directory of this source tree.
"""
from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from business_api_client.api_client import ApiClient


class MeasurementApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def app_list(self, advertiser_id, access_token, **kwargs):  # noqa: E501
        """Get the app list [App list](https://ads.tiktok.com/marketing_api/docs?id=1740859313270786)  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.app_list(advertiser_id, access_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str advertiser_id: Advertiser ID (required)
        :param str access_token: Authorized access token. For details, see [Authentication](https://ads.tiktok.com/marketing_api/docs?id=1738373164380162). (required)
        :param list[str] app_platform_ids: List of app platform ID for filter purpose
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.app_list_with_http_info(advertiser_id, access_token, **kwargs)  # noqa: E501
        else:
            (data) = self.app_list_with_http_info(advertiser_id, access_token, **kwargs)  # noqa: E501
            return data

    def app_list_with_http_info(self, advertiser_id, access_token, **kwargs):  # noqa: E501
        """Get the app list [App list](https://ads.tiktok.com/marketing_api/docs?id=1740859313270786)  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.app_list_with_http_info(advertiser_id, access_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str advertiser_id: Advertiser ID (required)
        :param str access_token: Authorized access token. For details, see [Authentication](https://ads.tiktok.com/marketing_api/docs?id=1738373164380162). (required)
        :param list[str] app_platform_ids: List of app platform ID for filter purpose
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['advertiser_id', 'access_token', 'app_platform_ids']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method app_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'advertiser_id' is set
        if ('advertiser_id' not in params or
                params['advertiser_id'] is None):
            raise ValueError("Missing the required parameter `advertiser_id` when calling `app_list`")  # noqa: E501
        # verify the required parameter 'access_token' is set
        if ('access_token' not in params or
                params['access_token'] is None):
            raise ValueError("Missing the required parameter `access_token` when calling `app_list`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'advertiser_id' in params:
            query_params.append(('advertiser_id', params['advertiser_id']))  # noqa: E501
        if 'app_platform_ids' in params:
            query_params.append(('app_platform_ids', params['app_platform_ids']))  # noqa: E501
            collection_formats['app_platform_ids'] = 'multi'  # noqa: E501

        header_params = {}
        if 'access_token' in params:
            header_params['Access-Token'] = params['access_token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/open_api/v1.3/app/list/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse200',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def app_optimization_event(self, app_id, advertiser_id, placement, optimization_goal, access_token, **kwargs):  # noqa: E501
        """Get App Events [App events](https://ads.tiktok.com/marketing_api/docs?id=1740859338750977)  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.app_optimization_event(app_id, advertiser_id, placement, optimization_goal, access_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str app_id: Your App ID, obtained after successfully creating your app (required)
        :param str advertiser_id: Advertiser ID (required)
        :param list[str] placement: Advertisement positioning, See [Enumeration-Placement](https://ads.tiktok.com/marketing_api/docs?id=1737174886619138) (required)
        :param str optimization_goal: Optimization goal. For enum values, see [Enumeration-Optimization Goal](https://ads.tiktok.com/marketing_api/docs?id=1737174886619138) for more (required)
        :param str access_token: Authorized access token. For details, see [Authentication](https://ads.tiktok.com/marketing_api/docs?id=1738373164380162). (required)
        :param str objective: Advertising Objective. For enum values, see [Enumeration-Advertising Objective](https://ads.tiktok.com/marketing_api/docs?id=1737174886619138)
        :param bool available_only: Whether to return only available conversion events. The default value: `True` (only return available conversion events)
        :param bool is_skan: Whether the app is using Skan features
        :param str app_promotion_type: App promotion type. Required when `objective_type` is `APP_PROMOTION`. Enum values: `APP_INSTALL`, `APP_RETARGETING`. Note: `APP_INSTALL` can be used in an iOS14 Dedicated Campaign, while `APP_RETARGETING` cannot be used
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.app_optimization_event_with_http_info(app_id, advertiser_id, placement, optimization_goal, access_token, **kwargs)  # noqa: E501
        else:
            (data) = self.app_optimization_event_with_http_info(app_id, advertiser_id, placement, optimization_goal, access_token, **kwargs)  # noqa: E501
            return data

    def app_optimization_event_with_http_info(self, app_id, advertiser_id, placement, optimization_goal, access_token, **kwargs):  # noqa: E501
        """Get App Events [App events](https://ads.tiktok.com/marketing_api/docs?id=1740859338750977)  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.app_optimization_event_with_http_info(app_id, advertiser_id, placement, optimization_goal, access_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str app_id: Your App ID, obtained after successfully creating your app (required)
        :param str advertiser_id: Advertiser ID (required)
        :param list[str] placement: Advertisement positioning, See [Enumeration-Placement](https://ads.tiktok.com/marketing_api/docs?id=1737174886619138) (required)
        :param str optimization_goal: Optimization goal. For enum values, see [Enumeration-Optimization Goal](https://ads.tiktok.com/marketing_api/docs?id=1737174886619138) for more (required)
        :param str access_token: Authorized access token. For details, see [Authentication](https://ads.tiktok.com/marketing_api/docs?id=1738373164380162). (required)
        :param str objective: Advertising Objective. For enum values, see [Enumeration-Advertising Objective](https://ads.tiktok.com/marketing_api/docs?id=1737174886619138)
        :param bool available_only: Whether to return only available conversion events. The default value: `True` (only return available conversion events)
        :param bool is_skan: Whether the app is using Skan features
        :param str app_promotion_type: App promotion type. Required when `objective_type` is `APP_PROMOTION`. Enum values: `APP_INSTALL`, `APP_RETARGETING`. Note: `APP_INSTALL` can be used in an iOS14 Dedicated Campaign, while `APP_RETARGETING` cannot be used
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['app_id', 'advertiser_id', 'placement', 'optimization_goal', 'access_token', 'objective', 'available_only', 'is_skan', 'app_promotion_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method app_optimization_event" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'app_id' is set
        if ('app_id' not in params or
                params['app_id'] is None):
            raise ValueError("Missing the required parameter `app_id` when calling `app_optimization_event`")  # noqa: E501
        # verify the required parameter 'advertiser_id' is set
        if ('advertiser_id' not in params or
                params['advertiser_id'] is None):
            raise ValueError("Missing the required parameter `advertiser_id` when calling `app_optimization_event`")  # noqa: E501
        # verify the required parameter 'placement' is set
        if ('placement' not in params or
                params['placement'] is None):
            raise ValueError("Missing the required parameter `placement` when calling `app_optimization_event`")  # noqa: E501
        # verify the required parameter 'optimization_goal' is set
        if ('optimization_goal' not in params or
                params['optimization_goal'] is None):
            raise ValueError("Missing the required parameter `optimization_goal` when calling `app_optimization_event`")  # noqa: E501
        # verify the required parameter 'access_token' is set
        if ('access_token' not in params or
                params['access_token'] is None):
            raise ValueError("Missing the required parameter `access_token` when calling `app_optimization_event`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'app_id' in params:
            query_params.append(('app_id', params['app_id']))  # noqa: E501
        if 'advertiser_id' in params:
            query_params.append(('advertiser_id', params['advertiser_id']))  # noqa: E501
        if 'placement' in params:
            query_params.append(('placement', params['placement']))  # noqa: E501
            collection_formats['placement'] = 'multi'  # noqa: E501
        if 'optimization_goal' in params:
            query_params.append(('optimization_goal', params['optimization_goal']))  # noqa: E501
        if 'objective' in params:
            query_params.append(('objective', params['objective']))  # noqa: E501
        if 'available_only' in params:
            query_params.append(('available_only', params['available_only']))  # noqa: E501
        if 'is_skan' in params:
            query_params.append(('is_skan', params['is_skan']))  # noqa: E501
        if 'app_promotion_type' in params:
            query_params.append(('app_promotion_type', params['app_promotion_type']))  # noqa: E501

        header_params = {}
        if 'access_token' in params:
            header_params['Access-Token'] = params['access_token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/open_api/v1.3/app/optimization_event/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse200',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
