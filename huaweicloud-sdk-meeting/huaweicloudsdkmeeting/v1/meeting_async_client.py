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


class MeetingAsyncClient(Client):
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
        super(MeetingAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkmeeting.v1.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls, "MeetingCredentials")

        if clazz.__name__ != "MeetingClient":
            raise TypeError("client type error, support client type is MeetingClient")

        return ClientBuilder(clazz, "MeetingCredentials")

    def add_corp_async(self, request):
        """SP管理员创建企业

        创建企业，默认管理员及分配资源。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for AddCorp
        :type request: :class:`huaweicloudsdkmeeting.v1.AddCorpRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.AddCorpResponse`
        """
        return self.add_corp_with_http_info(request)

    def add_corp_with_http_info(self, request):
        all_params = ['corp_dto', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/dcs/sp/corp',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='AddCorpResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def add_corp_admin_async(self, request):
        """添加企业管理员

        企业默认管理员添加企业普通管理员
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for AddCorpAdmin
        :type request: :class:`huaweicloudsdkmeeting.v1.AddCorpAdminRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.AddCorpAdminResponse`
        """
        return self.add_corp_admin_with_http_info(request)

    def add_corp_admin_with_http_info(self, request):
        all_params = ['admin_dto', 'x_request_id', 'accept_language', 'account_type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'account_type' in local_var_params:
            query_params.append(('accountType', local_var_params['account_type']))

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/dcs/corp/admin',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='AddCorpAdminResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def add_department_async(self, request):
        """添加部门

        企业管理员通过该接口添加部门，最多支持10级部门，每级子部门最多支持100个，默认企业最大部门数量为3000个。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for AddDepartment
        :type request: :class:`huaweicloudsdkmeeting.v1.AddDepartmentRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.AddDepartmentResponse`
        """
        return self.add_department_with_http_info(request)

    def add_department_with_http_info(self, request):
        all_params = ['dept_dto', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/dcs/corp/dept',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='AddDepartmentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def add_device_async(self, request):
        """增加终端

        企业管理员通过该接口添加硬终端。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for AddDevice
        :type request: :class:`huaweicloudsdkmeeting.v1.AddDeviceRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.AddDeviceResponse`
        """
        return self.add_device_with_http_info(request)

    def add_device_with_http_info(self, request):
        all_params = ['device_dto', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/dcs/corp/device',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='AddDeviceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def add_material_async(self, request):
        """新增信息窗素材

        新增信息窗素材（上传素材文件）
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for AddMaterial
        :type request: :class:`huaweicloudsdkmeeting.v1.AddMaterialRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.AddMaterialResponse`
        """
        return self.add_material_with_http_info(request)

    def add_material_with_http_info(self, request):
        all_params = ['file', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

        form_params = {}
        if 'file' in local_var_params:
            form_params['file'] = local_var_params['file']

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['multipart/form-data'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/usg/sss/materials',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='AddMaterialResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def add_program_async(self, request):
        """新增信息窗节目

        新增信息窗节目
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for AddProgram
        :type request: :class:`huaweicloudsdkmeeting.v1.AddProgramRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.AddProgramResponse`
        """
        return self.add_program_with_http_info(request)

    def add_program_with_http_info(self, request):
        all_params = ['program_dto', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/sss/programs',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='AddProgramResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def add_publication_async(self, request):
        """新增信息窗发布

        新增信息窗发布
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for AddPublication
        :type request: :class:`huaweicloudsdkmeeting.v1.AddPublicationRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.AddPublicationResponse`
        """
        return self.add_publication_with_http_info(request)

    def add_publication_with_http_info(self, request):
        all_params = ['publication_dto', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/sss/publications',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='AddPublicationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def add_resource_async(self, request):
        """SP管理员分配企业资源

        企业新增资源发放。优化适配，该接口同时支持修改，带resourceId后会判断该资源是否存在，存在即修改（支持修改的参数见修改接口），否则按新增处理
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for AddResource
        :type request: :class:`huaweicloudsdkmeeting.v1.AddResourceRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.AddResourceResponse`
        """
        return self.add_resource_with_http_info(request)

    def add_resource_with_http_info(self, request):
        all_params = ['corp_id', 'resource_list', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'corp_id' in local_var_params:
            path_params['corp_id'] = local_var_params['corp_id']

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/dcs/sp/corp/{corp_id}/resource',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='AddResourceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def add_to_personal_space_async(self, request):
        """保存会议纪要到个人云空间

        用户使用手机扫码后，手机端请求服务端将当前会议纪要文件保存到个人云空间。二维码内容  cloudlink://cloudlink.huawei.com/h5page?action&#x3D;SAVE_MEETING_FILE&amp;key1&#x3D;value1&amp;key2&#x3D;value2    key/value的个数可能变化，终端解析后，在发起后续请求时，将所有key/value存为map，作为入参即可。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for AddToPersonalSpace
        :type request: :class:`huaweicloudsdkmeeting.v1.AddToPersonalSpaceRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.AddToPersonalSpaceResponse`
        """
        return self.add_to_personal_space_with_http_info(request)

    def add_to_personal_space_with_http_info(self, request):
        all_params = ['info', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/sss/meeting-files/save-to-personal-space',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='AddToPersonalSpaceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def add_user_async(self, request):
        """添加用户

        企业管理员通过该接口添加企业用户。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for AddUser
        :type request: :class:`huaweicloudsdkmeeting.v1.AddUserRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.AddUserResponse`
        """
        return self.add_user_with_http_info(request)

    def add_user_with_http_info(self, request):
        all_params = ['user_dto', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/dcs/corp/member',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='AddUserResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def allow_guest_unmute_async(self, request):
        """与会者自己解除静音

        决定与会者是否可以自己解除静音。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for AllowGuestUnmute
        :type request: :class:`huaweicloudsdkmeeting.v1.AllowGuestUnmuteRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.AllowGuestUnmuteResponse`
        """
        return self.allow_guest_unmute_with_http_info(request)

    def allow_guest_unmute_with_http_info(self, request):
        all_params = ['conference_id', 'x_conference_authorization', 'req_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

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
            resource_path='/v1/mmc/control/conferences/mute/guestUnMute',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='AllowGuestUnmuteResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def associate_vmr_async(self, request):
        """分配云会议室

        企业管理员通过该接口将云会议室分配给用户、硬终端（当前仅支持分配TE10、TE20、HUAWEI Board、HUAWEI Bar 500及HUAWEI Box系列硬件终端）。云会议室分配给硬件终端后，需要重启或重新激活硬件终端。若需要管理云会议室、预约会议、录制会议或进行完整的会控操作，请同时将该云会议室分配给会议用户。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for AssociateVmr
        :type request: :class:`huaweicloudsdkmeeting.v1.AssociateVmrRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.AssociateVmrResponse`
        """
        return self.associate_vmr_with_http_info(request)

    def associate_vmr_with_http_info(self, request):
        all_params = ['account', 'assign_list', 'x_request_id', 'accept_language', 'account_type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'account' in local_var_params:
            path_params['account'] = local_var_params['account']

        query_params = []
        if 'account_type' in local_var_params:
            query_params.append(('accountType', local_var_params['account_type']))

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/dcs/corp/vmr/assign-to-member/{account}',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='AssociateVmrResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_delete_corp_admins_async(self, request):
        """批量删除企业管理员

        批量删除企业管理员
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for BatchDeleteCorpAdmins
        :type request: :class:`huaweicloudsdkmeeting.v1.BatchDeleteCorpAdminsRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.BatchDeleteCorpAdminsResponse`
        """
        return self.batch_delete_corp_admins_with_http_info(request)

    def batch_delete_corp_admins_with_http_info(self, request):
        all_params = ['del_list', 'x_request_id', 'accept_language', 'account_type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'account_type' in local_var_params:
            query_params.append(('accountType', local_var_params['account_type']))

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/dcs/corp/admin/delete',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchDeleteCorpAdminsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_delete_devices_async(self, request):
        """批量删除终端

        企业管理员通过该接口批量删除终端，返回删除失败的列表。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for BatchDeleteDevices
        :type request: :class:`huaweicloudsdkmeeting.v1.BatchDeleteDevicesRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.BatchDeleteDevicesResponse`
        """
        return self.batch_delete_devices_with_http_info(request)

    def batch_delete_devices_with_http_info(self, request):
        all_params = ['del_list', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/dcs/corp/device/delete',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchDeleteDevicesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_delete_materials_async(self, request):
        """删除信息窗素材

        删除信息窗素材
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for BatchDeleteMaterials
        :type request: :class:`huaweicloudsdkmeeting.v1.BatchDeleteMaterialsRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.BatchDeleteMaterialsResponse`
        """
        return self.batch_delete_materials_with_http_info(request)

    def batch_delete_materials_with_http_info(self, request):
        all_params = ['ids_request_dto', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/sss/materials/batch-delete',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchDeleteMaterialsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_delete_programs_async(self, request):
        """删除信息窗节目

        删除信息窗节目
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for BatchDeletePrograms
        :type request: :class:`huaweicloudsdkmeeting.v1.BatchDeleteProgramsRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.BatchDeleteProgramsResponse`
        """
        return self.batch_delete_programs_with_http_info(request)

    def batch_delete_programs_with_http_info(self, request):
        all_params = ['ids_request_dto', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/sss/programs/batch-delete',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchDeleteProgramsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_delete_publications_async(self, request):
        """删除信息窗发布

        删除信息窗发布
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for BatchDeletePublications
        :type request: :class:`huaweicloudsdkmeeting.v1.BatchDeletePublicationsRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.BatchDeletePublicationsResponse`
        """
        return self.batch_delete_publications_with_http_info(request)

    def batch_delete_publications_with_http_info(self, request):
        all_params = ['ids_request_dto', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/sss/publications/batch-delete',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchDeletePublicationsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_delete_users_async(self, request):
        """批量删除用户

        企业管理员通过该接口批量删除企业用户，全量成功或全量失败。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for BatchDeleteUsers
        :type request: :class:`huaweicloudsdkmeeting.v1.BatchDeleteUsersRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.BatchDeleteUsersResponse`
        """
        return self.batch_delete_users_with_http_info(request)

    def batch_delete_users_with_http_info(self, request):
        all_params = ['del_list', 'x_request_id', 'accept_language', 'account_type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'account_type' in local_var_params:
            query_params.append(('accountType', local_var_params['account_type']))

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/dcs/corp/member/delete',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchDeleteUsersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_update_devices_status_async(self, request):
        """批量修改终端状态

        批量修改终端状态
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for BatchUpdateDevicesStatus
        :type request: :class:`huaweicloudsdkmeeting.v1.BatchUpdateDevicesStatusRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.BatchUpdateDevicesStatusResponse`
        """
        return self.batch_update_devices_status_with_http_info(request)

    def batch_update_devices_status_with_http_info(self, request):
        all_params = ['value', 'sn_list', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'value' in local_var_params:
            path_params['value'] = local_var_params['value']

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/dcs/corp/device/status/{value}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchUpdateDevicesStatusResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_update_user_status_async(self, request):
        """批量修改用户状态

        企业管理员通过该接口批量修改用户状态，当用户账号数资源或者第三方电子白板资源到期后，若企业内对应资源的用户账号超过数量后会被系统随机自动停用，此时可通过该接口修改用户的状态。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for BatchUpdateUserStatus
        :type request: :class:`huaweicloudsdkmeeting.v1.BatchUpdateUserStatusRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.BatchUpdateUserStatusResponse`
        """
        return self.batch_update_user_status_with_http_info(request)

    def batch_update_user_status_with_http_info(self, request):
        all_params = ['value', 'account_list', 'x_request_id', 'accept_language', 'account_type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'value' in local_var_params:
            path_params['value'] = local_var_params['value']

        query_params = []
        if 'account_type' in local_var_params:
            query_params.append(('accountType', local_var_params['account_type']))

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/dcs/corp/member/status/{value}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchUpdateUserStatusResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def broadcast_participant_async(self, request):
        """广播会场

        同一时间，只允许一个与会者被广播。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for BroadcastParticipant
        :type request: :class:`huaweicloudsdkmeeting.v1.BroadcastParticipantRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.BroadcastParticipantResponse`
        """
        return self.broadcast_participant_with_http_info(request)

    def broadcast_participant_with_http_info(self, request):
        all_params = ['conference_id', 'participant_id', 'x_conference_authorization']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))
        if 'participant_id' in local_var_params:
            query_params.append(('participantID', local_var_params['participant_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/mmc/control/conferences/participants/broadcast',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BroadcastParticipantResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def cancel_meeting_async(self, request):
        """取消预约会议

        取消预约会议。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CancelMeeting
        :type request: :class:`huaweicloudsdkmeeting.v1.CancelMeetingRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.CancelMeetingResponse`
        """
        return self.cancel_meeting_with_http_info(request)

    def cancel_meeting_with_http_info(self, request):
        all_params = ['conference_id', 'user_uuid', 'type', 'x_authorization_type', 'x_site_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))
        if 'user_uuid' in local_var_params:
            query_params.append(('userUUID', local_var_params['user_uuid']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))

        header_params = {}
        if 'x_authorization_type' in local_var_params:
            header_params['X-Authorization-Type'] = local_var_params['x_authorization_type']
        if 'x_site_id' in local_var_params:
            header_params['X-Site-Id'] = local_var_params['x_site_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/mmc/management/conferences',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CancelMeetingResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def cancel_recurring_meeting_async(self, request):
        """取消周期会议

        管理员或UC账号可以通过该接口取消周期会议
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CancelRecurringMeeting
        :type request: :class:`huaweicloudsdkmeeting.v1.CancelRecurringMeetingRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.CancelRecurringMeetingResponse`
        """
        return self.cancel_recurring_meeting_with_http_info(request)

    def cancel_recurring_meeting_with_http_info(self, request):
        all_params = ['conference_id', 'x_authorization_type', 'user_uuid', 'x_site_id', 'type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_uuid' in local_var_params:
            query_params.append(('userUUID', local_var_params['user_uuid']))
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))

        header_params = {}
        if 'x_authorization_type' in local_var_params:
            header_params['X-Authorization-Type'] = local_var_params['x_authorization_type']
        if 'x_site_id' in local_var_params:
            header_params['X-Site-Id'] = local_var_params['x_site_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/mmc/management/cycleconferences',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CancelRecurringMeetingResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def cancel_recurring_sub_meeting_async(self, request):
        """取消周期子会议

        管理员或UC账号可以通过该接口取消周期会议
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CancelRecurringSubMeeting
        :type request: :class:`huaweicloudsdkmeeting.v1.CancelRecurringSubMeetingRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.CancelRecurringSubMeetingResponse`
        """
        return self.cancel_recurring_sub_meeting_with_http_info(request)

    def cancel_recurring_sub_meeting_with_http_info(self, request):
        all_params = ['conference_id', 'req_body', 'x_authorization_type', 'user_uuid', 'x_site_id', 'type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_uuid' in local_var_params:
            query_params.append(('userUUID', local_var_params['user_uuid']))
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))

        header_params = {}
        if 'x_authorization_type' in local_var_params:
            header_params['X-Authorization-Type'] = local_var_params['x_authorization_type']
        if 'x_site_id' in local_var_params:
            header_params['X-Site-Id'] = local_var_params['x_site_id']

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
            resource_path='/v1/mmc/management/conferences/cyclesubconf',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CancelRecurringSubMeetingResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def check_slide_verify_code_async(self, request):
        """校验滑块验证码

        该接口提供校验滑块验证码。服务器收到请求，返回校验结果。用户在前台界面通过滑块操作匹配图形，使得抠图和原图吻合。然后服务器进行校验滑块验证码。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CheckSlideVerifyCode
        :type request: :class:`huaweicloudsdkmeeting.v1.CheckSlideVerifyCodeRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.CheckSlideVerifyCodeResponse`
        """
        return self.check_slide_verify_code_with_http_info(request)

    def check_slide_verify_code_with_http_info(self, request):
        all_params = ['slide_verify_code_check_dto', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-ID'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/acs/auth/slideverifycode/check',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CheckSlideVerifyCodeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def check_token_async(self, request):
        """校验Token

        该接口提供校验token合法性功能。服务器收到请求后，验证token合法性并返回结果。如果参数needGenNewToken为true时，生成新的token并返回。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CheckToken
        :type request: :class:`huaweicloudsdkmeeting.v1.CheckTokenRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.CheckTokenResponse`
        """
        return self.check_token_with_http_info(request)

    def check_token_with_http_info(self, request):
        all_params = ['validate_token_req_dto', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-ID'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/acs/token/validate',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CheckTokenResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def check_veri_code_for_update_user_info_async(self, request):
        """校验手机和邮箱对应的验证码

        企业用户通过该接口校验手机和邮箱对应的验证码，一分钟内记录尝试次数不得超过5次。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CheckVeriCodeForUpdateUserInfo
        :type request: :class:`huaweicloudsdkmeeting.v1.CheckVeriCodeForUpdateUserInfoRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.CheckVeriCodeForUpdateUserInfoResponse`
        """
        return self.check_veri_code_for_update_user_info_with_http_info(request)

    def check_veri_code_for_update_user_info_with_http_info(self, request):
        all_params = ['verification_code_dto', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/dcs/member/verification-code/verify',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CheckVeriCodeForUpdateUserInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def check_verify_code_async(self, request):
        """校验验证码

        该接口提供校验验证码，服务器收到请求，返回结果。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CheckVerifyCode
        :type request: :class:`huaweicloudsdkmeeting.v1.CheckVerifyCodeRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.CheckVerifyCodeResponse`
        """
        return self.check_verify_code_with_http_info(request)

    def check_verify_code_with_http_info(self, request):
        all_params = ['verify_code_check_dto', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-ID'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/acs/verifycode/check',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CheckVerifyCodeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_anonymous_auth_random_async(self, request):
        """匿名用户会议鉴权

        未登陆终端，通过输入会议ID进行会议鉴权，返回鉴权随机数。如果需要密码则返回需要会议密码错误码，然后终端弹出输入会议ID输入框，用户输入密码后，终端再次调用该接口进行鉴权。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateAnonymousAuthRandom
        :type request: :class:`huaweicloudsdkmeeting.v1.CreateAnonymousAuthRandomRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.CreateAnonymousAuthRandomResponse`
        """
        return self.create_anonymous_auth_random_with_http_info(request)

    def create_anonymous_auth_random_with_http_info(self, request):
        all_params = ['conference_id', 'x_password']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))

        header_params = {}
        if 'x_password' in local_var_params:
            header_params['X-Password'] = local_var_params['x_password']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/mmc/management/conferences/anonymous/auth',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateAnonymousAuthRandomResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_conf_token_async(self, request):
        """获取会控Token

        获取会控授权令牌，然后会议会被拉起。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateConfToken
        :type request: :class:`huaweicloudsdkmeeting.v1.CreateConfTokenRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.CreateConfTokenResponse`
        """
        return self.create_conf_token_with_http_info(request)

    def create_conf_token_with_http_info(self, request):
        all_params = ['conference_id', 'x_password', 'x_login_type', 'x_conference_authorization', 'x_nonce']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']
        if 'x_password' in local_var_params:
            header_params['X-Password'] = local_var_params['x_password']
        if 'x_login_type' in local_var_params:
            header_params['X-Login-Type'] = local_var_params['x_login_type']
        if 'x_nonce' in local_var_params:
            header_params['X-Nonce'] = local_var_params['x_nonce']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/mmc/control/conferences/token',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateConfTokenResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_meeting_async(self, request):
        """创建会议

        您可根据需要创建立即会议和预约会议。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateMeeting
        :type request: :class:`huaweicloudsdkmeeting.v1.CreateMeetingRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.CreateMeetingResponse`
        """
        return self.create_meeting_with_http_info(request)

    def create_meeting_with_http_info(self, request):
        all_params = ['req_body', 'user_uuid', 'x_authorization_type', 'x_site_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_uuid' in local_var_params:
            query_params.append(('userUUID', local_var_params['user_uuid']))

        header_params = {}
        if 'x_authorization_type' in local_var_params:
            header_params['X-Authorization-Type'] = local_var_params['x_authorization_type']
        if 'x_site_id' in local_var_params:
            header_params['X-Site-Id'] = local_var_params['x_site_id']

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
            resource_path='/v1/mmc/management/conferences',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateMeetingResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_portal_ref_nonce_async(self, request):
        """获取页面免登陆跳转的nonce信息

        通过token生成页面免登陆跳转到华为云会议的Portal的nonce信息。获取到nonce信息后，通过链接https://bmeeting.huaweicloud.com/?lang&#x3D;zh-CN&amp;nonce&#x3D;xxxxxxxxxxxxx#/login进行免登陆跳转。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreatePortalRefNonce
        :type request: :class:`huaweicloudsdkmeeting.v1.CreatePortalRefNonceRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.CreatePortalRefNonceResponse`
        """
        return self.create_portal_ref_nonce_with_http_info(request)

    def create_portal_ref_nonce_with_http_info(self, request):
        all_params = ['x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/usg/acs/auth/portal-ref-nonce',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreatePortalRefNonceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_recurring_meeting_async(self, request):
        """创建周期会议

        管理员或UC账号可以通过该接口创建周期会议
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateRecurringMeeting
        :type request: :class:`huaweicloudsdkmeeting.v1.CreateRecurringMeetingRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.CreateRecurringMeetingResponse`
        """
        return self.create_recurring_meeting_with_http_info(request)

    def create_recurring_meeting_with_http_info(self, request):
        all_params = ['req_body', 'x_authorization_type', 'user_uuid', 'x_site_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_uuid' in local_var_params:
            query_params.append(('userUUID', local_var_params['user_uuid']))

        header_params = {}
        if 'x_authorization_type' in local_var_params:
            header_params['X-Authorization-Type'] = local_var_params['x_authorization_type']
        if 'x_site_id' in local_var_params:
            header_params['X-Site-Id'] = local_var_params['x_site_id']

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
            resource_path='/v1/mmc/management/cycleconferences',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateRecurringMeetingResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_vision_active_code_async(self, request):
        """企业管理员生成激活码

        企业管理员生成智慧屏、电子白板、Ideahub的激活码
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateVisionActiveCode
        :type request: :class:`huaweicloudsdkmeeting.v1.CreateVisionActiveCodeRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.CreateVisionActiveCodeResponse`
        """
        return self.create_vision_active_code_with_http_info(request)

    def create_vision_active_code_with_http_info(self, request):
        all_params = ['vision_activecode_dto', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/dcs/corp/vision/activecode',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateVisionActiveCodeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_web_socket_token_async(self, request):
        """获取websocket鉴权token

        获取websocket鉴权token。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateWebSocketToken
        :type request: :class:`huaweicloudsdkmeeting.v1.CreateWebSocketTokenRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.CreateWebSocketTokenResponse`
        """
        return self.create_web_socket_token_with_http_info(request)

    def create_web_socket_token_with_http_info(self, request):
        all_params = ['conference_id', 'x_conference_authorization']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/mmc/control/conferences/wsToken',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateWebSocketTokenResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_webinar_async(self, request):
        """预约网络研讨会

        您可根据需要预约网络研讨会。注意：暂不支持添加外部联系人作为与会嘉宾
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateWebinar
        :type request: :class:`huaweicloudsdkmeeting.v1.CreateWebinarRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.CreateWebinarResponse`
        """
        return self.create_webinar_with_http_info(request)

    def create_webinar_with_http_info(self, request):
        all_params = ['create_webinar_request_body', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/wss/webinar/open/conferences',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateWebinarResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_attendees_async(self, request):
        """删除与会者

        删除与会者。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteAttendees
        :type request: :class:`huaweicloudsdkmeeting.v1.DeleteAttendeesRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.DeleteAttendeesResponse`
        """
        return self.delete_attendees_with_http_info(request)

    def delete_attendees_with_http_info(self, request):
        all_params = ['conference_id', 'x_conference_authorization', 'req_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

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
            resource_path='/v1/mmc/control/conferences/attendees/delete',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteAttendeesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_corp_async(self, request):
        """SP管理员删除企业

        删除企业
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteCorp
        :type request: :class:`huaweicloudsdkmeeting.v1.DeleteCorpRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.DeleteCorpResponse`
        """
        return self.delete_corp_with_http_info(request)

    def delete_corp_with_http_info(self, request):
        all_params = ['id', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/usg/dcs/sp/corp/{id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteCorpResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_corp_vmr_async(self, request):
        """删除云会议室

        企业管理员通过该接口删除企业的云会议室
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteCorpVmr
        :type request: :class:`huaweicloudsdkmeeting.v1.DeleteCorpVmrRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.DeleteCorpVmrResponse`
        """
        return self.delete_corp_vmr_with_http_info(request)

    def delete_corp_vmr_with_http_info(self, request):
        all_params = ['del_list', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/dcs/corp/vmr/delete',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteCorpVmrResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_department_async(self, request):
        """删除部门

        企业管理员通过该接口删除部门。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteDepartment
        :type request: :class:`huaweicloudsdkmeeting.v1.DeleteDepartmentRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.DeleteDepartmentResponse`
        """
        return self.delete_department_with_http_info(request)

    def delete_department_with_http_info(self, request):
        all_params = ['dept_code', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'dept_code' in local_var_params:
            path_params['dept_code'] = local_var_params['dept_code']

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/usg/dcs/corp/dept/{dept_code}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteDepartmentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_recordings_async(self, request):
        """批量删除录制

        批量删除录制。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteRecordings
        :type request: :class:`huaweicloudsdkmeeting.v1.DeleteRecordingsRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.DeleteRecordingsResponse`
        """
        return self.delete_recordings_with_http_info(request)

    def delete_recordings_with_http_info(self, request):
        all_params = ['conf_uui_ds', 'user_uuid', 'x_authorization_type', 'x_site_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conf_uui_ds' in local_var_params:
            query_params.append(('confUUIDs', local_var_params['conf_uui_ds']))
        if 'user_uuid' in local_var_params:
            query_params.append(('userUUID', local_var_params['user_uuid']))

        header_params = {}
        if 'x_authorization_type' in local_var_params:
            header_params['X-Authorization-Type'] = local_var_params['x_authorization_type']
        if 'x_site_id' in local_var_params:
            header_params['X-Site-Id'] = local_var_params['x_site_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/mmc/management/record/files',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteRecordingsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_resource_async(self, request):
        """SP管理员根据删除企业资源

        企业删除资源项，删除资源项后，企业资源总数会自动减少
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteResource
        :type request: :class:`huaweicloudsdkmeeting.v1.DeleteResourceRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.DeleteResourceResponse`
        """
        return self.delete_resource_with_http_info(request)

    def delete_resource_with_http_info(self, request):
        all_params = ['corp_id', 'resource_id_list', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'corp_id' in local_var_params:
            path_params['corp_id'] = local_var_params['corp_id']

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/dcs/sp/corp/{corp_id}/resource/delete',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteResourceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_vision_active_code_async(self, request):
        """企业管理员删除激活码

        企业管理员批量删除激活码
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteVisionActiveCode
        :type request: :class:`huaweicloudsdkmeeting.v1.DeleteVisionActiveCodeRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.DeleteVisionActiveCodeResponse`
        """
        return self.delete_vision_active_code_with_http_info(request)

    def delete_vision_active_code_with_http_info(self, request):
        all_params = ['del_list', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/dcs/corp/vision/activecode',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteVisionActiveCodeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_web_hook_config_async(self, request):
        """删除事件订阅配置信息

        管理员可以通过该接口删除事件订阅(webhook)配置
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteWebHookConfig
        :type request: :class:`huaweicloudsdkmeeting.v1.DeleteWebHookConfigRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.DeleteWebHookConfigResponse`
        """
        return self.delete_web_hook_config_with_http_info(request)

    def delete_web_hook_config_with_http_info(self, request):
        all_params = ['id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))

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
            resource_path='/v1/mmc/management/webhook/link-config',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteWebHookConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_webinar_async(self, request):
        """取消网络研讨会

        您可根据需要取消网络研讨会。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteWebinar
        :type request: :class:`huaweicloudsdkmeeting.v1.DeleteWebinarRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.DeleteWebinarResponse`
        """
        return self.delete_webinar_with_http_info(request)

    def delete_webinar_with_http_info(self, request):
        all_params = ['conference_id', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'conference_id' in local_var_params:
            path_params['conference_id'] = local_var_params['conference_id']

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/wss/webinar/open/conferences/{conference_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteWebinarResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def disassociate_vmr_async(self, request):
        """回收云会议室

        企业管理员通过该接口回收云会议室
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DisassociateVmr
        :type request: :class:`huaweicloudsdkmeeting.v1.DisassociateVmrRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.DisassociateVmrResponse`
        """
        return self.disassociate_vmr_with_http_info(request)

    def disassociate_vmr_with_http_info(self, request):
        all_params = ['account', 'recycle_list', 'x_request_id', 'accept_language', 'account_type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'account' in local_var_params:
            path_params['account'] = local_var_params['account']

        query_params = []
        if 'account_type' in local_var_params:
            query_params.append(('accountType', local_var_params['account_type']))

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/dcs/corp/vmr/recycle-from-member/{account}',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DisassociateVmrResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def hand_async(self, request):
        """举手

        所有来宾可以举手。来宾举手后，可以取消自己的举手。主持人可以取消所有来宾的举手。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for Hand
        :type request: :class:`huaweicloudsdkmeeting.v1.HandRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.HandResponse`
        """
        return self.hand_with_http_info(request)

    def hand_with_http_info(self, request):
        all_params = ['conference_id', 'participant_id', 'x_conference_authorization', 'rest_hands_up_req_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))
        if 'participant_id' in local_var_params:
            query_params.append(('participantID', local_var_params['participant_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

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
            resource_path='/v1/mmc/control/conferences/participants/hands',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='HandResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def hang_up_async(self, request):
        """挂断与会者

        挂断正在通话中的与会者。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for HangUp
        :type request: :class:`huaweicloudsdkmeeting.v1.HangUpRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.HangUpResponse`
        """
        return self.hang_up_with_http_info(request)

    def hang_up_with_http_info(self, request):
        all_params = ['conference_id', 'x_conference_authorization', 'req_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

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
            resource_path='/v1/mmc/control/conferences/participants/delete',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='HangUpResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def invite_operate_video_async(self, request):
        """主持人邀请与会者开启、关闭摄像头

        主持人邀请与会者开启、关闭摄像头
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for InviteOperateVideo
        :type request: :class:`huaweicloudsdkmeeting.v1.InviteOperateVideoRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.InviteOperateVideoResponse`
        """
        return self.invite_operate_video_with_http_info(request)

    def invite_operate_video_with_http_info(self, request):
        all_params = ['conference_id', 'participant_id', 'x_conference_authorization', 'req_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))
        if 'participant_id' in local_var_params:
            query_params.append(('participantID', local_var_params['participant_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

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
            resource_path='/v1/mmc/control/conferences/participants/video',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='InviteOperateVideoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def invite_participant_async(self, request):
        """邀请与会者

        邀请与会者加入会议。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for InviteParticipant
        :type request: :class:`huaweicloudsdkmeeting.v1.InviteParticipantRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.InviteParticipantResponse`
        """
        return self.invite_participant_with_http_info(request)

    def invite_participant_with_http_info(self, request):
        all_params = ['conference_id', 'x_conference_authorization', 'req_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

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
            resource_path='/v1/mmc/control/conferences/participants',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='InviteParticipantResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def invite_share_async(self, request):
        """邀请共享

        场景描述：主席邀请、取消邀请会场共享 功能描述：主席邀请、取消邀请会场共享
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for InviteShare
        :type request: :class:`huaweicloudsdkmeeting.v1.InviteShareRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.InviteShareResponse`
        """
        return self.invite_share_with_http_info(request)

    def invite_share_with_http_info(self, request):
        all_params = ['conference_id', 'participant_id', 'x_conference_authorization', 'req_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))
        if 'participant_id' in local_var_params:
            query_params.append(('participantID', local_var_params['participant_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

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
            resource_path='/v1/mmc/control/conferences/participants/share/invite',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='InviteShareResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def invite_user_async(self, request):
        """邀请用户

        通过手机号码或者邮箱地址邀请用户加入企业。
        * 若被邀请用户在华为云会议系统中不存在，则：
          - 华为云会议免费版和华为云会议标准版发送短信/邮件邀请用户完成注册后加入企业。用户注册成功后，加入该企业。
          - 华为云会议旗舰版在企业内直接添加该用户。用户会收到华为云会议的初始密码，用户第一次以手机号或者邮箱登录时，需要修改密码。
        * 若被邀请用户在华为云会议系统中存在，则该用户会收到短信或者邮件确认。确认完成后改用户加入企业内。该用户的密码保持原来的密码不变。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for InviteUser
        :type request: :class:`huaweicloudsdkmeeting.v1.InviteUserRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.InviteUserResponse`
        """
        return self.invite_user_with_http_info(request)

    def invite_user_with_http_info(self, request):
        all_params = ['user_dto', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/dcs/corp/member/add',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='InviteUserResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def invite_with_pwd_async(self, request):
        """通过会议ID和密码邀请与会者

        通过会议ID和密码邀请与会者
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for InviteWithPwd
        :type request: :class:`huaweicloudsdkmeeting.v1.InviteWithPwdRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.InviteWithPwdResponse`
        """
        return self.invite_with_pwd_with_http_info(request)

    def invite_with_pwd_with_http_info(self, request):
        all_params = ['conference_id', 'req_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))

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
            resource_path='/v1/mmc/control/conferences/inviteWithPwd',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='InviteWithPwdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_history_webinars_async(self, request):
        """查询历史召开的网络研讨会列表

        查询历史召开的网络研讨会列表，企业管理员可查询企业内所有历史召开的网络研讨会，普通账号查询自己历史召开的网络研讨会
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListHistoryWebinars
        :type request: :class:`huaweicloudsdkmeeting.v1.ListHistoryWebinarsRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.ListHistoryWebinarsResponse`
        """
        return self.list_history_webinars_with_http_info(request)

    def list_history_webinars_with_http_info(self, request):
        all_params = ['x_request_id', 'accept_language', 'offset', 'limit', 'search_key', 'sort_type', 'start_time', 'end_time']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'search_key' in local_var_params:
            query_params.append(('searchKey', local_var_params['search_key']))
        if 'sort_type' in local_var_params:
            query_params.append(('sortType', local_var_params['sort_type']))
        if 'start_time' in local_var_params:
            query_params.append(('startTime', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('endTime', local_var_params['end_time']))

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/wss/webinar/open/conferences/history',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListHistoryWebinarsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_ongoing_webinars_async(self, request):
        """查询正在召开的网络研讨会列表

        查询正在召开的网络研讨会列表：企业管理员可查询企业内所有正在召开的网络研讨会，普通账号查询自己正在召开的网络研讨会
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListOngoingWebinars
        :type request: :class:`huaweicloudsdkmeeting.v1.ListOngoingWebinarsRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.ListOngoingWebinarsResponse`
        """
        return self.list_ongoing_webinars_with_http_info(request)

    def list_ongoing_webinars_with_http_info(self, request):
        all_params = ['x_request_id', 'accept_language', 'offset', 'limit', 'search_key', 'sort_type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'search_key' in local_var_params:
            query_params.append(('searchKey', local_var_params['search_key']))
        if 'sort_type' in local_var_params:
            query_params.append(('sortType', local_var_params['sort_type']))

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/wss/webinar/open/conferences/ongoing',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListOngoingWebinarsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_up_coming_webinars_async(self, request):
        """查询即将召开的网络研讨会列表

        查询即将召开的网络研讨会列表：企业管理员可查询企业内所有即将召开的网络研讨会，普通账号查询自己即将召开的网络研讨会
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListUpComingWebinars
        :type request: :class:`huaweicloudsdkmeeting.v1.ListUpComingWebinarsRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.ListUpComingWebinarsResponse`
        """
        return self.list_up_coming_webinars_with_http_info(request)

    def list_up_coming_webinars_with_http_info(self, request):
        all_params = ['x_request_id', 'accept_language', 'offset', 'limit', 'search_key', 'sort_type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'search_key' in local_var_params:
            query_params.append(('searchKey', local_var_params['search_key']))
        if 'sort_type' in local_var_params:
            query_params.append(('sortType', local_var_params['sort_type']))

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/wss/webinar/open/conferences/upcoming',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListUpComingWebinarsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def live_async(self, request):
        """启停会议直播

        启动或停止会议直播。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for Live
        :type request: :class:`huaweicloudsdkmeeting.v1.LiveRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.LiveResponse`
        """
        return self.live_with_http_info(request)

    def live_with_http_info(self, request):
        all_params = ['conference_id', 'x_conference_authorization', 'rest_set_live_req_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

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
            resource_path='/v1/mmc/control/conferences/live',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='LiveResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def lock_meeting_async(self, request):
        """锁定会议

        锁定或解锁会议。锁定会议后，不允许与会者加入会议。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for LockMeeting
        :type request: :class:`huaweicloudsdkmeeting.v1.LockMeetingRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.LockMeetingResponse`
        """
        return self.lock_meeting_with_http_info(request)

    def lock_meeting_with_http_info(self, request):
        all_params = ['conference_id', 'x_conference_authorization', 'rest_lock_req_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

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
            resource_path='/v1/mmc/control/conferences/lock',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='LockMeetingResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def lock_view_async(self, request):
        """锁定会场视频源

        锁定或者解锁某在线会场的视频源。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for LockView
        :type request: :class:`huaweicloudsdkmeeting.v1.LockViewRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.LockViewResponse`
        """
        return self.lock_view_with_http_info(request)

    def lock_view_with_http_info(self, request):
        all_params = ['conference_id', 'participant_id', 'x_conference_authorization', 'req_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))
        if 'participant_id' in local_var_params:
            query_params.append(('participantID', local_var_params['participant_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

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
            resource_path='/v1/mmc/control/conferences/lockView',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='LockViewResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def mute_meeting_async(self, request):
        """全场静音

        主持人可以通过该接口静音/取消静音整个会议所有与会者（主持人除外）。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for MuteMeeting
        :type request: :class:`huaweicloudsdkmeeting.v1.MuteMeetingRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.MuteMeetingResponse`
        """
        return self.mute_meeting_with_http_info(request)

    def mute_meeting_with_http_info(self, request):
        all_params = ['conference_id', 'x_conference_authorization', 'rest_mute_req_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

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
            resource_path='/v1/mmc/control/conferences/mute',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='MuteMeetingResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def mute_participant_async(self, request):
        """静音与会者

        主持人可以静音/取消静音任意与会者，来宾也可静音/取消静音自己。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for MuteParticipant
        :type request: :class:`huaweicloudsdkmeeting.v1.MuteParticipantRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.MuteParticipantResponse`
        """
        return self.mute_participant_with_http_info(request)

    def mute_participant_with_http_info(self, request):
        all_params = ['conference_id', 'participant_id', 'x_conference_authorization', 'rest_mute_participant_req_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))
        if 'participant_id' in local_var_params:
            query_params.append(('participantID', local_var_params['participant_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

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
            resource_path='/v1/mmc/control/conferences/participants/mute',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='MuteParticipantResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def prolong_meeting_async(self, request):
        """延长会议

        延长会议。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ProlongMeeting
        :type request: :class:`huaweicloudsdkmeeting.v1.ProlongMeetingRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.ProlongMeetingResponse`
        """
        return self.prolong_meeting_with_http_info(request)

    def prolong_meeting_with_http_info(self, request):
        all_params = ['conference_id', 'x_conference_authorization', 'rest_prolong_dur_req_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

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
            resource_path='/v1/mmc/control/conferences/duration',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ProlongMeetingResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def record_async(self, request):
        """启停会议录制

        启动或停止会议录制。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for Record
        :type request: :class:`huaweicloudsdkmeeting.v1.RecordRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.RecordResponse`
        """
        return self.record_with_http_info(request)

    def record_with_http_info(self, request):
        all_params = ['conference_id', 'x_conference_authorization', 'rest_set_record_req_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

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
            resource_path='/v1/mmc/control/conferences/record',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='RecordResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def rename_participant_async(self, request):
        """重命名与会者

        重命名某个与会者。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for RenameParticipant
        :type request: :class:`huaweicloudsdkmeeting.v1.RenameParticipantRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.RenameParticipantResponse`
        """
        return self.rename_participant_with_http_info(request)

    def rename_participant_with_http_info(self, request):
        all_params = ['conference_id', 'x_conference_authorization', 'rest_rename_part_req_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

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
            resource_path='/v1/mmc/control/conferences/participants/name',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='RenameParticipantResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def reset_activecode_async(self, request):
        """企业管理员重置硬终端激活码

        当硬终端激活码失效时，企业管理员可以通过该接口重置激活码，使用重新获取的激活码激活终端，每24小时可重新激活5次。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ResetActivecode
        :type request: :class:`huaweicloudsdkmeeting.v1.ResetActivecodeRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.ResetActivecodeResponse`
        """
        return self.reset_activecode_with_http_info(request)

    def reset_activecode_with_http_info(self, request):
        all_params = ['sn', 'active_dto', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'sn' in local_var_params:
            path_params['sn'] = local_var_params['sn']

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/dcs/corp/device/{sn}/activecode',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ResetActivecodeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def reset_pwd_async(self, request):
        """用户重置密码

        该接口提供给用户重置密码功能，服务器收到请求，重新设置用户密码并返回结果。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ResetPwd
        :type request: :class:`huaweicloudsdkmeeting.v1.ResetPwdRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.ResetPwdResponse`
        """
        return self.reset_pwd_with_http_info(request)

    def reset_pwd_with_http_info(self, request):
        all_params = ['reset_pwd_req_dtov1', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-ID'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/acs/password/reset',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ResetPwdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def reset_pwd_by_admin_async(self, request):
        """企业管理员重置企业成员密码

        企业管理员通过该接口提供企业管理员重置企业成员密码的功能。当服务器收到重置密码的请求时，发送新的密码到企业成员的邮箱或者短信，并返回结果。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ResetPwdByAdmin
        :type request: :class:`huaweicloudsdkmeeting.v1.ResetPwdByAdminRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.ResetPwdByAdminResponse`
        """
        return self.reset_pwd_by_admin_with_http_info(request)

    def reset_pwd_by_admin_with_http_info(self, request):
        all_params = ['admin_reset_pwd_req_dto', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-ID'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/acs/password/admin/reset',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ResetPwdByAdminResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def reset_vision_active_code_async(self, request):
        """企业管理员重置账号的激活码

        企业管理员重置账号的激活码，重置后，原设备直接解绑，必须重新激活使用,若手机邮箱不填，则不会发送新的激活码
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ResetVisionActiveCode
        :type request: :class:`huaweicloudsdkmeeting.v1.ResetVisionActiveCodeRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.ResetVisionActiveCodeResponse`
        """
        return self.reset_vision_active_code_with_http_info(request)

    def reset_vision_active_code_with_http_info(self, request):
        all_params = ['account', 'active_dto', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'account' in local_var_params:
            path_params['account'] = local_var_params['account']

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/dcs/corp/vision/activecode/{account}/reset',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ResetVisionActiveCodeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def rollcall_participant_async(self, request):
        """点名会场

        同一时间，只允许一个与会者被点名。点名会场的效果是除了主持人外，点名与会者为非静音状态，未点名的与会者统一为静音状态。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for RollcallParticipant
        :type request: :class:`huaweicloudsdkmeeting.v1.RollcallParticipantRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.RollcallParticipantResponse`
        """
        return self.rollcall_participant_with_http_info(request)

    def rollcall_participant_with_http_info(self, request):
        all_params = ['conference_id', 'participant_id', 'x_conference_authorization']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))
        if 'participant_id' in local_var_params:
            query_params.append(('participantID', local_var_params['participant_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/mmc/control/conferences/participants/rollCall',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='RollcallParticipantResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def search_attendance_records_of_his_meeting_async(self, request):
        """查询历史会议的与会者记录

        查询指定历史会议的与会者记录。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for SearchAttendanceRecordsOfHisMeeting
        :type request: :class:`huaweicloudsdkmeeting.v1.SearchAttendanceRecordsOfHisMeetingRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SearchAttendanceRecordsOfHisMeetingResponse`
        """
        return self.search_attendance_records_of_his_meeting_with_http_info(request)

    def search_attendance_records_of_his_meeting_with_http_info(self, request):
        all_params = ['conf_uuid', 'offset', 'limit', 'search_key', 'user_uuid', 'x_authorization_type', 'x_site_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conf_uuid' in local_var_params:
            query_params.append(('confUUID', local_var_params['conf_uuid']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'search_key' in local_var_params:
            query_params.append(('searchKey', local_var_params['search_key']))
        if 'user_uuid' in local_var_params:
            query_params.append(('userUUID', local_var_params['user_uuid']))

        header_params = {}
        if 'x_authorization_type' in local_var_params:
            header_params['X-Authorization-Type'] = local_var_params['x_authorization_type']
        if 'x_site_id' in local_var_params:
            header_params['X-Site-Id'] = local_var_params['x_site_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/mmc/management/conferences/history/confAttendeeRecord',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SearchAttendanceRecordsOfHisMeetingResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def search_corp_async(self, request):
        """SP管理员分页搜索企业

        分页搜索企业,支持名称、企业ID搜索
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for SearchCorp
        :type request: :class:`huaweicloudsdkmeeting.v1.SearchCorpRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SearchCorpResponse`
        """
        return self.search_corp_with_http_info(request)

    def search_corp_with_http_info(self, request):
        all_params = ['x_request_id', 'accept_language', 'offset', 'limit', 'search_key']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'search_key' in local_var_params:
            query_params.append(('searchKey', local_var_params['search_key']))

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/usg/dcs/sp/corp',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SearchCorpResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def search_corp_admins_async(self, request):
        """分页查询企业管理员

        通过该接口分页查询企业管理员。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for SearchCorpAdmins
        :type request: :class:`huaweicloudsdkmeeting.v1.SearchCorpAdminsRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SearchCorpAdminsResponse`
        """
        return self.search_corp_admins_with_http_info(request)

    def search_corp_admins_with_http_info(self, request):
        all_params = ['x_request_id', 'accept_language', 'offset', 'limit', 'search_key']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'search_key' in local_var_params:
            query_params.append(('searchKey', local_var_params['search_key']))

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/usg/dcs/corp/admin',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SearchCorpAdminsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def search_corp_dir_async(self, request):
        """查询企业通讯录

        企业用户（含管理员）通过该接口查询该企业的通讯录。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for SearchCorpDir
        :type request: :class:`huaweicloudsdkmeeting.v1.SearchCorpDirRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SearchCorpDirResponse`
        """
        return self.search_corp_dir_with_http_info(request)

    def search_corp_dir_with_http_info(self, request):
        all_params = ['x_request_id', 'accept_language', 'offset', 'limit', 'search_key', 'dept_code', 'query_sub_dept', 'search_scope']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'search_key' in local_var_params:
            query_params.append(('searchKey', local_var_params['search_key']))
        if 'dept_code' in local_var_params:
            query_params.append(('deptCode', local_var_params['dept_code']))
        if 'query_sub_dept' in local_var_params:
            query_params.append(('querySubDept', local_var_params['query_sub_dept']))
        if 'search_scope' in local_var_params:
            query_params.append(('searchScope', local_var_params['search_scope']))

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/usg/abs/users',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SearchCorpDirResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def search_corp_resources_async(self, request):
        """企业管理员分页查询企业资源订单列表

        企业管理员根据条件查询企业资源订单列表
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for SearchCorpResources
        :type request: :class:`huaweicloudsdkmeeting.v1.SearchCorpResourcesRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SearchCorpResourcesResponse`
        """
        return self.search_corp_resources_with_http_info(request)

    def search_corp_resources_with_http_info(self, request):
        all_params = ['x_request_id', 'accept_language', 'offset', 'limit', 'search_key', 'start_expire_date', 'end_expire_date', 'type', 'vmr_mode', 'type_id', 'order_id', 'status']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'search_key' in local_var_params:
            query_params.append(('searchKey', local_var_params['search_key']))
        if 'start_expire_date' in local_var_params:
            query_params.append(('startExpireDate', local_var_params['start_expire_date']))
        if 'end_expire_date' in local_var_params:
            query_params.append(('endExpireDate', local_var_params['end_expire_date']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'vmr_mode' in local_var_params:
            query_params.append(('vmrMode', local_var_params['vmr_mode']))
        if 'type_id' in local_var_params:
            query_params.append(('typeId', local_var_params['type_id']))
        if 'order_id' in local_var_params:
            query_params.append(('orderId', local_var_params['order_id']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/usg/dcs/corp/resource-list',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SearchCorpResourcesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def search_corp_vmr_async(self, request):
        """企业管理员分页查询企业云会议室

        企业管理员通过该接口分页查询企业的云会议室。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for SearchCorpVmr
        :type request: :class:`huaweicloudsdkmeeting.v1.SearchCorpVmrRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SearchCorpVmrResponse`
        """
        return self.search_corp_vmr_with_http_info(request)

    def search_corp_vmr_with_http_info(self, request):
        all_params = ['x_request_id', 'accept_language', 'offset', 'limit', 'search_key', 'vmr_mode', 'status']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'search_key' in local_var_params:
            query_params.append(('searchKey', local_var_params['search_key']))
        if 'vmr_mode' in local_var_params:
            query_params.append(('vmrMode', local_var_params['vmr_mode']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/usg/dcs/corp/vmr',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SearchCorpVmrResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def search_ctl_records_of_his_meeting_async(self, request):
        """查询历史会议的会控记录

        查询指定历史会议的会控记录。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for SearchCtlRecordsOfHisMeeting
        :type request: :class:`huaweicloudsdkmeeting.v1.SearchCtlRecordsOfHisMeetingRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SearchCtlRecordsOfHisMeetingResponse`
        """
        return self.search_ctl_records_of_his_meeting_with_http_info(request)

    def search_ctl_records_of_his_meeting_with_http_info(self, request):
        all_params = ['conf_uuid', 'offset', 'limit', 'user_uuid', 'x_authorization_type', 'x_site_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conf_uuid' in local_var_params:
            query_params.append(('confUUID', local_var_params['conf_uuid']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'user_uuid' in local_var_params:
            query_params.append(('userUUID', local_var_params['user_uuid']))

        header_params = {}
        if 'x_authorization_type' in local_var_params:
            header_params['X-Authorization-Type'] = local_var_params['x_authorization_type']
        if 'x_site_id' in local_var_params:
            header_params['X-Site-Id'] = local_var_params['x_site_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/mmc/management/conferences/history/confCtlRecord',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SearchCtlRecordsOfHisMeetingResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def search_department_by_name_async(self, request):
        """按名称查询所有的部门

        企业管理员通过该接口按名称查询所有的部门。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for SearchDepartmentByName
        :type request: :class:`huaweicloudsdkmeeting.v1.SearchDepartmentByNameRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SearchDepartmentByNameResponse`
        """
        return self.search_department_by_name_with_http_info(request)

    def search_department_by_name_with_http_info(self, request):
        all_params = ['dept_name', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'dept_name' in local_var_params:
            query_params.append(('deptName', local_var_params['dept_name']))

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/usg/dcs/member/dept',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SearchDepartmentByNameResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def search_devices_async(self, request):
        """分页查询终端

        企业管理员通过该接口分页查询终端信息。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for SearchDevices
        :type request: :class:`huaweicloudsdkmeeting.v1.SearchDevicesRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SearchDevicesResponse`
        """
        return self.search_devices_with_http_info(request)

    def search_devices_with_http_info(self, request):
        all_params = ['x_request_id', 'accept_language', 'offset', 'limit', 'search_key', 'model', 'dept_code', 'enable_sub_dept']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'search_key' in local_var_params:
            query_params.append(('searchKey', local_var_params['search_key']))
        if 'model' in local_var_params:
            query_params.append(('model', local_var_params['model']))
        if 'dept_code' in local_var_params:
            query_params.append(('deptCode', local_var_params['dept_code']))
        if 'enable_sub_dept' in local_var_params:
            query_params.append(('enableSubDept', local_var_params['enable_sub_dept']))

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/usg/dcs/corp/device',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SearchDevicesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def search_his_meetings_async(self, request):
        """查询历史会议列表

        管理员可以查询管理权限域内所有的历史会议，普通用户仅能查询当前帐号管理的历史会议。不带查询参数时，默认查询权限范围内的历史会议。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for SearchHisMeetings
        :type request: :class:`huaweicloudsdkmeeting.v1.SearchHisMeetingsRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SearchHisMeetingsResponse`
        """
        return self.search_his_meetings_with_http_info(request)

    def search_his_meetings_with_http_info(self, request):
        all_params = ['start_date', 'end_date', 'user_uuid', 'offset', 'limit', 'search_key', 'query_all', 'sort_type', 'x_authorization_type', 'x_site_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_uuid' in local_var_params:
            query_params.append(('userUUID', local_var_params['user_uuid']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'search_key' in local_var_params:
            query_params.append(('searchKey', local_var_params['search_key']))
        if 'query_all' in local_var_params:
            query_params.append(('queryAll', local_var_params['query_all']))
        if 'start_date' in local_var_params:
            query_params.append(('startDate', local_var_params['start_date']))
        if 'end_date' in local_var_params:
            query_params.append(('endDate', local_var_params['end_date']))
        if 'sort_type' in local_var_params:
            query_params.append(('sortType', local_var_params['sort_type']))

        header_params = {}
        if 'x_authorization_type' in local_var_params:
            header_params['X-Authorization-Type'] = local_var_params['x_authorization_type']
        if 'x_site_id' in local_var_params:
            header_params['X-Site-Id'] = local_var_params['x_site_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/mmc/management/conferences/history',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SearchHisMeetingsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def search_materials_async(self, request):
        """分页查询信息窗素材

        分页查询信息窗素材
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for SearchMaterials
        :type request: :class:`huaweicloudsdkmeeting.v1.SearchMaterialsRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SearchMaterialsResponse`
        """
        return self.search_materials_with_http_info(request)

    def search_materials_with_http_info(self, request):
        all_params = ['x_request_id', 'accept_language', 'offset', 'limit', 'search_key']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'search_key' in local_var_params:
            query_params.append(('searchKey', local_var_params['search_key']))

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/usg/sss/materials',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SearchMaterialsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def search_meeting_file_list_async(self, request):
        """查询会议纪要列表

        用户查询自己的会议纪要列表
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for SearchMeetingFileList
        :type request: :class:`huaweicloudsdkmeeting.v1.SearchMeetingFileListRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SearchMeetingFileListResponse`
        """
        return self.search_meeting_file_list_with_http_info(request)

    def search_meeting_file_list_with_http_info(self, request):
        all_params = ['x_request_id', 'accept_language', 'offset', 'limit', 'search_key']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'search_key' in local_var_params:
            query_params.append(('searchKey', local_var_params['search_key']))

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/usg/sss/meeting-files',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SearchMeetingFileListResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def search_meetings_async(self, request):
        """查询会议列表

        管理员可以查询管理权限域内所有的会议，普通用户仅能查询当前帐号管理的会议。不带查询参数时，默认查询权限范围内正在召开或还未召开的会议。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for SearchMeetings
        :type request: :class:`huaweicloudsdkmeeting.v1.SearchMeetingsRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SearchMeetingsResponse`
        """
        return self.search_meetings_with_http_info(request)

    def search_meetings_with_http_info(self, request):
        all_params = ['user_uuid', 'offset', 'limit', 'query_all', 'search_key', 'query_conf_mode', 'sort_type', 'x_authorization_type', 'x_site_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_uuid' in local_var_params:
            query_params.append(('userUUID', local_var_params['user_uuid']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'query_all' in local_var_params:
            query_params.append(('queryAll', local_var_params['query_all']))
        if 'search_key' in local_var_params:
            query_params.append(('searchKey', local_var_params['search_key']))
        if 'query_conf_mode' in local_var_params:
            query_params.append(('queryConfMode', local_var_params['query_conf_mode']))
        if 'sort_type' in local_var_params:
            query_params.append(('sortType', local_var_params['sort_type']))

        header_params = {}
        if 'x_authorization_type' in local_var_params:
            header_params['X-Authorization-Type'] = local_var_params['x_authorization_type']
        if 'x_site_id' in local_var_params:
            header_params['X-Site-Id'] = local_var_params['x_site_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/mmc/management/conferences',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SearchMeetingsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def search_member_vmr_async(self, request):
        """普通用户分页查询云会议室及个人会议ID

        企业用户通过该接口查询个人已分配的云会议室及个人会议ID。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for SearchMemberVmr
        :type request: :class:`huaweicloudsdkmeeting.v1.SearchMemberVmrRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SearchMemberVmrResponse`
        """
        return self.search_member_vmr_with_http_info(request)

    def search_member_vmr_with_http_info(self, request):
        all_params = ['x_request_id', 'accept_language', 'offset', 'limit', 'search_key', 'special_vmr']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'search_key' in local_var_params:
            query_params.append(('searchKey', local_var_params['search_key']))
        if 'special_vmr' in local_var_params:
            query_params.append(('specialVmr', local_var_params['special_vmr']))

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/usg/dcs/member/vmr',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SearchMemberVmrResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def search_online_meetings_async(self, request):
        """查询在线会议列表

        管理员可以查询管理权限域内所有在线会议，普通用户仅能查询当前自己帐号管理的在线会议。不带查询参数时，默认查询权限范围内的在线会议，按开始时间升序排列。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for SearchOnlineMeetings
        :type request: :class:`huaweicloudsdkmeeting.v1.SearchOnlineMeetingsRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SearchOnlineMeetingsResponse`
        """
        return self.search_online_meetings_with_http_info(request)

    def search_online_meetings_with_http_info(self, request):
        all_params = ['user_uuid', 'offset', 'limit', 'query_all', 'search_key', 'x_authorization_type', 'x_site_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_uuid' in local_var_params:
            query_params.append(('userUUID', local_var_params['user_uuid']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'query_all' in local_var_params:
            query_params.append(('queryAll', local_var_params['query_all']))
        if 'search_key' in local_var_params:
            query_params.append(('searchKey', local_var_params['search_key']))

        header_params = {}
        if 'x_authorization_type' in local_var_params:
            header_params['X-Authorization-Type'] = local_var_params['x_authorization_type']
        if 'x_site_id' in local_var_params:
            header_params['X-Site-Id'] = local_var_params['x_site_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/mmc/management/conferences/online',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SearchOnlineMeetingsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def search_programs_async(self, request):
        """查询信息窗节目

        获取信息窗节目
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for SearchPrograms
        :type request: :class:`huaweicloudsdkmeeting.v1.SearchProgramsRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SearchProgramsResponse`
        """
        return self.search_programs_with_http_info(request)

    def search_programs_with_http_info(self, request):
        all_params = ['x_request_id', 'accept_language', 'offset', 'limit', 'search_key']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'search_key' in local_var_params:
            query_params.append(('searchKey', local_var_params['search_key']))

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/usg/sss/programs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SearchProgramsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def search_publications_async(self, request):
        """查询信息窗发布

        获取信息窗发布
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for SearchPublications
        :type request: :class:`huaweicloudsdkmeeting.v1.SearchPublicationsRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SearchPublicationsResponse`
        """
        return self.search_publications_with_http_info(request)

    def search_publications_with_http_info(self, request):
        all_params = ['x_request_id', 'accept_language', 'offset', 'limit', 'search_key']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'search_key' in local_var_params:
            query_params.append(('searchKey', local_var_params['search_key']))

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/usg/sss/publications',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SearchPublicationsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def search_recordings_async(self, request):
        """查询录制列表

        管理员可以查询管理权限域内所有的录制，普通用户仅能查询当前帐号管理的录制。不带查询参数时，默认查询权限范围内的录制。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for SearchRecordings
        :type request: :class:`huaweicloudsdkmeeting.v1.SearchRecordingsRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SearchRecordingsResponse`
        """
        return self.search_recordings_with_http_info(request)

    def search_recordings_with_http_info(self, request):
        all_params = ['start_date', 'end_date', 'user_uuid', 'offset', 'limit', 'query_all', 'search_key', 'sort_type', 'x_authorization_type', 'x_site_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_uuid' in local_var_params:
            query_params.append(('userUUID', local_var_params['user_uuid']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'query_all' in local_var_params:
            query_params.append(('queryAll', local_var_params['query_all']))
        if 'search_key' in local_var_params:
            query_params.append(('searchKey', local_var_params['search_key']))
        if 'start_date' in local_var_params:
            query_params.append(('startDate', local_var_params['start_date']))
        if 'end_date' in local_var_params:
            query_params.append(('endDate', local_var_params['end_date']))
        if 'sort_type' in local_var_params:
            query_params.append(('sortType', local_var_params['sort_type']))

        header_params = {}
        if 'x_authorization_type' in local_var_params:
            header_params['X-Authorization-Type'] = local_var_params['x_authorization_type']
        if 'x_site_id' in local_var_params:
            header_params['X-Site-Id'] = local_var_params['x_site_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/mmc/management/record/files',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SearchRecordingsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def search_resource_async(self, request):
        """SP管理员根据分页查询企业资源

        SP根据条件查询企业的资源项
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for SearchResource
        :type request: :class:`huaweicloudsdkmeeting.v1.SearchResourceRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SearchResourceResponse`
        """
        return self.search_resource_with_http_info(request)

    def search_resource_with_http_info(self, request):
        all_params = ['corp_id', 'x_request_id', 'accept_language', 'offset', 'limit', 'search_key', 'start_expire_date', 'end_expire_date', 'type', 'type_id', 'status']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'corp_id' in local_var_params:
            path_params['corp_id'] = local_var_params['corp_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'search_key' in local_var_params:
            query_params.append(('searchKey', local_var_params['search_key']))
        if 'start_expire_date' in local_var_params:
            query_params.append(('startExpireDate', local_var_params['start_expire_date']))
        if 'end_expire_date' in local_var_params:
            query_params.append(('endExpireDate', local_var_params['end_expire_date']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'type_id' in local_var_params:
            query_params.append(('typeId', local_var_params['type_id']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/usg/dcs/sp/corp/{corp_id}/resource',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SearchResourceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def search_resource_op_record_async(self, request):
        """SP管理员根据分页查询企业资源操作记录

        SP根据根据条件查询企业的资源操作记录，支持根据resourceId模糊搜索
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for SearchResourceOpRecord
        :type request: :class:`huaweicloudsdkmeeting.v1.SearchResourceOpRecordRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SearchResourceOpRecordResponse`
        """
        return self.search_resource_op_record_with_http_info(request)

    def search_resource_op_record_with_http_info(self, request):
        all_params = ['corp_id', 'x_request_id', 'accept_language', 'offset', 'limit', 'search_key', 'start_expire_date', 'end_expire_date', 'start_operate_date', 'end_operate_date', 'type', 'type_id', 'operate_type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'corp_id' in local_var_params:
            path_params['corp_id'] = local_var_params['corp_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'search_key' in local_var_params:
            query_params.append(('searchKey', local_var_params['search_key']))
        if 'start_expire_date' in local_var_params:
            query_params.append(('startExpireDate', local_var_params['start_expire_date']))
        if 'end_expire_date' in local_var_params:
            query_params.append(('endExpireDate', local_var_params['end_expire_date']))
        if 'start_operate_date' in local_var_params:
            query_params.append(('startOperateDate', local_var_params['start_operate_date']))
        if 'end_operate_date' in local_var_params:
            query_params.append(('endOperateDate', local_var_params['end_operate_date']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'type_id' in local_var_params:
            query_params.append(('typeId', local_var_params['type_id']))
        if 'operate_type' in local_var_params:
            query_params.append(('operateType', local_var_params['operate_type']))

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/usg/dcs/sp/corp/{corp_id}/resource-record',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SearchResourceOpRecordResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def search_users_async(self, request):
        """分页查询用户

        企业管理员通过该接口分页查询企业用户。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for SearchUsers
        :type request: :class:`huaweicloudsdkmeeting.v1.SearchUsersRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SearchUsersResponse`
        """
        return self.search_users_with_http_info(request)

    def search_users_with_http_info(self, request):
        all_params = ['x_request_id', 'accept_language', 'offset', 'limit', 'search_key', 'sort_field', 'is_asc', 'dept_code', 'enable_sub_dept', 'admin_type', 'enable_room', 'user_type', 'status', 'contains_un_active']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'search_key' in local_var_params:
            query_params.append(('searchKey', local_var_params['search_key']))
        if 'sort_field' in local_var_params:
            query_params.append(('sortField', local_var_params['sort_field']))
        if 'is_asc' in local_var_params:
            query_params.append(('isAsc', local_var_params['is_asc']))
        if 'dept_code' in local_var_params:
            query_params.append(('deptCode', local_var_params['dept_code']))
        if 'enable_sub_dept' in local_var_params:
            query_params.append(('enableSubDept', local_var_params['enable_sub_dept']))
        if 'admin_type' in local_var_params:
            query_params.append(('adminType', local_var_params['admin_type']))
        if 'enable_room' in local_var_params:
            query_params.append(('enableRoom', local_var_params['enable_room']))
        if 'user_type' in local_var_params:
            query_params.append(('userType', local_var_params['user_type']))
            collection_formats['userType'] = 'csv'
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'contains_un_active' in local_var_params:
            query_params.append(('containsUnActive', local_var_params['contains_un_active']))

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/usg/dcs/corp/member',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SearchUsersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def search_vision_active_code_async(self, request):
        """企业管理员分页查询激活码

        企业管理员分页查询激活码，支持激活码、终端名称模糊查询。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for SearchVisionActiveCode
        :type request: :class:`huaweicloudsdkmeeting.v1.SearchVisionActiveCodeRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SearchVisionActiveCodeResponse`
        """
        return self.search_vision_active_code_with_http_info(request)

    def search_vision_active_code_with_http_info(self, request):
        all_params = ['x_request_id', 'accept_language', 'offset', 'limit', 'search_key', 'dev_type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'search_key' in local_var_params:
            query_params.append(('searchKey', local_var_params['search_key']))
        if 'dev_type' in local_var_params:
            query_params.append(('devType', local_var_params['dev_type']))

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/usg/dcs/corp/vision/activecode',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SearchVisionActiveCodeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def send_slide_verify_code_async(self, request):
        """发送滑块验证码

        该接口提供发送滑块验证码。服务器收到请求，返回抠图以及抠图后的原图等结果。需要在前台界面显示出抠图以及抠图后的原图，用户通过滑块操作来匹配图形。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for SendSlideVerifyCode
        :type request: :class:`huaweicloudsdkmeeting.v1.SendSlideVerifyCodeRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SendSlideVerifyCodeResponse`
        """
        return self.send_slide_verify_code_with_http_info(request)

    def send_slide_verify_code_with_http_info(self, request):
        all_params = ['slide_verify_code_send_dto', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-ID'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/acs/auth/slideverifycode/send',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SendSlideVerifyCodeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def send_veri_code_for_change_pwd_async(self, request):
        """发送验证码

        该接口提供发送验证码，服务器收到请求，发送验证码到邮箱或者短信并返回结果。用户在前台界面通过滑块验证后，再进行发送验证码操作。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for SendVeriCodeForChangePwd
        :type request: :class:`huaweicloudsdkmeeting.v1.SendVeriCodeForChangePwdRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SendVeriCodeForChangePwdResponse`
        """
        return self.send_veri_code_for_change_pwd_with_http_info(request)

    def send_veri_code_for_change_pwd_with_http_info(self, request):
        all_params = ['verify_code_send_dtov1', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-ID'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/acs/verifycode/send',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SendVeriCodeForChangePwdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def send_veri_code_for_update_user_info_async(self, request):
        """获取验证码

        获取验证码，向手机或邮箱发送，一分钟内只会发送一次。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for SendVeriCodeForUpdateUserInfo
        :type request: :class:`huaweicloudsdkmeeting.v1.SendVeriCodeForUpdateUserInfoRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SendVeriCodeForUpdateUserInfoResponse`
        """
        return self.send_veri_code_for_update_user_info_with_http_info(request)

    def send_veri_code_for_update_user_info_with_http_info(self, request):
        all_params = ['verification_code_dto', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/dcs/member/verification-code',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SendVeriCodeForUpdateUserInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def set_custom_multi_picture_async(self, request):
        """设置自定义多画面

        场景描述：会议管理员在confportal手动设置多画面 功能描述：提供给会议管理员手动设置多画面的功能
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for SetCustomMultiPicture
        :type request: :class:`huaweicloudsdkmeeting.v1.SetCustomMultiPictureRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SetCustomMultiPictureResponse`
        """
        return self.set_custom_multi_picture_with_http_info(request)

    def set_custom_multi_picture_with_http_info(self, request):
        all_params = ['conference_id', 'x_conference_authorization', 'req_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

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
            resource_path='/v1/mmc/control/conferences/display/customMultiPicture',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SetCustomMultiPictureResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def set_host_view_async(self, request):
        """主持人选看

        用于主持人轮询、主持人选看多画面、主持人选看会场操作。目前只适用于硬终端为主持人的场景。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for SetHostView
        :type request: :class:`huaweicloudsdkmeeting.v1.SetHostViewRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SetHostViewResponse`
        """
        return self.set_host_view_with_http_info(request)

    def set_host_view_with_http_info(self, request):
        all_params = ['conference_id', 'x_conference_authorization', 'req_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

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
            resource_path='/v1/mmc/control/conferences/chairView',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SetHostViewResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def set_multi_picture_async(self, request):
        """设置多画面

        设置会议多画面。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for SetMultiPicture
        :type request: :class:`huaweicloudsdkmeeting.v1.SetMultiPictureRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SetMultiPictureResponse`
        """
        return self.set_multi_picture_with_http_info(request)

    def set_multi_picture_with_http_info(self, request):
        all_params = ['conference_id', 'x_conference_authorization', 'req_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

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
            resource_path='/v1/mmc/control/conferences/display/multiPicture',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SetMultiPictureResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def set_participant_view_async(self, request):
        """会场选看

        目前只适用于硬终端选看其他会场人的场景。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for SetParticipantView
        :type request: :class:`huaweicloudsdkmeeting.v1.SetParticipantViewRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SetParticipantViewResponse`
        """
        return self.set_participant_view_with_http_info(request)

    def set_participant_view_with_http_info(self, request):
        all_params = ['conference_id', 'participant_id', 'x_conference_authorization', 'req_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))
        if 'participant_id' in local_var_params:
            query_params.append(('participantID', local_var_params['participant_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

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
            resource_path='/v1/mmc/control/conferences/partView',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SetParticipantViewResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def set_role_async(self, request):
        """申请主持人

        申请或释放主持人。普通用户可申请主持人，主持人可释放主持人权限。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for SetRole
        :type request: :class:`huaweicloudsdkmeeting.v1.SetRoleRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SetRoleResponse`
        """
        return self.set_role_with_http_info(request)

    def set_role_with_http_info(self, request):
        all_params = ['conference_id', 'participant_id', 'x_conference_authorization', 'rest_chair_token_req_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))
        if 'participant_id' in local_var_params:
            query_params.append(('participantID', local_var_params['participant_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

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
            resource_path='/v1/mmc/control/conferences/participants/role',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SetRoleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def set_sso_config_async(self, request):
        """设置SSO鉴权配置

        设置SSO鉴权配置
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for SetSsoConfig
        :type request: :class:`huaweicloudsdkmeeting.v1.SetSsoConfigRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SetSsoConfigResponse`
        """
        return self.set_sso_config_with_http_info(request)

    def set_sso_config_with_http_info(self, request):
        all_params = ['authorize_config_info', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/acs/authorizeconfig',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SetSsoConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def set_web_hook_config_async(self, request):
        """设置事件订阅配置信息

        设置企业事件订阅配置设置
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for SetWebHookConfig
        :type request: :class:`huaweicloudsdkmeeting.v1.SetWebHookConfigRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SetWebHookConfigResponse`
        """
        return self.set_web_hook_config_with_http_info(request)

    def set_web_hook_config_with_http_info(self, request):
        all_params = ['request']
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
            resource_path='/v1/mmc/management/webhook/link-config',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SetWebHookConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_conf_org_async(self, request):
        """通过会议ID查询企业ID

        与某个会议在同一个SP下的用户，可以通过会议ID查询到该会议对应的企业ID。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowConfOrg
        :type request: :class:`huaweicloudsdkmeeting.v1.ShowConfOrgRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.ShowConfOrgResponse`
        """
        return self.show_conf_org_with_http_info(request)

    def show_conf_org_with_http_info(self, request):
        all_params = ['conference_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))

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
            resource_path='/v1/mmc/management/conferences/confOrg',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowConfOrgResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_corp_async(self, request):
        """SP管理员查询企业

        获取企业
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowCorp
        :type request: :class:`huaweicloudsdkmeeting.v1.ShowCorpRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.ShowCorpResponse`
        """
        return self.show_corp_with_http_info(request)

    def show_corp_with_http_info(self, request):
        all_params = ['id', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/usg/dcs/sp/corp/{id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowCorpResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_corp_admin_async(self, request):
        """查询企业管理员

        通过该接口查询企业管理员。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowCorpAdmin
        :type request: :class:`huaweicloudsdkmeeting.v1.ShowCorpAdminRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.ShowCorpAdminResponse`
        """
        return self.show_corp_admin_with_http_info(request)

    def show_corp_admin_with_http_info(self, request):
        all_params = ['account', 'x_request_id', 'accept_language', 'account_type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'account' in local_var_params:
            path_params['account'] = local_var_params['account']

        query_params = []
        if 'account_type' in local_var_params:
            query_params.append(('accountType', local_var_params['account_type']))

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/usg/dcs/corp/admin/{account}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowCorpAdminResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_corp_basic_info_async(self, request):
        """企业管理员查询企业注册信息

        企业管理员通过该接口查询企业注册信息。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowCorpBasicInfo
        :type request: :class:`huaweicloudsdkmeeting.v1.ShowCorpBasicInfoRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.ShowCorpBasicInfoResponse`
        """
        return self.show_corp_basic_info_with_http_info(request)

    def show_corp_basic_info_with_http_info(self, request):
        all_params = ['x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/usg/dcs/corp',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowCorpBasicInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_corp_resource_async(self, request):
        """企业管理员查询企业内资源及业务权限

        企业管理员通过该接口查询企业内资源及业务权限，包括查询已使用的资源情况。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowCorpResource
        :type request: :class:`huaweicloudsdkmeeting.v1.ShowCorpResourceRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.ShowCorpResourceResponse`
        """
        return self.show_corp_resource_with_http_info(request)

    def show_corp_resource_with_http_info(self, request):
        all_params = ['x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/usg/dcs/corp/resource',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowCorpResourceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_department_async(self, request):
        """通过部门编码查询部门信息

        通过部门编码查询部门信息
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowDepartment
        :type request: :class:`huaweicloudsdkmeeting.v1.ShowDepartmentRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.ShowDepartmentResponse`
        """
        return self.show_department_with_http_info(request)

    def show_department_with_http_info(self, request):
        all_params = ['dept_code', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'dept_code' in local_var_params:
            path_params['dept_code'] = local_var_params['dept_code']

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/usg/abs/departments/{dept_code}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowDepartmentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_dept_and_child_dept_async(self, request):
        """查询部门及其一级子部门列表

        企业管理员通过该接口查询部门及其一级子部门列表。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowDeptAndChildDept
        :type request: :class:`huaweicloudsdkmeeting.v1.ShowDeptAndChildDeptRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.ShowDeptAndChildDeptResponse`
        """
        return self.show_dept_and_child_dept_with_http_info(request)

    def show_dept_and_child_dept_with_http_info(self, request):
        all_params = ['dept_code', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'dept_code' in local_var_params:
            path_params['dept_code'] = local_var_params['dept_code']

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/usg/dcs/member/dept/{dept_code}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowDeptAndChildDeptResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_device_detail_async(self, request):
        """查询终端详情

        企业管理员通过该接口查询终端详情。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowDeviceDetail
        :type request: :class:`huaweicloudsdkmeeting.v1.ShowDeviceDetailRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.ShowDeviceDetailResponse`
        """
        return self.show_device_detail_with_http_info(request)

    def show_device_detail_with_http_info(self, request):
        all_params = ['sn', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'sn' in local_var_params:
            path_params['sn'] = local_var_params['sn']

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/usg/dcs/corp/device/{sn}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowDeviceDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_device_status_async(self, request):
        """查询设备状态

        调用本接口可以查询硬终端的状态。
        硬终端与发起查询请求的帐号需在同一企业下，否则会鉴权失败。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowDeviceStatus
        :type request: :class:`huaweicloudsdkmeeting.v1.ShowDeviceStatusRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.ShowDeviceStatusResponse`
        """
        return self.show_device_status_with_http_info(request)

    def show_device_status_with_http_info(self, request):
        all_params = ['number', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-ID'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/acs/ap/userstatus',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowDeviceStatusResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_device_types_async(self, request):
        """获取所有终端类型

        企业管理员通过该接口获取所有的终端类型。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowDeviceTypes
        :type request: :class:`huaweicloudsdkmeeting.v1.ShowDeviceTypesRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.ShowDeviceTypesResponse`
        """
        return self.show_device_types_with_http_info(request)

    def show_device_types_with_http_info(self, request):
        all_params = ['x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/usg/dcs/termdevtype',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowDeviceTypesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_his_meeting_detail_async(self, request):
        """查询历史会议详情

        管理员可以查询管理权限域内所有的历史会议详情，普通用户仅能查询当前帐号管理的历史会议详情。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowHisMeetingDetail
        :type request: :class:`huaweicloudsdkmeeting.v1.ShowHisMeetingDetailRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.ShowHisMeetingDetailResponse`
        """
        return self.show_his_meeting_detail_with_http_info(request)

    def show_his_meeting_detail_with_http_info(self, request):
        all_params = ['conf_uuid', 'offset', 'limit', 'search_key', 'user_uuid', 'x_type', 'x_query_type', 'x_authorization_type', 'x_site_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conf_uuid' in local_var_params:
            query_params.append(('confUUID', local_var_params['conf_uuid']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'search_key' in local_var_params:
            query_params.append(('searchKey', local_var_params['search_key']))
        if 'user_uuid' in local_var_params:
            query_params.append(('userUUID', local_var_params['user_uuid']))

        header_params = {}
        if 'x_type' in local_var_params:
            header_params['X-Type'] = local_var_params['x_type']
        if 'x_query_type' in local_var_params:
            header_params['X-Query-Type'] = local_var_params['x_query_type']
        if 'x_authorization_type' in local_var_params:
            header_params['X-Authorization-Type'] = local_var_params['x_authorization_type']
        if 'x_site_id' in local_var_params:
            header_params['X-Site-Id'] = local_var_params['x_site_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/mmc/management/conferences/history/confDetail',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowHisMeetingDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_meeting_detail_async(self, request):
        """查询会议详情

        管理员可以查询管理权限域内所有会议的详情，普通用户仅能查询当前帐号管理的会议详情。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowMeetingDetail
        :type request: :class:`huaweicloudsdkmeeting.v1.ShowMeetingDetailRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.ShowMeetingDetailResponse`
        """
        return self.show_meeting_detail_with_http_info(request)

    def show_meeting_detail_with_http_info(self, request):
        all_params = ['conference_id', 'offset', 'limit', 'search_key', 'user_uuid', 'x_type', 'x_query_type', 'x_authorization_type', 'x_site_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'search_key' in local_var_params:
            query_params.append(('searchKey', local_var_params['search_key']))
        if 'user_uuid' in local_var_params:
            query_params.append(('userUUID', local_var_params['user_uuid']))

        header_params = {}
        if 'x_type' in local_var_params:
            header_params['X-Type'] = local_var_params['x_type']
        if 'x_query_type' in local_var_params:
            header_params['X-Query-Type'] = local_var_params['x_query_type']
        if 'x_authorization_type' in local_var_params:
            header_params['X-Authorization-Type'] = local_var_params['x_authorization_type']
        if 'x_site_id' in local_var_params:
            header_params['X-Site-Id'] = local_var_params['x_site_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/mmc/management/conferences/confDetail',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowMeetingDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_meeting_file_async(self, request):
        """查询会议纪要详情

        用户查询单个会议纪要详情（主要目的是为了得到外链）。 IdeaHub是使用fileCode来查，所以终端保持一致。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowMeetingFile
        :type request: :class:`huaweicloudsdkmeeting.v1.ShowMeetingFileRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.ShowMeetingFileResponse`
        """
        return self.show_meeting_file_with_http_info(request)

    def show_meeting_file_with_http_info(self, request):
        all_params = ['file_code', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'file_code' in local_var_params:
            path_params['file_code'] = local_var_params['file_code']

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/usg/sss/meeting-files/{file_code}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowMeetingFileResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_meeting_file_list_async(self, request):
        """打开会议纪要文件列表

        用户使用手机扫码后，手机端请求服务端，让服务端通知指定IdeaHub打开指定用户的会议纪要文件列表。二维码内容  cloudlink://cloudlink.huawei.com/h5page?action&#x3D;OPEN_MEETING_FILE_LIST&amp;key1&#x3D;value1&amp;key2&#x3D;value2    key/value的个数可能变化，终端解析后，在发起后续请求时，将所有key/value存为map，作为入参即可。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowMeetingFileList
        :type request: :class:`huaweicloudsdkmeeting.v1.ShowMeetingFileListRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.ShowMeetingFileListResponse`
        """
        return self.show_meeting_file_list_with_http_info(request)

    def show_meeting_file_list_with_http_info(self, request):
        all_params = ['info', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/sss/meeting-files/open-meeting-file-list',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowMeetingFileListResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_my_info_async(self, request):
        """用户查询自己的信息

        企业用户通过该接口查询自己的信息。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowMyInfo
        :type request: :class:`huaweicloudsdkmeeting.v1.ShowMyInfoRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.ShowMyInfoResponse`
        """
        return self.show_my_info_with_http_info(request)

    def show_my_info_with_http_info(self, request):
        all_params = ['x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/usg/dcs/member',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowMyInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_online_meeting_detail_async(self, request):
        """查询在线会议详情

        管理员可以查询管理权限域内所有的在线会议详情，普通用户仅能查询当前自己的帐号管理的在线会议详情。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowOnlineMeetingDetail
        :type request: :class:`huaweicloudsdkmeeting.v1.ShowOnlineMeetingDetailRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.ShowOnlineMeetingDetailResponse`
        """
        return self.show_online_meeting_detail_with_http_info(request)

    def show_online_meeting_detail_with_http_info(self, request):
        all_params = ['conference_id', 'offset', 'limit', 'search_key', 'user_uuid', 'x_type', 'x_query_type', 'x_authorization_type', 'x_site_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'search_key' in local_var_params:
            query_params.append(('searchKey', local_var_params['search_key']))
        if 'user_uuid' in local_var_params:
            query_params.append(('userUUID', local_var_params['user_uuid']))

        header_params = {}
        if 'x_type' in local_var_params:
            header_params['X-Type'] = local_var_params['x_type']
        if 'x_query_type' in local_var_params:
            header_params['X-Query-Type'] = local_var_params['x_query_type']
        if 'x_authorization_type' in local_var_params:
            header_params['X-Authorization-Type'] = local_var_params['x_authorization_type']
        if 'x_site_id' in local_var_params:
            header_params['X-Site-Id'] = local_var_params['x_site_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/mmc/management/conferences/online/confDetail',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowOnlineMeetingDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_org_res_async(self, request):
        """查询企业的资源使用信息

        企业管理员查询资源使用信息
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowOrgRes
        :type request: :class:`huaweicloudsdkmeeting.v1.ShowOrgResRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.ShowOrgResResponse`
        """
        return self.show_org_res_with_http_info(request)

    def show_org_res_with_http_info(self, request):
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
            resource_path='/v1/mmc/management/orgRes',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowOrgResResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_program_async(self, request):
        """根据ID查询节目详情

        根据ID获取节目详情
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowProgram
        :type request: :class:`huaweicloudsdkmeeting.v1.ShowProgramRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.ShowProgramResponse`
        """
        return self.show_program_with_http_info(request)

    def show_program_with_http_info(self, request):
        all_params = ['id', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/usg/sss/programs/{id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowProgramResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_publication_async(self, request):
        """根据ID查询信息窗发布详情

        根据ID获取发布详情
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowPublication
        :type request: :class:`huaweicloudsdkmeeting.v1.ShowPublicationRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.ShowPublicationResponse`
        """
        return self.show_publication_with_http_info(request)

    def show_publication_with_http_info(self, request):
        all_params = ['id', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/usg/sss/publications/{id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowPublicationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_real_time_info_of_meeting_async(self, request):
        """查询会议实时信息

        查询会议实时信息
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowRealTimeInfoOfMeeting
        :type request: :class:`huaweicloudsdkmeeting.v1.ShowRealTimeInfoOfMeetingRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.ShowRealTimeInfoOfMeetingResponse`
        """
        return self.show_real_time_info_of_meeting_with_http_info(request)

    def show_real_time_info_of_meeting_with_http_info(self, request):
        all_params = ['conference_id', 'x_conference_authorization']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/mmc/control/conferences/realTimeInfo',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowRealTimeInfoOfMeetingResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_recording_detail_async(self, request):
        """查询录制详情

        查询某个录制详情。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowRecordingDetail
        :type request: :class:`huaweicloudsdkmeeting.v1.ShowRecordingDetailRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.ShowRecordingDetailResponse`
        """
        return self.show_recording_detail_with_http_info(request)

    def show_recording_detail_with_http_info(self, request):
        all_params = ['conf_uuid', 'user_uuid', 'x_authorization_type', 'x_site_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conf_uuid' in local_var_params:
            query_params.append(('confUUID', local_var_params['conf_uuid']))
        if 'user_uuid' in local_var_params:
            query_params.append(('userUUID', local_var_params['user_uuid']))

        header_params = {}
        if 'x_authorization_type' in local_var_params:
            header_params['X-Authorization-Type'] = local_var_params['x_authorization_type']
        if 'x_site_id' in local_var_params:
            header_params['X-Site-Id'] = local_var_params['x_site_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/mmc/management/conferences/record/files',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowRecordingDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_recording_file_download_urls_async(self, request):
        """查询录制文件下载链接

        查询某个录制文件下载链接。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowRecordingFileDownloadUrls
        :type request: :class:`huaweicloudsdkmeeting.v1.ShowRecordingFileDownloadUrlsRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.ShowRecordingFileDownloadUrlsResponse`
        """
        return self.show_recording_file_download_urls_with_http_info(request)

    def show_recording_file_download_urls_with_http_info(self, request):
        all_params = ['conf_uuid', 'offset', 'limit', 'x_authorization_type', 'x_site_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conf_uuid' in local_var_params:
            query_params.append(('confUUID', local_var_params['conf_uuid']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}
        if 'x_authorization_type' in local_var_params:
            header_params['X-Authorization-Type'] = local_var_params['x_authorization_type']
        if 'x_site_id' in local_var_params:
            header_params['X-Site-Id'] = local_var_params['x_site_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/mmc/management/record/downloadurls',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowRecordingFileDownloadUrlsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_region_info_of_meeting_async(self, request):
        """查询会议所在区域信息

        查询会议所在区域信息，如果会议不存在或者会议未召开，返回对应的错误码。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowRegionInfoOfMeeting
        :type request: :class:`huaweicloudsdkmeeting.v1.ShowRegionInfoOfMeetingRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.ShowRegionInfoOfMeetingResponse`
        """
        return self.show_region_info_of_meeting_with_http_info(request)

    def show_region_info_of_meeting_with_http_info(self, request):
        all_params = ['conference_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))

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
            resource_path='/v1/mmc/management/conferences/region/info',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowRegionInfoOfMeetingResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_room_setting_async(self, request):
        """查询直播间高级设置

        查询直播间高级设置
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowRoomSetting
        :type request: :class:`huaweicloudsdkmeeting.v1.ShowRoomSettingRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.ShowRoomSettingResponse`
        """
        return self.show_room_setting_with_http_info(request)

    def show_room_setting_with_http_info(self, request):
        all_params = ['conference_id', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'conference_id' in local_var_params:
            path_params['conference_id'] = local_var_params['conference_id']

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/wss/webinar/open/room-setting/{conference_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowRoomSettingResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_sp_res_async(self, request):
        """查询SP的共享资源使用信息

        SP管理查询所属SP的共享资源使用信息
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowSpRes
        :type request: :class:`huaweicloudsdkmeeting.v1.ShowSpResRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.ShowSpResResponse`
        """
        return self.show_sp_res_with_http_info(request)

    def show_sp_res_with_http_info(self, request):
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
            resource_path='/v1/mmc/management/spRes',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowSpResResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_sp_resource_async(self, request):
        """SP管理员查询资源信息

        SP管理员查询SP的所有资源，包括已使用的资源
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowSpResource
        :type request: :class:`huaweicloudsdkmeeting.v1.ShowSpResourceRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.ShowSpResourceResponse`
        """
        return self.show_sp_resource_with_http_info(request)

    def show_sp_resource_with_http_info(self, request):
        all_params = ['x_request_id', 'accept_language', 'query_group']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'query_group' in local_var_params:
            query_params.append(('queryGroup', local_var_params['query_group']))

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/usg/dcs/sp/resource',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowSpResourceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_sso_config_async(self, request):
        """查询SSO鉴权配置

        查询SSO鉴权配置
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowSsoConfig
        :type request: :class:`huaweicloudsdkmeeting.v1.ShowSsoConfigRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.ShowSsoConfigResponse`
        """
        return self.show_sso_config_with_http_info(request)

    def show_sso_config_with_http_info(self, request):
        all_params = ['x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/usg/acs/authorizeconfig',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowSsoConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_user_detail_async(self, request):
        """查询用户详情

        企业管理员通过该接口查询企业用户详情
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowUserDetail
        :type request: :class:`huaweicloudsdkmeeting.v1.ShowUserDetailRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.ShowUserDetailResponse`
        """
        return self.show_user_detail_with_http_info(request)

    def show_user_detail_with_http_info(self, request):
        all_params = ['account', 'x_request_id', 'accept_language', 'account_type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'account' in local_var_params:
            path_params['account'] = local_var_params['account']

        query_params = []
        if 'account_type' in local_var_params:
            query_params.append(('accountType', local_var_params['account_type']))

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/usg/dcs/corp/member/{account}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowUserDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_web_hook_config_async(self, request):
        """查询事件订阅配置信息

        查询企业事件订阅配置
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowWebHookConfig
        :type request: :class:`huaweicloudsdkmeeting.v1.ShowWebHookConfigRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.ShowWebHookConfigResponse`
        """
        return self.show_web_hook_config_with_http_info(request)

    def show_web_hook_config_with_http_info(self, request):
        all_params = ['corp_id', 'sp_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'corp_id' in local_var_params:
            query_params.append(('corpId', local_var_params['corp_id']))
        if 'sp_id' in local_var_params:
            query_params.append(('spId', local_var_params['sp_id']))

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
            resource_path='/v1/mmc/management/webhook/link-config',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowWebHookConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_webinar_async(self, request):
        """查询网络研讨会详情

        根据conference_id查询网络研讨会详情。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowWebinar
        :type request: :class:`huaweicloudsdkmeeting.v1.ShowWebinarRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.ShowWebinarResponse`
        """
        return self.show_webinar_with_http_info(request)

    def show_webinar_with_http_info(self, request):
        all_params = ['conference_id', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'conference_id' in local_var_params:
            path_params['conference_id'] = local_var_params['conference_id']

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/wss/webinar/open/conferences/{conference_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowWebinarResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def start_meeting_async(self, request):
        """通过会议ID和密码激活会议

        终端到会管进行鉴权并激活会议，先通过该接口获取会议所在Region信息，该接口需要携带会议主席密码，在会议未召开的情况下，该接口会拉起会议。如果已存在会议，则直接返回在线会议所在Region信息
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for StartMeeting
        :type request: :class:`huaweicloudsdkmeeting.v1.StartMeetingRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.StartMeetingResponse`
        """
        return self.start_meeting_with_http_info(request)

    def start_meeting_with_http_info(self, request):
        all_params = ['start_request']
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
            resource_path='/v1/mmc/management/conferences/start',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='StartMeetingResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def stop_meeting_async(self, request):
        """结束会议

        结束会议。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for StopMeeting
        :type request: :class:`huaweicloudsdkmeeting.v1.StopMeetingRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.StopMeetingResponse`
        """
        return self.stop_meeting_with_http_info(request)

    def stop_meeting_with_http_info(self, request):
        all_params = ['conference_id', 'x_conference_authorization']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/mmc/control/conferences/stop',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='StopMeetingResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def switch_mode_async(self, request):
        """切换视频显示策略

        切换视频显示策略
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for SwitchMode
        :type request: :class:`huaweicloudsdkmeeting.v1.SwitchModeRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SwitchModeResponse`
        """
        return self.switch_mode_with_http_info(request)

    def switch_mode_with_http_info(self, request):
        all_params = ['conference_id', 'x_conference_authorization', 'req_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

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
            resource_path='/v1/mmc/control/conferences/display/mode',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SwitchModeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_contact_async(self, request):
        """修改手机或邮箱

        企业用户通过该接口修改手机或邮箱，需要先获取验证码，验证多次失败会禁止修改。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateContact
        :type request: :class:`huaweicloudsdkmeeting.v1.UpdateContactRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.UpdateContactResponse`
        """
        return self.update_contact_with_http_info(request)

    def update_contact_with_http_info(self, request):
        all_params = ['verification_code_dto', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/dcs/member/contact',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateContactResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_corp_async(self, request):
        """SP管理员修改企业

        修改企业，若任一参数为null或者不携带则不修改
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateCorp
        :type request: :class:`huaweicloudsdkmeeting.v1.UpdateCorpRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.UpdateCorpResponse`
        """
        return self.update_corp_with_http_info(request)

    def update_corp_with_http_info(self, request):
        all_params = ['id', 'corp_dto', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/dcs/sp/corp/{id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateCorpResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_corp_basic_info_async(self, request):
        """企业管理员修改企业注册信息

        企业管理员通过该接口修改企业注册信息。当前只支持修改地址。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateCorpBasicInfo
        :type request: :class:`huaweicloudsdkmeeting.v1.UpdateCorpBasicInfoRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.UpdateCorpBasicInfoResponse`
        """
        return self.update_corp_basic_info_with_http_info(request)

    def update_corp_basic_info_with_http_info(self, request):
        all_params = ['mod_dto', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/dcs/corp',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateCorpBasicInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_department_async(self, request):
        """修改部门

        企业管理员通过该接口修改部门。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateDepartment
        :type request: :class:`huaweicloudsdkmeeting.v1.UpdateDepartmentRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.UpdateDepartmentResponse`
        """
        return self.update_department_with_http_info(request)

    def update_department_with_http_info(self, request):
        all_params = ['dept_code', 'dept_dto', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'dept_code' in local_var_params:
            path_params['dept_code'] = local_var_params['dept_code']

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/dcs/corp/dept/{dept_code}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateDepartmentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_device_async(self, request):
        """修改终端

        企业管理员通过该接口修改终端。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateDevice
        :type request: :class:`huaweicloudsdkmeeting.v1.UpdateDeviceRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.UpdateDeviceResponse`
        """
        return self.update_device_with_http_info(request)

    def update_device_with_http_info(self, request):
        all_params = ['sn', 'device_dto', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'sn' in local_var_params:
            path_params['sn'] = local_var_params['sn']

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/dcs/corp/device/{sn}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateDeviceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_material_async(self, request):
        """更新信息窗素材

        更新信息窗素材
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateMaterial
        :type request: :class:`huaweicloudsdkmeeting.v1.UpdateMaterialRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.UpdateMaterialResponse`
        """
        return self.update_material_with_http_info(request)

    def update_material_with_http_info(self, request):
        all_params = ['id', 'update_material_request_dto', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/sss/materials/{id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateMaterialResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_meeting_async(self, request):
        """编辑预约会议

        编辑预约会议。会议开始后，不能被编辑。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateMeeting
        :type request: :class:`huaweicloudsdkmeeting.v1.UpdateMeetingRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.UpdateMeetingResponse`
        """
        return self.update_meeting_with_http_info(request)

    def update_meeting_with_http_info(self, request):
        all_params = ['conference_id', 'req_body', 'user_uuid', 'x_authorization_type', 'x_site_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))
        if 'user_uuid' in local_var_params:
            query_params.append(('userUUID', local_var_params['user_uuid']))

        header_params = {}
        if 'x_authorization_type' in local_var_params:
            header_params['X-Authorization-Type'] = local_var_params['x_authorization_type']
        if 'x_site_id' in local_var_params:
            header_params['X-Site-Id'] = local_var_params['x_site_id']

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
            resource_path='/v1/mmc/management/conferences',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateMeetingResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_member_vmr_async(self, request):
        """修改用会议室及个人会议ID信息

        企业用户登录后可以修改分配给用户的云会议室及个人会议ID。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateMemberVmr
        :type request: :class:`huaweicloudsdkmeeting.v1.UpdateMemberVmrRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.UpdateMemberVmrResponse`
        """
        return self.update_member_vmr_with_http_info(request)

    def update_member_vmr_with_http_info(self, request):
        all_params = ['id', 'mod_dto', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/dcs/member/vmr/{id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateMemberVmrResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_my_info_async(self, request):
        """用户修改自己的信息

        企业用户通过该接口修改自己的信息。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateMyInfo
        :type request: :class:`huaweicloudsdkmeeting.v1.UpdateMyInfoRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.UpdateMyInfoResponse`
        """
        return self.update_my_info_with_http_info(request)

    def update_my_info_with_http_info(self, request):
        all_params = ['member_dto', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/dcs/member',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateMyInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_program_async(self, request):
        """更新信息窗节目

        更新信息窗节目
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateProgram
        :type request: :class:`huaweicloudsdkmeeting.v1.UpdateProgramRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.UpdateProgramResponse`
        """
        return self.update_program_with_http_info(request)

    def update_program_with_http_info(self, request):
        all_params = ['id', 'program_dto', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/sss/programs/{id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateProgramResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_publication_async(self, request):
        """修改信息窗发布

        修改信息窗发布
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdatePublication
        :type request: :class:`huaweicloudsdkmeeting.v1.UpdatePublicationRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.UpdatePublicationResponse`
        """
        return self.update_publication_with_http_info(request)

    def update_publication_with_http_info(self, request):
        all_params = ['id', 'publication_dto', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/sss/publications/{id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdatePublicationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_pwd_async(self, request):
        """修改密码

        企业成员通过该接口提供用户修改密码功能，服务器收到请求，修改用户密码并返回结果。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdatePwd
        :type request: :class:`huaweicloudsdkmeeting.v1.UpdatePwdRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.UpdatePwdResponse`
        """
        return self.update_pwd_with_http_info(request)

    def update_pwd_with_http_info(self, request):
        all_params = ['mod_pwd_req_dto', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-ID'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/acs/password',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdatePwdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_recurring_meeting_async(self, request):
        """修改预定周期会议

        修改预定的周期会议；会议开始时，不能修改会议
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateRecurringMeeting
        :type request: :class:`huaweicloudsdkmeeting.v1.UpdateRecurringMeetingRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.UpdateRecurringMeetingResponse`
        """
        return self.update_recurring_meeting_with_http_info(request)

    def update_recurring_meeting_with_http_info(self, request):
        all_params = ['conference_id', 'req_body', 'x_authorization_type', 'user_uuid', 'x_site_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_uuid' in local_var_params:
            query_params.append(('userUUID', local_var_params['user_uuid']))
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))

        header_params = {}
        if 'x_authorization_type' in local_var_params:
            header_params['X-Authorization-Type'] = local_var_params['x_authorization_type']
        if 'x_site_id' in local_var_params:
            header_params['X-Site-Id'] = local_var_params['x_site_id']

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
            resource_path='/v1/mmc/management/cycleconferences',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateRecurringMeetingResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_recurring_sub_meeting_async(self, request):
        """修改预定周期子会议

        修改预定的周期子会议；会议开始时，不能修改会议
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateRecurringSubMeeting
        :type request: :class:`huaweicloudsdkmeeting.v1.UpdateRecurringSubMeetingRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.UpdateRecurringSubMeetingResponse`
        """
        return self.update_recurring_sub_meeting_with_http_info(request)

    def update_recurring_sub_meeting_with_http_info(self, request):
        all_params = ['conference_id', 'req_body', 'x_authorization_type', 'user_uuid', 'x_site_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_uuid' in local_var_params:
            query_params.append(('userUUID', local_var_params['user_uuid']))
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))

        header_params = {}
        if 'x_authorization_type' in local_var_params:
            header_params['X-Authorization-Type'] = local_var_params['x_authorization_type']
        if 'x_site_id' in local_var_params:
            header_params['X-Site-Id'] = local_var_params['x_site_id']

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
            resource_path='/v1/mmc/management/conferences/cyclesubconf',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateRecurringSubMeetingResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_resource_async(self, request):
        """SP管理员根据修改企业资源

        企业修改资源的过期时间、停用状态
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateResource
        :type request: :class:`huaweicloudsdkmeeting.v1.UpdateResourceRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.UpdateResourceResponse`
        """
        return self.update_resource_with_http_info(request)

    def update_resource_with_http_info(self, request):
        all_params = ['corp_id', 'resource_list', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'corp_id' in local_var_params:
            path_params['corp_id'] = local_var_params['corp_id']

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/dcs/sp/corp/{corp_id}/resource',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateResourceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_room_setting_async(self, request):
        """高级设置 - 直播间设置

        保存直播间高级设置。如有部分配置信息修改，则其他未修改的原始值也需要传入，否则部分字段会替换为默认值(即：只支持全量保存)
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateRoomSetting
        :type request: :class:`huaweicloudsdkmeeting.v1.UpdateRoomSettingRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.UpdateRoomSettingResponse`
        """
        return self.update_room_setting_with_http_info(request)

    def update_room_setting_with_http_info(self, request):
        all_params = ['conference_id', 'x_request_id', 'accept_language', 'open_room_setting_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'conference_id' in local_var_params:
            path_params['conference_id'] = local_var_params['conference_id']

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/wss/webinar/open/room-setting/{conference_id}',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateRoomSettingResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_started_conf_config_async(self, request):
        """会中修改配置

        会中修改配置。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateStartedConfConfig
        :type request: :class:`huaweicloudsdkmeeting.v1.UpdateStartedConfConfigRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.UpdateStartedConfConfigResponse`
        """
        return self.update_started_conf_config_with_http_info(request)

    def update_started_conf_config_with_http_info(self, request):
        all_params = ['conference_id', 'x_conference_authorization', 'update_started_config_req_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

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
            resource_path='/v1/mmc/control/conferences/updateStartedConfConfig',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateStartedConfConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_token_async(self, request):
        """刷新Token

        该接口提供刷新Token功能，根据传入的Token，刷新Token失效时间并返回结果。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateToken
        :type request: :class:`huaweicloudsdkmeeting.v1.UpdateTokenRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.UpdateTokenResponse`
        """
        return self.update_token_with_http_info(request)

    def update_token_with_http_info(self, request):
        all_params = ['x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-ID'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/usg/acs/token',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateTokenResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_user_async(self, request):
        """修改用户

        企业管理员通过该接口修改企业用户。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateUser
        :type request: :class:`huaweicloudsdkmeeting.v1.UpdateUserRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.UpdateUserResponse`
        """
        return self.update_user_with_http_info(request)

    def update_user_with_http_info(self, request):
        all_params = ['account', 'user_dto', 'x_request_id', 'accept_language', 'account_type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'account' in local_var_params:
            path_params['account'] = local_var_params['account']

        query_params = []
        if 'account_type' in local_var_params:
            query_params.append(('accountType', local_var_params['account_type']))

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/dcs/corp/member/{account}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateUserResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_web_hook_config_status_async(self, request):
        """变更订阅配置使用状态

        变更订阅配置使用状态
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateWebHookConfigStatus
        :type request: :class:`huaweicloudsdkmeeting.v1.UpdateWebHookConfigStatusRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.UpdateWebHookConfigStatusResponse`
        """
        return self.update_web_hook_config_status_with_http_info(request)

    def update_web_hook_config_status_with_http_info(self, request):
        all_params = ['id', 'status']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))

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
            resource_path='/v1/mmc/management/webhook/change-status',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateWebHookConfigStatusResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_webinar_async(self, request):
        """编辑网络研讨会

        您可根据需要修改普通网络研讨会和周期网络研讨会。注意：暂不支持添加外部联系人作为与会嘉宾
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateWebinar
        :type request: :class:`huaweicloudsdkmeeting.v1.UpdateWebinarRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.UpdateWebinarResponse`
        """
        return self.update_webinar_with_http_info(request)

    def update_webinar_with_http_info(self, request):
        all_params = ['edit_webinar_request_body', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/wss/webinar/open/conferences',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateWebinarResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def upload_file_async(self, request):
        """开放接口 - 文件上传

        文件上传的开放接口
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UploadFile
        :type request: :class:`huaweicloudsdkmeeting.v1.UploadFileRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.UploadFileResponse`
        """
        return self.upload_file_with_http_info(request)

    def upload_file_with_http_info(self, request):
        all_params = ['file', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

        form_params = {}
        if 'file' in local_var_params:
            form_params['file'] = local_var_params['file']

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['multipart/form-data'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/wss/webinar/open/res/file',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UploadFileResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def search_qos_history_meetings_async(self, request):
        """查询QoS历史会议列表

        * 查询企业内QoS历史会议列表。
        * 支持按照时间范围查询，可查询最近3个月内数据。
        * 权限角色 &#x3D; 旗舰版企业/标准版企业 + 管理员。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for SearchQosHistoryMeetings
        :type request: :class:`huaweicloudsdkmeeting.v1.SearchQosHistoryMeetingsRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SearchQosHistoryMeetingsResponse`
        """
        return self.search_qos_history_meetings_with_http_info(request)

    def search_qos_history_meetings_with_http_info(self, request):
        all_params = ['start_date', 'end_date', 'offset', 'limit', 'search_key']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start_date' in local_var_params:
            query_params.append(('startDate', local_var_params['start_date']))
        if 'end_date' in local_var_params:
            query_params.append(('endDate', local_var_params['end_date']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'search_key' in local_var_params:
            query_params.append(('searchKey', local_var_params['search_key']))

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
            resource_path='/v1/metrics/conferences/history',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SearchQosHistoryMeetingsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def search_qos_online_meetings_async(self, request):
        """查询QoS在线会议列表

        * 查询企业内QoS在线会议列表。
        * 权限角色 &#x3D; 旗舰版企业/标准版企业 + 管理员。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for SearchQosOnlineMeetings
        :type request: :class:`huaweicloudsdkmeeting.v1.SearchQosOnlineMeetingsRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SearchQosOnlineMeetingsResponse`
        """
        return self.search_qos_online_meetings_with_http_info(request)

    def search_qos_online_meetings_with_http_info(self, request):
        all_params = ['offset', 'limit', 'search_key']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'search_key' in local_var_params:
            query_params.append(('searchKey', local_var_params['search_key']))

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
            resource_path='/v1/metrics/conferences/online',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SearchQosOnlineMeetingsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def search_qos_participant_detail_async(self, request):
        """查询与会者的QoS数据

        * 查询企业内指定与会者的QoS数据，按照音频，视频，屏幕共享，CPU分类查询QoS数据。
        * QoS数据的打点周期为5秒。
        * 权限角色 &#x3D; 旗舰版企业/标准版企业 + 管理员。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for SearchQosParticipantDetail
        :type request: :class:`huaweicloudsdkmeeting.v1.SearchQosParticipantDetailRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SearchQosParticipantDetailResponse`
        """
        return self.search_qos_participant_detail_with_http_info(request)

    def search_qos_participant_detail_with_http_info(self, request):
        all_params = ['conf_uuid', 'conf_type', 'participant_id', 'qos_type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conf_uuid' in local_var_params:
            query_params.append(('confUUID', local_var_params['conf_uuid']))
        if 'conf_type' in local_var_params:
            query_params.append(('confType', local_var_params['conf_type']))
        if 'participant_id' in local_var_params:
            query_params.append(('participantID', local_var_params['participant_id']))
        if 'qos_type' in local_var_params:
            query_params.append(('qosType', local_var_params['qos_type']))

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
            resource_path='/v1/metrics/conference/participant/qos',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SearchQosParticipantDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def search_qos_participants_async(self, request):
        """查询QoS会议与会者列表

        * 查询企业内QoS会议与会者列表。
        * 权限角色 &#x3D; 旗舰版企业/标准版企业 + 管理员。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for SearchQosParticipants
        :type request: :class:`huaweicloudsdkmeeting.v1.SearchQosParticipantsRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SearchQosParticipantsResponse`
        """
        return self.search_qos_participants_with_http_info(request)

    def search_qos_participants_with_http_info(self, request):
        all_params = ['conf_uuid', 'conf_type', 'offset', 'limit', 'search_key']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conf_uuid' in local_var_params:
            query_params.append(('confUUID', local_var_params['conf_uuid']))
        if 'conf_type' in local_var_params:
            query_params.append(('confType', local_var_params['conf_type']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'search_key' in local_var_params:
            query_params.append(('searchKey', local_var_params['search_key']))

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
            resource_path='/v1/metrics/conference/participants',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SearchQosParticipantsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def set_qos_threshold_async(self, request):
        """设置企业租户指定类型的会议质量阈值

        * 设置企业租户指定类型的会议质量阈值。
        * 权限角色 &#x3D; 旗舰版企业/标准版企业 + 管理员。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for SetQosThreshold
        :type request: :class:`huaweicloudsdkmeeting.v1.SetQosThresholdRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SetQosThresholdResponse`
        """
        return self.set_qos_threshold_with_http_info(request)

    def set_qos_threshold_with_http_info(self, request):
        all_params = ['threshold_type', 'set_qos_threshold_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'threshold_type' in local_var_params:
            query_params.append(('thresholdType', local_var_params['threshold_type']))

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json; charset=utf-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/metrics/conference/threshold',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SetQosThresholdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_qos_threshold_async(self, request):
        """查询企业租户指定类型的会议质量阈值

        * 查询企业租户指定类型的会议质量阈值。
        * 权限角色 &#x3D; 旗舰版企业/标准版企业 + 管理员。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowQosThreshold
        :type request: :class:`huaweicloudsdkmeeting.v1.ShowQosThresholdRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.ShowQosThresholdResponse`
        """
        return self.show_qos_threshold_with_http_info(request)

    def show_qos_threshold_with_http_info(self, request):
        all_params = ['threshold_type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'threshold_type' in local_var_params:
            query_params.append(('thresholdType', local_var_params['threshold_type']))

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
            resource_path='/v1/metrics/conference/threshold',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowQosThresholdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def search_statistic_conference_info_async(self, request):
        """查询企业级会议总体统计数据

        * 查询企业级会议指定时间范围内总体统计数据，按日/按月统计。
        * 查询企业级会议单日内总体统计数据，按小时统计。
        * 权限角色 &#x3D; 旗舰版企业/标准版企业 + 管理员。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for SearchStatisticConferenceInfo
        :type request: :class:`huaweicloudsdkmeeting.v1.SearchStatisticConferenceInfoRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SearchStatisticConferenceInfoResponse`
        """
        return self.search_statistic_conference_info_with_http_info(request)

    def search_statistic_conference_info_with_http_info(self, request):
        all_params = ['time_unit', 'start_time', 'end_time', 'category', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'time_unit' in local_var_params:
            query_params.append(('timeUnit', local_var_params['time_unit']))
        if 'start_time' in local_var_params:
            query_params.append(('startTime', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('endTime', local_var_params['end_time']))
        if 'category' in local_var_params:
            query_params.append(('category', local_var_params['category']))

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
            resource_path='/v1/metrics/dashboard/statistic/conference/info',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SearchStatisticConferenceInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def search_statistic_conference_participant_async(self, request):
        """查询企业级会议与会统计数据

        * 查询企业级会议与会用户统计数据，按日/按月统计。
        * 查询企业级会议与会硬件终端统计数据，按日/按月统计。
        * 查询企业级会议与会设备统计数据，按日/按月统计。
        * 权限角色 &#x3D; 旗舰版企业/标准版企业 + 管理员。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for SearchStatisticConferenceParticipant
        :type request: :class:`huaweicloudsdkmeeting.v1.SearchStatisticConferenceParticipantRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SearchStatisticConferenceParticipantResponse`
        """
        return self.search_statistic_conference_participant_with_http_info(request)

    def search_statistic_conference_participant_with_http_info(self, request):
        all_params = ['time_unit', 'start_time', 'end_time', 'category', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'time_unit' in local_var_params:
            query_params.append(('timeUnit', local_var_params['time_unit']))
        if 'start_time' in local_var_params:
            query_params.append(('startTime', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('endTime', local_var_params['end_time']))
        if 'category' in local_var_params:
            query_params.append(('category', local_var_params['category']))

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
            resource_path='/v1/metrics/dashboard/statistic/conference/participant',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SearchStatisticConferenceParticipantResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def search_statistic_resource_info_async(self, request):
        """查询企业级会议已购资源使用统计数据

        * 查询企业级会议的已购资源使用状况，按日/按月统计。
        * 权限角色 &#x3D; 旗舰版企业/标准版企业 + 管理员。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for SearchStatisticResourceInfo
        :type request: :class:`huaweicloudsdkmeeting.v1.SearchStatisticResourceInfoRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SearchStatisticResourceInfoResponse`
        """
        return self.search_statistic_resource_info_with_http_info(request)

    def search_statistic_resource_info_with_http_info(self, request):
        all_params = ['time_unit', 'start_time', 'end_time', 'category', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'time_unit' in local_var_params:
            query_params.append(('timeUnit', local_var_params['time_unit']))
        if 'start_time' in local_var_params:
            query_params.append(('startTime', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('endTime', local_var_params['end_time']))
        if 'category' in local_var_params:
            query_params.append(('category', local_var_params['category']))

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
            resource_path='/v1/metrics/dashboard/statistic/resource/info',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SearchStatisticResourceInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def search_statistic_user_info_async(self, request):
        """查询企业级会议的用户统计数据

        * 查询企业级会议用户登录数据，按日/按月统计。
        * 查询企业级会议用户激活数据，按日/按月统计。
        * 查询企业级会议用户登录设备数据，按日/按月统计。
        * 权限角色 &#x3D; 旗舰版企业/标准版企业 + 管理员。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for SearchStatisticUserInfo
        :type request: :class:`huaweicloudsdkmeeting.v1.SearchStatisticUserInfoRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SearchStatisticUserInfoResponse`
        """
        return self.search_statistic_user_info_with_http_info(request)

    def search_statistic_user_info_with_http_info(self, request):
        all_params = ['time_unit', 'start_time', 'end_time', 'category', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'time_unit' in local_var_params:
            query_params.append(('timeUnit', local_var_params['time_unit']))
        if 'start_time' in local_var_params:
            query_params.append(('startTime', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('endTime', local_var_params['end_time']))
        if 'category' in local_var_params:
            query_params.append(('category', local_var_params['category']))

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
            resource_path='/v1/metrics/dashboard/statistic/user/info',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SearchStatisticUserInfoResponse',
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
