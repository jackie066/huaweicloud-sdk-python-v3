# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowQueueDetailRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'queue_type': 'str',
        'queue_name': 'str'
    }

    attribute_map = {
        'queue_type': 'queue_type',
        'queue_name': 'queue_name'
    }

    def __init__(self, queue_type=None, queue_name=None):
        """ShowQueueDetailRequest

        The model defined in huaweicloud sdk

        :param queue_type: 队列的类型,。有如下三种类型： sql general all 如果不指定，默认为sql。
        :type queue_type: str
        :param queue_name: 指定查询的队列名称。
        :type queue_name: str
        """
        
        

        self._queue_type = None
        self._queue_name = None
        self.discriminator = None

        if queue_type is not None:
            self.queue_type = queue_type
        self.queue_name = queue_name

    @property
    def queue_type(self):
        """Gets the queue_type of this ShowQueueDetailRequest.

        队列的类型,。有如下三种类型： sql general all 如果不指定，默认为sql。

        :return: The queue_type of this ShowQueueDetailRequest.
        :rtype: str
        """
        return self._queue_type

    @queue_type.setter
    def queue_type(self, queue_type):
        """Sets the queue_type of this ShowQueueDetailRequest.

        队列的类型,。有如下三种类型： sql general all 如果不指定，默认为sql。

        :param queue_type: The queue_type of this ShowQueueDetailRequest.
        :type queue_type: str
        """
        self._queue_type = queue_type

    @property
    def queue_name(self):
        """Gets the queue_name of this ShowQueueDetailRequest.

        指定查询的队列名称。

        :return: The queue_name of this ShowQueueDetailRequest.
        :rtype: str
        """
        return self._queue_name

    @queue_name.setter
    def queue_name(self, queue_name):
        """Sets the queue_name of this ShowQueueDetailRequest.

        指定查询的队列名称。

        :param queue_name: The queue_name of this ShowQueueDetailRequest.
        :type queue_name: str
        """
        self._queue_name = queue_name

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
        if not isinstance(other, ShowQueueDetailRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
