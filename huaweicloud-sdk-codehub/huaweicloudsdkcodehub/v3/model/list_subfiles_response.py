# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSubfilesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'trees': 'list[LogsTree]',
        'total': 'int'
    }

    attribute_map = {
        'trees': 'trees',
        'total': 'total'
    }

    def __init__(self, trees=None, total=None):
        """ListSubfilesResponse

        The model defined in huaweicloud sdk

        :param trees: 文件日志树
        :type trees: list[:class:`huaweicloudsdkcodehub.v3.LogsTree`]
        :param total: 记录总数
        :type total: int
        """
        
        super(ListSubfilesResponse, self).__init__()

        self._trees = None
        self._total = None
        self.discriminator = None

        if trees is not None:
            self.trees = trees
        if total is not None:
            self.total = total

    @property
    def trees(self):
        """Gets the trees of this ListSubfilesResponse.

        文件日志树

        :return: The trees of this ListSubfilesResponse.
        :rtype: list[:class:`huaweicloudsdkcodehub.v3.LogsTree`]
        """
        return self._trees

    @trees.setter
    def trees(self, trees):
        """Sets the trees of this ListSubfilesResponse.

        文件日志树

        :param trees: The trees of this ListSubfilesResponse.
        :type trees: list[:class:`huaweicloudsdkcodehub.v3.LogsTree`]
        """
        self._trees = trees

    @property
    def total(self):
        """Gets the total of this ListSubfilesResponse.

        记录总数

        :return: The total of this ListSubfilesResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListSubfilesResponse.

        记录总数

        :param total: The total of this ListSubfilesResponse.
        :type total: int
        """
        self._total = total

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
        if not isinstance(other, ListSubfilesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
