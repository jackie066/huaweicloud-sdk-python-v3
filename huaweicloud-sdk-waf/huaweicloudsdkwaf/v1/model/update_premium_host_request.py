# coding: utf-8

import pprint
import re

import six





class UpdatePremiumHostRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'host_id': 'str',
        'body': 'UpdatePremiumHostRequestBody'
    }

    attribute_map = {
        'host_id': 'host_id',
        'body': 'body'
    }

    def __init__(self, host_id=None, body=None):
        """UpdatePremiumHostRequest - a model defined in huaweicloud sdk"""
        
        

        self._host_id = None
        self._body = None
        self.discriminator = None

        self.host_id = host_id
        if body is not None:
            self.body = body

    @property
    def host_id(self):
        """Gets the host_id of this UpdatePremiumHostRequest.

        独享模式域名ID

        :return: The host_id of this UpdatePremiumHostRequest.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        """Sets the host_id of this UpdatePremiumHostRequest.

        独享模式域名ID

        :param host_id: The host_id of this UpdatePremiumHostRequest.
        :type: str
        """
        self._host_id = host_id

    @property
    def body(self):
        """Gets the body of this UpdatePremiumHostRequest.


        :return: The body of this UpdatePremiumHostRequest.
        :rtype: UpdatePremiumHostRequestBody
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdatePremiumHostRequest.


        :param body: The body of this UpdatePremiumHostRequest.
        :type: UpdatePremiumHostRequestBody
        """
        self._body = body

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
        if not isinstance(other, UpdatePremiumHostRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
