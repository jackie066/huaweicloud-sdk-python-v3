# coding: utf-8

import pprint
import re

import six





class ListStatisticsRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        '_from': 'int',
        'to': 'int',
        'hosts': 'str',
        'instances': 'str'
    }

    attribute_map = {
        '_from': 'from',
        'to': 'to',
        'hosts': 'hosts',
        'instances': 'instances'
    }

    def __init__(self, _from=None, to=None, hosts=None, instances=None):
        """ListStatisticsRequest - a model defined in huaweicloud sdk"""
        
        

        self.__from = None
        self._to = None
        self._hosts = None
        self._instances = None
        self.discriminator = None

        self._from = _from
        self.to = to
        if hosts is not None:
            self.hosts = hosts
        if instances is not None:
            self.instances = instances

    @property
    def _from(self):
        """Gets the _from of this ListStatisticsRequest.

        起始时间

        :return: The _from of this ListStatisticsRequest.
        :rtype: int
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this ListStatisticsRequest.

        起始时间

        :param _from: The _from of this ListStatisticsRequest.
        :type: int
        """
        self.__from = _from

    @property
    def to(self):
        """Gets the to of this ListStatisticsRequest.

        结束时间

        :return: The to of this ListStatisticsRequest.
        :rtype: int
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this ListStatisticsRequest.

        结束时间

        :param to: The to of this ListStatisticsRequest.
        :type: int
        """
        self._to = to

    @property
    def hosts(self):
        """Gets the hosts of this ListStatisticsRequest.

        要查询域名列表

        :return: The hosts of this ListStatisticsRequest.
        :rtype: str
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        """Sets the hosts of this ListStatisticsRequest.

        要查询域名列表

        :param hosts: The hosts of this ListStatisticsRequest.
        :type: str
        """
        self._hosts = hosts

    @property
    def instances(self):
        """Gets the instances of this ListStatisticsRequest.

        要查询实例列表

        :return: The instances of this ListStatisticsRequest.
        :rtype: str
        """
        return self._instances

    @instances.setter
    def instances(self, instances):
        """Sets the instances of this ListStatisticsRequest.

        要查询实例列表

        :param instances: The instances of this ListStatisticsRequest.
        :type: str
        """
        self._instances = instances

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
        if not isinstance(other, ListStatisticsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
