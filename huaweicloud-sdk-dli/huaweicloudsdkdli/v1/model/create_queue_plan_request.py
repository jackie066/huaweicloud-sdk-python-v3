# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateQueuePlanRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'queue_name': 'str',
        'body': 'SetQueuePlanReq'
    }

    attribute_map = {
        'queue_name': 'queue_name',
        'body': 'body'
    }

    def __init__(self, queue_name=None, body=None):
        """CreateQueuePlanRequest

        The model defined in huaweicloud sdk

        :param queue_name: 需要设置定时扩缩计划的队列名称，名称只能包含数字、英文字母和下划线，但不能是纯数字，且不能以下划线开头。长度限制：1~128个字符。 说明：  队列名称不区分大小写，系统会自动转换为小写。
        :type queue_name: str
        :param body: Body of the CreateQueuePlanRequest
        :type body: :class:`huaweicloudsdkdli.v1.SetQueuePlanReq`
        """
        
        

        self._queue_name = None
        self._body = None
        self.discriminator = None

        self.queue_name = queue_name
        if body is not None:
            self.body = body

    @property
    def queue_name(self):
        """Gets the queue_name of this CreateQueuePlanRequest.

        需要设置定时扩缩计划的队列名称，名称只能包含数字、英文字母和下划线，但不能是纯数字，且不能以下划线开头。长度限制：1~128个字符。 说明：  队列名称不区分大小写，系统会自动转换为小写。

        :return: The queue_name of this CreateQueuePlanRequest.
        :rtype: str
        """
        return self._queue_name

    @queue_name.setter
    def queue_name(self, queue_name):
        """Sets the queue_name of this CreateQueuePlanRequest.

        需要设置定时扩缩计划的队列名称，名称只能包含数字、英文字母和下划线，但不能是纯数字，且不能以下划线开头。长度限制：1~128个字符。 说明：  队列名称不区分大小写，系统会自动转换为小写。

        :param queue_name: The queue_name of this CreateQueuePlanRequest.
        :type queue_name: str
        """
        self._queue_name = queue_name

    @property
    def body(self):
        """Gets the body of this CreateQueuePlanRequest.


        :return: The body of this CreateQueuePlanRequest.
        :rtype: :class:`huaweicloudsdkdli.v1.SetQueuePlanReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this CreateQueuePlanRequest.


        :param body: The body of this CreateQueuePlanRequest.
        :type body: :class:`huaweicloudsdkdli.v1.SetQueuePlanReq`
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
        if not isinstance(other, CreateQueuePlanRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
