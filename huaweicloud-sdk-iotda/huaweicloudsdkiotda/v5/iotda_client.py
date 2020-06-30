# coding: utf-8

from __future__ import absolute_import

import datetime
import re
import importlib

import six

from huaweicloudsdkcore.client import Client
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkcore.utils import http_utils


class IoTDAClient(Client):
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
        super(IoTDAClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkiotda.v5.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}



    def create_batch_task(self, request):
        """创建批量任务

        应用服务器可调用此接口为创建批量处理任务，对多个设备进行批量操作。当前支持批量软固件升级、批量创建设备、批量删除设备、批量冻结设备、批量解冻设备。

        :param CreateBatchTaskRequest request
        :return: CreateBatchTaskResponse
        """
        return self.create_batch_task_with_http_info(request)

    def create_batch_task_with_http_info(self, request):
        """创建批量任务

        应用服务器可调用此接口为创建批量处理任务，对多个设备进行批量操作。当前支持批量软固件升级、批量创建设备、批量删除设备、批量冻结设备、批量解冻设备。

        :param CreateBatchTaskRequest request
        :return: tuple(CreateBatchTaskResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['create_batch_task_request_body', 'instance_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])
        auth_settings = []

        return self.call_api(
            '/v5/iot/{project_id}/batchtasks', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateBatchTaskResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_batch_tasks(self, request):
        """查询批量任务列表

        应用服务器可调用此接口查询物联网平台中批量任务列表，每一个任务又包括具体的任务内容、任务状态、任务完成情况统计等。

        :param ListBatchTasksRequest request
        :return: ListBatchTasksResponse
        """
        return self.list_batch_tasks_with_http_info(request)

    def list_batch_tasks_with_http_info(self, request):
        """查询批量任务列表

        应用服务器可调用此接口查询物联网平台中批量任务列表，每一个任务又包括具体的任务内容、任务状态、任务完成情况统计等。

        :param ListBatchTasksRequest request
        :return: tuple(ListBatchTasksResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['task_type', 'instance_id', 'app_id', 'status', 'limit', 'marker', 'offset']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'app_id' in local_var_params:
            query_params.append(('app_id', local_var_params['app_id']))
        if 'task_type' in local_var_params:
            query_params.append(('task_type', local_var_params['task_type']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            '/v5/iot/{project_id}/batchtasks', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListBatchTasksResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_batch_task(self, request):
        """查询批量任务

        应用服务器可调用此接口查询物联网平台中指定批量任务的信息，包括任务内容、任务状态、任务完成情况统计以及子任务列表等。

        :param ShowBatchTaskRequest request
        :return: ShowBatchTaskResponse
        """
        return self.show_batch_task_with_http_info(request)

    def show_batch_task_with_http_info(self, request):
        """查询批量任务

        应用服务器可调用此接口查询物联网平台中指定批量任务的信息，包括任务内容、任务状态、任务完成情况统计以及子任务列表等。

        :param ShowBatchTaskRequest request
        :return: tuple(ShowBatchTaskResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['task_id', 'instance_id', 'limit', 'marker', 'offset']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            '/v5/iot/{project_id}/batchtasks/{task_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowBatchTaskResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def add_certificate(self, request):
        """上传设备CA证书

        应用服务器可调用此接口在物联网平台上传设备的CA证书

        :param AddCertificateRequest request
        :return: AddCertificateResponse
        """
        return self.add_certificate_with_http_info(request)

    def add_certificate_with_http_info(self, request):
        """上传设备CA证书

        应用服务器可调用此接口在物联网平台上传设备的CA证书

        :param AddCertificateRequest request
        :return: tuple(AddCertificateResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['add_certificate_request_body', 'instance_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])
        auth_settings = []

        return self.call_api(
            '/v5/iot/{project_id}/certificates', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='AddCertificateResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def check_certificate(self, request):
        """验证设备CA证书

        应用服务器可调用此接口在物联网平台验证设备的CA证书，目的是为了验证用户持有设备CA证书的私钥

        :param CheckCertificateRequest request
        :return: str
        """
        return self.check_certificate_with_http_info(request)

    def check_certificate_with_http_info(self, request):
        """验证设备CA证书

        应用服务器可调用此接口在物联网平台验证设备的CA证书，目的是为了验证用户持有设备CA证书的私钥

        :param CheckCertificateRequest request
        :return: tuple(str, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['certificate_id', 'action_id', 'check_certificate_request_body', 'instance_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'certificate_id' in local_var_params:
            path_params['certificate_id'] = local_var_params['certificate_id']

        query_params = []
        if 'action_id' in local_var_params:
            query_params.append(('action_id', local_var_params['action_id']))

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])
        auth_settings = []

        return self.call_api(
            '/v5/iot/{project_id}/certificates/{certificate_id}/action', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='str',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_certificate(self, request):
        """删除设备CA证书

        应用服务器可调用此接口在物联网平台删除设备的CA证书

        :param DeleteCertificateRequest request
        :return: str
        """
        return self.delete_certificate_with_http_info(request)

    def delete_certificate_with_http_info(self, request):
        """删除设备CA证书

        应用服务器可调用此接口在物联网平台删除设备的CA证书

        :param DeleteCertificateRequest request
        :return: tuple(str, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['certificate_id', 'instance_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'certificate_id' in local_var_params:
            path_params['certificate_id'] = local_var_params['certificate_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            '/v5/iot/{project_id}/certificates/{certificate_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='str',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_certificates(self, request):
        """获取设备CA证书列表

        应用服务器可调用此接口在物联网平台获取设备的CA证书列表

        :param ListCertificatesRequest request
        :return: ListCertificatesResponse
        """
        return self.list_certificates_with_http_info(request)

    def list_certificates_with_http_info(self, request):
        """获取设备CA证书列表

        应用服务器可调用此接口在物联网平台获取设备的CA证书列表

        :param ListCertificatesRequest request
        :return: tuple(ListCertificatesResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['instance_id', 'app_id', 'limit', 'marker', 'offset']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'app_id' in local_var_params:
            query_params.append(('app_id', local_var_params['app_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            '/v5/iot/{project_id}/certificates', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListCertificatesResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_command(self, request):
        """下发设备命令

        设备的产品模型中定义了物联网平台可向设备下发的命令，应用服务器可调用此接口向指定设备下发命令，以实现对设备的同步控制。平台负责将命令以同步方式发送给设备，并将设备执行命令结果同步返回, 如果设备没有响应，平台会返回给应用服务器超时。注意：此接口适用于MQTT设备同步命令下发，暂不支持NB-IoT设备异步命令下发。 

        :param CreateCommandRequest request
        :return: CreateCommandResponse
        """
        return self.create_command_with_http_info(request)

    def create_command_with_http_info(self, request):
        """下发设备命令

        设备的产品模型中定义了物联网平台可向设备下发的命令，应用服务器可调用此接口向指定设备下发命令，以实现对设备的同步控制。平台负责将命令以同步方式发送给设备，并将设备执行命令结果同步返回, 如果设备没有响应，平台会返回给应用服务器超时。注意：此接口适用于MQTT设备同步命令下发，暂不支持NB-IoT设备异步命令下发。 

        :param CreateCommandRequest request
        :return: tuple(CreateCommandResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['device_id', 'create_command_request_body', 'instance_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'device_id' in local_var_params:
            path_params['device_id'] = local_var_params['device_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])
        auth_settings = []

        return self.call_api(
            '/v5/iot/{project_id}/devices/{device_id}/commands', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateCommandResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_commands(self, request):
        """查询设备命令

        查询设备下发的同步命令，每个设备最多支持查询20条最新下发的命令。 

        :param ListCommandsRequest request
        :return: ListCommandsResponse
        """
        return self.list_commands_with_http_info(request)

    def list_commands_with_http_info(self, request):
        """查询设备命令

        查询设备下发的同步命令，每个设备最多支持查询20条最新下发的命令。 

        :param ListCommandsRequest request
        :return: tuple(ListCommandsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['device_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'device_id' in local_var_params:
            path_params['device_id'] = local_var_params['device_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            '/v5/iot/{project_id}/devices/{device_id}/commands', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListCommandsResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def add_device_group(self, request):
        """添加设备组

        应用服务器可调用此接口新建设备组，一个华为云账号下最多可有1,000个分组，包括父分组和子分组。设备组的最大层级关系不超过5层，即群组形成的关系树最大深度不超过5。

        :param AddDeviceGroupRequest request
        :return: AddDeviceGroupResponse
        """
        return self.add_device_group_with_http_info(request)

    def add_device_group_with_http_info(self, request):
        """添加设备组

        应用服务器可调用此接口新建设备组，一个华为云账号下最多可有1,000个分组，包括父分组和子分组。设备组的最大层级关系不超过5层，即群组形成的关系树最大深度不超过5。

        :param AddDeviceGroupRequest request
        :return: tuple(AddDeviceGroupResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['instance_id', 'add_device_group_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])
        auth_settings = []

        return self.call_api(
            '/v5/iot/{project_id}/device-group', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='AddDeviceGroupResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_or_delete_device_in_group(self, request):
        """管理设备组中的设备

        应用服务器可调用此接口管理设备组中的设备。单个设备组内最多添加20,000个设备，一个设备最多可以被添加到10个设备组中。

        :param CreateOrDeleteDeviceInGroupRequest request
        :return: str
        """
        return self.create_or_delete_device_in_group_with_http_info(request)

    def create_or_delete_device_in_group_with_http_info(self, request):
        """管理设备组中的设备

        应用服务器可调用此接口管理设备组中的设备。单个设备组内最多添加20,000个设备，一个设备最多可以被添加到10个设备组中。

        :param CreateOrDeleteDeviceInGroupRequest request
        :return: tuple(str, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['group_id', 'action_id', 'device_id', 'instance_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

        query_params = []
        if 'action_id' in local_var_params:
            query_params.append(('action_id', local_var_params['action_id']))
        if 'device_id' in local_var_params:
            query_params.append(('device_id', local_var_params['device_id']))

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            '/v5/iot/{project_id}/device-group/{group_id}/action', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='str',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_device_group(self, request):
        """删除设备组

        应用服务器可调用此接口删除指定设备组，如果该设备组存在子设备组或者该设备组中存在设备，必须先删除子设备组并将设备从该设备组移除，才能删除该设备组。

        :param DeleteDeviceGroupRequest request
        :return: str
        """
        return self.delete_device_group_with_http_info(request)

    def delete_device_group_with_http_info(self, request):
        """删除设备组

        应用服务器可调用此接口删除指定设备组，如果该设备组存在子设备组或者该设备组中存在设备，必须先删除子设备组并将设备从该设备组移除，才能删除该设备组。

        :param DeleteDeviceGroupRequest request
        :return: tuple(str, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['group_id', 'instance_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            '/v5/iot/{project_id}/device-group/{group_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='str',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_device_groups(self, request):
        """查询设备组列表

        应用服务器可调用此接口查询物联网平台中的设备组信息列表。

        :param ListDeviceGroupsRequest request
        :return: ListDeviceGroupsResponse
        """
        return self.list_device_groups_with_http_info(request)

    def list_device_groups_with_http_info(self, request):
        """查询设备组列表

        应用服务器可调用此接口查询物联网平台中的设备组信息列表。

        :param ListDeviceGroupsRequest request
        :return: tuple(ListDeviceGroupsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['instance_id', 'limit', 'marker', 'offset', 'last_modified_time', 'app_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'last_modified_time' in local_var_params:
            query_params.append(('last_modified_time', local_var_params['last_modified_time']))
        if 'app_id' in local_var_params:
            query_params.append(('app_id', local_var_params['app_id']))

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            '/v5/iot/{project_id}/device-group', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListDeviceGroupsResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_device_group(self, request):
        """查询设备组

        应用服务器可调用此接口查询指定设备组详情。

        :param ShowDeviceGroupRequest request
        :return: ShowDeviceGroupResponse
        """
        return self.show_device_group_with_http_info(request)

    def show_device_group_with_http_info(self, request):
        """查询设备组

        应用服务器可调用此接口查询指定设备组详情。

        :param ShowDeviceGroupRequest request
        :return: tuple(ShowDeviceGroupResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['group_id', 'instance_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            '/v5/iot/{project_id}/device-group/{group_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowDeviceGroupResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_devices_in_group(self, request):
        """查询设备组设备列表

        应用服务器可调用此接口查询指定设备组下的设备列表。

        :param ShowDevicesInGroupRequest request
        :return: ShowDevicesInGroupResponse
        """
        return self.show_devices_in_group_with_http_info(request)

    def show_devices_in_group_with_http_info(self, request):
        """查询设备组设备列表

        应用服务器可调用此接口查询指定设备组下的设备列表。

        :param ShowDevicesInGroupRequest request
        :return: tuple(ShowDevicesInGroupResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['group_id', 'instance_id', 'limit', 'marker', 'offset']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            '/v5/iot/{project_id}/device-group/{group_id}/devices', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowDevicesInGroupResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_device_group(self, request):
        """修改设备组

        应用服务器可调用此接口修改物联网平台中指定设备组。

        :param UpdateDeviceGroupRequest request
        :return: UpdateDeviceGroupResponse
        """
        return self.update_device_group_with_http_info(request)

    def update_device_group_with_http_info(self, request):
        """修改设备组

        应用服务器可调用此接口修改物联网平台中指定设备组。

        :param UpdateDeviceGroupRequest request
        :return: tuple(UpdateDeviceGroupResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['group_id', 'update_device_group_request_body', 'instance_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])
        auth_settings = []

        return self.call_api(
            '/v5/iot/{project_id}/device-group/{group_id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateDeviceGroupResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def add_device(self, request):
        """创建设备

        应用服务器可调用此接口在物联网平台创建一个设备，仅在创建后设备才可以接入物联网平台。  - 该接口支持使用gateway_id参数指定在父设备下创建一个子设备，并且支持多级子设备，当前最大支持二级子设备。 - 该接口同时还支持对设备进行初始配置，接口会读取创建设备请求参数product_id对应的产品详情，如果产品的属性有定义默认值，则会将该属性默认值写入该设备的设备影子中。 - 用户还可以使用创建设备请求参数shadow字段为设备指定初始配置，指定后将会根据service_id和desired设置的属性值与产品中对应属性的默认值比对，如果不同，则将以shadow字段中设置的属性值为准写入到设备影子中。

        :param AddDeviceRequest request
        :return: AddDeviceResponse
        """
        return self.add_device_with_http_info(request)

    def add_device_with_http_info(self, request):
        """创建设备

        应用服务器可调用此接口在物联网平台创建一个设备，仅在创建后设备才可以接入物联网平台。  - 该接口支持使用gateway_id参数指定在父设备下创建一个子设备，并且支持多级子设备，当前最大支持二级子设备。 - 该接口同时还支持对设备进行初始配置，接口会读取创建设备请求参数product_id对应的产品详情，如果产品的属性有定义默认值，则会将该属性默认值写入该设备的设备影子中。 - 用户还可以使用创建设备请求参数shadow字段为设备指定初始配置，指定后将会根据service_id和desired设置的属性值与产品中对应属性的默认值比对，如果不同，则将以shadow字段中设置的属性值为准写入到设备影子中。

        :param AddDeviceRequest request
        :return: tuple(AddDeviceResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['add_device_request_body', 'instance_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])
        auth_settings = []

        return self.call_api(
            '/v5/iot/{project_id}/devices', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='AddDeviceResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_device(self, request):
        """删除设备

        应用服务器可调用此接口在物联网平台上删除指定设备。若设备下连接了非直连设备，则必须把设备下的非直连设备都删除后，才能删除该设备。

        :param DeleteDeviceRequest request
        :return: str
        """
        return self.delete_device_with_http_info(request)

    def delete_device_with_http_info(self, request):
        """删除设备

        应用服务器可调用此接口在物联网平台上删除指定设备。若设备下连接了非直连设备，则必须把设备下的非直连设备都删除后，才能删除该设备。

        :param DeleteDeviceRequest request
        :return: tuple(str, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['device_id', 'instance_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'device_id' in local_var_params:
            path_params['device_id'] = local_var_params['device_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            '/v5/iot/{project_id}/devices/{device_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='str',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def freeze_device(self, request):
        """冻结设备

        应用服务器可调用此接口冻结设备，设备冻结后不能再连接上线，可以通过解冻设备接口解除设备冻结。注意，当前仅支持冻结与平台直连的设备。

        :param FreezeDeviceRequest request
        :return: str
        """
        return self.freeze_device_with_http_info(request)

    def freeze_device_with_http_info(self, request):
        """冻结设备

        应用服务器可调用此接口冻结设备，设备冻结后不能再连接上线，可以通过解冻设备接口解除设备冻结。注意，当前仅支持冻结与平台直连的设备。

        :param FreezeDeviceRequest request
        :return: tuple(str, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['device_id', 'instance_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'device_id' in local_var_params:
            path_params['device_id'] = local_var_params['device_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            '/v5/iot/{project_id}/devices/{device_id}/freeze', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='str',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_devices(self, request):
        """查询设备列表

        应用服务器可调用此接口查询物联网平台中的设备信息列表。

        :param ListDevicesRequest request
        :return: ListDevicesResponse
        """
        return self.list_devices_with_http_info(request)

    def list_devices_with_http_info(self, request):
        """查询设备列表

        应用服务器可调用此接口查询物联网平台中的设备信息列表。

        :param ListDevicesRequest request
        :return: tuple(ListDevicesResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['instance_id', 'product_id', 'gateway_id', 'is_cascade_query', 'node_id', 'device_name', 'limit', 'marker', 'offset', 'start_time', 'end_time', 'app_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'product_id' in local_var_params:
            query_params.append(('product_id', local_var_params['product_id']))
        if 'gateway_id' in local_var_params:
            query_params.append(('gateway_id', local_var_params['gateway_id']))
        if 'is_cascade_query' in local_var_params:
            query_params.append(('is_cascade_query', local_var_params['is_cascade_query']))
        if 'node_id' in local_var_params:
            query_params.append(('node_id', local_var_params['node_id']))
        if 'device_name' in local_var_params:
            query_params.append(('device_name', local_var_params['device_name']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'app_id' in local_var_params:
            query_params.append(('app_id', local_var_params['app_id']))

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            '/v5/iot/{project_id}/devices', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListDevicesResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def reset_device_secret(self, request):
        """重置设备密钥

        应用服务器可调用此接口重置设备密钥，携带指定密钥时平台将设备密钥重置为指定的密钥，不携带密钥时平台将自动生成一个新的随机密钥返回。

        :param ResetDeviceSecretRequest request
        :return: ResetDeviceSecretResponse
        """
        return self.reset_device_secret_with_http_info(request)

    def reset_device_secret_with_http_info(self, request):
        """重置设备密钥

        应用服务器可调用此接口重置设备密钥，携带指定密钥时平台将设备密钥重置为指定的密钥，不携带密钥时平台将自动生成一个新的随机密钥返回。

        :param ResetDeviceSecretRequest request
        :return: tuple(ResetDeviceSecretResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['device_id', 'action_id', 'reset_device_secret_request_body', 'instance_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'device_id' in local_var_params:
            path_params['device_id'] = local_var_params['device_id']

        query_params = []
        if 'action_id' in local_var_params:
            query_params.append(('action_id', local_var_params['action_id']))

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])
        auth_settings = []

        return self.call_api(
            '/v5/iot/{project_id}/devices/{device_id}/action', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ResetDeviceSecretResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_device(self, request):
        """查询设备

        应用服务器可调用此接口查询物联网平台中指定设备的详细信息。

        :param ShowDeviceRequest request
        :return: ShowDeviceResponse
        """
        return self.show_device_with_http_info(request)

    def show_device_with_http_info(self, request):
        """查询设备

        应用服务器可调用此接口查询物联网平台中指定设备的详细信息。

        :param ShowDeviceRequest request
        :return: tuple(ShowDeviceResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['device_id', 'instance_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'device_id' in local_var_params:
            path_params['device_id'] = local_var_params['device_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            '/v5/iot/{project_id}/devices/{device_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowDeviceResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def unfreeze_device(self, request):
        """解冻设备

        应用服务器可调用此接口解冻设备，解除冻结后，设备可以连接上线。

        :param UnfreezeDeviceRequest request
        :return: str
        """
        return self.unfreeze_device_with_http_info(request)

    def unfreeze_device_with_http_info(self, request):
        """解冻设备

        应用服务器可调用此接口解冻设备，解除冻结后，设备可以连接上线。

        :param UnfreezeDeviceRequest request
        :return: tuple(str, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['device_id', 'instance_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'device_id' in local_var_params:
            path_params['device_id'] = local_var_params['device_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            '/v5/iot/{project_id}/devices/{device_id}/unfreeze', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='str',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_device(self, request):
        """修改设备

        应用服务器可调用此接口修改物联网平台中指定设备的基本信息。

        :param UpdateDeviceRequest request
        :return: UpdateDeviceResponse
        """
        return self.update_device_with_http_info(request)

    def update_device_with_http_info(self, request):
        """修改设备

        应用服务器可调用此接口修改物联网平台中指定设备的基本信息。

        :param UpdateDeviceRequest request
        :return: tuple(UpdateDeviceResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['device_id', 'update_device_request_body', 'instance_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'device_id' in local_var_params:
            path_params['device_id'] = local_var_params['device_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])
        auth_settings = []

        return self.call_api(
            '/v5/iot/{project_id}/devices/{device_id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateDeviceResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_device_shadow(self, request):
        """查询设备影子数据

        应用服务器可调用此接口查询指定设备的设备影子信息，包括对设备的期望属性信息（desired区）和设备最新上报的属性信息（reported区）。  设备影子介绍： 设备影子是一个用于存储和检索设备当前状态信息的JSON文档。 - 每个设备有且只有一个设备影子，由设备ID唯一标识 - 设备影子仅保存最近一次设备的上报数据和预期数据 - 无论该设备是否在线，都可以通过该影子获取和设置设备的属性 - 设备上线或者设备上报属性时，如果desired区和reported区存在差异，则将差异部分下发给设备，配置的预期属性需在产品模型中定义且method具有可写属性“W”才可下发 

        :param ShowDeviceShadowRequest request
        :return: ShowDeviceShadowResponse
        """
        return self.show_device_shadow_with_http_info(request)

    def show_device_shadow_with_http_info(self, request):
        """查询设备影子数据

        应用服务器可调用此接口查询指定设备的设备影子信息，包括对设备的期望属性信息（desired区）和设备最新上报的属性信息（reported区）。  设备影子介绍： 设备影子是一个用于存储和检索设备当前状态信息的JSON文档。 - 每个设备有且只有一个设备影子，由设备ID唯一标识 - 设备影子仅保存最近一次设备的上报数据和预期数据 - 无论该设备是否在线，都可以通过该影子获取和设置设备的属性 - 设备上线或者设备上报属性时，如果desired区和reported区存在差异，则将差异部分下发给设备，配置的预期属性需在产品模型中定义且method具有可写属性“W”才可下发 

        :param ShowDeviceShadowRequest request
        :return: tuple(ShowDeviceShadowResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['device_id', 'instance_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'device_id' in local_var_params:
            path_params['device_id'] = local_var_params['device_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            '/v5/iot/{project_id}/devices/{device_id}/shadow', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowDeviceShadowResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_device_shadow_desired_data(self, request):
        """配置设备影子预期数据

        应用服务器可调用此接口配置设备影子的预期属性（desired区），当设备上线或者设备上报属性时把属性下发给设备。  设备影子介绍： 设备影子是一个用于存储和检索设备当前状态信息的JSON文档。 - 每个设备有且只有一个设备影子，由设备ID唯一标识 - 设备影子仅保存最近一次设备的上报数据和预期数据 - 无论该设备是否在线，都可以通过该影子获取和设置设备的属性 - 设备上线或者设备上报属性时，如果desired区和reported区存在差异，则将差异部分下发给设备，配置的预期属性需在产品模型中定义且method具有可写属性“W”才可下发 

        :param UpdateDeviceShadowDesiredDataRequest request
        :return: UpdateDeviceShadowDesiredDataResponse
        """
        return self.update_device_shadow_desired_data_with_http_info(request)

    def update_device_shadow_desired_data_with_http_info(self, request):
        """配置设备影子预期数据

        应用服务器可调用此接口配置设备影子的预期属性（desired区），当设备上线或者设备上报属性时把属性下发给设备。  设备影子介绍： 设备影子是一个用于存储和检索设备当前状态信息的JSON文档。 - 每个设备有且只有一个设备影子，由设备ID唯一标识 - 设备影子仅保存最近一次设备的上报数据和预期数据 - 无论该设备是否在线，都可以通过该影子获取和设置设备的属性 - 设备上线或者设备上报属性时，如果desired区和reported区存在差异，则将差异部分下发给设备，配置的预期属性需在产品模型中定义且method具有可写属性“W”才可下发 

        :param UpdateDeviceShadowDesiredDataRequest request
        :return: tuple(UpdateDeviceShadowDesiredDataResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['device_id', 'update_device_shadow_desired_data_request_body', 'instance_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'device_id' in local_var_params:
            path_params['device_id'] = local_var_params['device_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])
        auth_settings = []

        return self.call_api(
            '/v5/iot/{project_id}/devices/{device_id}/shadow', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateDeviceShadowDesiredDataResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_message(self, request):
        """下发设备消息

        物联网平台可向设备下发消息，应用服务器可调用此接口向指定设备下发消息，以实现对设备的控制。应用将消息下发给平台后，平台返回应用响应结果，平台再将消息发送给设备。 

        :param CreateMessageRequest request
        :return: CreateMessageResponse
        """
        return self.create_message_with_http_info(request)

    def create_message_with_http_info(self, request):
        """下发设备消息

        物联网平台可向设备下发消息，应用服务器可调用此接口向指定设备下发消息，以实现对设备的控制。应用将消息下发给平台后，平台返回应用响应结果，平台再将消息发送给设备。 

        :param CreateMessageRequest request
        :return: tuple(CreateMessageResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['device_id', 'create_message_request_body', 'instance_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'device_id' in local_var_params:
            path_params['device_id'] = local_var_params['device_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])
        auth_settings = []

        return self.call_api(
            '/v5/iot/{project_id}/devices/{device_id}/messages', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateMessageResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_device_messages(self, request):
        """查询设备消息

        物联网平台可查询指定设备下的消息，平台为每个设备默认最多保存20条消息，超过20条后， 后续的消息会替换下发最早的消息。 

        :param ListDeviceMessagesRequest request
        :return: ListDeviceMessagesResponse
        """
        return self.list_device_messages_with_http_info(request)

    def list_device_messages_with_http_info(self, request):
        """查询设备消息

        物联网平台可查询指定设备下的消息，平台为每个设备默认最多保存20条消息，超过20条后， 后续的消息会替换下发最早的消息。 

        :param ListDeviceMessagesRequest request
        :return: tuple(ListDeviceMessagesResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['device_id', 'instance_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'device_id' in local_var_params:
            path_params['device_id'] = local_var_params['device_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            '/v5/iot/{project_id}/devices/{device_id}/messages', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListDeviceMessagesResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_device_message(self, request):
        """查询指定消息id的消息

        物联网平台可查询指定消息id的消息。 

        :param ShowDeviceMessageRequest request
        :return: ShowDeviceMessageResponse
        """
        return self.show_device_message_with_http_info(request)

    def show_device_message_with_http_info(self, request):
        """查询指定消息id的消息

        物联网平台可查询指定消息id的消息。 

        :param ShowDeviceMessageRequest request
        :return: tuple(ShowDeviceMessageResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['device_id', 'message_id', 'instance_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'device_id' in local_var_params:
            path_params['device_id'] = local_var_params['device_id']
        if 'message_id' in local_var_params:
            path_params['message_id'] = local_var_params['message_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            '/v5/iot/{project_id}/devices/{device_id}/messages/{message_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowDeviceMessageResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_product(self, request):
        """创建产品

        应用服务器可调用此接口创建产品。

        :param CreateProductRequest request
        :return: CreateProductResponse
        """
        return self.create_product_with_http_info(request)

    def create_product_with_http_info(self, request):
        """创建产品

        应用服务器可调用此接口创建产品。

        :param CreateProductRequest request
        :return: tuple(CreateProductResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['instance_id', 'create_product_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v5/iot/{project_id}/products', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateProductResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_product(self, request):
        """删除产品

        应用服务器可调用此接口删除已导入物联网平台的指定产品模型。

        :param DeleteProductRequest request
        :return: str
        """
        return self.delete_product_with_http_info(request)

    def delete_product_with_http_info(self, request):
        """删除产品

        应用服务器可调用此接口删除已导入物联网平台的指定产品模型。

        :param DeleteProductRequest request
        :return: tuple(str, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['product_id', 'instance_id', 'app_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'product_id' in local_var_params:
            path_params['product_id'] = local_var_params['product_id']

        query_params = []
        if 'app_id' in local_var_params:
            query_params.append(('app_id', local_var_params['app_id']))

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            '/v5/iot/{project_id}/products/{product_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='str',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_products(self, request):
        """查询产品列表

        应用服务器可调用此接口查询已导入物联网平台的产品模型信息列表，了解产品模型的概要信息。

        :param ListProductsRequest request
        :return: ListProductsResponse
        """
        return self.list_products_with_http_info(request)

    def list_products_with_http_info(self, request):
        """查询产品列表

        应用服务器可调用此接口查询已导入物联网平台的产品模型信息列表，了解产品模型的概要信息。

        :param ListProductsRequest request
        :return: tuple(ListProductsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['instance_id', 'limit', 'marker', 'app_id', 'offset']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'app_id' in local_var_params:
            query_params.append(('app_id', local_var_params['app_id']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            '/v5/iot/{project_id}/products', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListProductsResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_product(self, request):
        """查询产品

        应用服务器可调用此接口查询已导入物联网平台的指定产品模型详细信息，包括产品模型的服务、属性、命令等。

        :param ShowProductRequest request
        :return: ShowProductResponse
        """
        return self.show_product_with_http_info(request)

    def show_product_with_http_info(self, request):
        """查询产品

        应用服务器可调用此接口查询已导入物联网平台的指定产品模型详细信息，包括产品模型的服务、属性、命令等。

        :param ShowProductRequest request
        :return: tuple(ShowProductResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['product_id', 'instance_id', 'app_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'product_id' in local_var_params:
            path_params['product_id'] = local_var_params['product_id']

        query_params = []
        if 'app_id' in local_var_params:
            query_params.append(('app_id', local_var_params['app_id']))

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            '/v5/iot/{project_id}/products/{product_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowProductResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_product(self, request):
        """修改产品

        应用服务器可调用此接口修改已导入物联网平台的指定产品模型，包括产品模型的服务、属性、命令等。

        :param UpdateProductRequest request
        :return: UpdateProductResponse
        """
        return self.update_product_with_http_info(request)

    def update_product_with_http_info(self, request):
        """修改产品

        应用服务器可调用此接口修改已导入物联网平台的指定产品模型，包括产品模型的服务、属性、命令等。

        :param UpdateProductRequest request
        :return: tuple(UpdateProductResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['product_id', 'update_product_request_body', 'instance_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'product_id' in local_var_params:
            path_params['product_id'] = local_var_params['product_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v5/iot/{project_id}/products/{product_id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateProductResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_properties(self, request):
        """查询设备属性

        设备的产品模型中定义了物联网平台可向设备下发的属性，应用服务器可调用此接口查询指定设备下属性。 

        :param ListPropertiesRequest request
        :return: ListPropertiesResponse
        """
        return self.list_properties_with_http_info(request)

    def list_properties_with_http_info(self, request):
        """查询设备属性

        设备的产品模型中定义了物联网平台可向设备下发的属性，应用服务器可调用此接口查询指定设备下属性。 

        :param ListPropertiesRequest request
        :return: tuple(ListPropertiesResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['device_id', 'service_id', 'instance_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'device_id' in local_var_params:
            path_params['device_id'] = local_var_params['device_id']

        query_params = []
        if 'service_id' in local_var_params:
            query_params.append(('service_id', local_var_params['service_id']))

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            '/v5/iot/{project_id}/devices/{device_id}/properties', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListPropertiesResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_properties(self, request):
        """修改设备属性

        设备的产品模型中定义了物联网平台可向设备下发的属性，应用服务器可调用此接口向指定设备下属性。平台负责将属性以同步方式发送给设备，并将设备执行属性结果同步返回。 

        :param UpdatePropertiesRequest request
        :return: UpdatePropertiesResponse
        """
        return self.update_properties_with_http_info(request)

    def update_properties_with_http_info(self, request):
        """修改设备属性

        设备的产品模型中定义了物联网平台可向设备下发的属性，应用服务器可调用此接口向指定设备下属性。平台负责将属性以同步方式发送给设备，并将设备执行属性结果同步返回。 

        :param UpdatePropertiesRequest request
        :return: tuple(UpdatePropertiesResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['device_id', 'update_properties_request_body', 'instance_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'device_id' in local_var_params:
            path_params['device_id'] = local_var_params['device_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])
        auth_settings = []

        return self.call_api(
            '/v5/iot/{project_id}/devices/{device_id}/properties', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdatePropertiesResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def change_rule_status(self, request):
        """修改规则状态

        应用服务器可调用此接口修改物联网平台中指定规则的状态，激活或者去激活规则。

        :param ChangeRuleStatusRequest request
        :return: ChangeRuleStatusResponse
        """
        return self.change_rule_status_with_http_info(request)

    def change_rule_status_with_http_info(self, request):
        """修改规则状态

        应用服务器可调用此接口修改物联网平台中指定规则的状态，激活或者去激活规则。

        :param ChangeRuleStatusRequest request
        :return: tuple(ChangeRuleStatusResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['rule_id', 'change_rule_status_request_body', 'instance_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])
        auth_settings = []

        return self.call_api(
            '/v5/iot/{project_id}/rules/{rule_id}/status', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ChangeRuleStatusResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_rule(self, request):
        """创建规则

        应用服务器可调用此接口在物联网平台创建一条规则。

        :param CreateRuleRequest request
        :return: CreateRuleResponse
        """
        return self.create_rule_with_http_info(request)

    def create_rule_with_http_info(self, request):
        """创建规则

        应用服务器可调用此接口在物联网平台创建一条规则。

        :param CreateRuleRequest request
        :return: tuple(CreateRuleResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['create_rule_request_body', 'instance_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])
        auth_settings = []

        return self.call_api(
            '/v5/iot/{project_id}/rules', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateRuleResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_rule(self, request):
        """删除规则

        应用服务器可调用此接口删除物联网平台中的指定规则。

        :param DeleteRuleRequest request
        :return: str
        """
        return self.delete_rule_with_http_info(request)

    def delete_rule_with_http_info(self, request):
        """删除规则

        应用服务器可调用此接口删除物联网平台中的指定规则。

        :param DeleteRuleRequest request
        :return: tuple(str, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['rule_id', 'instance_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            '/v5/iot/{project_id}/rules/{rule_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='str',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_rules(self, request):
        """查询规则列表

        应用服务器可调用此接口查询物联网平台中设置的规则列表。

        :param ListRulesRequest request
        :return: ListRulesResponse
        """
        return self.list_rules_with_http_info(request)

    def list_rules_with_http_info(self, request):
        """查询规则列表

        应用服务器可调用此接口查询物联网平台中设置的规则列表。

        :param ListRulesRequest request
        :return: tuple(ListRulesResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['instance_id', 'app_id', 'limit', 'marker', 'offset']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'app_id' in local_var_params:
            query_params.append(('app_id', local_var_params['app_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            '/v5/iot/{project_id}/rules', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListRulesResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_rule(self, request):
        """查询规则

        应用服务器可调用此接口查询物联网平台中指定规则的配置信息。

        :param ShowRuleRequest request
        :return: ShowRuleResponse
        """
        return self.show_rule_with_http_info(request)

    def show_rule_with_http_info(self, request):
        """查询规则

        应用服务器可调用此接口查询物联网平台中指定规则的配置信息。

        :param ShowRuleRequest request
        :return: tuple(ShowRuleResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['rule_id', 'instance_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            '/v5/iot/{project_id}/rules/{rule_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowRuleResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_rule(self, request):
        """修改规则

        应用服务器可调用此接口修改物联网平台中指定规则的配置。

        :param UpdateRuleRequest request
        :return: UpdateRuleResponse
        """
        return self.update_rule_with_http_info(request)

    def update_rule_with_http_info(self, request):
        """修改规则

        应用服务器可调用此接口修改物联网平台中指定规则的配置。

        :param UpdateRuleRequest request
        :return: tuple(UpdateRuleResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['rule_id', 'update_rule_request_body', 'instance_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])
        auth_settings = []

        return self.call_api(
            '/v5/iot/{project_id}/rules/{rule_id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateRuleResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_subscription(self, request):
        """创建订阅

        应用服务器可调用此接口订阅物联网平台资源的变化事件，当资源发生变化时（如设备激活，设备数据更新等），平台会向应用服务器发送通知消息。

        :param CreateSubscriptionRequest request
        :return: CreateSubscriptionResponse
        """
        return self.create_subscription_with_http_info(request)

    def create_subscription_with_http_info(self, request):
        """创建订阅

        应用服务器可调用此接口订阅物联网平台资源的变化事件，当资源发生变化时（如设备激活，设备数据更新等），平台会向应用服务器发送通知消息。

        :param CreateSubscriptionRequest request
        :return: tuple(CreateSubscriptionResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['instance_id', 'create_subscription_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])
        auth_settings = []

        return self.call_api(
            '/v5/iot/{project_id}/subscriptions', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateSubscriptionResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_subscription(self, request):
        """删除订阅

        应用服务器可调用此接口删除物联网平台中的指定订阅配置。

        :param DeleteSubscriptionRequest request
        :return: str
        """
        return self.delete_subscription_with_http_info(request)

    def delete_subscription_with_http_info(self, request):
        """删除订阅

        应用服务器可调用此接口删除物联网平台中的指定订阅配置。

        :param DeleteSubscriptionRequest request
        :return: tuple(str, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['subscription_id', 'instance_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'subscription_id' in local_var_params:
            path_params['subscription_id'] = local_var_params['subscription_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            '/v5/iot/{project_id}/subscriptions/{subscription_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='str',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_subscriptions(self, request):
        """查询订阅列表

        应用服务器可调用此接口查询物联网平台中的订阅配置信息列表。

        :param ListSubscriptionsRequest request
        :return: ListSubscriptionsResponse
        """
        return self.list_subscriptions_with_http_info(request)

    def list_subscriptions_with_http_info(self, request):
        """查询订阅列表

        应用服务器可调用此接口查询物联网平台中的订阅配置信息列表。

        :param ListSubscriptionsRequest request
        :return: tuple(ListSubscriptionsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['instance_id', 'resource', 'event', 'callbackurl', 'app_id', 'channel', 'limit', 'marker', 'offset']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'resource' in local_var_params:
            query_params.append(('resource', local_var_params['resource']))
        if 'event' in local_var_params:
            query_params.append(('event', local_var_params['event']))
        if 'callbackurl' in local_var_params:
            query_params.append(('callbackurl', local_var_params['callbackurl']))
        if 'app_id' in local_var_params:
            query_params.append(('app_id', local_var_params['app_id']))
        if 'channel' in local_var_params:
            query_params.append(('channel', local_var_params['channel']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            '/v5/iot/{project_id}/subscriptions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListSubscriptionsResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_subscription(self, request):
        """查询订阅

        应用服务器可调用此接口查询物联网平台中指定订阅的配置信息。

        :param ShowSubscriptionRequest request
        :return: ShowSubscriptionResponse
        """
        return self.show_subscription_with_http_info(request)

    def show_subscription_with_http_info(self, request):
        """查询订阅

        应用服务器可调用此接口查询物联网平台中指定订阅的配置信息。

        :param ShowSubscriptionRequest request
        :return: tuple(ShowSubscriptionResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['subscription_id', 'instance_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'subscription_id' in local_var_params:
            path_params['subscription_id'] = local_var_params['subscription_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            '/v5/iot/{project_id}/subscriptions/{subscription_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowSubscriptionResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_subscription(self, request):
        """修改订阅

        应用服务器可调用此接口修改物联网平台中的指定订阅配置，当前仅支持修改订阅回调地址（callbackurl）。

        :param UpdateSubscriptionRequest request
        :return: UpdateSubscriptionResponse
        """
        return self.update_subscription_with_http_info(request)

    def update_subscription_with_http_info(self, request):
        """修改订阅

        应用服务器可调用此接口修改物联网平台中的指定订阅配置，当前仅支持修改订阅回调地址（callbackurl）。

        :param UpdateSubscriptionRequest request
        :return: tuple(UpdateSubscriptionResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['subscription_id', 'instance_id', 'update_subscription_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'subscription_id' in local_var_params:
            path_params['subscription_id'] = local_var_params['subscription_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])
        auth_settings = []

        return self.call_api(
            '/v5/iot/{project_id}/subscriptions/{subscription_id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateSubscriptionResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_resources_by_tags(self, request):
        """按标签查询资源

        应用服务器可调用此接口查询绑定了指定标签的资源。当前支持标签的资源有Device(设备)。

        :param ListResourcesByTagsRequest request
        :return: ListResourcesByTagsResponse
        """
        return self.list_resources_by_tags_with_http_info(request)

    def list_resources_by_tags_with_http_info(self, request):
        """按标签查询资源

        应用服务器可调用此接口查询绑定了指定标签的资源。当前支持标签的资源有Device(设备)。

        :param ListResourcesByTagsRequest request
        :return: tuple(ListResourcesByTagsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['instance_id', 'limit', 'marker', 'offset', 'list_resources_by_tags_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])
        auth_settings = []

        return self.call_api(
            '/v5/iot/{project_id}/tags/query-resources', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListResourcesByTagsResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def tag_device(self, request):
        """绑定标签

        应用服务器可调用此接口为指定资源绑定标签。当前支持标签的资源有Device(设备)。

        :param TagDeviceRequest request
        :return: str
        """
        return self.tag_device_with_http_info(request)

    def tag_device_with_http_info(self, request):
        """绑定标签

        应用服务器可调用此接口为指定资源绑定标签。当前支持标签的资源有Device(设备)。

        :param TagDeviceRequest request
        :return: tuple(str, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['instance_id', 'tag_device_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])
        auth_settings = []

        return self.call_api(
            '/v5/iot/{project_id}/tags/bind-resource', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='str',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def untag_device(self, request):
        """解绑标签

        应用服务器可调用此接口为指定资源解绑标签。当前支持标签的资源有Device(设备)。

        :param UntagDeviceRequest request
        :return: str
        """
        return self.untag_device_with_http_info(request)

    def untag_device_with_http_info(self, request):
        """解绑标签

        应用服务器可调用此接口为指定资源解绑标签。当前支持标签的资源有Device(设备)。

        :param UntagDeviceRequest request
        :return: tuple(str, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['instance_id', 'untag_device_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])
        auth_settings = []

        return self.call_api(
            '/v5/iot/{project_id}/tags/unbind-resource', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='str',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def call_api(self, resource_path, method, path_params=None, query_params=None, header_params=None,
                 body=None, post_params=None, response_type=None, auth_settings=None, collection_formats=None,
                 request_type=None):
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
        :param collection_formats: dict of collection formats for path, query,
            header, and post parameters.
        :return:
            Return the response directly.
        """
        return self.do_http_request(method, resource_path, path_params,
                                    query_params, header_params, body, post_params,
                                    response_type, collection_formats, request_type)
