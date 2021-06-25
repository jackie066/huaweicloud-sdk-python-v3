# coding: utf-8

import pprint
import re

import six





class Subtitle:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'type': 'str',
        'language': 'str',
        'md5': 'str',
        'description': 'str'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'language': 'language',
        'md5': 'md5',
        'description': 'description'
    }

    def __init__(self, id=None, type=None, language=None, md5=None, description=None):
        """Subtitle - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._type = None
        self._language = None
        self._md5 = None
        self._description = None
        self.discriminator = None

        self.id = id
        self.type = type
        self.language = language
        if md5 is not None:
            self.md5 = md5
        if description is not None:
            self.description = description

    @property
    def id(self):
        """Gets the id of this Subtitle.

        字幕文件id<br/> 

        :return: The id of this Subtitle.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Subtitle.

        字幕文件id<br/> 

        :param id: The id of this Subtitle.
        :type: int
        """
        self._id = id

    @property
    def type(self):
        """Gets the type of this Subtitle.

        字幕文件类型<br/> 

        :return: The type of this Subtitle.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Subtitle.

        字幕文件类型<br/> 

        :param type: The type of this Subtitle.
        :type: str
        """
        self._type = type

    @property
    def language(self):
        """Gets the language of this Subtitle.

        字幕文件语音种类<br/> 

        :return: The language of this Subtitle.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this Subtitle.

        字幕文件语音种类<br/> 

        :param language: The language of this Subtitle.
        :type: str
        """
        self._language = language

    @property
    def md5(self):
        """Gets the md5 of this Subtitle.

        字幕文件md5值<br/> 

        :return: The md5 of this Subtitle.
        :rtype: str
        """
        return self._md5

    @md5.setter
    def md5(self, md5):
        """Sets the md5 of this Subtitle.

        字幕文件md5值<br/> 

        :param md5: The md5 of this Subtitle.
        :type: str
        """
        self._md5 = md5

    @property
    def description(self):
        """Gets the description of this Subtitle.

        字幕文件描述<br/> 

        :return: The description of this Subtitle.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Subtitle.

        字幕文件描述<br/> 

        :param description: The description of this Subtitle.
        :type: str
        """
        self._description = description

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
        if not isinstance(other, Subtitle):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
