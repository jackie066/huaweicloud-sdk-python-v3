# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePrivacyRuleRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'url': 'str',
        'category': 'str',
        'index': 'str',
        'description': 'str'
    }

    attribute_map = {
        'url': 'url',
        'category': 'category',
        'index': 'index',
        'description': 'description'
    }

    def __init__(self, url=None, category=None, index=None, description=None):
        """CreatePrivacyRuleRequestBody

        The model defined in huaweicloud sdk

        :param url: 隐私屏蔽规则防护的url，需要填写标准的url格式，例如/admin/xxx或者/admin/*,以\&quot;*\&quot;号结尾代表路径前缀
        :type url: str
        :param category: 屏蔽字段
        :type category: str
        :param index: 屏蔽字段名
        :type index: str
        :param description: 规则描述
        :type description: str
        """
        
        

        self._url = None
        self._category = None
        self._index = None
        self._description = None
        self.discriminator = None

        self.url = url
        self.category = category
        self.index = index
        if description is not None:
            self.description = description

    @property
    def url(self):
        """Gets the url of this CreatePrivacyRuleRequestBody.

        隐私屏蔽规则防护的url，需要填写标准的url格式，例如/admin/xxx或者/admin/*,以\"*\"号结尾代表路径前缀

        :return: The url of this CreatePrivacyRuleRequestBody.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this CreatePrivacyRuleRequestBody.

        隐私屏蔽规则防护的url，需要填写标准的url格式，例如/admin/xxx或者/admin/*,以\"*\"号结尾代表路径前缀

        :param url: The url of this CreatePrivacyRuleRequestBody.
        :type url: str
        """
        self._url = url

    @property
    def category(self):
        """Gets the category of this CreatePrivacyRuleRequestBody.

        屏蔽字段

        :return: The category of this CreatePrivacyRuleRequestBody.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this CreatePrivacyRuleRequestBody.

        屏蔽字段

        :param category: The category of this CreatePrivacyRuleRequestBody.
        :type category: str
        """
        self._category = category

    @property
    def index(self):
        """Gets the index of this CreatePrivacyRuleRequestBody.

        屏蔽字段名

        :return: The index of this CreatePrivacyRuleRequestBody.
        :rtype: str
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this CreatePrivacyRuleRequestBody.

        屏蔽字段名

        :param index: The index of this CreatePrivacyRuleRequestBody.
        :type index: str
        """
        self._index = index

    @property
    def description(self):
        """Gets the description of this CreatePrivacyRuleRequestBody.

        规则描述

        :return: The description of this CreatePrivacyRuleRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreatePrivacyRuleRequestBody.

        规则描述

        :param description: The description of this CreatePrivacyRuleRequestBody.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, CreatePrivacyRuleRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
