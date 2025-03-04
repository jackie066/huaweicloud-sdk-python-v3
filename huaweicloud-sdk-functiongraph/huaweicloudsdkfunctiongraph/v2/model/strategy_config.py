# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StrategyConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'concurrency': 'int',
        'concurrent_num': 'int'
    }

    attribute_map = {
        'concurrency': 'concurrency',
        'concurrent_num': 'concurrent_num'
    }

    def __init__(self, concurrency=None, concurrent_num=None):
        """StrategyConfig

        The model defined in huaweicloud sdk

        :param concurrency: 0：函数被禁用;-1：函数被启用。
        :type concurrency: int
        :param concurrent_num: 函数并发数
        :type concurrent_num: int
        """
        
        

        self._concurrency = None
        self._concurrent_num = None
        self.discriminator = None

        self.concurrency = concurrency
        if concurrent_num is not None:
            self.concurrent_num = concurrent_num

    @property
    def concurrency(self):
        """Gets the concurrency of this StrategyConfig.

        0：函数被禁用;-1：函数被启用。

        :return: The concurrency of this StrategyConfig.
        :rtype: int
        """
        return self._concurrency

    @concurrency.setter
    def concurrency(self, concurrency):
        """Sets the concurrency of this StrategyConfig.

        0：函数被禁用;-1：函数被启用。

        :param concurrency: The concurrency of this StrategyConfig.
        :type concurrency: int
        """
        self._concurrency = concurrency

    @property
    def concurrent_num(self):
        """Gets the concurrent_num of this StrategyConfig.

        函数并发数

        :return: The concurrent_num of this StrategyConfig.
        :rtype: int
        """
        return self._concurrent_num

    @concurrent_num.setter
    def concurrent_num(self, concurrent_num):
        """Sets the concurrent_num of this StrategyConfig.

        函数并发数

        :param concurrent_num: The concurrent_num of this StrategyConfig.
        :type concurrent_num: int
        """
        self._concurrent_num = concurrent_num

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
        if not isinstance(other, StrategyConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
