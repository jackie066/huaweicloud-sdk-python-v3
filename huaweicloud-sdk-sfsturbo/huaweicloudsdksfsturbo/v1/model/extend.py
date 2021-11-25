# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Extend:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'new_size': 'int'
    }

    attribute_map = {
        'new_size': 'new_size'
    }

    def __init__(self, new_size=None):
        """Extend - a model defined in huaweicloud sdk"""
        
        

        self._new_size = None
        self.discriminator = None

        self.new_size = new_size

    @property
    def new_size(self):
        """Gets the new_size of this Extend.

        扩容后文件系统的新容量，以GB为单位。扩容步长大于等于100GB。  普通文件系统容量，取值范围500~32768。  带宽型文件系统，容量范围是10240~327680

        :return: The new_size of this Extend.
        :rtype: int
        """
        return self._new_size

    @new_size.setter
    def new_size(self, new_size):
        """Sets the new_size of this Extend.

        扩容后文件系统的新容量，以GB为单位。扩容步长大于等于100GB。  普通文件系统容量，取值范围500~32768。  带宽型文件系统，容量范围是10240~327680

        :param new_size: The new_size of this Extend.
        :type: int
        """
        self._new_size = new_size

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
        if not isinstance(other, Extend):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
