# coding: utf-8

import pprint
import re

import six





class RefreshTaskRequestRefreshTask:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'urls': 'list[str]'
    }

    attribute_map = {
        'type': 'type',
        'urls': 'urls'
    }

    def __init__(self, type=None, urls=None):
        """RefreshTaskRequestRefreshTask - a model defined in huaweicloud sdk"""
        
        

        self._type = None
        self._urls = None
        self.discriminator = None

        if type is not None:
            self.type = type
        self.urls = urls

    @property
    def type(self):
        """Gets the type of this RefreshTaskRequestRefreshTask.

        刷新的类型，其值可以为file 或directory，默认为file

        :return: The type of this RefreshTaskRequestRefreshTask.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RefreshTaskRequestRefreshTask.

        刷新的类型，其值可以为file 或directory，默认为file

        :param type: The type of this RefreshTaskRequestRefreshTask.
        :type: str
        """
        self._type = type

    @property
    def urls(self):
        """Gets the urls of this RefreshTaskRequestRefreshTask.

        输入URL必须带有“http://”或“https://”，多个URL用逗号分隔，单个url的长度限制为10240字符，单次最多输入1000个url。

        :return: The urls of this RefreshTaskRequestRefreshTask.
        :rtype: list[str]
        """
        return self._urls

    @urls.setter
    def urls(self, urls):
        """Sets the urls of this RefreshTaskRequestRefreshTask.

        输入URL必须带有“http://”或“https://”，多个URL用逗号分隔，单个url的长度限制为10240字符，单次最多输入1000个url。

        :param urls: The urls of this RefreshTaskRequestRefreshTask.
        :type: list[str]
        """
        self._urls = urls

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RefreshTaskRequestRefreshTask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
