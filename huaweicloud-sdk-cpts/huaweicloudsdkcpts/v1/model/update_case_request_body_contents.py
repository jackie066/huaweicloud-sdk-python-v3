# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateCaseRequestBodyContents:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'content': 'list[UpdateCaseRequestBodyContent1]',
        'content_id': 'int',
        'data_type': 'int',
        'index': 'int'
    }

    attribute_map = {
        'content': 'content',
        'content_id': 'content_id',
        'data_type': 'data_type',
        'index': 'index'
    }

    def __init__(self, content=None, content_id=None, data_type=None, index=None):
        """UpdateCaseRequestBodyContents - a model defined in huaweicloud sdk"""
        
        

        self._content = None
        self._content_id = None
        self._data_type = None
        self._index = None
        self.discriminator = None

        if content is not None:
            self.content = content
        if content_id is not None:
            self.content_id = content_id
        if data_type is not None:
            self.data_type = data_type
        if index is not None:
            self.index = index

    @property
    def content(self):
        """Gets the content of this UpdateCaseRequestBodyContents.

        content

        :return: The content of this UpdateCaseRequestBodyContents.
        :rtype: list[UpdateCaseRequestBodyContent1]
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this UpdateCaseRequestBodyContents.

        content

        :param content: The content of this UpdateCaseRequestBodyContents.
        :type: list[UpdateCaseRequestBodyContent1]
        """
        self._content = content

    @property
    def content_id(self):
        """Gets the content_id of this UpdateCaseRequestBodyContents.

        content_id

        :return: The content_id of this UpdateCaseRequestBodyContents.
        :rtype: int
        """
        return self._content_id

    @content_id.setter
    def content_id(self, content_id):
        """Sets the content_id of this UpdateCaseRequestBodyContents.

        content_id

        :param content_id: The content_id of this UpdateCaseRequestBodyContents.
        :type: int
        """
        self._content_id = content_id

    @property
    def data_type(self):
        """Gets the data_type of this UpdateCaseRequestBodyContents.

        data_type

        :return: The data_type of this UpdateCaseRequestBodyContents.
        :rtype: int
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this UpdateCaseRequestBodyContents.

        data_type

        :param data_type: The data_type of this UpdateCaseRequestBodyContents.
        :type: int
        """
        self._data_type = data_type

    @property
    def index(self):
        """Gets the index of this UpdateCaseRequestBodyContents.

        index

        :return: The index of this UpdateCaseRequestBodyContents.
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this UpdateCaseRequestBodyContents.

        index

        :param index: The index of this UpdateCaseRequestBodyContents.
        :type: int
        """
        self._index = index

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
        if not isinstance(other, UpdateCaseRequestBodyContents):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
