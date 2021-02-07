# coding: utf-8

import pprint
import re

import six





class MrsKafkaForwarding:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'addresses': 'list[NetAddress]',
        'topic': 'str'
    }

    attribute_map = {
        'addresses': 'addresses',
        'topic': 'topic'
    }

    def __init__(self, addresses=None, topic=None):
        """MrsKafkaForwarding - a model defined in huaweicloud sdk"""
        
        

        self._addresses = None
        self._topic = None
        self.discriminator = None

        self.addresses = addresses
        self.topic = topic

    @property
    def addresses(self):
        """Gets the addresses of this MrsKafkaForwarding.

        转发kafka消息对应的地址列表

        :return: The addresses of this MrsKafkaForwarding.
        :rtype: list[NetAddress]
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """Sets the addresses of this MrsKafkaForwarding.

        转发kafka消息对应的地址列表

        :param addresses: The addresses of this MrsKafkaForwarding.
        :type: list[NetAddress]
        """
        self._addresses = addresses

    @property
    def topic(self):
        """Gets the topic of this MrsKafkaForwarding.

        转发kafka消息关联的topic信息。

        :return: The topic of this MrsKafkaForwarding.
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        """Sets the topic of this MrsKafkaForwarding.

        转发kafka消息关联的topic信息。

        :param topic: The topic of this MrsKafkaForwarding.
        :type: str
        """
        self._topic = topic

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
        if not isinstance(other, MrsKafkaForwarding):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
