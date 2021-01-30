# coding: utf-8

import pprint
import re

import six





class ProduceAuditlogLinksRequestBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'ids': 'list[str]'
    }

    attribute_map = {
        'ids': 'ids'
    }

    def __init__(self, ids=None):
        """ProduceAuditlogLinksRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._ids = None
        self.discriminator = None

        self.ids = ids

    @property
    def ids(self):
        """Gets the ids of this ProduceAuditlogLinksRequestBody.

        审计日志ID列表，限制50条以内。

        :return: The ids of this ProduceAuditlogLinksRequestBody.
        :rtype: list[str]
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        """Sets the ids of this ProduceAuditlogLinksRequestBody.

        审计日志ID列表，限制50条以内。

        :param ids: The ids of this ProduceAuditlogLinksRequestBody.
        :type: list[str]
        """
        self._ids = ids

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
        if not isinstance(other, ProduceAuditlogLinksRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
