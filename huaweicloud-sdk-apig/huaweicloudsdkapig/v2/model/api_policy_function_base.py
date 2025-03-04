# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApiPolicyFunctionBase:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'function_urn': 'str',
        'invocation_type': 'str',
        'version': 'str',
        'timeout': 'int'
    }

    attribute_map = {
        'function_urn': 'function_urn',
        'invocation_type': 'invocation_type',
        'version': 'version',
        'timeout': 'timeout'
    }

    def __init__(self, function_urn=None, invocation_type=None, version=None, timeout=None):
        """ApiPolicyFunctionBase

        The model defined in huaweicloud sdk

        :param function_urn: 函数URN
        :type function_urn: str
        :param invocation_type: 调用类型 - async： 异步 - sync：同步
        :type invocation_type: str
        :param version: 版本。字符长度不超过64
        :type version: str
        :param timeout: API网关请求后端服务的超时时间。最大超时时间可通过实例特性backend_timeout配置修改，可修改的上限为600000。  单位：毫秒。
        :type timeout: int
        """
        
        

        self._function_urn = None
        self._invocation_type = None
        self._version = None
        self._timeout = None
        self.discriminator = None

        self.function_urn = function_urn
        self.invocation_type = invocation_type
        if version is not None:
            self.version = version
        if timeout is not None:
            self.timeout = timeout

    @property
    def function_urn(self):
        """Gets the function_urn of this ApiPolicyFunctionBase.

        函数URN

        :return: The function_urn of this ApiPolicyFunctionBase.
        :rtype: str
        """
        return self._function_urn

    @function_urn.setter
    def function_urn(self, function_urn):
        """Sets the function_urn of this ApiPolicyFunctionBase.

        函数URN

        :param function_urn: The function_urn of this ApiPolicyFunctionBase.
        :type function_urn: str
        """
        self._function_urn = function_urn

    @property
    def invocation_type(self):
        """Gets the invocation_type of this ApiPolicyFunctionBase.

        调用类型 - async： 异步 - sync：同步

        :return: The invocation_type of this ApiPolicyFunctionBase.
        :rtype: str
        """
        return self._invocation_type

    @invocation_type.setter
    def invocation_type(self, invocation_type):
        """Sets the invocation_type of this ApiPolicyFunctionBase.

        调用类型 - async： 异步 - sync：同步

        :param invocation_type: The invocation_type of this ApiPolicyFunctionBase.
        :type invocation_type: str
        """
        self._invocation_type = invocation_type

    @property
    def version(self):
        """Gets the version of this ApiPolicyFunctionBase.

        版本。字符长度不超过64

        :return: The version of this ApiPolicyFunctionBase.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ApiPolicyFunctionBase.

        版本。字符长度不超过64

        :param version: The version of this ApiPolicyFunctionBase.
        :type version: str
        """
        self._version = version

    @property
    def timeout(self):
        """Gets the timeout of this ApiPolicyFunctionBase.

        API网关请求后端服务的超时时间。最大超时时间可通过实例特性backend_timeout配置修改，可修改的上限为600000。  单位：毫秒。

        :return: The timeout of this ApiPolicyFunctionBase.
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this ApiPolicyFunctionBase.

        API网关请求后端服务的超时时间。最大超时时间可通过实例特性backend_timeout配置修改，可修改的上限为600000。  单位：毫秒。

        :param timeout: The timeout of this ApiPolicyFunctionBase.
        :type timeout: int
        """
        self._timeout = timeout

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ApiPolicyFunctionBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
