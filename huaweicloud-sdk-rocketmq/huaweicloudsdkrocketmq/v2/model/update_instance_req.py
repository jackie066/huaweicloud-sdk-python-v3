# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateInstanceReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'security_group_id': 'str',
        'retention_policy': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'security_group_id': 'security_group_id',
        'retention_policy': 'retention_policy'
    }

    def __init__(self, name=None, description=None, security_group_id=None, retention_policy=None):
        """UpdateInstanceReq

        The model defined in huaweicloud sdk

        :param name: 实例名称。  由英文字符开头，只能由英文字母、数字、中划线组成，长度为4~64的字符。
        :type name: str
        :param description: 实例的描述信息。  长度不超过1024的字符串。  &gt; \\与\&quot;在json报文中属于特殊字符，如果参数值中需要显示\\或者\&quot;字符，请在字符前增加转义字符\\，比如\\\\或者\\\&quot;。
        :type description: str
        :param security_group_id: 安全组ID。
        :type security_group_id: str
        :param retention_policy: ACL访问控制。
        :type retention_policy: bool
        """
        
        

        self._name = None
        self._description = None
        self._security_group_id = None
        self._retention_policy = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if security_group_id is not None:
            self.security_group_id = security_group_id
        if retention_policy is not None:
            self.retention_policy = retention_policy

    @property
    def name(self):
        """Gets the name of this UpdateInstanceReq.

        实例名称。  由英文字符开头，只能由英文字母、数字、中划线组成，长度为4~64的字符。

        :return: The name of this UpdateInstanceReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateInstanceReq.

        实例名称。  由英文字符开头，只能由英文字母、数字、中划线组成，长度为4~64的字符。

        :param name: The name of this UpdateInstanceReq.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this UpdateInstanceReq.

        实例的描述信息。  长度不超过1024的字符串。  > \\与\"在json报文中属于特殊字符，如果参数值中需要显示\\或者\"字符，请在字符前增加转义字符\\，比如\\\\或者\\\"。

        :return: The description of this UpdateInstanceReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateInstanceReq.

        实例的描述信息。  长度不超过1024的字符串。  > \\与\"在json报文中属于特殊字符，如果参数值中需要显示\\或者\"字符，请在字符前增加转义字符\\，比如\\\\或者\\\"。

        :param description: The description of this UpdateInstanceReq.
        :type description: str
        """
        self._description = description

    @property
    def security_group_id(self):
        """Gets the security_group_id of this UpdateInstanceReq.

        安全组ID。

        :return: The security_group_id of this UpdateInstanceReq.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        """Sets the security_group_id of this UpdateInstanceReq.

        安全组ID。

        :param security_group_id: The security_group_id of this UpdateInstanceReq.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

    @property
    def retention_policy(self):
        """Gets the retention_policy of this UpdateInstanceReq.

        ACL访问控制。

        :return: The retention_policy of this UpdateInstanceReq.
        :rtype: bool
        """
        return self._retention_policy

    @retention_policy.setter
    def retention_policy(self, retention_policy):
        """Sets the retention_policy of this UpdateInstanceReq.

        ACL访问控制。

        :param retention_policy: The retention_policy of this UpdateInstanceReq.
        :type retention_policy: bool
        """
        self._retention_policy = retention_policy

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
        if not isinstance(other, UpdateInstanceReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
