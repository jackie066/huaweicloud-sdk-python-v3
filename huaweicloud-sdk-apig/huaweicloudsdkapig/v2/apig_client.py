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


class ApigClient(Client):
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
        super(ApigClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkapig.v2.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "ApigClient":
            raise TypeError("client type error, support client type is ApigClient")

        return ClientBuilder(clazz)

    def add_eip_v2(self, request):
        """实例更新或绑定EIP

        实例更新或绑定EIP
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for AddEipV2
        :type request: :class:`huaweicloudsdkapig.v2.AddEipV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.AddEipV2Response`
        """
        return self.add_eip_v2_with_http_info(request)

    def add_eip_v2_with_http_info(self, request):
        all_params = ['instance_id', 'add_eip_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/eip',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='AddEipV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def add_engress_eip_v2(self, request):
        """开启实例公网出口

        实例开启公网出口
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for AddEngressEipV2
        :type request: :class:`huaweicloudsdkapig.v2.AddEngressEipV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.AddEngressEipV2Response`
        """
        return self.add_engress_eip_v2_with_http_info(request)

    def add_engress_eip_v2_with_http_info(self, request):
        all_params = ['instance_id', 'add_engress_eip_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/nat-eip',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='AddEngressEipV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def associate_certificate_v2(self, request):
        """绑定域名证书

        如果创建API时，“定义API请求”使用HTTPS请求协议，那么在独立域名中需要添加SSL证书。
        本章节主要介绍为特定域名绑定证书。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for AssociateCertificateV2
        :type request: :class:`huaweicloudsdkapig.v2.AssociateCertificateV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.AssociateCertificateV2Response`
        """
        return self.associate_certificate_v2_with_http_info(request)

    def associate_certificate_v2_with_http_info(self, request):
        all_params = ['instance_id', 'group_id', 'domain_id', 'associate_certificate_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/api-groups/{group_id}/domains/{domain_id}/certificate',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='AssociateCertificateV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def associate_domain_v2(self, request):
        """绑定域名

        用户自定义的域名，需要CNAME到API分组的子域名上才能生效，具体方法请参见《云解析服务用户指南》的“添加CANME类型记录集”章节。
        每个API分组下最多可绑定5个域名。绑定域名后，用户可通过自定义域名调用API。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for AssociateDomainV2
        :type request: :class:`huaweicloudsdkapig.v2.AssociateDomainV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.AssociateDomainV2Response`
        """
        return self.associate_domain_v2_with_http_info(request)

    def associate_domain_v2_with_http_info(self, request):
        all_params = ['instance_id', 'group_id', 'associate_domain_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/api-groups/{group_id}/domains',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='AssociateDomainV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def associate_signature_key_v2(self, request):
        """绑定签名密钥

        签名密钥创建后，需要绑定到API才能生效。
        
        将签名密钥绑定到API后，则API网关请求后端服务时就会使用这个签名密钥进行加密签名，后端服务可以校验这个签名来验证请求来源。
        
        将指定的签名密钥绑定到一个或多个已发布的API上。同一个API发布到不同的环境可以绑定不同的签名密钥；一个API在发布到特定环境后只能绑定一个签名密钥。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for AssociateSignatureKeyV2
        :type request: :class:`huaweicloudsdkapig.v2.AssociateSignatureKeyV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.AssociateSignatureKeyV2Response`
        """
        return self.associate_signature_key_v2_with_http_info(request)

    def associate_signature_key_v2_with_http_info(self, request):
        all_params = ['instance_id', 'associate_signature_key_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/sign-bindings',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='AssociateSignatureKeyV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_custom_authorizer_v2(self, request):
        """创建自定义认证

        创建自定义认证
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateCustomAuthorizerV2
        :type request: :class:`huaweicloudsdkapig.v2.CreateCustomAuthorizerV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.CreateCustomAuthorizerV2Response`
        """
        return self.create_custom_authorizer_v2_with_http_info(request)

    def create_custom_authorizer_v2_with_http_info(self, request):
        all_params = ['instance_id', 'create_custom_authorizer_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/authorizers',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateCustomAuthorizerV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_environment_v2(self, request):
        """创建环境

        在实际的生产中，API提供者可能有多个环境，如开发环境、测试环境、生产环境等，用户可以自由将API发布到某个环境，供调用者调用。
        
        对于不同的环境，API的版本、请求地址甚至于包括请求消息等均有可能不同。如：某个API，v1.0的版本为稳定版本，发布到了生产环境供生产使用，同时，该API正处于迭代中，v1.1的版本是开发人员交付测试人员进行测试的版本，发布在测试环境上，而v1.2的版本目前开发团队正处于开发过程中，可以发布到开发环境进行自测等。
        
        为此，API网关提供多环境管理功能，使租户能够最大化的模拟实际场景，低成本的接入API网关。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateEnvironmentV2
        :type request: :class:`huaweicloudsdkapig.v2.CreateEnvironmentV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.CreateEnvironmentV2Response`
        """
        return self.create_environment_v2_with_http_info(request)

    def create_environment_v2_with_http_info(self, request):
        all_params = ['instance_id', 'create_environment_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/envs',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateEnvironmentV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_environment_variable_v2(self, request):
        """新建变量

        将API发布到不同的环境后，对于不同的环境，可能会有不同的环境变量，比如，API的服务部署地址，请求的版本号等。
        
        用户可以定义不同的环境变量，用户在定义API时，在API的定义中使用这些变量，当调用API时，API网关会将这些变量替换成真实的变量值，以达到不同环境的区分效果。
        
        环境变量定义在API分组上，该分组下的所有API都可以使用这些变量。
        &gt; 1.环境变量的变量名称必须保持唯一，即一个分组在同一个环境上不能有两个同名的变量
          2.环境变量区分大小写，即变量ABC与变量abc是两个不同的变量
          3.设置了环境变量后，使用到该变量的API的调试功能将不可使用。
          4.定义了环境变量后，使用到环境变量的地方应该以对称的#标识环境变量，当API发布到相应的环境后，会对环境变量的值进行替换，如：定义的API的URL为：https://#address#:8080，环境变量address在RELEASE环境上的值为：192.168.1.5，则API发布到RELEASE环境后的真实的URL为：https://192.168.1.5:8080。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateEnvironmentVariableV2
        :type request: :class:`huaweicloudsdkapig.v2.CreateEnvironmentVariableV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.CreateEnvironmentVariableV2Response`
        """
        return self.create_environment_variable_v2_with_http_info(request)

    def create_environment_variable_v2_with_http_info(self, request):
        all_params = ['instance_id', 'create_environment_variable_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/env-variables',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateEnvironmentVariableV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_feature_v2(self, request):
        """实例配置特性

        为实例配置需要的特性。
        
        支持配置的特性列表及特性配置示例如下：
        
        | 特性名称 | 特性描述 | 特性配置示例 | 特性配置参数 |  |  |  |
        --------| :------- | :-------| :-------| :-------| :-------| :-------
        |  |  |  | 参数名称 | 参数描述 | 参数默认值 | 参数范围 |
        | lts | 是否支持shubao访问日志上报功能。|{\&quot;name\&quot;:\&quot;lts\&quot;,\&quot;enable\&quot;:true,\&quot;config\&quot;: \&quot;{\\\\\&quot;group_id\\\\\&quot;: \\\&quot;\\,\\\\\&quot;topic_id\\\\\&quot;:\\\\\&quot;\\\\\&quot;,\\\\\&quot;log_group\\\\\&quot;:\\\\\&quot;\\\\\&quot;,\\\\\&quot;log_stream\\\\\&quot;:\\\\\&quot;\\\\\&quot;}\&quot;} | group_id | 日志组ID | | |
        |  |  |  | topic_id | 日志流ID | | |
        |  |  |  | log_group | 日志组名称 | | |
        |  |  |  | log_stream | 日志流名称 | | |
        | ratelimit | 是否支持自定义流控值。|{\&quot;name\&quot;:\&quot;ratelimit\&quot;,\&quot;enable\&quot;:true,\&quot;config\&quot;: \&quot;{\\\\\&quot;api_limits\\\\\&quot;: 500}\&quot;} | api_limits | API全局默认流控值。注意：如果配置过小会导致业务持续被流控，请根据业务谨慎修改。 | 200 次/秒 | 1-1000000 次/秒 |
        | request_body_size | 是否支持指定最大请求Body大小。|{\&quot;name\&quot;:\&quot;request_body_size\&quot;,\&quot;enable\&quot;:true,\&quot;config\&quot;: \&quot;104857600\&quot;} | request_body_size | 请求中允许携带的Body大小上限。 | 12 M | 1-9536 M |
        | backend_timeout | 是否支持配置后端API最大超时时间。|{\&quot;name\&quot;:\&quot;backend_timeout\&quot;,\&quot;enable\&quot;:true,\&quot;config\&quot;: \&quot;{\\\&quot;max_timeout\\\&quot;: 500}\&quot;} | max_timeout | API网关到后端服务的超时时间上限。 | 60000 ms | 1-600000 ms |
        | app_token | 是否开启app_token认证方式。|{\&quot;name\&quot;:\&quot;app_token\&quot;,\&quot;enable\&quot;:true,\&quot;config\&quot;: \&quot;{\\\\\&quot;enable\\\\\&quot;: \\\\\&quot;on\\\\\&quot;, \\\\\&quot;app_token_expire_time\\\\\&quot;: 3600, \\\\\&quot;app_token_uri\\\\\&quot;: \\\\\&quot;/v1/apigw/oauth2/token\\\\\&quot;, \\\\\&quot;refresh_token_expire_time\\\\\&quot;: 7200}\&quot;} | enable | 是否开启 | off | on/off |
        |  |  |  | app_token_expire_time | access token的有效时间 | 3600 s | 1-72000 s |
        |  |  |  | refresh_token_expire_time | refresh token的有效时间 | 7200 s | 1-72000 s |
        |  |  |  | app_token_uri | 获取token的uri | /v1/apigw/oauth2/token |  |
        |  |  |  | app_token_key | token的加密key |  |  |
        | app_api_key | 是否开启app_api_key认证方式。|{\&quot;name\&quot;:\&quot;app_api_key\&quot;,\&quot;enable\&quot;:true,\&quot;config\&quot;: \&quot;on\&quot;} |  |  | off | on/off |
        | app_basic | 是否开启app_basic认证方式。|{\&quot;name\&quot;:\&quot;app_basic\&quot;,\&quot;enable\&quot;:true,\&quot;config\&quot;: \&quot;on\&quot;} |  |  | off | on/off |
        | app_secret | 是否支持app_secret认证方式。|{\&quot;name\&quot;:\&quot;app_secret\&quot;,\&quot;enable\&quot;:true,\&quot;config\&quot;: \&quot;on\&quot;} |  |  | off | on/off |
        | app_jwt | 是否支持app_jwt认证方式。|{\&quot;name\&quot;:\&quot;app_jwt\&quot;,\&quot;enable\&quot;:true,\&quot;config\&quot;: \&quot;{\\\\\&quot;enable\\\\\&quot;: \\\\\&quot;on\\\\\&quot;, \\\\\&quot;auth_header\\\\\&quot;: \\\\\&quot;Authorization\\\\\&quot;}\&quot;}| enable | 是否开启app_jwt认证方式。 | off | on/off |
        |  |  |  | auth_header | app_jwt认证头 | Authorization |  |
        | public_key | 是否支持public_key类型的后端签名。|{\&quot;name\&quot;:\&quot;public_key\&quot;,\&quot;enable\&quot;:true,\&quot;config\&quot;: \&quot;{\\\\\&quot;enable\\\\\&quot;: \\\\\&quot;on\\\\\&quot;, \\\\\&quot;public_key_uri_prefix\\\\\&quot;: \\\\\&quot;/apigw/authadv/v2/public-key/\\\\\&quot;}\&quot;}| enable | 是否开启app_jwt认证方式。 | off | on/off |
        |  |  |  | public_key_uri_prefix | 获取public key的uri前缀 | /apigw/authadv/v2/public-key/ |  |
        | backend_token_allow | 是否支持普通租户透传token到后端。|{\&quot;name\&quot;:\&quot;backend_token_allow\&quot;,\&quot;enable\&quot;:true,\&quot;config\&quot;: \&quot;{\\\\\&quot;backend_token_allow_users\\\\\&quot;: [\\\\\&quot;paas_apig_wwx548366_01\\\\\&quot;]}\&quot;} | backend_token_allow_users | 透传token到后端普通租户白名单，匹配普通租户domain name正则表达式 |  |  |
        | backend_client_certificate | 是否开启后端双向认证。|{\&quot;name\&quot;:\&quot;backend_client_certificate\&quot;,\&quot;enable\&quot;:true,\&quot;config\&quot;: \&quot;{\\\\\&quot;enable\\\\\&quot;: \\\\\&quot;on\\\\\&quot;,\\\\\&quot;ca\\\\\&quot;: \\\\\&quot;\\\\\&quot;,\\\\\&quot;content\\\\\&quot;: \\\\\&quot;\\\\\&quot;,\\\\\&quot;key\\\\\&quot;: \\\\\&quot;\\\\\&quot;}\&quot;} | enable | 是否开启 | off | on/off |
        |  |  |  | ca | 双向认证信任证书 |  |  |
        |  |  |  | content | 双向认证证书 |  |  |
        |  |  |  | key | 双向认证信任私钥 |  |  |
        | ssl_ciphers | 是否支持https加密套件。|{\&quot;name\&quot;:\&quot;ssl_ciphers\&quot;,\&quot;enable\&quot;:true,\&quot;config\&quot;: \&quot;config\&quot;: \&quot;{\\\\\&quot;ssl_ciphers\\\\\&quot;: [\\\\\&quot;ECDHE-ECDSA-AES256-GCM-SHA384\\\\\&quot;]}\&quot;} | ssl_ciphers | 支持的加解密套件。ssl_ciphers数组中只允许出现默认值中的字符串，且数组不能为空。 |  | ECDHE-ECDSA-AES256-GCM-SHA384,ECDHE-RSA-AES256-GCM-SHA384,ECDHE-ECDSA-AES128-GCM-SHA256,ECDHE-RSA-AES128-GCM-SHA256,ECDHE-ECDSA-AES256-SHA384,ECDHE-RSA-AES256-SHA384,ECDHE-ECDSA-AES128-SHA256,ECDHE-RSA-AES128-SHA256 |
        | real_ip_from_xff | 是否开启使用xff头作为访问控制、流控策略的源ip生效依据。|{\&quot;name\&quot;:\&quot;real_ip_from_xff\&quot;,\&quot;enable\&quot;: true,\&quot;config\&quot;: \&quot;{\\\\\&quot;enable\\\\\&quot;: \\\\\&quot;on\\\\\&quot;,\\\\\&quot;xff_index\\\\\&quot;: 1}\&quot;} | enable | 是否开启 | off | on/off |
        |  |  |  | xff_index | 源ip所在xff头的索引位置（支持负数，-1为最后一位，以此类推） | -1 | int32有效值 |
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateFeatureV2
        :type request: :class:`huaweicloudsdkapig.v2.CreateFeatureV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.CreateFeatureV2Response`
        """
        return self.create_feature_v2_with_http_info(request)

    def create_feature_v2_with_http_info(self, request):
        all_params = ['instance_id', 'create_feature_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/features',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateFeatureV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_gateway_response_v2(self, request):
        """创建分组自定义响应

        新增分组下自定义响应
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateGatewayResponseV2
        :type request: :class:`huaweicloudsdkapig.v2.CreateGatewayResponseV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.CreateGatewayResponseV2Response`
        """
        return self.create_gateway_response_v2_with_http_info(request)

    def create_gateway_response_v2_with_http_info(self, request):
        all_params = ['instance_id', 'group_id', 'create_gateway_response_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/api-groups/{group_id}/gateway-responses',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateGatewayResponseV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_instance_v2(self, request):
        """创建专享版实例

        创建专享版实例
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateInstanceV2
        :type request: :class:`huaweicloudsdkapig.v2.CreateInstanceV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.CreateInstanceV2Response`
        """
        return self.create_instance_v2_with_http_info(request)

    def create_instance_v2_with_http_info(self, request):
        all_params = ['create_instance_v2_request_body']
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/apigw/instances',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateInstanceV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_request_throttling_policy_v2(self, request):
        """创建流控策略

        当API上线后，系统会默认给每个API提供一个流控策略，API提供者可以根据自身API的服务能力及负载情况变更这个流控策略。 流控策略即限制API在一定长度的时间内，能够允许被访问的最大次数。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateRequestThrottlingPolicyV2
        :type request: :class:`huaweicloudsdkapig.v2.CreateRequestThrottlingPolicyV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.CreateRequestThrottlingPolicyV2Response`
        """
        return self.create_request_throttling_policy_v2_with_http_info(request)

    def create_request_throttling_policy_v2_with_http_info(self, request):
        all_params = ['instance_id', 'create_request_throttling_policy_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/throttles',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateRequestThrottlingPolicyV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_signature_key_v2(self, request):
        """创建签名密钥

        为了保护API的安全性，建议租户为API的访问提供一套保护机制，即租户开放的API，需要对请求来源进行认证，不符合认证的请求直接拒绝访问。
        
        其中，签名密钥就是API安全保护机制的一种。
        
        租户创建一个签名密钥，并将签名密钥与API进行绑定，则API网关在请求这个API时，就会使用绑定的签名密钥对请求参数进行数据加密，生成签名。当租户的后端服务收到请求时，可以校验这个签名，如果签名校验不通过，则该请求不是API网关发出的请求，租户可以拒绝这个请求，从而保证API的安全性，避免API被未知来源的请求攻击。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateSignatureKeyV2
        :type request: :class:`huaweicloudsdkapig.v2.CreateSignatureKeyV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.CreateSignatureKeyV2Response`
        """
        return self.create_signature_key_v2_with_http_info(request)

    def create_signature_key_v2_with_http_info(self, request):
        all_params = ['instance_id', 'create_signature_key_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/signs',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateSignatureKeyV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_special_throttling_configuration_v2(self, request):
        """创建特殊设置

        流控策略可以限制一段时间内可以访问API的最大次数，也可以限制一段时间内单个租户和单个APP可以访问API的最大次数。
        
        如果想要对某个特定的APP进行特殊设置，例如设置所有APP每分钟的访问次数为500次，但想设置APP1每分钟的访问次数为800次，可以通过在流控策略中设置特殊APP来实现该功能。
        
        为流控策略添加一个特殊设置的对象，可以是APP，也可以是租户。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateSpecialThrottlingConfigurationV2
        :type request: :class:`huaweicloudsdkapig.v2.CreateSpecialThrottlingConfigurationV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.CreateSpecialThrottlingConfigurationV2Response`
        """
        return self.create_special_throttling_configuration_v2_with_http_info(request)

    def create_special_throttling_configuration_v2_with_http_info(self, request):
        all_params = ['instance_id', 'throttle_id', 'create_special_throttling_configuration_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'throttle_id' in local_var_params:
            path_params['throttle_id'] = local_var_params['throttle_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/throttles/{throttle_id}/throttle-specials',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateSpecialThrottlingConfigurationV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_custom_authorizer_v2(self, request):
        """删除自定义认证

        删除自定义认证
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteCustomAuthorizerV2
        :type request: :class:`huaweicloudsdkapig.v2.DeleteCustomAuthorizerV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.DeleteCustomAuthorizerV2Response`
        """
        return self.delete_custom_authorizer_v2_with_http_info(request)

    def delete_custom_authorizer_v2_with_http_info(self, request):
        all_params = ['instance_id', 'authorizer_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'authorizer_id' in local_var_params:
            path_params['authorizer_id'] = local_var_params['authorizer_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/authorizers/{authorizer_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteCustomAuthorizerV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_environment_v2(self, request):
        """删除环境

        删除指定的环境。
        
        该操作将导致此API在指定的环境无法被访问，可能会影响相当一部分应用和用户。请确保已经告知用户，或者确认需要强制下线。
        
        环境上存在已发布的API时，该环境不能被删除。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteEnvironmentV2
        :type request: :class:`huaweicloudsdkapig.v2.DeleteEnvironmentV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.DeleteEnvironmentV2Response`
        """
        return self.delete_environment_v2_with_http_info(request)

    def delete_environment_v2_with_http_info(self, request):
        all_params = ['instance_id', 'env_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'env_id' in local_var_params:
            path_params['env_id'] = local_var_params['env_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/envs/{env_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteEnvironmentV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_environment_variable_v2(self, request):
        """删除变量

        删除指定的环境变量。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteEnvironmentVariableV2
        :type request: :class:`huaweicloudsdkapig.v2.DeleteEnvironmentVariableV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.DeleteEnvironmentVariableV2Response`
        """
        return self.delete_environment_variable_v2_with_http_info(request)

    def delete_environment_variable_v2_with_http_info(self, request):
        all_params = ['instance_id', 'env_variable_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'env_variable_id' in local_var_params:
            path_params['env_variable_id'] = local_var_params['env_variable_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/env-variables/{env_variable_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteEnvironmentVariableV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_gateway_response_type_v2(self, request):
        """删除分组指定错误类型的自定义响应配置

        删除分组指定错误类型的自定义响应配置，还原为使用默认值的配置。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteGatewayResponseTypeV2
        :type request: :class:`huaweicloudsdkapig.v2.DeleteGatewayResponseTypeV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.DeleteGatewayResponseTypeV2Response`
        """
        return self.delete_gateway_response_type_v2_with_http_info(request)

    def delete_gateway_response_type_v2_with_http_info(self, request):
        all_params = ['instance_id', 'group_id', 'response_id', 'response_type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']
        if 'response_id' in local_var_params:
            path_params['response_id'] = local_var_params['response_id']
        if 'response_type' in local_var_params:
            path_params['response_type'] = local_var_params['response_type']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/api-groups/{group_id}/gateway-responses/{response_id}/{response_type}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteGatewayResponseTypeV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_gateway_response_v2(self, request):
        """删除分组自定义响应

        删除分组自定义响应
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteGatewayResponseV2
        :type request: :class:`huaweicloudsdkapig.v2.DeleteGatewayResponseV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.DeleteGatewayResponseV2Response`
        """
        return self.delete_gateway_response_v2_with_http_info(request)

    def delete_gateway_response_v2_with_http_info(self, request):
        all_params = ['instance_id', 'group_id', 'response_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']
        if 'response_id' in local_var_params:
            path_params['response_id'] = local_var_params['response_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/api-groups/{group_id}/gateway-responses/{response_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteGatewayResponseV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_instances_v2(self, request):
        """删除专享版实例

        删除专享版实例
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteInstancesV2
        :type request: :class:`huaweicloudsdkapig.v2.DeleteInstancesV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.DeleteInstancesV2Response`
        """
        return self.delete_instances_v2_with_http_info(request)

    def delete_instances_v2_with_http_info(self, request):
        all_params = ['instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteInstancesV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_request_throttling_policy_v2(self, request):
        """删除流控策略

        删除指定的流控策略,以及该流控策略与API的所有绑定关系。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteRequestThrottlingPolicyV2
        :type request: :class:`huaweicloudsdkapig.v2.DeleteRequestThrottlingPolicyV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.DeleteRequestThrottlingPolicyV2Response`
        """
        return self.delete_request_throttling_policy_v2_with_http_info(request)

    def delete_request_throttling_policy_v2_with_http_info(self, request):
        all_params = ['instance_id', 'throttle_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'throttle_id' in local_var_params:
            path_params['throttle_id'] = local_var_params['throttle_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/throttles/{throttle_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteRequestThrottlingPolicyV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_signature_key_v2(self, request):
        """删除签名密钥

        删除指定的签名密钥,删除签名密钥时，其配置的绑定关系会一并删除，相应的签名密钥会失效。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteSignatureKeyV2
        :type request: :class:`huaweicloudsdkapig.v2.DeleteSignatureKeyV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.DeleteSignatureKeyV2Response`
        """
        return self.delete_signature_key_v2_with_http_info(request)

    def delete_signature_key_v2_with_http_info(self, request):
        all_params = ['instance_id', 'sign_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'sign_id' in local_var_params:
            path_params['sign_id'] = local_var_params['sign_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/signs/{sign_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteSignatureKeyV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_special_throttling_configuration_v2(self, request):
        """删除特殊设置

        删除某个流控策略的某个特殊配置。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteSpecialThrottlingConfigurationV2
        :type request: :class:`huaweicloudsdkapig.v2.DeleteSpecialThrottlingConfigurationV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.DeleteSpecialThrottlingConfigurationV2Response`
        """
        return self.delete_special_throttling_configuration_v2_with_http_info(request)

    def delete_special_throttling_configuration_v2_with_http_info(self, request):
        all_params = ['instance_id', 'throttle_id', 'strategy_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'throttle_id' in local_var_params:
            path_params['throttle_id'] = local_var_params['throttle_id']
        if 'strategy_id' in local_var_params:
            path_params['strategy_id'] = local_var_params['strategy_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/throttles/{throttle_id}/throttle-specials/{strategy_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteSpecialThrottlingConfigurationV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def disassociate_certificate_v2(self, request):
        """删除域名证书

        如果域名证书不再需要或者已过期，则可以删除证书内容。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DisassociateCertificateV2
        :type request: :class:`huaweicloudsdkapig.v2.DisassociateCertificateV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.DisassociateCertificateV2Response`
        """
        return self.disassociate_certificate_v2_with_http_info(request)

    def disassociate_certificate_v2_with_http_info(self, request):
        all_params = ['instance_id', 'group_id', 'domain_id', 'certificate_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']
        if 'certificate_id' in local_var_params:
            path_params['certificate_id'] = local_var_params['certificate_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/api-groups/{group_id}/domains/{domain_id}/certificate/{certificate_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DisassociateCertificateV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def disassociate_domain_v2(self, request):
        """解绑域名

        如果API分组不再需要绑定某个自定义域名，则可以为此API分组解绑此域名。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DisassociateDomainV2
        :type request: :class:`huaweicloudsdkapig.v2.DisassociateDomainV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.DisassociateDomainV2Response`
        """
        return self.disassociate_domain_v2_with_http_info(request)

    def disassociate_domain_v2_with_http_info(self, request):
        all_params = ['instance_id', 'group_id', 'domain_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/api-groups/{group_id}/domains/{domain_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DisassociateDomainV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def disassociate_signature_key_v2(self, request):
        """解除绑定

        解除API与签名密钥的绑定关系。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DisassociateSignatureKeyV2
        :type request: :class:`huaweicloudsdkapig.v2.DisassociateSignatureKeyV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.DisassociateSignatureKeyV2Response`
        """
        return self.disassociate_signature_key_v2_with_http_info(request)

    def disassociate_signature_key_v2_with_http_info(self, request):
        all_params = ['instance_id', 'sign_bindings_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'sign_bindings_id' in local_var_params:
            path_params['sign_bindings_id'] = local_var_params['sign_bindings_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/sign-bindings/{sign_bindings_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DisassociateSignatureKeyV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_api_groups_quantities_v2(self, request):
        """查询API分组概况

        查询租户名下的API分组概况。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListApiGroupsQuantitiesV2
        :type request: :class:`huaweicloudsdkapig.v2.ListApiGroupsQuantitiesV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListApiGroupsQuantitiesV2Response`
        """
        return self.list_api_groups_quantities_v2_with_http_info(request)

    def list_api_groups_quantities_v2_with_http_info(self, request):
        all_params = ['instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/resources/outline/groups',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListApiGroupsQuantitiesV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_api_quantities_v2(self, request):
        """查询API概况

        查询租户名下的API概况：已发布到RELEASE环境的API个数，未发布到RELEASE环境的API个数。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListApiQuantitiesV2
        :type request: :class:`huaweicloudsdkapig.v2.ListApiQuantitiesV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListApiQuantitiesV2Response`
        """
        return self.list_api_quantities_v2_with_http_info(request)

    def list_api_quantities_v2_with_http_info(self, request):
        all_params = ['instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/resources/outline/apis',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListApiQuantitiesV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_apis_binded_to_signature_key_v2(self, request):
        """查看签名密钥绑定的API列表

        查询某个签名密钥上已经绑定的API列表。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListApisBindedToSignatureKeyV2
        :type request: :class:`huaweicloudsdkapig.v2.ListApisBindedToSignatureKeyV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListApisBindedToSignatureKeyV2Response`
        """
        return self.list_apis_binded_to_signature_key_v2_with_http_info(request)

    def list_apis_binded_to_signature_key_v2_with_http_info(self, request):
        all_params = ['instance_id', 'sign_id', 'offset', 'limit', 'env_id', 'api_id', 'api_name', 'group_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'sign_id' in local_var_params:
            query_params.append(('sign_id', local_var_params['sign_id']))
        if 'env_id' in local_var_params:
            query_params.append(('env_id', local_var_params['env_id']))
        if 'api_id' in local_var_params:
            query_params.append(('api_id', local_var_params['api_id']))
        if 'api_name' in local_var_params:
            query_params.append(('api_name', local_var_params['api_name']))
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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/sign-bindings/binded-apis',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListApisBindedToSignatureKeyV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_apis_not_bound_with_signature_key_v2(self, request):
        """查看签名密钥未绑定的API列表

        查询所有未绑定到该签名密钥上的API列表。需要API已经发布，未发布的API不予展示。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListApisNotBoundWithSignatureKeyV2
        :type request: :class:`huaweicloudsdkapig.v2.ListApisNotBoundWithSignatureKeyV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListApisNotBoundWithSignatureKeyV2Response`
        """
        return self.list_apis_not_bound_with_signature_key_v2_with_http_info(request)

    def list_apis_not_bound_with_signature_key_v2_with_http_info(self, request):
        all_params = ['instance_id', 'sign_id', 'offset', 'limit', 'env_id', 'api_id', 'api_name', 'group_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'sign_id' in local_var_params:
            query_params.append(('sign_id', local_var_params['sign_id']))
        if 'env_id' in local_var_params:
            query_params.append(('env_id', local_var_params['env_id']))
        if 'api_id' in local_var_params:
            query_params.append(('api_id', local_var_params['api_id']))
        if 'api_name' in local_var_params:
            query_params.append(('api_name', local_var_params['api_name']))
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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/sign-bindings/unbinded-apis',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListApisNotBoundWithSignatureKeyV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_app_quantities_v2(self, request):
        """查询APP概况

        查询租户名下的APP概况：已进行API访问授权的APP个数，未进行API访问授权的APP个数。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListAppQuantitiesV2
        :type request: :class:`huaweicloudsdkapig.v2.ListAppQuantitiesV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListAppQuantitiesV2Response`
        """
        return self.list_app_quantities_v2_with_http_info(request)

    def list_app_quantities_v2_with_http_info(self, request):
        all_params = ['instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/resources/outline/apps',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListAppQuantitiesV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_available_zones_v2(self, request):
        """查看可用区信息

        查看可用区信息
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListAvailableZonesV2
        :type request: :class:`huaweicloudsdkapig.v2.ListAvailableZonesV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListAvailableZonesV2Response`
        """
        return self.list_available_zones_v2_with_http_info(request)

    def list_available_zones_v2_with_http_info(self, request):
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
            resource_path='/v2/{project_id}/apigw/available-zones',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListAvailableZonesV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_custom_authorizers_v2(self, request):
        """查询自定义认证列表

        查询自定义认证列表
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListCustomAuthorizersV2
        :type request: :class:`huaweicloudsdkapig.v2.ListCustomAuthorizersV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListCustomAuthorizersV2Response`
        """
        return self.list_custom_authorizers_v2_with_http_info(request)

    def list_custom_authorizers_v2_with_http_info(self, request):
        all_params = ['instance_id', 'offset', 'limit', 'id', 'name', 'type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/authorizers',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListCustomAuthorizersV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_environment_variables_v2(self, request):
        """查询变量列表

        查询分组下的所有环境变量的列表。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListEnvironmentVariablesV2
        :type request: :class:`huaweicloudsdkapig.v2.ListEnvironmentVariablesV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListEnvironmentVariablesV2Response`
        """
        return self.list_environment_variables_v2_with_http_info(request)

    def list_environment_variables_v2_with_http_info(self, request):
        all_params = ['instance_id', 'group_id', 'offset', 'limit', 'env_id', 'variable_name', 'precise_search']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))
        if 'env_id' in local_var_params:
            query_params.append(('env_id', local_var_params['env_id']))
        if 'variable_name' in local_var_params:
            query_params.append(('variable_name', local_var_params['variable_name']))
        if 'precise_search' in local_var_params:
            query_params.append(('precise_search', local_var_params['precise_search']))

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/env-variables',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListEnvironmentVariablesV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_environments_v2(self, request):
        """查询环境列表

        查询符合条件的环境列表。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListEnvironmentsV2
        :type request: :class:`huaweicloudsdkapig.v2.ListEnvironmentsV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListEnvironmentsV2Response`
        """
        return self.list_environments_v2_with_http_info(request)

    def list_environments_v2_with_http_info(self, request):
        all_params = ['instance_id', 'offset', 'limit', 'name']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/envs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListEnvironmentsV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_features_v2(self, request):
        """查看实例特性列表

        查看实例特性列表。注意：实例不支持以下特性的需要联系技术支持升级实例版本。
        
        当前支持的特性列表如下：
        
        特性名称 | 特性描述 | 特性是否可配置|
        --------| :------- | :-------|
        lts | 是否支持shubao访问日志上报功能。| 是 |
        gateway_responses | 是否支持网关自定义响应。| 否 |
        ratelimit | 是否支持自定义流控值。| 是 |
        request_body_size | 是否支持指定最大请求Body大小。| 是 |
        backend_timeout | 是否支持配置后端API最大超时时间。| 是 |
        app_token | 是否开启app_token认证方式。| 是 |
        app_api_key | 是否开启app_api_key认证方式。| 是 |
        app_basic | 是否开启app_basic认证方式。| 是 |
        app_secret | 是否支持app_secret认证方式。| 是 |
        app_jwt | 是否支持app_jwt认证方式。| 是 |
        public_key | 是否支持public_key类型的后端签名。| 是 |
        backend_token_allow | 是否支持普通租户透传token到后端。| 是 |
        sign_basic | 签名秘钥是否支持basic类型。| 否 |
        multi_auth | API是否支持双重认证方式。| 否 |
        backend_client_certificate | 是否开启后端双向认证。| 是 |
        ssl_ciphers | 是否支持https加密套件。  | 是 |
        route | 是否支持自定义路由。| 否 |
        cors | 是否支持API使用插件功能。| 否 |
        real_ip_from_xff | 是否开启使用xff头作为访问控制、流控策略的源ip生效依据。  | 是 |
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListFeaturesV2
        :type request: :class:`huaweicloudsdkapig.v2.ListFeaturesV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListFeaturesV2Response`
        """
        return self.list_features_v2_with_http_info(request)

    def list_features_v2_with_http_info(self, request):
        all_params = ['instance_id', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/features',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListFeaturesV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_gateway_responses_v2(self, request):
        """查询分组自定义响应列表

        查询分组自定义响应列表
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListGatewayResponsesV2
        :type request: :class:`huaweicloudsdkapig.v2.ListGatewayResponsesV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListGatewayResponsesV2Response`
        """
        return self.list_gateway_responses_v2_with_http_info(request)

    def list_gateway_responses_v2_with_http_info(self, request):
        all_params = ['instance_id', 'group_id', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/api-groups/{group_id}/gateway-responses',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListGatewayResponsesV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_instance_configs_v2(self, request):
        """查询租户实例配置列表

        查询租户实例配置列表
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListInstanceConfigsV2
        :type request: :class:`huaweicloudsdkapig.v2.ListInstanceConfigsV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListInstanceConfigsV2Response`
        """
        return self.list_instance_configs_v2_with_http_info(request)

    def list_instance_configs_v2_with_http_info(self, request):
        all_params = ['offset', 'limit']
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
            resource_path='/v2/{project_id}/apigw/instance/configs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListInstanceConfigsV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_instances_v2(self, request):
        """查询专享版实例列表

        查询专享版实例列表
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListInstancesV2
        :type request: :class:`huaweicloudsdkapig.v2.ListInstancesV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListInstancesV2Response`
        """
        return self.list_instances_v2_with_http_info(request)

    def list_instances_v2_with_http_info(self, request):
        all_params = ['offset', 'limit', 'instance_id', 'instance_name', 'status']
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
        if 'instance_id' in local_var_params:
            query_params.append(('instance_id', local_var_params['instance_id']))
        if 'instance_name' in local_var_params:
            query_params.append(('instance_name', local_var_params['instance_name']))
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
            resource_path='/v2/{project_id}/apigw/instances',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListInstancesV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_lately_api_statistics_v2(self, request):
        """API统计信息查询-最近一段时间

        根据API的id和最近的一段时间查询API被调用的次数，统计周期为1分钟。查询范围一小时以内，一分钟一个样本，其样本值为一分钟内的累计值。
        &gt; 为了安全起见，在服务器上使用curl命令调用接口查询信息后，需要清理历史操作记录，包括但不限于“~/.bash_history”、“/var/log/messages”（如有）。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListLatelyApiStatisticsV2
        :type request: :class:`huaweicloudsdkapig.v2.ListLatelyApiStatisticsV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListLatelyApiStatisticsV2Response`
        """
        return self.list_lately_api_statistics_v2_with_http_info(request)

    def list_lately_api_statistics_v2_with_http_info(self, request):
        all_params = ['instance_id', 'api_id', 'duration']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'api_id' in local_var_params:
            query_params.append(('api_id', local_var_params['api_id']))
        if 'duration' in local_var_params:
            query_params.append(('duration', local_var_params['duration']))

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/statistics/api/latest',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListLatelyApiStatisticsV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_lately_group_statistics_v2(self, request):
        """分组统计信息查询-最近一小时内

        根据API分组的编号查询该分组下所有API被调用的总次数，统计周期为1分钟。查询范围一小时以内，一分钟一个样本，其样本值为一分钟内的累计值。
        &gt; 为了安全起见，在服务器上使用curl命令调用接口查询信息后，需要清理历史操作记录，包括但不限于“~/.bash_history”、“/var/log/messages”（如有）。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListLatelyGroupStatisticsV2
        :type request: :class:`huaweicloudsdkapig.v2.ListLatelyGroupStatisticsV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListLatelyGroupStatisticsV2Response`
        """
        return self.list_lately_group_statistics_v2_with_http_info(request)

    def list_lately_group_statistics_v2_with_http_info(self, request):
        all_params = ['instance_id', 'group_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/statistics/group/latest',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListLatelyGroupStatisticsV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_project_cofigs_v2(self, request):
        """查询某个实例的租户配置列表

        查询某个实例的租户配置列表，用户可以通过此接口查看各类型资源配置及使用情况。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListProjectCofigsV2
        :type request: :class:`huaweicloudsdkapig.v2.ListProjectCofigsV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListProjectCofigsV2Response`
        """
        return self.list_project_cofigs_v2_with_http_info(request)

    def list_project_cofigs_v2_with_http_info(self, request):
        all_params = ['instance_id', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/project/configs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListProjectCofigsV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_request_throttling_policy_v2(self, request):
        """查询流控策略列表

        查询所有流控策略的信息。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListRequestThrottlingPolicyV2
        :type request: :class:`huaweicloudsdkapig.v2.ListRequestThrottlingPolicyV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListRequestThrottlingPolicyV2Response`
        """
        return self.list_request_throttling_policy_v2_with_http_info(request)

    def list_request_throttling_policy_v2_with_http_info(self, request):
        all_params = ['instance_id', 'offset', 'limit', 'id', 'name', 'precise_search']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'precise_search' in local_var_params:
            query_params.append(('precise_search', local_var_params['precise_search']))

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/throttles',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListRequestThrottlingPolicyV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_signature_keys_binded_to_api_v2(self, request):
        """查看API绑定的签名密钥列表

        查询某个API绑定的签名密钥列表。每个API在每个环境上应该最多只会绑定一个签名密钥。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListSignatureKeysBindedToApiV2
        :type request: :class:`huaweicloudsdkapig.v2.ListSignatureKeysBindedToApiV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListSignatureKeysBindedToApiV2Response`
        """
        return self.list_signature_keys_binded_to_api_v2_with_http_info(request)

    def list_signature_keys_binded_to_api_v2_with_http_info(self, request):
        all_params = ['instance_id', 'api_id', 'offset', 'limit', 'sign_id', 'sign_name', 'env_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'api_id' in local_var_params:
            query_params.append(('api_id', local_var_params['api_id']))
        if 'sign_id' in local_var_params:
            query_params.append(('sign_id', local_var_params['sign_id']))
        if 'sign_name' in local_var_params:
            query_params.append(('sign_name', local_var_params['sign_name']))
        if 'env_id' in local_var_params:
            query_params.append(('env_id', local_var_params['env_id']))

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/sign-bindings/binded-signs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListSignatureKeysBindedToApiV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_signature_keys_v2(self, request):
        """查询签名密钥列表

        查询所有签名密钥的信息。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListSignatureKeysV2
        :type request: :class:`huaweicloudsdkapig.v2.ListSignatureKeysV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListSignatureKeysV2Response`
        """
        return self.list_signature_keys_v2_with_http_info(request)

    def list_signature_keys_v2_with_http_info(self, request):
        all_params = ['instance_id', 'offset', 'limit', 'id', 'name', 'precise_search']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'precise_search' in local_var_params:
            query_params.append(('precise_search', local_var_params['precise_search']))

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/signs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListSignatureKeysV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_special_throttling_configurations_v2(self, request):
        """查看特殊设置列表

        查看给流控策略设置的特殊配置。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListSpecialThrottlingConfigurationsV2
        :type request: :class:`huaweicloudsdkapig.v2.ListSpecialThrottlingConfigurationsV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListSpecialThrottlingConfigurationsV2Response`
        """
        return self.list_special_throttling_configurations_v2_with_http_info(request)

    def list_special_throttling_configurations_v2_with_http_info(self, request):
        all_params = ['instance_id', 'throttle_id', 'offset', 'limit', 'object_type', 'app_name', 'user']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'throttle_id' in local_var_params:
            path_params['throttle_id'] = local_var_params['throttle_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'object_type' in local_var_params:
            query_params.append(('object_type', local_var_params['object_type']))
        if 'app_name' in local_var_params:
            query_params.append(('app_name', local_var_params['app_name']))
        if 'user' in local_var_params:
            query_params.append(('user', local_var_params['user']))

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/throttles/{throttle_id}/throttle-specials',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListSpecialThrottlingConfigurationsV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_tags_v2(self, request):
        """查询标签列表

        查询标签列表
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListTagsV2
        :type request: :class:`huaweicloudsdkapig.v2.ListTagsV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListTagsV2Response`
        """
        return self.list_tags_v2_with_http_info(request)

    def list_tags_v2_with_http_info(self, request):
        all_params = ['instance_id', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListTagsV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def remove_eip_v2(self, request):
        """实例解绑EIP

        实例解绑EIP
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for RemoveEipV2
        :type request: :class:`huaweicloudsdkapig.v2.RemoveEipV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.RemoveEipV2Response`
        """
        return self.remove_eip_v2_with_http_info(request)

    def remove_eip_v2_with_http_info(self, request):
        all_params = ['instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/eip',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='RemoveEipV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def remove_engress_eip_v2(self, request):
        """关闭实例公网出口

        关闭实例公网出口
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for RemoveEngressEipV2
        :type request: :class:`huaweicloudsdkapig.v2.RemoveEngressEipV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.RemoveEngressEipV2Response`
        """
        return self.remove_engress_eip_v2_with_http_info(request)

    def remove_engress_eip_v2_with_http_info(self, request):
        all_params = ['instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/nat-eip',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='RemoveEngressEipV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_details_of_custom_authorizers_v2(self, request):
        """查看自定义认证详情

        查看自定义认证详情
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowDetailsOfCustomAuthorizersV2
        :type request: :class:`huaweicloudsdkapig.v2.ShowDetailsOfCustomAuthorizersV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ShowDetailsOfCustomAuthorizersV2Response`
        """
        return self.show_details_of_custom_authorizers_v2_with_http_info(request)

    def show_details_of_custom_authorizers_v2_with_http_info(self, request):
        all_params = ['instance_id', 'authorizer_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'authorizer_id' in local_var_params:
            path_params['authorizer_id'] = local_var_params['authorizer_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/authorizers/{authorizer_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowDetailsOfCustomAuthorizersV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_details_of_domain_name_certificate_v2(self, request):
        """查看域名证书

        查看域名下绑定的证书详情。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowDetailsOfDomainNameCertificateV2
        :type request: :class:`huaweicloudsdkapig.v2.ShowDetailsOfDomainNameCertificateV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ShowDetailsOfDomainNameCertificateV2Response`
        """
        return self.show_details_of_domain_name_certificate_v2_with_http_info(request)

    def show_details_of_domain_name_certificate_v2_with_http_info(self, request):
        all_params = ['instance_id', 'group_id', 'domain_id', 'certificate_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']
        if 'certificate_id' in local_var_params:
            path_params['certificate_id'] = local_var_params['certificate_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/api-groups/{group_id}/domains/{domain_id}/certificate/{certificate_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowDetailsOfDomainNameCertificateV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_details_of_environment_variable_v2(self, request):
        """查看变量详情

        查看指定的环境变量的详情。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowDetailsOfEnvironmentVariableV2
        :type request: :class:`huaweicloudsdkapig.v2.ShowDetailsOfEnvironmentVariableV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ShowDetailsOfEnvironmentVariableV2Response`
        """
        return self.show_details_of_environment_variable_v2_with_http_info(request)

    def show_details_of_environment_variable_v2_with_http_info(self, request):
        all_params = ['instance_id', 'env_variable_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'env_variable_id' in local_var_params:
            path_params['env_variable_id'] = local_var_params['env_variable_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/env-variables/{env_variable_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowDetailsOfEnvironmentVariableV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_details_of_gateway_response_type_v2(self, request):
        """查看分组下指定错误类型的自定义响应

        查看分组下指定错误类型的自定义响应
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowDetailsOfGatewayResponseTypeV2
        :type request: :class:`huaweicloudsdkapig.v2.ShowDetailsOfGatewayResponseTypeV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ShowDetailsOfGatewayResponseTypeV2Response`
        """
        return self.show_details_of_gateway_response_type_v2_with_http_info(request)

    def show_details_of_gateway_response_type_v2_with_http_info(self, request):
        all_params = ['instance_id', 'group_id', 'response_id', 'response_type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']
        if 'response_id' in local_var_params:
            path_params['response_id'] = local_var_params['response_id']
        if 'response_type' in local_var_params:
            path_params['response_type'] = local_var_params['response_type']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/api-groups/{group_id}/gateway-responses/{response_id}/{response_type}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowDetailsOfGatewayResponseTypeV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_details_of_gateway_response_v2(self, request):
        """查询分组自定义响应详情

        查询分组自定义响应详情
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowDetailsOfGatewayResponseV2
        :type request: :class:`huaweicloudsdkapig.v2.ShowDetailsOfGatewayResponseV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ShowDetailsOfGatewayResponseV2Response`
        """
        return self.show_details_of_gateway_response_v2_with_http_info(request)

    def show_details_of_gateway_response_v2_with_http_info(self, request):
        all_params = ['instance_id', 'group_id', 'response_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']
        if 'response_id' in local_var_params:
            path_params['response_id'] = local_var_params['response_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/api-groups/{group_id}/gateway-responses/{response_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowDetailsOfGatewayResponseV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_details_of_instance_progress_v2(self, request):
        """查看专享版实例创建进度

        查看专享版实例创建进度
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowDetailsOfInstanceProgressV2
        :type request: :class:`huaweicloudsdkapig.v2.ShowDetailsOfInstanceProgressV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ShowDetailsOfInstanceProgressV2Response`
        """
        return self.show_details_of_instance_progress_v2_with_http_info(request)

    def show_details_of_instance_progress_v2_with_http_info(self, request):
        all_params = ['instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/progress',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowDetailsOfInstanceProgressV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_details_of_instance_v2(self, request):
        """查看专享版实例详情

        查看专享版实例详情
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowDetailsOfInstanceV2
        :type request: :class:`huaweicloudsdkapig.v2.ShowDetailsOfInstanceV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ShowDetailsOfInstanceV2Response`
        """
        return self.show_details_of_instance_v2_with_http_info(request)

    def show_details_of_instance_v2_with_http_info(self, request):
        all_params = ['instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowDetailsOfInstanceV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_details_of_request_throttling_policy_v2(self, request):
        """查看流控策略详情

        查看指定流控策略的详细信息。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowDetailsOfRequestThrottlingPolicyV2
        :type request: :class:`huaweicloudsdkapig.v2.ShowDetailsOfRequestThrottlingPolicyV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ShowDetailsOfRequestThrottlingPolicyV2Response`
        """
        return self.show_details_of_request_throttling_policy_v2_with_http_info(request)

    def show_details_of_request_throttling_policy_v2_with_http_info(self, request):
        all_params = ['instance_id', 'throttle_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'throttle_id' in local_var_params:
            path_params['throttle_id'] = local_var_params['throttle_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/throttles/{throttle_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowDetailsOfRequestThrottlingPolicyV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_custom_authorizer_v2(self, request):
        """修改自定义认证

        修改自定义认证
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateCustomAuthorizerV2
        :type request: :class:`huaweicloudsdkapig.v2.UpdateCustomAuthorizerV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.UpdateCustomAuthorizerV2Response`
        """
        return self.update_custom_authorizer_v2_with_http_info(request)

    def update_custom_authorizer_v2_with_http_info(self, request):
        all_params = ['instance_id', 'authorizer_id', 'update_custom_authorizer_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'authorizer_id' in local_var_params:
            path_params['authorizer_id'] = local_var_params['authorizer_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/authorizers/{authorizer_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateCustomAuthorizerV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_domain_v2(self, request):
        """修改域名

        修改绑定的域名所对应的配置信息。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateDomainV2
        :type request: :class:`huaweicloudsdkapig.v2.UpdateDomainV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.UpdateDomainV2Response`
        """
        return self.update_domain_v2_with_http_info(request)

    def update_domain_v2_with_http_info(self, request):
        all_params = ['instance_id', 'group_id', 'domain_id', 'update_domain_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/api-groups/{group_id}/domains/{domain_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateDomainV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_engress_eip_v2(self, request):
        """更新实例出公网带宽

        更新实例出公网带宽
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateEngressEipV2
        :type request: :class:`huaweicloudsdkapig.v2.UpdateEngressEipV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.UpdateEngressEipV2Response`
        """
        return self.update_engress_eip_v2_with_http_info(request)

    def update_engress_eip_v2_with_http_info(self, request):
        all_params = ['instance_id', 'update_engress_eip_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/nat-eip',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateEngressEipV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_environment_v2(self, request):
        """修改环境

        修改指定环境的信息。其中可修改的属性为：name、remark，其它属性不可修改。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateEnvironmentV2
        :type request: :class:`huaweicloudsdkapig.v2.UpdateEnvironmentV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.UpdateEnvironmentV2Response`
        """
        return self.update_environment_v2_with_http_info(request)

    def update_environment_v2_with_http_info(self, request):
        all_params = ['instance_id', 'env_id', 'update_environment_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'env_id' in local_var_params:
            path_params['env_id'] = local_var_params['env_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/envs/{env_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateEnvironmentV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_gateway_response_type_v2(self, request):
        """修改分组下指定错误类型的自定义响应

        修改分组下指定错误类型的自定义响应。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateGatewayResponseTypeV2
        :type request: :class:`huaweicloudsdkapig.v2.UpdateGatewayResponseTypeV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.UpdateGatewayResponseTypeV2Response`
        """
        return self.update_gateway_response_type_v2_with_http_info(request)

    def update_gateway_response_type_v2_with_http_info(self, request):
        all_params = ['instance_id', 'group_id', 'response_id', 'response_type', 'update_gateway_response_type_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']
        if 'response_id' in local_var_params:
            path_params['response_id'] = local_var_params['response_id']
        if 'response_type' in local_var_params:
            path_params['response_type'] = local_var_params['response_type']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/api-groups/{group_id}/gateway-responses/{response_id}/{response_type}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateGatewayResponseTypeV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_gateway_response_v2(self, request):
        """修改分组自定义响应

        修改分组自定义响应
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateGatewayResponseV2
        :type request: :class:`huaweicloudsdkapig.v2.UpdateGatewayResponseV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.UpdateGatewayResponseV2Response`
        """
        return self.update_gateway_response_v2_with_http_info(request)

    def update_gateway_response_v2_with_http_info(self, request):
        all_params = ['instance_id', 'group_id', 'response_id', 'update_gateway_response_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']
        if 'response_id' in local_var_params:
            path_params['response_id'] = local_var_params['response_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/api-groups/{group_id}/gateway-responses/{response_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateGatewayResponseV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_instance_v2(self, request):
        """更新专享版实例

        更新专享版实例
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateInstanceV2
        :type request: :class:`huaweicloudsdkapig.v2.UpdateInstanceV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.UpdateInstanceV2Response`
        """
        return self.update_instance_v2_with_http_info(request)

    def update_instance_v2_with_http_info(self, request):
        all_params = ['instance_id', 'update_instance_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateInstanceV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_request_throttling_policy_v2(self, request):
        """修改流控策略

        修改指定流控策略的详细信息。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateRequestThrottlingPolicyV2
        :type request: :class:`huaweicloudsdkapig.v2.UpdateRequestThrottlingPolicyV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.UpdateRequestThrottlingPolicyV2Response`
        """
        return self.update_request_throttling_policy_v2_with_http_info(request)

    def update_request_throttling_policy_v2_with_http_info(self, request):
        all_params = ['instance_id', 'throttle_id', 'update_request_throttling_policy_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'throttle_id' in local_var_params:
            path_params['throttle_id'] = local_var_params['throttle_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/throttles/{throttle_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateRequestThrottlingPolicyV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_signature_key_v2(self, request):
        """修改签名密钥

        修改指定签名密钥的详细信息。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateSignatureKeyV2
        :type request: :class:`huaweicloudsdkapig.v2.UpdateSignatureKeyV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.UpdateSignatureKeyV2Response`
        """
        return self.update_signature_key_v2_with_http_info(request)

    def update_signature_key_v2_with_http_info(self, request):
        all_params = ['instance_id', 'sign_id', 'update_signature_key_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'sign_id' in local_var_params:
            path_params['sign_id'] = local_var_params['sign_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/signs/{sign_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateSignatureKeyV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_special_throttling_configuration_v2(self, request):
        """修改特殊设置

        修改某个流控策略下的某个特殊设置。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateSpecialThrottlingConfigurationV2
        :type request: :class:`huaweicloudsdkapig.v2.UpdateSpecialThrottlingConfigurationV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.UpdateSpecialThrottlingConfigurationV2Response`
        """
        return self.update_special_throttling_configuration_v2_with_http_info(request)

    def update_special_throttling_configuration_v2_with_http_info(self, request):
        all_params = ['instance_id', 'throttle_id', 'strategy_id', 'update_special_throttling_configuration_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'throttle_id' in local_var_params:
            path_params['throttle_id'] = local_var_params['throttle_id']
        if 'strategy_id' in local_var_params:
            path_params['strategy_id'] = local_var_params['strategy_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/throttles/{throttle_id}/throttle-specials/{strategy_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateSpecialThrottlingConfigurationV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_delete_acl_v2(self, request):
        """批量删除ACL策略

        批量删除指定的多个ACL策略。
        
        删除ACL策略时，如果存在ACL策略与API绑定关系，则无法删除。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for BatchDeleteAclV2
        :type request: :class:`huaweicloudsdkapig.v2.BatchDeleteAclV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.BatchDeleteAclV2Response`
        """
        return self.batch_delete_acl_v2_with_http_info(request)

    def batch_delete_acl_v2_with_http_info(self, request):
        all_params = ['instance_id', 'action', 'batch_delete_acl_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'action' in local_var_params:
            query_params.append(('action', local_var_params['action']))

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/acls',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchDeleteAclV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_acl_strategy_v2(self, request):
        """创建ACL策略

        增加一个ACL策略，策略类型通过字段acl_type来确定（permit或者deny），限制的对象的类型可以为IP或者DOMAIN，这里的DOMAIN对应的acl_value的值为租户名称，而非“www.exampleDomain.com\&quot;之类的网络域名。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateAclStrategyV2
        :type request: :class:`huaweicloudsdkapig.v2.CreateAclStrategyV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.CreateAclStrategyV2Response`
        """
        return self.create_acl_strategy_v2_with_http_info(request)

    def create_acl_strategy_v2_with_http_info(self, request):
        all_params = ['instance_id', 'create_acl_strategy_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/acls',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateAclStrategyV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_acl_v2(self, request):
        """删除ACL策略

        删除指定的ACL策略， 如果存在api与该ACL策略的绑定关系，则无法删除
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteAclV2
        :type request: :class:`huaweicloudsdkapig.v2.DeleteAclV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.DeleteAclV2Response`
        """
        return self.delete_acl_v2_with_http_info(request)

    def delete_acl_v2_with_http_info(self, request):
        all_params = ['instance_id', 'acl_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'acl_id' in local_var_params:
            path_params['acl_id'] = local_var_params['acl_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/acls/{acl_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteAclV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_acl_strategies_v2(self, request):
        """查看ACL策略列表

        查询所有的ACL策略列表。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListAclStrategiesV2
        :type request: :class:`huaweicloudsdkapig.v2.ListAclStrategiesV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListAclStrategiesV2Response`
        """
        return self.list_acl_strategies_v2_with_http_info(request)

    def list_acl_strategies_v2_with_http_info(self, request):
        all_params = ['instance_id', 'offset', 'limit', 'id', 'name', 'acl_type', 'entity_type', 'precise_search']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'acl_type' in local_var_params:
            query_params.append(('acl_type', local_var_params['acl_type']))
        if 'entity_type' in local_var_params:
            query_params.append(('entity_type', local_var_params['entity_type']))
        if 'precise_search' in local_var_params:
            query_params.append(('precise_search', local_var_params['precise_search']))

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/acls',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListAclStrategiesV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_details_of_acl_policy_v2(self, request):
        """查看ACL策略详情

        查询指定ACL策略的详情。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowDetailsOfAclPolicyV2
        :type request: :class:`huaweicloudsdkapig.v2.ShowDetailsOfAclPolicyV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ShowDetailsOfAclPolicyV2Response`
        """
        return self.show_details_of_acl_policy_v2_with_http_info(request)

    def show_details_of_acl_policy_v2_with_http_info(self, request):
        all_params = ['instance_id', 'acl_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'acl_id' in local_var_params:
            path_params['acl_id'] = local_var_params['acl_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/acls/{acl_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowDetailsOfAclPolicyV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_acl_strategy_v2(self, request):
        """修改ACL策略

        修改指定的ACL策略，其中可修改的属性为：acl_name、acl_type、acl_value，其它属性不可修改。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateAclStrategyV2
        :type request: :class:`huaweicloudsdkapig.v2.UpdateAclStrategyV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.UpdateAclStrategyV2Response`
        """
        return self.update_acl_strategy_v2_with_http_info(request)

    def update_acl_strategy_v2_with_http_info(self, request):
        all_params = ['instance_id', 'acl_id', 'update_acl_strategy_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'acl_id' in local_var_params:
            path_params['acl_id'] = local_var_params['acl_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/acls/{acl_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateAclStrategyV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def associate_request_throttling_policy_v2(self, request):
        """绑定流控策略

        将流控策略应用于API，则所有对该API的访问将会受到该流控策略的限制。
        
        当一定时间内的访问次数超过流控策略设置的API最大访问次数限制后，后续的访问将会被拒绝，从而能够较好的保护后端API免受异常流量的冲击，保障服务的稳定运行。
        
        为指定的API绑定流控策略，绑定时，需要指定在哪个环境上生效。同一个API发布到不同的环境可以绑定不同的流控策略；一个API在发布到特定环境后只能绑定一个默认的流控策略。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for AssociateRequestThrottlingPolicyV2
        :type request: :class:`huaweicloudsdkapig.v2.AssociateRequestThrottlingPolicyV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.AssociateRequestThrottlingPolicyV2Response`
        """
        return self.associate_request_throttling_policy_v2_with_http_info(request)

    def associate_request_throttling_policy_v2_with_http_info(self, request):
        all_params = ['instance_id', 'associate_request_throttling_policy_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/throttle-bindings',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='AssociateRequestThrottlingPolicyV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_disassociate_throttling_policy_v2(self, request):
        """批量解绑流控策略

        批量解除API与流控策略的绑定关系
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for BatchDisassociateThrottlingPolicyV2
        :type request: :class:`huaweicloudsdkapig.v2.BatchDisassociateThrottlingPolicyV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.BatchDisassociateThrottlingPolicyV2Response`
        """
        return self.batch_disassociate_throttling_policy_v2_with_http_info(request)

    def batch_disassociate_throttling_policy_v2_with_http_info(self, request):
        all_params = ['instance_id', 'action', 'batch_disassociate_throttling_policy_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'action' in local_var_params:
            query_params.append(('action', local_var_params['action']))

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/throttle-bindings',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchDisassociateThrottlingPolicyV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_publish_or_offline_api_v2(self, request):
        """批量发布或下线API

        将多个API发布到一个指定的环境，或将多个API从指定的环境下线。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for BatchPublishOrOfflineApiV2
        :type request: :class:`huaweicloudsdkapig.v2.BatchPublishOrOfflineApiV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.BatchPublishOrOfflineApiV2Response`
        """
        return self.batch_publish_or_offline_api_v2_with_http_info(request)

    def batch_publish_or_offline_api_v2_with_http_info(self, request):
        all_params = ['instance_id', 'action', 'batch_publish_or_offline_api_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'action' in local_var_params:
            query_params.append(('action', local_var_params['action']))

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/apis/publish',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchPublishOrOfflineApiV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def change_api_version_v2(self, request):
        """切换API版本

        API每次发布时，会基于当前的API定义生成一个版本。版本记录了API发布时的各种定义及状态。
        
        多个版本之间可以进行随意切换。但一个API在一个环境上，只能有一个版本生效。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ChangeApiVersionV2
        :type request: :class:`huaweicloudsdkapig.v2.ChangeApiVersionV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ChangeApiVersionV2Response`
        """
        return self.change_api_version_v2_with_http_info(request)

    def change_api_version_v2_with_http_info(self, request):
        all_params = ['instance_id', 'api_id', 'change_api_version_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'api_id' in local_var_params:
            path_params['api_id'] = local_var_params['api_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/apis/publish/{api_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ChangeApiVersionV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_api_group_v2(self, request):
        """创建API分组

        API分组是API的管理单元，一个API分组等同于一个服务入口，创建API分组时，返回一个子域名作为访问入口。建议一个API分组下的API具有一定的相关性。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateApiGroupV2
        :type request: :class:`huaweicloudsdkapig.v2.CreateApiGroupV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.CreateApiGroupV2Response`
        """
        return self.create_api_group_v2_with_http_info(request)

    def create_api_group_v2_with_http_info(self, request):
        all_params = ['instance_id', 'create_api_group_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/api-groups',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateApiGroupV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_api_v2(self, request):
        """注册API

        添加一个API，API即一个服务接口，具体的服务能力。
        
        API分为两部分，第一部分为面向API使用者的API接口，定义了使用者如何调用这个API。第二部分面向API提供者，由API提供者定义这个API的真实的后端情况，定义了API网关如何去访问真实的后端服务。API的真实后端服务目前支持三种类型：传统的HTTP/HTTPS形式的web后端、函数工作流、MOCK。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateApiV2
        :type request: :class:`huaweicloudsdkapig.v2.CreateApiV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.CreateApiV2Response`
        """
        return self.create_api_v2_with_http_info(request)

    def create_api_v2_with_http_info(self, request):
        all_params = ['instance_id', 'create_api_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/apis',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateApiV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_or_delete_publish_record_for_api_v2(self, request):
        """发布或下线API

        对API进行发布或下线。
        
        发布操作是将一个指定的API发布到一个指定的环境，API只有发布后，才能够被调用，且只能在该环境上才能被调用。未发布的API无法被调用。
        
        下线操作是将API从某个已发布的环境上下线，下线后，API将无法再被调用。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateOrDeletePublishRecordForApiV2
        :type request: :class:`huaweicloudsdkapig.v2.CreateOrDeletePublishRecordForApiV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.CreateOrDeletePublishRecordForApiV2Response`
        """
        return self.create_or_delete_publish_record_for_api_v2_with_http_info(request)

    def create_or_delete_publish_record_for_api_v2_with_http_info(self, request):
        all_params = ['instance_id', 'create_or_delete_publish_record_for_api_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/apis/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateOrDeletePublishRecordForApiV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def debug_api_v2(self, request):
        """调试API

        调试一个API在指定运行环境下的定义，接口调用者需要具有操作该API的权限。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DebugApiV2
        :type request: :class:`huaweicloudsdkapig.v2.DebugApiV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.DebugApiV2Response`
        """
        return self.debug_api_v2_with_http_info(request)

    def debug_api_v2_with_http_info(self, request):
        all_params = ['instance_id', 'api_id', 'debug_api_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'api_id' in local_var_params:
            path_params['api_id'] = local_var_params['api_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/apis/debug/{api_id}',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DebugApiV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_api_by_version_id_v2(self, request):
        """根据版本编号下线API

        对某个生效中的API版本进行下线操作，下线后，API在该版本生效的环境中将不再能够被调用。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteApiByVersionIdV2
        :type request: :class:`huaweicloudsdkapig.v2.DeleteApiByVersionIdV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.DeleteApiByVersionIdV2Response`
        """
        return self.delete_api_by_version_id_v2_with_http_info(request)

    def delete_api_by_version_id_v2_with_http_info(self, request):
        all_params = ['instance_id', 'version_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'version_id' in local_var_params:
            path_params['version_id'] = local_var_params['version_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/apis/versions/{version_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteApiByVersionIdV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_api_group_v2(self, request):
        """删除API分组

        删除指定的API分组。
        删除API分组前，要先下线并删除分组下的所有API。
        删除时，会一并删除直接或间接关联到该分组下的所有资源，包括独立域名、SSL证书信息等等。并会将外部域名与子域名的绑定关系进行解除（取决于域名cname方式）。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteApiGroupV2
        :type request: :class:`huaweicloudsdkapig.v2.DeleteApiGroupV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.DeleteApiGroupV2Response`
        """
        return self.delete_api_group_v2_with_http_info(request)

    def delete_api_group_v2_with_http_info(self, request):
        all_params = ['instance_id', 'group_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/api-groups/{group_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteApiGroupV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_api_v2(self, request):
        """删除API

        删除指定的API。
        
        删除API时，会删除该API所有相关的资源信息或绑定关系，如API的发布记录，绑定的后端服务，对APP的授权信息等。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteApiV2
        :type request: :class:`huaweicloudsdkapig.v2.DeleteApiV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.DeleteApiV2Response`
        """
        return self.delete_api_v2_with_http_info(request)

    def delete_api_v2_with_http_info(self, request):
        all_params = ['instance_id', 'api_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'api_id' in local_var_params:
            path_params['api_id'] = local_var_params['api_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/apis/{api_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteApiV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def disassociate_request_throttling_policy_v2(self, request):
        """解除API与流控策略的绑定关系

        解除API与流控策略的绑定关系。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DisassociateRequestThrottlingPolicyV2
        :type request: :class:`huaweicloudsdkapig.v2.DisassociateRequestThrottlingPolicyV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.DisassociateRequestThrottlingPolicyV2Response`
        """
        return self.disassociate_request_throttling_policy_v2_with_http_info(request)

    def disassociate_request_throttling_policy_v2_with_http_info(self, request):
        all_params = ['instance_id', 'throttle_binding_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'throttle_binding_id' in local_var_params:
            path_params['throttle_binding_id'] = local_var_params['throttle_binding_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/throttle-bindings/{throttle_binding_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DisassociateRequestThrottlingPolicyV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_api_groups_v2(self, request):
        """查询分组列表

        查询API分组列表。
        
        如果是租户操作，则查询该租户下所有的分组；如果是管理员操作，则查询的是所有租户的分组。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListApiGroupsV2
        :type request: :class:`huaweicloudsdkapig.v2.ListApiGroupsV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListApiGroupsV2Response`
        """
        return self.list_api_groups_v2_with_http_info(request)

    def list_api_groups_v2_with_http_info(self, request):
        all_params = ['instance_id', 'offset', 'limit', 'id', 'name', 'precise_search']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'precise_search' in local_var_params:
            query_params.append(('precise_search', local_var_params['precise_search']))

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/api-groups',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListApiGroupsV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_api_runtime_definition_v2(self, request):
        """查询API运行时定义

        查看指定的API在指定的环境上的运行时定义，默认查询RELEASE环境上的运行时定义。
        
        API的定义分为临时定义和运行时定义，分别代表如下含义：
        - 临时定义：API在编辑中的定义，表示用户最后一次编辑后的API的状态
        - 运行时定义：API在发布到某个环境时，对发布时的API的临时定义进行快照，固化出来的API的状态。
        
        访问某个环境上的API，其实访问的就是其运行时的定义
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListApiRuntimeDefinitionV2
        :type request: :class:`huaweicloudsdkapig.v2.ListApiRuntimeDefinitionV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListApiRuntimeDefinitionV2Response`
        """
        return self.list_api_runtime_definition_v2_with_http_info(request)

    def list_api_runtime_definition_v2_with_http_info(self, request):
        all_params = ['instance_id', 'api_id', 'env_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'api_id' in local_var_params:
            path_params['api_id'] = local_var_params['api_id']

        query_params = []
        if 'env_id' in local_var_params:
            query_params.append(('env_id', local_var_params['env_id']))

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/apis/runtime/{api_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListApiRuntimeDefinitionV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_api_version_detail_v2(self, request):
        """查看版本详情

        查询某个指定的版本详情。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListApiVersionDetailV2
        :type request: :class:`huaweicloudsdkapig.v2.ListApiVersionDetailV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListApiVersionDetailV2Response`
        """
        return self.list_api_version_detail_v2_with_http_info(request)

    def list_api_version_detail_v2_with_http_info(self, request):
        all_params = ['instance_id', 'version_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'version_id' in local_var_params:
            path_params['version_id'] = local_var_params['version_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/apis/versions/{version_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListApiVersionDetailV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_api_versions_v2(self, request):
        """查询API历史版本列表

        查询某个API的历史版本。每个API在一个环境上最多存在10个历史版本。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListApiVersionsV2
        :type request: :class:`huaweicloudsdkapig.v2.ListApiVersionsV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListApiVersionsV2Response`
        """
        return self.list_api_versions_v2_with_http_info(request)

    def list_api_versions_v2_with_http_info(self, request):
        all_params = ['instance_id', 'api_id', 'offset', 'limit', 'env_id', 'env_name']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'api_id' in local_var_params:
            path_params['api_id'] = local_var_params['api_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'env_id' in local_var_params:
            query_params.append(('env_id', local_var_params['env_id']))
        if 'env_name' in local_var_params:
            query_params.append(('env_name', local_var_params['env_name']))

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/apis/publish/{api_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListApiVersionsV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_apis_binded_to_request_throttling_policy_v2(self, request):
        """查看流控策略绑定的API列表

        查询某个流控策略上已经绑定的API列表。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListApisBindedToRequestThrottlingPolicyV2
        :type request: :class:`huaweicloudsdkapig.v2.ListApisBindedToRequestThrottlingPolicyV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListApisBindedToRequestThrottlingPolicyV2Response`
        """
        return self.list_apis_binded_to_request_throttling_policy_v2_with_http_info(request)

    def list_apis_binded_to_request_throttling_policy_v2_with_http_info(self, request):
        all_params = ['instance_id', 'throttle_id', 'offset', 'limit', 'env_id', 'group_id', 'api_id', 'api_name']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'throttle_id' in local_var_params:
            query_params.append(('throttle_id', local_var_params['throttle_id']))
        if 'env_id' in local_var_params:
            query_params.append(('env_id', local_var_params['env_id']))
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))
        if 'api_id' in local_var_params:
            query_params.append(('api_id', local_var_params['api_id']))
        if 'api_name' in local_var_params:
            query_params.append(('api_name', local_var_params['api_name']))

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/throttle-bindings/binded-apis',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListApisBindedToRequestThrottlingPolicyV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_apis_unbinded_to_request_throttling_policy_v2(self, request):
        """查看流控策略未绑定的API列表

        查询所有未绑定到该流控策略上的自有API列表。需要API已经发布，未发布的API不予展示。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListApisUnbindedToRequestThrottlingPolicyV2
        :type request: :class:`huaweicloudsdkapig.v2.ListApisUnbindedToRequestThrottlingPolicyV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListApisUnbindedToRequestThrottlingPolicyV2Response`
        """
        return self.list_apis_unbinded_to_request_throttling_policy_v2_with_http_info(request)

    def list_apis_unbinded_to_request_throttling_policy_v2_with_http_info(self, request):
        all_params = ['instance_id', 'throttle_id', 'offset', 'limit', 'env_id', 'group_id', 'api_id', 'api_name']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'throttle_id' in local_var_params:
            query_params.append(('throttle_id', local_var_params['throttle_id']))
        if 'env_id' in local_var_params:
            query_params.append(('env_id', local_var_params['env_id']))
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))
        if 'api_id' in local_var_params:
            query_params.append(('api_id', local_var_params['api_id']))
        if 'api_name' in local_var_params:
            query_params.append(('api_name', local_var_params['api_name']))

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/throttle-bindings/unbinded-apis',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListApisUnbindedToRequestThrottlingPolicyV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_apis_v2(self, request):
        """查询API列表

        查看API列表，返回API详细信息、发布信息等，但不能查看到后端服务信息。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListApisV2
        :type request: :class:`huaweicloudsdkapig.v2.ListApisV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListApisV2Response`
        """
        return self.list_apis_v2_with_http_info(request)

    def list_apis_v2_with_http_info(self, request):
        all_params = ['instance_id', 'offset', 'limit', 'id', 'name', 'group_id', 'req_protocol', 'req_method', 'req_uri', 'auth_type', 'env_id', 'type', 'precise_search']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))
        if 'req_protocol' in local_var_params:
            query_params.append(('req_protocol', local_var_params['req_protocol']))
        if 'req_method' in local_var_params:
            query_params.append(('req_method', local_var_params['req_method']))
        if 'req_uri' in local_var_params:
            query_params.append(('req_uri', local_var_params['req_uri']))
        if 'auth_type' in local_var_params:
            query_params.append(('auth_type', local_var_params['auth_type']))
        if 'env_id' in local_var_params:
            query_params.append(('env_id', local_var_params['env_id']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'precise_search' in local_var_params:
            query_params.append(('precise_search', local_var_params['precise_search']))

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/apis',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListApisV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_request_throttling_policies_binded_to_api_v2(self, request):
        """查看API绑定的流控策略列表

        查询某个API绑定的流控策略列表。每个环境上应该最多只有一个流控策略。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListRequestThrottlingPoliciesBindedToApiV2
        :type request: :class:`huaweicloudsdkapig.v2.ListRequestThrottlingPoliciesBindedToApiV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListRequestThrottlingPoliciesBindedToApiV2Response`
        """
        return self.list_request_throttling_policies_binded_to_api_v2_with_http_info(request)

    def list_request_throttling_policies_binded_to_api_v2_with_http_info(self, request):
        all_params = ['instance_id', 'api_id', 'offset', 'limit', 'throttle_id', 'throttle_name', 'env_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'api_id' in local_var_params:
            query_params.append(('api_id', local_var_params['api_id']))
        if 'throttle_id' in local_var_params:
            query_params.append(('throttle_id', local_var_params['throttle_id']))
        if 'throttle_name' in local_var_params:
            query_params.append(('throttle_name', local_var_params['throttle_name']))
        if 'env_id' in local_var_params:
            query_params.append(('env_id', local_var_params['env_id']))

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/throttle-bindings/binded-throttles',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListRequestThrottlingPoliciesBindedToApiV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_details_of_api_group_v2(self, request):
        """查询分组详情

        查询指定分组的详细信息。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowDetailsOfApiGroupV2
        :type request: :class:`huaweicloudsdkapig.v2.ShowDetailsOfApiGroupV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ShowDetailsOfApiGroupV2Response`
        """
        return self.show_details_of_api_group_v2_with_http_info(request)

    def show_details_of_api_group_v2_with_http_info(self, request):
        all_params = ['instance_id', 'group_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/api-groups/{group_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowDetailsOfApiGroupV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_details_of_api_v2(self, request):
        """查询API详情

        查看指定的API的详细信息。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowDetailsOfApiV2
        :type request: :class:`huaweicloudsdkapig.v2.ShowDetailsOfApiV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ShowDetailsOfApiV2Response`
        """
        return self.show_details_of_api_v2_with_http_info(request)

    def show_details_of_api_v2_with_http_info(self, request):
        all_params = ['instance_id', 'api_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'api_id' in local_var_params:
            path_params['api_id'] = local_var_params['api_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/apis/{api_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowDetailsOfApiV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_api_group_v2(self, request):
        """修改API分组

        修改API分组属性。其中name和remark可修改，其他属性不可修改。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateApiGroupV2
        :type request: :class:`huaweicloudsdkapig.v2.UpdateApiGroupV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.UpdateApiGroupV2Response`
        """
        return self.update_api_group_v2_with_http_info(request)

    def update_api_group_v2_with_http_info(self, request):
        all_params = ['instance_id', 'group_id', 'update_api_group_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/api-groups/{group_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateApiGroupV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_api_v2(self, request):
        """修改API

        修改指定API的信息，包括后端服务信息。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateApiV2
        :type request: :class:`huaweicloudsdkapig.v2.UpdateApiV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.UpdateApiV2Response`
        """
        return self.update_api_v2_with_http_info(request)

    def update_api_v2_with_http_info(self, request):
        all_params = ['instance_id', 'api_id', 'update_api_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'api_id' in local_var_params:
            path_params['api_id'] = local_var_params['api_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/apis/{api_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateApiV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_delete_api_acl_binding_v2(self, request):
        """批量解除API与ACL策略的绑定

        批量解除API与ACL策略的绑定
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for BatchDeleteApiAclBindingV2
        :type request: :class:`huaweicloudsdkapig.v2.BatchDeleteApiAclBindingV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.BatchDeleteApiAclBindingV2Response`
        """
        return self.batch_delete_api_acl_binding_v2_with_http_info(request)

    def batch_delete_api_acl_binding_v2_with_http_info(self, request):
        all_params = ['instance_id', 'action', 'batch_delete_api_acl_binding_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'action' in local_var_params:
            query_params.append(('action', local_var_params['action']))

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/acl-bindings',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchDeleteApiAclBindingV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_api_acl_binding_v2(self, request):
        """将API与ACL策略进行绑定

        将API与ACL策略进行绑定。
        
        同一个API发布到不同的环境可以绑定不同的ACL策略；一个API在发布到特定环境后只能绑定一个同一种类型的ACL策略。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateApiAclBindingV2
        :type request: :class:`huaweicloudsdkapig.v2.CreateApiAclBindingV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.CreateApiAclBindingV2Response`
        """
        return self.create_api_acl_binding_v2_with_http_info(request)

    def create_api_acl_binding_v2_with_http_info(self, request):
        all_params = ['instance_id', 'create_api_acl_binding_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/acl-bindings',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateApiAclBindingV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_api_acl_binding_v2(self, request):
        """解除API与ACL策略的绑定

        解除某条API与ACL策略的绑定关系
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteApiAclBindingV2
        :type request: :class:`huaweicloudsdkapig.v2.DeleteApiAclBindingV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.DeleteApiAclBindingV2Response`
        """
        return self.delete_api_acl_binding_v2_with_http_info(request)

    def delete_api_acl_binding_v2_with_http_info(self, request):
        all_params = ['instance_id', 'acl_bindings_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'acl_bindings_id' in local_var_params:
            path_params['acl_bindings_id'] = local_var_params['acl_bindings_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/acl-bindings/{acl_bindings_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteApiAclBindingV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_acl_policy_binded_to_api_v2(self, request):
        """查看API绑定的ACL策略列表

        查看API绑定的ACL策略列表
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListAclPolicyBindedToApiV2
        :type request: :class:`huaweicloudsdkapig.v2.ListAclPolicyBindedToApiV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListAclPolicyBindedToApiV2Response`
        """
        return self.list_acl_policy_binded_to_api_v2_with_http_info(request)

    def list_acl_policy_binded_to_api_v2_with_http_info(self, request):
        all_params = ['instance_id', 'api_id', 'offset', 'limit', 'env_id', 'env_name', 'acl_id', 'acl_name']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'api_id' in local_var_params:
            query_params.append(('api_id', local_var_params['api_id']))
        if 'env_id' in local_var_params:
            query_params.append(('env_id', local_var_params['env_id']))
        if 'env_name' in local_var_params:
            query_params.append(('env_name', local_var_params['env_name']))
        if 'acl_id' in local_var_params:
            query_params.append(('acl_id', local_var_params['acl_id']))
        if 'acl_name' in local_var_params:
            query_params.append(('acl_name', local_var_params['acl_name']))

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/acl-bindings/binded-acls',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListAclPolicyBindedToApiV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_apis_binded_to_acl_policy_v2(self, request):
        """查看ACL策略绑定的API列表

        查看ACL策略绑定的API列表
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListApisBindedToAclPolicyV2
        :type request: :class:`huaweicloudsdkapig.v2.ListApisBindedToAclPolicyV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListApisBindedToAclPolicyV2Response`
        """
        return self.list_apis_binded_to_acl_policy_v2_with_http_info(request)

    def list_apis_binded_to_acl_policy_v2_with_http_info(self, request):
        all_params = ['instance_id', 'acl_id', 'offset', 'limit', 'api_id', 'api_name', 'env_id', 'group_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'acl_id' in local_var_params:
            query_params.append(('acl_id', local_var_params['acl_id']))
        if 'api_id' in local_var_params:
            query_params.append(('api_id', local_var_params['api_id']))
        if 'api_name' in local_var_params:
            query_params.append(('api_name', local_var_params['api_name']))
        if 'env_id' in local_var_params:
            query_params.append(('env_id', local_var_params['env_id']))
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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/acl-bindings/binded-apis',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListApisBindedToAclPolicyV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_apis_unbinded_to_acl_policy_v2(self, request):
        """查看ACL策略未绑定的API列表

        查看ACL策略未绑定的API列表，需要API已发布
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListApisUnbindedToAclPolicyV2
        :type request: :class:`huaweicloudsdkapig.v2.ListApisUnbindedToAclPolicyV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListApisUnbindedToAclPolicyV2Response`
        """
        return self.list_apis_unbinded_to_acl_policy_v2_with_http_info(request)

    def list_apis_unbinded_to_acl_policy_v2_with_http_info(self, request):
        all_params = ['instance_id', 'acl_id', 'offset', 'limit', 'api_id', 'api_name', 'env_id', 'group_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'acl_id' in local_var_params:
            query_params.append(('acl_id', local_var_params['acl_id']))
        if 'api_id' in local_var_params:
            query_params.append(('api_id', local_var_params['api_id']))
        if 'api_name' in local_var_params:
            query_params.append(('api_name', local_var_params['api_name']))
        if 'env_id' in local_var_params:
            query_params.append(('env_id', local_var_params['env_id']))
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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/acl-bindings/unbinded-apis',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListApisUnbindedToAclPolicyV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def canceling_authorization_v2(self, request):
        """解除授权

        解除API对APP的授权关系。解除授权后，APP将不再能够调用该API。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CancelingAuthorizationV2
        :type request: :class:`huaweicloudsdkapig.v2.CancelingAuthorizationV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.CancelingAuthorizationV2Response`
        """
        return self.canceling_authorization_v2_with_http_info(request)

    def canceling_authorization_v2_with_http_info(self, request):
        all_params = ['instance_id', 'app_auth_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'app_auth_id' in local_var_params:
            path_params['app_auth_id'] = local_var_params['app_auth_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/app-auths/{app_auth_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CancelingAuthorizationV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def check_app_v2(self, request):
        """校验APP

        校验app是否存在，非APP所有者可以调用该接口校验APP是否真实存在。这个接口只展示app的基本信息id 、name、 remark，其他信息不显示。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CheckAppV2
        :type request: :class:`huaweicloudsdkapig.v2.CheckAppV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.CheckAppV2Response`
        """
        return self.check_app_v2_with_http_info(request)

    def check_app_v2_with_http_info(self, request):
        all_params = ['instance_id', 'app_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/apps/validation/{app_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CheckAppV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_an_app_v2(self, request):
        """创建APP

        APP即应用，是一个可以访问API的身份标识。将API授权给APP后，APP即可调用API。
        创建一个APP。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateAnAppV2
        :type request: :class:`huaweicloudsdkapig.v2.CreateAnAppV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.CreateAnAppV2Response`
        """
        return self.create_an_app_v2_with_http_info(request)

    def create_an_app_v2_with_http_info(self, request):
        all_params = ['instance_id', 'create_an_app_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/apps',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateAnAppV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_app_code_auto_v2(self, request):
        """自动生成APP Code

        创建App Code时，可以不指定具体值，由后台自动生成随机字符串填充。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateAppCodeAutoV2
        :type request: :class:`huaweicloudsdkapig.v2.CreateAppCodeAutoV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.CreateAppCodeAutoV2Response`
        """
        return self.create_app_code_auto_v2_with_http_info(request)

    def create_app_code_auto_v2_with_http_info(self, request):
        all_params = ['instance_id', 'app_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/apps/{app_id}/app-codes',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateAppCodeAutoV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_app_code_v2(self, request):
        """创建APP Code

        App Code为APP应用下的子模块，创建App Code之后，可以实现简易的APP认证。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateAppCodeV2
        :type request: :class:`huaweicloudsdkapig.v2.CreateAppCodeV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.CreateAppCodeV2Response`
        """
        return self.create_app_code_v2_with_http_info(request)

    def create_app_code_v2_with_http_info(self, request):
        all_params = ['instance_id', 'app_id', 'create_app_code_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/apps/{app_id}/app-codes',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateAppCodeV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_authorizing_apps_v2(self, request):
        """APP授权

        APP创建成功后，还不能访问API，如果想要访问某个环境上的API，需要将该API在该环境上授权给APP。授权成功后，APP即可访问该环境上的这个API。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateAuthorizingAppsV2
        :type request: :class:`huaweicloudsdkapig.v2.CreateAuthorizingAppsV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.CreateAuthorizingAppsV2Response`
        """
        return self.create_authorizing_apps_v2_with_http_info(request)

    def create_authorizing_apps_v2_with_http_info(self, request):
        all_params = ['instance_id', 'create_authorizing_apps_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/app-auths',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateAuthorizingAppsV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_app_code_v2(self, request):
        """删除APP Code

        删除App Code，App Code删除后，将无法再通过简易认证访问对应的API。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteAppCodeV2
        :type request: :class:`huaweicloudsdkapig.v2.DeleteAppCodeV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.DeleteAppCodeV2Response`
        """
        return self.delete_app_code_v2_with_http_info(request)

    def delete_app_code_v2_with_http_info(self, request):
        all_params = ['instance_id', 'app_id', 'app_code_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']
        if 'app_code_id' in local_var_params:
            path_params['app_code_id'] = local_var_params['app_code_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/apps/{app_id}/app-codes/{app_code_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteAppCodeV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_app_v2(self, request):
        """删除APP

        删除指定的APP。
        APP删除后，将无法再调用任何API；其中，云市场自动创建的APP无法被删除。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteAppV2
        :type request: :class:`huaweicloudsdkapig.v2.DeleteAppV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.DeleteAppV2Response`
        """
        return self.delete_app_v2_with_http_info(request)

    def delete_app_v2_with_http_info(self, request):
        all_params = ['instance_id', 'app_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/apps/{app_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteAppV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_apis_binded_to_app_v2(self, request):
        """查看APP已绑定的API列表

        查询APP已经绑定的API列表。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListApisBindedToAppV2
        :type request: :class:`huaweicloudsdkapig.v2.ListApisBindedToAppV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListApisBindedToAppV2Response`
        """
        return self.list_apis_binded_to_app_v2_with_http_info(request)

    def list_apis_binded_to_app_v2_with_http_info(self, request):
        all_params = ['instance_id', 'app_id', 'offset', 'limit', 'api_id', 'api_name', 'group_id', 'group_name', 'env_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'app_id' in local_var_params:
            query_params.append(('app_id', local_var_params['app_id']))
        if 'api_id' in local_var_params:
            query_params.append(('api_id', local_var_params['api_id']))
        if 'api_name' in local_var_params:
            query_params.append(('api_name', local_var_params['api_name']))
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))
        if 'group_name' in local_var_params:
            query_params.append(('group_name', local_var_params['group_name']))
        if 'env_id' in local_var_params:
            query_params.append(('env_id', local_var_params['env_id']))

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/app-auths/binded-apis',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListApisBindedToAppV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_apis_unbinded_to_app_v2(self, request):
        """查看APP未绑定的API列表

        查询指定环境上某个APP未绑定的API列表，包括自有API和从云市场购买的API。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListApisUnbindedToAppV2
        :type request: :class:`huaweicloudsdkapig.v2.ListApisUnbindedToAppV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListApisUnbindedToAppV2Response`
        """
        return self.list_apis_unbinded_to_app_v2_with_http_info(request)

    def list_apis_unbinded_to_app_v2_with_http_info(self, request):
        all_params = ['instance_id', 'app_id', 'env_id', 'offset', 'limit', 'group_id', 'api_id', 'api_name']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'app_id' in local_var_params:
            query_params.append(('app_id', local_var_params['app_id']))
        if 'env_id' in local_var_params:
            query_params.append(('env_id', local_var_params['env_id']))
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))
        if 'api_id' in local_var_params:
            query_params.append(('api_id', local_var_params['api_id']))
        if 'api_name' in local_var_params:
            query_params.append(('api_name', local_var_params['api_name']))

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/app-auths/unbinded-apis',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListApisUnbindedToAppV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_app_codes_v2(self, request):
        """查询APP Code列表

        查询App Code列表。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListAppCodesV2
        :type request: :class:`huaweicloudsdkapig.v2.ListAppCodesV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListAppCodesV2Response`
        """
        return self.list_app_codes_v2_with_http_info(request)

    def list_app_codes_v2_with_http_info(self, request):
        all_params = ['instance_id', 'app_id', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/apps/{app_id}/app-codes',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListAppCodesV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_apps_binded_to_api_v2(self, request):
        """查看API已绑定的APP列表

        查询API绑定的APP列表。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListAppsBindedToApiV2
        :type request: :class:`huaweicloudsdkapig.v2.ListAppsBindedToApiV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListAppsBindedToApiV2Response`
        """
        return self.list_apps_binded_to_api_v2_with_http_info(request)

    def list_apps_binded_to_api_v2_with_http_info(self, request):
        all_params = ['instance_id', 'offset', 'limit', 'api_id', 'app_name', 'app_id', 'env_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'api_id' in local_var_params:
            query_params.append(('api_id', local_var_params['api_id']))
        if 'app_name' in local_var_params:
            query_params.append(('app_name', local_var_params['app_name']))
        if 'app_id' in local_var_params:
            query_params.append(('app_id', local_var_params['app_id']))
        if 'env_id' in local_var_params:
            query_params.append(('env_id', local_var_params['env_id']))

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/app-auths/binded-apps',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListAppsBindedToApiV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_apps_v2(self, request):
        """查询APP列表

        查询APP列表。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListAppsV2
        :type request: :class:`huaweicloudsdkapig.v2.ListAppsV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListAppsV2Response`
        """
        return self.list_apps_v2_with_http_info(request)

    def list_apps_v2_with_http_info(self, request):
        all_params = ['instance_id', 'offset', 'limit', 'id', 'name', 'status', 'app_key', 'creator', 'precise_search']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'app_key' in local_var_params:
            query_params.append(('app_key', local_var_params['app_key']))
        if 'creator' in local_var_params:
            query_params.append(('creator', local_var_params['creator']))
        if 'precise_search' in local_var_params:
            query_params.append(('precise_search', local_var_params['precise_search']))

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/apps',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListAppsV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def resetting_app_secret_v2(self, request):
        """重置密钥

        重置指定APP的密钥。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ResettingAppSecretV2
        :type request: :class:`huaweicloudsdkapig.v2.ResettingAppSecretV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ResettingAppSecretV2Response`
        """
        return self.resetting_app_secret_v2_with_http_info(request)

    def resetting_app_secret_v2_with_http_info(self, request):
        all_params = ['instance_id', 'app_id', 'resetting_app_secret_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/apps/secret/{app_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ResettingAppSecretV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_details_of_app_code_v2(self, request):
        """查看APP Code详情

        App Code为APP应用下的子模块，创建App Code之后，可以实现简易的APP认证。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowDetailsOfAppCodeV2
        :type request: :class:`huaweicloudsdkapig.v2.ShowDetailsOfAppCodeV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ShowDetailsOfAppCodeV2Response`
        """
        return self.show_details_of_app_code_v2_with_http_info(request)

    def show_details_of_app_code_v2_with_http_info(self, request):
        all_params = ['instance_id', 'app_id', 'app_code_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']
        if 'app_code_id' in local_var_params:
            path_params['app_code_id'] = local_var_params['app_code_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/apps/{app_id}/app-codes/{app_code_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowDetailsOfAppCodeV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_details_of_app_v2(self, request):
        """查看APP详情

        查看指定APP的详细信息。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowDetailsOfAppV2
        :type request: :class:`huaweicloudsdkapig.v2.ShowDetailsOfAppV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ShowDetailsOfAppV2Response`
        """
        return self.show_details_of_app_v2_with_http_info(request)

    def show_details_of_app_v2_with_http_info(self, request):
        all_params = ['instance_id', 'app_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/apps/{app_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowDetailsOfAppV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_app_v2(self, request):
        """修改APP

        修改指定APP的信息。其中可修改的属性为：name、remark，当支持用户自定义key和secret的开关开启时，app_key和app_secret也支持修改，其它属性不可修改。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateAppV2
        :type request: :class:`huaweicloudsdkapig.v2.UpdateAppV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.UpdateAppV2Response`
        """
        return self.update_app_v2_with_http_info(request)

    def update_app_v2_with_http_info(self, request):
        all_params = ['instance_id', 'app_id', 'update_app_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/apps/{app_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateAppV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def export_api_definitions_v2(self, request):
        """导出API

        导出分组下API的定义信息。导出文件内容符合swagger标准规范，API网关自定义扩展字段请参考《API网关开发指南》的“导入导出API：扩展定义”章节。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ExportApiDefinitionsV2
        :type request: :class:`huaweicloudsdkapig.v2.ExportApiDefinitionsV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ExportApiDefinitionsV2Response`
        """
        return self.export_api_definitions_v2_with_http_info(request)

    def export_api_definitions_v2_with_http_info(self, request):
        all_params = ['instance_id', 'export_api_definitions_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/openapi/export',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ExportApiDefinitionsV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def import_api_definitions_v2(self, request):
        """导入API

        导入API。导入文件内容需要符合swagger标准规范，API网关自定义扩展字段请参考《API网关开发指南》的“导入导出API：扩展定义”章节。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ImportApiDefinitionsV2
        :type request: :class:`huaweicloudsdkapig.v2.ImportApiDefinitionsV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ImportApiDefinitionsV2Response`
        """
        return self.import_api_definitions_v2_with_http_info(request)

    def import_api_definitions_v2_with_http_info(self, request):
        all_params = ['instance_id', 'file_name', 'is_create_group', 'group_id', 'extend_mode', 'simple_mode', 'mock_mode', 'api_mode']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}

        form_params = {}
        if 'is_create_group' in local_var_params:
            form_params['is_create_group'] = local_var_params['is_create_group']
        if 'group_id' in local_var_params:
            form_params['group_id'] = local_var_params['group_id']
        if 'extend_mode' in local_var_params:
            form_params['extend_mode'] = local_var_params['extend_mode']
        if 'simple_mode' in local_var_params:
            form_params['simple_mode'] = local_var_params['simple_mode']
        if 'mock_mode' in local_var_params:
            form_params['mock_mode'] = local_var_params['mock_mode']
        if 'api_mode' in local_var_params:
            form_params['api_mode'] = local_var_params['api_mode']
        if 'file_name' in local_var_params:
            form_params['file_name'] = local_var_params['file_name']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/openapi/import',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ImportApiDefinitionsV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def adding_backend_instances_v2(self, request):
        """添加后端实例

        为指定的VPC通道添加弹性云服务器
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for AddingBackendInstancesV2
        :type request: :class:`huaweicloudsdkapig.v2.AddingBackendInstancesV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.AddingBackendInstancesV2Response`
        """
        return self.adding_backend_instances_v2_with_http_info(request)

    def adding_backend_instances_v2_with_http_info(self, request):
        all_params = ['instance_id', 'vpc_channel_id', 'adding_backend_instances_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'vpc_channel_id' in local_var_params:
            path_params['vpc_channel_id'] = local_var_params['vpc_channel_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/vpc-channels/{vpc_channel_id}/members',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='AddingBackendInstancesV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_vpc_channel_v2(self, request):
        """创建VPC通道

        在API网关中创建连接私有VPC资源的通道，并在创建API时将后端节点配置为使用这些VPC通道，以便API网关直接访问私有VPC资源。
        &gt; 每个用户最多创建30个VPC通道。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateVpcChannelV2
        :type request: :class:`huaweicloudsdkapig.v2.CreateVpcChannelV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.CreateVpcChannelV2Response`
        """
        return self.create_vpc_channel_v2_with_http_info(request)

    def create_vpc_channel_v2_with_http_info(self, request):
        all_params = ['instance_id', 'create_vpc_channel_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/vpc-channels',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateVpcChannelV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_backend_instance_v2(self, request):
        """删除后端实例

        删除指定VPC通道中的弹性云服务器
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteBackendInstanceV2
        :type request: :class:`huaweicloudsdkapig.v2.DeleteBackendInstanceV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.DeleteBackendInstanceV2Response`
        """
        return self.delete_backend_instance_v2_with_http_info(request)

    def delete_backend_instance_v2_with_http_info(self, request):
        all_params = ['instance_id', 'vpc_channel_id', 'member_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'vpc_channel_id' in local_var_params:
            path_params['vpc_channel_id'] = local_var_params['vpc_channel_id']
        if 'member_id' in local_var_params:
            path_params['member_id'] = local_var_params['member_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/vpc-channels/{vpc_channel_id}/members/{member_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteBackendInstanceV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_vpc_channel_v2(self, request):
        """删除VPC通道

        删除指定的VPC通道
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteVpcChannelV2
        :type request: :class:`huaweicloudsdkapig.v2.DeleteVpcChannelV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.DeleteVpcChannelV2Response`
        """
        return self.delete_vpc_channel_v2_with_http_info(request)

    def delete_vpc_channel_v2_with_http_info(self, request):
        all_params = ['instance_id', 'vpc_channel_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'vpc_channel_id' in local_var_params:
            path_params['vpc_channel_id'] = local_var_params['vpc_channel_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/vpc-channels/{vpc_channel_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteVpcChannelV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_backend_instances_v2(self, request):
        """查看后端实例列表

        查看指定VPC通道的弹性云服务器列表。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListBackendInstancesV2
        :type request: :class:`huaweicloudsdkapig.v2.ListBackendInstancesV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListBackendInstancesV2Response`
        """
        return self.list_backend_instances_v2_with_http_info(request)

    def list_backend_instances_v2_with_http_info(self, request):
        all_params = ['instance_id', 'vpc_channel_id', 'offset', 'limit', 'name']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'vpc_channel_id' in local_var_params:
            path_params['vpc_channel_id'] = local_var_params['vpc_channel_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/vpc-channels/{vpc_channel_id}/members',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListBackendInstancesV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_vpc_channels_v2(self, request):
        """查询VPC通道列表

        查看VPC通道列表
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListVpcChannelsV2
        :type request: :class:`huaweicloudsdkapig.v2.ListVpcChannelsV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListVpcChannelsV2Response`
        """
        return self.list_vpc_channels_v2_with_http_info(request)

    def list_vpc_channels_v2_with_http_info(self, request):
        all_params = ['instance_id', 'offset', 'limit', 'id', 'name', 'precise_search']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'precise_search' in local_var_params:
            query_params.append(('precise_search', local_var_params['precise_search']))

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/vpc-channels',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListVpcChannelsV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_details_of_vpc_channel_v2(self, request):
        """查看VPC通道详情

        查看指定的VPC通道详情
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowDetailsOfVpcChannelV2
        :type request: :class:`huaweicloudsdkapig.v2.ShowDetailsOfVpcChannelV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ShowDetailsOfVpcChannelV2Response`
        """
        return self.show_details_of_vpc_channel_v2_with_http_info(request)

    def show_details_of_vpc_channel_v2_with_http_info(self, request):
        all_params = ['instance_id', 'vpc_channel_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'vpc_channel_id' in local_var_params:
            path_params['vpc_channel_id'] = local_var_params['vpc_channel_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/vpc-channels/{vpc_channel_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowDetailsOfVpcChannelV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_vpc_channel_v2(self, request):
        """更新VPC通道

        更新指定VPC通道的参数
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateVpcChannelV2
        :type request: :class:`huaweicloudsdkapig.v2.UpdateVpcChannelV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.UpdateVpcChannelV2Response`
        """
        return self.update_vpc_channel_v2_with_http_info(request)

    def update_vpc_channel_v2_with_http_info(self, request):
        all_params = ['instance_id', 'vpc_channel_id', 'update_vpc_channel_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'vpc_channel_id' in local_var_params:
            path_params['vpc_channel_id'] = local_var_params['vpc_channel_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/vpc-channels/{vpc_channel_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateVpcChannelV2Response',
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
        :param header_params: Header parameters to be placed in the request header.
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
            request_type=request_type)
