# coding: utf-8

import pprint
import re

import six





class QueryCategoryRsp:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'children': 'list[QueryCategoryRsp]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'children': 'children'
    }

    def __init__(self, id=None, name=None, children=None):
        """QueryCategoryRsp - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._name = None
        self._children = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if children is not None:
            self.children = children

    @property
    def id(self):
        """Gets the id of this QueryCategoryRsp.

        视频分类ID<br/> 

        :return: The id of this QueryCategoryRsp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this QueryCategoryRsp.

        视频分类ID<br/> 

        :param id: The id of this QueryCategoryRsp.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this QueryCategoryRsp.

        视频分类名称<br/> 

        :return: The name of this QueryCategoryRsp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this QueryCategoryRsp.

        视频分类名称<br/> 

        :param name: The name of this QueryCategoryRsp.
        :type: str
        """
        self._name = name

    @property
    def children(self):
        """Gets the children of this QueryCategoryRsp.

        子分类信息<br/> 

        :return: The children of this QueryCategoryRsp.
        :rtype: list[QueryCategoryRsp]
        """
        return self._children

    @children.setter
    def children(self, children):
        """Sets the children of this QueryCategoryRsp.

        子分类信息<br/> 

        :param children: The children of this QueryCategoryRsp.
        :type: list[QueryCategoryRsp]
        """
        self._children = children

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
        if not isinstance(other, QueryCategoryRsp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
