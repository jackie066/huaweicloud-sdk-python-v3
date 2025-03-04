# coding: utf-8

from __future__ import absolute_import

import datetime
import re
import importlib

import six

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest


class MpcAsyncClient(Client):
    """
    :param configuration: .Configuration object for this client
    :param pool_threads: The number of threads to use for async requests
        to the API. More threads means more concurrent API requests.
    """

    PRIMITIVE_TYPES = (float, bool, bytes, six.text_type) + six.integer_types
    NATIVE_TYPES_MAPPING = {
        'int': int,
        'long': int if six.PY3 else long,
        'float': float,
        'str': str,
        'bool': bool,
        'date': datetime.date,
        'datetime': datetime.datetime,
        'object': object,
    }

    def __init__(self):
        super(MpcAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkmpc.v1.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "MpcClient":
            raise TypeError("client type error, support client type is MpcClient")

        return ClientBuilder(clazz)

    def create_animated_graphics_task_async(self, request):
        """新建转动图任务

        创建动图任务，用于将完整的视频文件或视频文件中的一部分转换为动态图文件，暂只支持输出GIF文件。
        待转动图的视频文件需要存储在与媒体处理服务同区域的OBS桶中，且该OBS桶已授权。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateAnimatedGraphicsTask
        :type request: :class:`huaweicloudsdkmpc.v1.CreateAnimatedGraphicsTaskRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.CreateAnimatedGraphicsTaskResponse`
        """
        return self.create_animated_graphics_task_with_http_info(request)

    def create_animated_graphics_task_with_http_info(self, request):
        all_params = ['create_animated_graphics_task_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/animated-graphics',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateAnimatedGraphicsTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_animated_graphics_task_async(self, request):
        """取消转动图任务

        取消已下发的生成动图任务，仅支持取消正在排队中的任务。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteAnimatedGraphicsTask
        :type request: :class:`huaweicloudsdkmpc.v1.DeleteAnimatedGraphicsTaskRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.DeleteAnimatedGraphicsTaskResponse`
        """
        return self.delete_animated_graphics_task_with_http_info(request)

    def delete_animated_graphics_task_with_http_info(self, request):
        all_params = ['task_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/animated-graphics',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteAnimatedGraphicsTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_animated_graphics_task_async(self, request):
        """查询转动图任务

        查询动图任务的状态。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListAnimatedGraphicsTask
        :type request: :class:`huaweicloudsdkmpc.v1.ListAnimatedGraphicsTaskRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.ListAnimatedGraphicsTaskResponse`
        """
        return self.list_animated_graphics_task_with_http_info(request)

    def list_animated_graphics_task_with_http_info(self, request):
        all_params = ['x_language', 'task_id', 'status', 'start_time', 'end_time', 'page', 'size']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))
            collection_formats['task_id'] = 'multi'
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'size' in local_var_params:
            query_params.append(('size', local_var_params['size']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['x-language'] = local_var_params['x_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/animated-graphics',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListAnimatedGraphicsTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_editing_job_async(self, request):
        """新建剪辑任务

        创建剪辑任务，用于将多个视频文件进行裁剪成多个视频分段，并且可以把这些视频分段合并成一个视频，剪切和拼接功能可以单独使用。
        待剪辑的视频文件需要存储在与媒体处理服务同区域的OBS桶中，且该OBS桶已授权。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateEditingJob
        :type request: :class:`huaweicloudsdkmpc.v1.CreateEditingJobRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.CreateEditingJobResponse`
        """
        return self.create_editing_job_with_http_info(request)

    def create_editing_job_with_http_info(self, request):
        all_params = ['create_editing_job_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/editing/jobs',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateEditingJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_editing_job_async(self, request):
        """取消剪辑任务

        取消已下发的生成剪辑任务，仅支持取消正在排队中的任务。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteEditingJob
        :type request: :class:`huaweicloudsdkmpc.v1.DeleteEditingJobRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.DeleteEditingJobResponse`
        """
        return self.delete_editing_job_with_http_info(request)

    def delete_editing_job_with_http_info(self, request):
        all_params = ['job_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'job_id' in local_var_params:
            query_params.append(('job_id', local_var_params['job_id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/editing/jobs',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteEditingJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_editing_job_async(self, request):
        """查询剪辑任务

        查询剪辑任务的状态。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListEditingJob
        :type request: :class:`huaweicloudsdkmpc.v1.ListEditingJobRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.ListEditingJobResponse`
        """
        return self.list_editing_job_with_http_info(request)

    def list_editing_job_with_http_info(self, request):
        all_params = ['x_language', 'job_id', 'status', 'start_time', 'end_time', 'page', 'size']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'job_id' in local_var_params:
            query_params.append(('job_id', local_var_params['job_id']))
            collection_formats['job_id'] = 'multi'
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'size' in local_var_params:
            query_params.append(('size', local_var_params['size']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['x-language'] = local_var_params['x_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/editing/jobs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListEditingJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_encrypt_task_async(self, request):
        """新建独立加密任务

        支持独立加密，包括创建、查询、删除独立加密任务。
        
        约束：
          - 只支持转码后的文件进行加密。
          - 加密的文件必须是m3u8或者mpd结尾的文件。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateEncryptTask
        :type request: :class:`huaweicloudsdkmpc.v1.CreateEncryptTaskRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.CreateEncryptTaskResponse`
        """
        return self.create_encrypt_task_with_http_info(request)

    def create_encrypt_task_with_http_info(self, request):
        all_params = ['create_encrypt_task_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/encryptions',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateEncryptTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_encrypt_task_async(self, request):
        """取消独立加密任务

        取消独立加密任务。
        
        约束：
        
          只能取消正在任务队列中排队的任务。已开始加密或已完成的加密任务不能取消。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteEncryptTask
        :type request: :class:`huaweicloudsdkmpc.v1.DeleteEncryptTaskRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.DeleteEncryptTaskResponse`
        """
        return self.delete_encrypt_task_with_http_info(request)

    def delete_encrypt_task_with_http_info(self, request):
        all_params = ['task_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/encryptions',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteEncryptTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_encrypt_task_async(self, request):
        """查询独立加密任务

        查询独立加密任务状态。返回任务执行结果或当前状态。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListEncryptTask
        :type request: :class:`huaweicloudsdkmpc.v1.ListEncryptTaskRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.ListEncryptTaskResponse`
        """
        return self.list_encrypt_task_with_http_info(request)

    def list_encrypt_task_with_http_info(self, request):
        all_params = ['task_id', 'status', 'start_time', 'end_time', 'page', 'size']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))
            collection_formats['task_id'] = 'multi'
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'size' in local_var_params:
            query_params.append(('size', local_var_params['size']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/encryptions',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListEncryptTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_extract_task_async(self, request):
        """新建视频解析任务

        创建视频解析任务，解析视频元数据。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateExtractTask
        :type request: :class:`huaweicloudsdkmpc.v1.CreateExtractTaskRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.CreateExtractTaskResponse`
        """
        return self.create_extract_task_with_http_info(request)

    def create_extract_task_with_http_info(self, request):
        all_params = ['create_extract_task_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/extract-metadata',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateExtractTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_extract_task_async(self, request):
        """取消视频解析任务

        取消已下发的视频解析任务，仅支持取消正在排队中的任务。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteExtractTask
        :type request: :class:`huaweicloudsdkmpc.v1.DeleteExtractTaskRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.DeleteExtractTaskResponse`
        """
        return self.delete_extract_task_with_http_info(request)

    def delete_extract_task_with_http_info(self, request):
        all_params = ['task_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/extract-metadata',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteExtractTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_extract_task_async(self, request):
        """查询视频解析任务

        查询解析任务的状态和结果。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListExtractTask
        :type request: :class:`huaweicloudsdkmpc.v1.ListExtractTaskRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.ListExtractTaskResponse`
        """
        return self.list_extract_task_with_http_info(request)

    def list_extract_task_with_http_info(self, request):
        all_params = ['x_language', 'task_id', 'status', 'start_time', 'end_time', 'page', 'size']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))
            collection_formats['task_id'] = 'multi'
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'size' in local_var_params:
            query_params.append(('size', local_var_params['size']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['x-language'] = local_var_params['x_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/extract-metadata',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListExtractTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_mb_tasks_report_async(self, request):
        """合并多声道任务、重置声轨任务上报接口

        ## 典型场景 ##
          合并音频多声道文件任务、重置音频文件声轨任务上报结果接口。
        ## 接口功能 ##
          合并音频多声道文件任务、重置音频文件声轨任务上报结果接口。
        ## 接口约束 ##
          无。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateMbTasksReport
        :type request: :class:`huaweicloudsdkmpc.v1.CreateMbTasksReportRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.CreateMbTasksReportResponse`
        """
        return self.create_mb_tasks_report_with_http_info(request)

    def create_mb_tasks_report_with_http_info(self, request):
        all_params = ['create_mb_tasks_report_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/mediabox/tasks/report',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateMbTasksReportResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_merge_channels_task_async(self, request):
        """创建声道合并任务

        创建声道合并任务，合并声道任务支持将每个声道各放一个文件中的片源，合并为单个音频文件。
        执行合并声道的源音频文件需要存储在与媒体处理服务同区域的OBS桶中，且该OBS桶已授权。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateMergeChannelsTask
        :type request: :class:`huaweicloudsdkmpc.v1.CreateMergeChannelsTaskRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.CreateMergeChannelsTaskResponse`
        """
        return self.create_merge_channels_task_with_http_info(request)

    def create_merge_channels_task_with_http_info(self, request):
        all_params = ['create_merge_channels_task_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/audio/services/merge_channels/task',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateMergeChannelsTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_reset_tracks_task_async(self, request):
        """创建音轨重置任务

        创建音轨重置任务，重置音轨任务支持按人工指定关系声道layout，语言标签，转封装片源，使其满足转码输入。
        执行音轨重置的源音频文件需要存储在与媒体处理服务同区域的OBS桶中，且该OBS桶已授权。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateResetTracksTask
        :type request: :class:`huaweicloudsdkmpc.v1.CreateResetTracksTaskRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.CreateResetTracksTaskResponse`
        """
        return self.create_reset_tracks_task_with_http_info(request)

    def create_reset_tracks_task_with_http_info(self, request):
        all_params = ['create_reset_tracks_task_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/audio/services/reset_tracks/task',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateResetTracksTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_merge_channels_task_async(self, request):
        """取消声道合并任务

        取消合并音频多声道文件。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteMergeChannelsTask
        :type request: :class:`huaweicloudsdkmpc.v1.DeleteMergeChannelsTaskRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.DeleteMergeChannelsTaskResponse`
        """
        return self.delete_merge_channels_task_with_http_info(request)

    def delete_merge_channels_task_with_http_info(self, request):
        all_params = ['task_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/audio/services/merge_channels/task',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteMergeChannelsTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_reset_tracks_task_async(self, request):
        """取消音轨重置任务

        取消重置音频文件声轨任务。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteResetTracksTask
        :type request: :class:`huaweicloudsdkmpc.v1.DeleteResetTracksTaskRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.DeleteResetTracksTaskResponse`
        """
        return self.delete_reset_tracks_task_with_http_info(request)

    def delete_reset_tracks_task_with_http_info(self, request):
        all_params = ['task_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/audio/services/reset_tracks/task',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteResetTracksTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_merge_channels_task_async(self, request):
        """查询声道合并任务

        查询声道合并任务的状态。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListMergeChannelsTask
        :type request: :class:`huaweicloudsdkmpc.v1.ListMergeChannelsTaskRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.ListMergeChannelsTaskResponse`
        """
        return self.list_merge_channels_task_with_http_info(request)

    def list_merge_channels_task_with_http_info(self, request):
        all_params = ['task_id', 'status', 'start_time', 'end_time', 'page', 'size']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))
            collection_formats['task_id'] = 'multi'
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'size' in local_var_params:
            query_params.append(('size', local_var_params['size']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/audio/services/merge_channels/task',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListMergeChannelsTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_reset_tracks_task_async(self, request):
        """查询音轨重置任务

        查询音轨重置任务的状态。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListResetTracksTask
        :type request: :class:`huaweicloudsdkmpc.v1.ListResetTracksTaskRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.ListResetTracksTaskResponse`
        """
        return self.list_reset_tracks_task_with_http_info(request)

    def list_reset_tracks_task_with_http_info(self, request):
        all_params = ['task_id', 'status', 'start_time', 'end_time', 'page', 'size']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))
            collection_formats['task_id'] = 'multi'
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'size' in local_var_params:
            query_params.append(('size', local_var_params['size']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/audio/services/reset_tracks/task',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListResetTracksTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_media_process_task_async(self, request):
        """创建视频增强任务

        ## 典型场景 ##
          创建视频增强任务。
        
        ## 接口功能 ##
          创建视频增强任务。
        
        ## 接口约束 ##
          无。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateMediaProcessTask
        :type request: :class:`huaweicloudsdkmpc.v1.CreateMediaProcessTaskRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.CreateMediaProcessTaskResponse`
        """
        return self.create_media_process_task_with_http_info(request)

    def create_media_process_task_with_http_info(self, request):
        all_params = ['create_media_process_task_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/enhancements',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateMediaProcessTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_media_process_task_async(self, request):
        """取消视频增强任务

        ## 典型场景 ##
          取消视频增强任务。
        
        ## 接口功能 ##
          取消视频增强任务。
        
        ## 接口约束 ##
          仅可删除正在排队中的任务。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteMediaProcessTask
        :type request: :class:`huaweicloudsdkmpc.v1.DeleteMediaProcessTaskRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.DeleteMediaProcessTaskResponse`
        """
        return self.delete_media_process_task_with_http_info(request)

    def delete_media_process_task_with_http_info(self, request):
        all_params = ['task_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/enhancements',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteMediaProcessTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_media_process_task_async(self, request):
        """查询视频增强任务

        ## 典型场景 ##
          查询视频增强任务。
        
        ## 接口功能 ##
          查询视频增强任务。
        
        ## 接口约束 ##
          无。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListMediaProcessTask
        :type request: :class:`huaweicloudsdkmpc.v1.ListMediaProcessTaskRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.ListMediaProcessTaskResponse`
        """
        return self.list_media_process_task_with_http_info(request)

    def list_media_process_task_with_http_info(self, request):
        all_params = ['task_id', 'status', 'start_time', 'end_time', 'page', 'size']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))
            collection_formats['task_id'] = 'multi'
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'size' in local_var_params:
            query_params.append(('size', local_var_params['size']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/enhancements',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListMediaProcessTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_mpe_call_back_async(self, request):
        """mpe通知mpc

        ## 典型场景 ##
          mpe通知mpc。
        ## 接口功能 ##
          mpe调用此接口通知mpc转封装等结果。
        ## 接口约束 ##
          无。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateMpeCallBack
        :type request: :class:`huaweicloudsdkmpc.v1.CreateMpeCallBackRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.CreateMpeCallBackResponse`
        """
        return self.create_mpe_call_back_with_http_info(request)

    def create_mpe_call_back_with_http_info(self, request):
        all_params = ['create_mpe_call_back_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/mpe/notification',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateMpeCallBackResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_quality_enhance_template_async(self, request):
        """创建视频增强模板

        创建视频增强模板
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateQualityEnhanceTemplate
        :type request: :class:`huaweicloudsdkmpc.v1.CreateQualityEnhanceTemplateRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.CreateQualityEnhanceTemplateResponse`
        """
        return self.create_quality_enhance_template_with_http_info(request)

    def create_quality_enhance_template_with_http_info(self, request):
        all_params = ['create_quality_enhance_template_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/template/qualityenhance',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateQualityEnhanceTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_quality_enhance_template_async(self, request):
        """删除用户视频增强模板

        删除用户视频增强模板。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteQualityEnhanceTemplate
        :type request: :class:`huaweicloudsdkmpc.v1.DeleteQualityEnhanceTemplateRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.DeleteQualityEnhanceTemplateResponse`
        """
        return self.delete_quality_enhance_template_with_http_info(request)

    def delete_quality_enhance_template_with_http_info(self, request):
        all_params = ['template_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'template_id' in local_var_params:
            query_params.append(('template_id', local_var_params['template_id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/template/qualityenhance',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteQualityEnhanceTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_quality_enhance_default_template_async(self, request):
        """查询视频增强预置模板

        查询视频增强预置模板，返回所有结果。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListQualityEnhanceDefaultTemplate
        :type request: :class:`huaweicloudsdkmpc.v1.ListQualityEnhanceDefaultTemplateRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.ListQualityEnhanceDefaultTemplateResponse`
        """
        return self.list_quality_enhance_default_template_with_http_info(request)

    def list_quality_enhance_default_template_with_http_info(self, request):
        all_params = []
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/template/qualityenhance/default',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListQualityEnhanceDefaultTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_quality_enhance_template_async(self, request):
        """更新视频增强模板

        更新视频增强模板。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateQualityEnhanceTemplate
        :type request: :class:`huaweicloudsdkmpc.v1.UpdateQualityEnhanceTemplateRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.UpdateQualityEnhanceTemplateResponse`
        """
        return self.update_quality_enhance_template_with_http_info(request)

    def update_quality_enhance_template_with_http_info(self, request):
        all_params = ['update_quality_enhance_template_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/template/qualityenhance',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateQualityEnhanceTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_transcode_detail_async(self, request):
        """查询媒资转码详情

        查询媒资转码详情
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListTranscodeDetail
        :type request: :class:`huaweicloudsdkmpc.v1.ListTranscodeDetailRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.ListTranscodeDetailResponse`
        """
        return self.list_transcode_detail_with_http_info(request)

    def list_transcode_detail_with_http_info(self, request):
        all_params = ['task_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))
            collection_formats['task_id'] = 'multi'

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/transcodings/detail',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListTranscodeDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def cancel_remux_task_async(self, request):
        """取消转封装任务

        取消已下发的转封装任务，仅支持取消正在排队中的任务。。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CancelRemuxTask
        :type request: :class:`huaweicloudsdkmpc.v1.CancelRemuxTaskRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.CancelRemuxTaskResponse`
        """
        return self.cancel_remux_task_with_http_info(request)

    def cancel_remux_task_with_http_info(self, request):
        all_params = ['task_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/remux',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CancelRemuxTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_remux_task_async(self, request):
        """新建转封装任务

        创建转封装任务，转换音视频文件的格式，但不改变其分辨率和码率。
        待转封装的媒资文件需要存储在与媒体处理服务同区域的OBS桶中，且该OBS桶已授权。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateRemuxTask
        :type request: :class:`huaweicloudsdkmpc.v1.CreateRemuxTaskRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.CreateRemuxTaskResponse`
        """
        return self.create_remux_task_with_http_info(request)

    def create_remux_task_with_http_info(self, request):
        all_params = ['create_remux_task_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/remux',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateRemuxTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_retry_remux_task_async(self, request):
        """重试转封装任务

        对失败的转封装任务进行重试。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateRetryRemuxTask
        :type request: :class:`huaweicloudsdkmpc.v1.CreateRetryRemuxTaskRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.CreateRetryRemuxTaskResponse`
        """
        return self.create_retry_remux_task_with_http_info(request)

    def create_retry_remux_task_with_http_info(self, request):
        all_params = ['create_retry_remux_task_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/remux',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateRetryRemuxTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_remux_task_async(self, request):
        """删除转封装任务(仅供Console调用)

        删除转封装任务
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteRemuxTask
        :type request: :class:`huaweicloudsdkmpc.v1.DeleteRemuxTaskRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.DeleteRemuxTaskResponse`
        """
        return self.delete_remux_task_with_http_info(request)

    def delete_remux_task_with_http_info(self, request):
        all_params = ['task_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/remux/task',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteRemuxTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_remux_task_async(self, request):
        """查询转封装任务

        查询转封装任务状态。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListRemuxTask
        :type request: :class:`huaweicloudsdkmpc.v1.ListRemuxTaskRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.ListRemuxTaskResponse`
        """
        return self.list_remux_task_with_http_info(request)

    def list_remux_task_with_http_info(self, request):
        all_params = ['task_id', 'status', 'start_time', 'end_time', 'input_bucket', 'input_object', 'page', 'size']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))
            collection_formats['task_id'] = 'multi'
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'input_bucket' in local_var_params:
            query_params.append(('input_bucket', local_var_params['input_bucket']))
        if 'input_object' in local_var_params:
            query_params.append(('input_object', local_var_params['input_object']))
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'size' in local_var_params:
            query_params.append(('size', local_var_params['size']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/remux',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListRemuxTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_template_group_async(self, request):
        """新建转码模板组

        新建转码模板组，最多支持一进六出。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateTemplateGroup
        :type request: :class:`huaweicloudsdkmpc.v1.CreateTemplateGroupRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.CreateTemplateGroupResponse`
        """
        return self.create_template_group_with_http_info(request)

    def create_template_group_with_http_info(self, request):
        all_params = ['create_template_group_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/template_group/transcodings',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateTemplateGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_template_group_async(self, request):
        """删除转码模板组

        删除转码模板组。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteTemplateGroup
        :type request: :class:`huaweicloudsdkmpc.v1.DeleteTemplateGroupRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.DeleteTemplateGroupResponse`
        """
        return self.delete_template_group_with_http_info(request)

    def delete_template_group_with_http_info(self, request):
        all_params = ['group_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/template_group/transcodings',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteTemplateGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_template_group_async(self, request):
        """查询转码模板组

        查询转码模板组列表。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListTemplateGroup
        :type request: :class:`huaweicloudsdkmpc.v1.ListTemplateGroupRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.ListTemplateGroupResponse`
        """
        return self.list_template_group_with_http_info(request)

    def list_template_group_with_http_info(self, request):
        all_params = ['group_id', 'group_name', 'page', 'size']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))
            collection_formats['group_id'] = 'multi'
        if 'group_name' in local_var_params:
            query_params.append(('group_name', local_var_params['group_name']))
            collection_formats['group_name'] = 'multi'
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'size' in local_var_params:
            query_params.append(('size', local_var_params['size']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/template_group/transcodings',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListTemplateGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_template_group_async(self, request):
        """更新转码模板组

        修改模板组接口。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateTemplateGroup
        :type request: :class:`huaweicloudsdkmpc.v1.UpdateTemplateGroupRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.UpdateTemplateGroupResponse`
        """
        return self.update_template_group_with_http_info(request)

    def update_template_group_with_http_info(self, request):
        all_params = ['update_template_group_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/template_group/transcodings',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateTemplateGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_thumbnails_task_async(self, request):
        """新建截图任务

        新建截图任务，视频截图将从首帧开始，按设置的时间间隔截图，最后截取末帧。
        待截图的视频文件需要存储在与媒体处理服务同区域的OBS桶中，且该OBS桶已授权。
        
        约束：
          暂只支持生成JPG格式的图片文件。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateThumbnailsTask
        :type request: :class:`huaweicloudsdkmpc.v1.CreateThumbnailsTaskRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.CreateThumbnailsTaskResponse`
        """
        return self.create_thumbnails_task_with_http_info(request)

    def create_thumbnails_task_with_http_info(self, request):
        all_params = ['create_thumbnails_task_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/thumbnails',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateThumbnailsTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_thumbnails_task_async(self, request):
        """取消截图任务

        取消已下发截图任务。
        只能取消已接受尚在队列中等待处理的任务，已完成或正在执行阶段的任务不能取消。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteThumbnailsTask
        :type request: :class:`huaweicloudsdkmpc.v1.DeleteThumbnailsTaskRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.DeleteThumbnailsTaskResponse`
        """
        return self.delete_thumbnails_task_with_http_info(request)

    def delete_thumbnails_task_with_http_info(self, request):
        all_params = ['task_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/thumbnails',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteThumbnailsTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_thumbnails_task_async(self, request):
        """查询截图任务

        查询截图任务状态。返回任务执行结果，包括状态、输入、输出等信息。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListThumbnailsTask
        :type request: :class:`huaweicloudsdkmpc.v1.ListThumbnailsTaskRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.ListThumbnailsTaskResponse`
        """
        return self.list_thumbnails_task_with_http_info(request)

    def list_thumbnails_task_with_http_info(self, request):
        all_params = ['x_language', 'task_id', 'status', 'start_time', 'end_time', 'page', 'size']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))
            collection_formats['task_id'] = 'multi'
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'size' in local_var_params:
            query_params.append(('size', local_var_params['size']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['x-language'] = local_var_params['x_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/thumbnails',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListThumbnailsTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_transcoding_task_async(self, request):
        """新建转码任务

        新建转码任务可以将视频进行转码，并在转码过程中压制水印、视频截图等。视频转码前需要配置转码模板。
        待转码的音视频需要存储在与媒体处理服务同区域的OBS桶中，且该OBS桶已授权。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateTranscodingTask
        :type request: :class:`huaweicloudsdkmpc.v1.CreateTranscodingTaskRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.CreateTranscodingTaskResponse`
        """
        return self.create_transcoding_task_with_http_info(request)

    def create_transcoding_task_with_http_info(self, request):
        all_params = ['create_transcoding_task_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/transcodings',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateTranscodingTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_transcoding_task_async(self, request):
        """取消转码任务

        取消已下发转码任务。
        只能取消正在转码任务队列中排队的转码任务。已开始转码或已完成的转码任务不能取消。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteTranscodingTask
        :type request: :class:`huaweicloudsdkmpc.v1.DeleteTranscodingTaskRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.DeleteTranscodingTaskResponse`
        """
        return self.delete_transcoding_task_with_http_info(request)

    def delete_transcoding_task_with_http_info(self, request):
        all_params = ['task_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/transcodings',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteTranscodingTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_transcoding_task_async(self, request):
        """查询转码任务

        查询转码任务状态。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListTranscodingTask
        :type request: :class:`huaweicloudsdkmpc.v1.ListTranscodingTaskRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.ListTranscodingTaskResponse`
        """
        return self.list_transcoding_task_with_http_info(request)

    def list_transcoding_task_with_http_info(self, request):
        all_params = ['x_language', 'task_id', 'status', 'start_time', 'end_time', 'page', 'size']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))
            collection_formats['task_id'] = 'multi'
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'size' in local_var_params:
            query_params.append(('size', local_var_params['size']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['x-language'] = local_var_params['x_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/transcodings',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListTranscodingTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_trans_template_async(self, request):
        """新建转码模板

        新建转码模板，采用自定义的模板转码。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateTransTemplate
        :type request: :class:`huaweicloudsdkmpc.v1.CreateTransTemplateRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.CreateTransTemplateResponse`
        """
        return self.create_trans_template_with_http_info(request)

    def create_trans_template_with_http_info(self, request):
        all_params = ['create_trans_template_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/template/transcodings',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateTransTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_template_async(self, request):
        """删除转码模板

        删除转码模板。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteTemplate
        :type request: :class:`huaweicloudsdkmpc.v1.DeleteTemplateRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.DeleteTemplateResponse`
        """
        return self.delete_template_with_http_info(request)

    def delete_template_with_http_info(self, request):
        all_params = ['template_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'template_id' in local_var_params:
            query_params.append(('template_id', local_var_params['template_id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/template/transcodings',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_template_async(self, request):
        """查询转码模板

        查询用户自定义转码配置模板。
        支持指定模板ID查询，或分页全量查询。转码配置模板ID，最多10个。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListTemplate
        :type request: :class:`huaweicloudsdkmpc.v1.ListTemplateRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.ListTemplateResponse`
        """
        return self.list_template_with_http_info(request)

    def list_template_with_http_info(self, request):
        all_params = ['template_id', 'page', 'size']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'template_id' in local_var_params:
            query_params.append(('template_id', local_var_params['template_id']))
            collection_formats['template_id'] = 'multi'
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'size' in local_var_params:
            query_params.append(('size', local_var_params['size']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/template/transcodings',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_trans_template_async(self, request):
        """更新转码模板

        更新转码模板。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateTransTemplate
        :type request: :class:`huaweicloudsdkmpc.v1.UpdateTransTemplateRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.UpdateTransTemplateResponse`
        """
        return self.update_trans_template_with_http_info(request)

    def update_trans_template_with_http_info(self, request):
        all_params = ['update_trans_template_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/template/transcodings',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateTransTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_watermark_template_async(self, request):
        """新建水印模板

        自定义水印模板。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateWatermarkTemplate
        :type request: :class:`huaweicloudsdkmpc.v1.CreateWatermarkTemplateRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.CreateWatermarkTemplateResponse`
        """
        return self.create_watermark_template_with_http_info(request)

    def create_watermark_template_with_http_info(self, request):
        all_params = ['create_watermark_template_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/template/watermark',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateWatermarkTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_watermark_template_async(self, request):
        """删除水印模板

        删除自定义水印模板。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteWatermarkTemplate
        :type request: :class:`huaweicloudsdkmpc.v1.DeleteWatermarkTemplateRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.DeleteWatermarkTemplateResponse`
        """
        return self.delete_watermark_template_with_http_info(request)

    def delete_watermark_template_with_http_info(self, request):
        all_params = ['template_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'template_id' in local_var_params:
            query_params.append(('template_id', local_var_params['template_id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/template/watermark',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteWatermarkTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_watermark_template_async(self, request):
        """查询水印模板

        查询自定义水印模板。支持指定模板ID查询，或分页全量查询。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListWatermarkTemplate
        :type request: :class:`huaweicloudsdkmpc.v1.ListWatermarkTemplateRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.ListWatermarkTemplateResponse`
        """
        return self.list_watermark_template_with_http_info(request)

    def list_watermark_template_with_http_info(self, request):
        all_params = ['template_id', 'page', 'size']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'template_id' in local_var_params:
            query_params.append(('template_id', local_var_params['template_id']))
            collection_formats['template_id'] = 'multi'
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'size' in local_var_params:
            query_params.append(('size', local_var_params['size']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/template/watermark',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListWatermarkTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_watermark_template_async(self, request):
        """更新水印模板

        更新自定义水印模板。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateWatermarkTemplate
        :type request: :class:`huaweicloudsdkmpc.v1.UpdateWatermarkTemplateRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.UpdateWatermarkTemplateResponse`
        """
        return self.update_watermark_template_with_http_info(request)

    def update_watermark_template_with_http_info(self, request):
        all_params = ['update_watermark_template_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/template/watermark',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateWatermarkTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def call_api(self, resource_path, method, path_params=None, query_params=None, header_params=None, body=None,
                 post_params=None, response_type=None, response_headers=None, auth_settings=None,
                 collection_formats=None, request_type=None):
        """Makes the HTTP request and returns deserialized data.

        :param resource_path: Path to method endpoint.
        :param method: Method to call.
        :param path_params: Path parameters in the url.
        :param query_params: Query parameters in the url.
        :param header_params: Header parameters to be
            placed in the request header.
        :param body: Request body.
        :param post_params dict: Request post form parameters,
            for `application/x-www-form-urlencoded`, `multipart/form-data`.
        :param auth_settings list: Auth Settings names for the request.
        :param response_type: Response data type.
        :param response_headers: Header should be added to response data.
        :param collection_formats: dict of collection formats for path, query,
            header, and post parameters.
        :param request_type: Request data type.
        :return:
            Return the response directly.
        """
        return self.do_http_request(
            method=method,
            resource_path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body,
            post_params=post_params,
            response_type=response_type,
            response_headers=response_headers,
            collection_formats=collection_formats,
            request_type=request_type,
	    async_request=True)
