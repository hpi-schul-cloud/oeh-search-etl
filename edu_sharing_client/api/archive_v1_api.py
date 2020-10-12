# coding: utf-8

"""
    edu-sharing Repository REST API

    The public restful API of the edu-sharing repository.  # noqa: E501

    OpenAPI spec version: 1.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from edu_sharing_client.api_client import ApiClient


class ARCHIVEV1Api(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def purge(self, repository, archived_node_ids, **kwargs):  # noqa: E501
        """Searches for archive nodes.  # noqa: E501

        Searches for archive nodes.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.purge(repository, archived_node_ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repository: ID of repository (or \"-home-\" for home repository) (required)
        :param list[str] archived_node_ids: archived node (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.purge_with_http_info(repository, archived_node_ids, **kwargs)  # noqa: E501
        else:
            (data) = self.purge_with_http_info(repository, archived_node_ids, **kwargs)  # noqa: E501
            return data

    def purge_with_http_info(self, repository, archived_node_ids, **kwargs):  # noqa: E501
        """Searches for archive nodes.  # noqa: E501

        Searches for archive nodes.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.purge_with_http_info(repository, archived_node_ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repository: ID of repository (or \"-home-\" for home repository) (required)
        :param list[str] archived_node_ids: archived node (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['repository', 'archived_node_ids']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method purge" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'repository' is set
        if ('repository' not in params or
                params['repository'] is None):
            raise ValueError("Missing the required parameter `repository` when calling `purge`")  # noqa: E501
        # verify the required parameter 'archived_node_ids' is set
        if ('archived_node_ids' not in params or
                params['archived_node_ids'] is None):
            raise ValueError("Missing the required parameter `archived_node_ids` when calling `purge`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'repository' in params:
            path_params['repository'] = params['repository']  # noqa: E501

        query_params = []
        if 'archived_node_ids' in params:
            query_params.append(('archivedNodeIds', params['archived_node_ids']))  # noqa: E501
            collection_formats['archivedNodeIds'] = 'multi'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/archive/v1/purge/{repository}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def restore(self, repository, archived_node_ids, **kwargs):  # noqa: E501
        """restore archived nodes.  # noqa: E501

        restores archived nodes. restoreStatus can have the following values: FALLBACK_PARENT_NOT_EXISTS, FALLBACK_PARENT_NO_PERMISSION, DUPLICATENAME, FINE  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.restore(repository, archived_node_ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repository: ID of repository (or \"-home-\" for home repository) (required)
        :param list[str] archived_node_ids: archived nodes (required)
        :param str target: to target
        :return: RestoreResults
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.restore_with_http_info(repository, archived_node_ids, **kwargs)  # noqa: E501
        else:
            (data) = self.restore_with_http_info(repository, archived_node_ids, **kwargs)  # noqa: E501
            return data

    def restore_with_http_info(self, repository, archived_node_ids, **kwargs):  # noqa: E501
        """restore archived nodes.  # noqa: E501

        restores archived nodes. restoreStatus can have the following values: FALLBACK_PARENT_NOT_EXISTS, FALLBACK_PARENT_NO_PERMISSION, DUPLICATENAME, FINE  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.restore_with_http_info(repository, archived_node_ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repository: ID of repository (or \"-home-\" for home repository) (required)
        :param list[str] archived_node_ids: archived nodes (required)
        :param str target: to target
        :return: RestoreResults
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['repository', 'archived_node_ids', 'target']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method restore" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'repository' is set
        if ('repository' not in params or
                params['repository'] is None):
            raise ValueError("Missing the required parameter `repository` when calling `restore`")  # noqa: E501
        # verify the required parameter 'archived_node_ids' is set
        if ('archived_node_ids' not in params or
                params['archived_node_ids'] is None):
            raise ValueError("Missing the required parameter `archived_node_ids` when calling `restore`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'repository' in params:
            path_params['repository'] = params['repository']  # noqa: E501

        query_params = []
        if 'archived_node_ids' in params:
            query_params.append(('archivedNodeIds', params['archived_node_ids']))  # noqa: E501
            collection_formats['archivedNodeIds'] = 'multi'  # noqa: E501
        if 'target' in params:
            query_params.append(('target', params['target']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/archive/v1/restore/{repository}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RestoreResults',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search(self, repository, pattern, **kwargs):  # noqa: E501
        """Searches for archive nodes.  # noqa: E501

        Searches for archive nodes.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search(repository, pattern, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repository: ID of repository (or \"-home-\" for home repository) (required)
        :param str pattern: search pattern (required)
        :param int max_items: maximum items per page
        :param int skip_count: skip a number of items
        :param list[str] sort_properties: sort properties
        :param list[bool] sort_ascending: sort ascending
        :param list[str] property_filter: property filter for result nodes (or \"-all-\" for all properties)
        :return: SearchResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_with_http_info(repository, pattern, **kwargs)  # noqa: E501
        else:
            (data) = self.search_with_http_info(repository, pattern, **kwargs)  # noqa: E501
            return data

    def search_with_http_info(self, repository, pattern, **kwargs):  # noqa: E501
        """Searches for archive nodes.  # noqa: E501

        Searches for archive nodes.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_with_http_info(repository, pattern, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repository: ID of repository (or \"-home-\" for home repository) (required)
        :param str pattern: search pattern (required)
        :param int max_items: maximum items per page
        :param int skip_count: skip a number of items
        :param list[str] sort_properties: sort properties
        :param list[bool] sort_ascending: sort ascending
        :param list[str] property_filter: property filter for result nodes (or \"-all-\" for all properties)
        :return: SearchResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['repository', 'pattern', 'max_items', 'skip_count', 'sort_properties', 'sort_ascending', 'property_filter']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'repository' is set
        if ('repository' not in params or
                params['repository'] is None):
            raise ValueError("Missing the required parameter `repository` when calling `search`")  # noqa: E501
        # verify the required parameter 'pattern' is set
        if ('pattern' not in params or
                params['pattern'] is None):
            raise ValueError("Missing the required parameter `pattern` when calling `search`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'repository' in params:
            path_params['repository'] = params['repository']  # noqa: E501
        if 'pattern' in params:
            path_params['pattern'] = params['pattern']  # noqa: E501

        query_params = []
        if 'max_items' in params:
            query_params.append(('maxItems', params['max_items']))  # noqa: E501
        if 'skip_count' in params:
            query_params.append(('skipCount', params['skip_count']))  # noqa: E501
        if 'sort_properties' in params:
            query_params.append(('sortProperties', params['sort_properties']))  # noqa: E501
            collection_formats['sortProperties'] = 'multi'  # noqa: E501
        if 'sort_ascending' in params:
            query_params.append(('sortAscending', params['sort_ascending']))  # noqa: E501
            collection_formats['sortAscending'] = 'multi'  # noqa: E501
        if 'property_filter' in params:
            query_params.append(('propertyFilter', params['property_filter']))  # noqa: E501
            collection_formats['propertyFilter'] = 'multi'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/archive/v1/search/{repository}/{pattern}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SearchResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search_0(self, repository, pattern, person, **kwargs):  # noqa: E501
        """Searches for archive nodes.  # noqa: E501

        Searches for archive nodes.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_0(repository, pattern, person, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repository: ID of repository (or \"-home-\" for home repository) (required)
        :param str pattern: search pattern (required)
        :param str person: person (required)
        :param int max_items: maximum items per page
        :param int skip_count: skip a number of items
        :param list[str] sort_properties: sort properties
        :param list[bool] sort_ascending: sort ascending
        :param list[str] property_filter: property filter for result nodes (or \"-all-\" for all properties)
        :return: SearchResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_0_with_http_info(repository, pattern, person, **kwargs)  # noqa: E501
        else:
            (data) = self.search_0_with_http_info(repository, pattern, person, **kwargs)  # noqa: E501
            return data

    def search_0_with_http_info(self, repository, pattern, person, **kwargs):  # noqa: E501
        """Searches for archive nodes.  # noqa: E501

        Searches for archive nodes.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_0_with_http_info(repository, pattern, person, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repository: ID of repository (or \"-home-\" for home repository) (required)
        :param str pattern: search pattern (required)
        :param str person: person (required)
        :param int max_items: maximum items per page
        :param int skip_count: skip a number of items
        :param list[str] sort_properties: sort properties
        :param list[bool] sort_ascending: sort ascending
        :param list[str] property_filter: property filter for result nodes (or \"-all-\" for all properties)
        :return: SearchResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['repository', 'pattern', 'person', 'max_items', 'skip_count', 'sort_properties', 'sort_ascending', 'property_filter']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_0" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'repository' is set
        if ('repository' not in params or
                params['repository'] is None):
            raise ValueError("Missing the required parameter `repository` when calling `search_0`")  # noqa: E501
        # verify the required parameter 'pattern' is set
        if ('pattern' not in params or
                params['pattern'] is None):
            raise ValueError("Missing the required parameter `pattern` when calling `search_0`")  # noqa: E501
        # verify the required parameter 'person' is set
        if ('person' not in params or
                params['person'] is None):
            raise ValueError("Missing the required parameter `person` when calling `search_0`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'repository' in params:
            path_params['repository'] = params['repository']  # noqa: E501
        if 'pattern' in params:
            path_params['pattern'] = params['pattern']  # noqa: E501
        if 'person' in params:
            path_params['person'] = params['person']  # noqa: E501

        query_params = []
        if 'max_items' in params:
            query_params.append(('maxItems', params['max_items']))  # noqa: E501
        if 'skip_count' in params:
            query_params.append(('skipCount', params['skip_count']))  # noqa: E501
        if 'sort_properties' in params:
            query_params.append(('sortProperties', params['sort_properties']))  # noqa: E501
            collection_formats['sortProperties'] = 'multi'  # noqa: E501
        if 'sort_ascending' in params:
            query_params.append(('sortAscending', params['sort_ascending']))  # noqa: E501
            collection_formats['sortAscending'] = 'multi'  # noqa: E501
        if 'property_filter' in params:
            query_params.append(('propertyFilter', params['property_filter']))  # noqa: E501
            collection_formats['propertyFilter'] = 'multi'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/archive/v1/search/{repository}/{pattern}/{person}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SearchResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)