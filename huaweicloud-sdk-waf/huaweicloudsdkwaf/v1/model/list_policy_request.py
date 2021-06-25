# coding: utf-8

import pprint
import re

import six





class ListPolicyRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'page': 'int',
        'pagesize': 'int',
        'name': 'str'
    }

    attribute_map = {
        'page': 'page',
        'pagesize': 'pagesize',
        'name': 'name'
    }

    def __init__(self, page=None, pagesize=None, name=None):
        """ListPolicyRequest - a model defined in huaweicloud sdk"""
        
        

        self._page = None
        self._pagesize = None
        self._name = None
        self.discriminator = None

        if page is not None:
            self.page = page
        if pagesize is not None:
            self.pagesize = pagesize
        if name is not None:
            self.name = name

    @property
    def page(self):
        """Gets the page of this ListPolicyRequest.

        page

        :return: The page of this ListPolicyRequest.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this ListPolicyRequest.

        page

        :param page: The page of this ListPolicyRequest.
        :type: int
        """
        self._page = page

    @property
    def pagesize(self):
        """Gets the pagesize of this ListPolicyRequest.

        pagesize

        :return: The pagesize of this ListPolicyRequest.
        :rtype: int
        """
        return self._pagesize

    @pagesize.setter
    def pagesize(self, pagesize):
        """Sets the pagesize of this ListPolicyRequest.

        pagesize

        :param pagesize: The pagesize of this ListPolicyRequest.
        :type: int
        """
        self._pagesize = pagesize

    @property
    def name(self):
        """Gets the name of this ListPolicyRequest.

        name

        :return: The name of this ListPolicyRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListPolicyRequest.

        name

        :param name: The name of this ListPolicyRequest.
        :type: str
        """
        self._name = name

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
        if not isinstance(other, ListPolicyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
