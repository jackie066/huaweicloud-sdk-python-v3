# coding: utf-8

import pprint
import re

import six





class TransTemplateGroup:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'status': 'str',
        'type': 'str',
        'auto_encrypt': 'int',
        'quality_info_list': 'list[QualityInfo]',
        'common': 'Common',
        'watermark_template_ids': 'list[str]',
        'description': 'str'
    }

    attribute_map = {
        'name': 'name',
        'status': 'status',
        'type': 'type',
        'auto_encrypt': 'auto_encrypt',
        'quality_info_list': 'quality_info_list',
        'common': 'common',
        'watermark_template_ids': 'watermark_template_ids',
        'description': 'description'
    }

    def __init__(self, name=None, status=None, type=None, auto_encrypt=None, quality_info_list=None, common=None, watermark_template_ids=None, description=None):
        """TransTemplateGroup - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._status = None
        self._type = None
        self._auto_encrypt = None
        self._quality_info_list = None
        self._common = None
        self._watermark_template_ids = None
        self._description = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if type is not None:
            self.type = type
        if auto_encrypt is not None:
            self.auto_encrypt = auto_encrypt
        if quality_info_list is not None:
            self.quality_info_list = quality_info_list
        if common is not None:
            self.common = common
        if watermark_template_ids is not None:
            self.watermark_template_ids = watermark_template_ids
        if description is not None:
            self.description = description

    @property
    def name(self):
        """Gets the name of this TransTemplateGroup.

        模板组名称<br/> 

        :return: The name of this TransTemplateGroup.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TransTemplateGroup.

        模板组名称<br/> 

        :param name: The name of this TransTemplateGroup.
        :type: str
        """
        self._name = name

    @property
    def status(self):
        """Gets the status of this TransTemplateGroup.

        是否设置默认<br/> 

        :return: The status of this TransTemplateGroup.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TransTemplateGroup.

        是否设置默认<br/> 

        :param status: The status of this TransTemplateGroup.
        :type: str
        """
        self._status = status

    @property
    def type(self):
        """Gets the type of this TransTemplateGroup.

        模板组类型<br/> 

        :return: The type of this TransTemplateGroup.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TransTemplateGroup.

        模板组类型<br/> 

        :param type: The type of this TransTemplateGroup.
        :type: str
        """
        self._type = type

    @property
    def auto_encrypt(self):
        """Gets the auto_encrypt of this TransTemplateGroup.

        是否自动加密

        :return: The auto_encrypt of this TransTemplateGroup.
        :rtype: int
        """
        return self._auto_encrypt

    @auto_encrypt.setter
    def auto_encrypt(self, auto_encrypt):
        """Sets the auto_encrypt of this TransTemplateGroup.

        是否自动加密

        :param auto_encrypt: The auto_encrypt of this TransTemplateGroup.
        :type: int
        """
        self._auto_encrypt = auto_encrypt

    @property
    def quality_info_list(self):
        """Gets the quality_info_list of this TransTemplateGroup.

        画质配置信息列表<br/> 

        :return: The quality_info_list of this TransTemplateGroup.
        :rtype: list[QualityInfo]
        """
        return self._quality_info_list

    @quality_info_list.setter
    def quality_info_list(self, quality_info_list):
        """Sets the quality_info_list of this TransTemplateGroup.

        画质配置信息列表<br/> 

        :param quality_info_list: The quality_info_list of this TransTemplateGroup.
        :type: list[QualityInfo]
        """
        self._quality_info_list = quality_info_list

    @property
    def common(self):
        """Gets the common of this TransTemplateGroup.


        :return: The common of this TransTemplateGroup.
        :rtype: Common
        """
        return self._common

    @common.setter
    def common(self, common):
        """Sets the common of this TransTemplateGroup.


        :param common: The common of this TransTemplateGroup.
        :type: Common
        """
        self._common = common

    @property
    def watermark_template_ids(self):
        """Gets the watermark_template_ids of this TransTemplateGroup.

        绑定的水印模板组ID数组<br/> 

        :return: The watermark_template_ids of this TransTemplateGroup.
        :rtype: list[str]
        """
        return self._watermark_template_ids

    @watermark_template_ids.setter
    def watermark_template_ids(self, watermark_template_ids):
        """Sets the watermark_template_ids of this TransTemplateGroup.

        绑定的水印模板组ID数组<br/> 

        :param watermark_template_ids: The watermark_template_ids of this TransTemplateGroup.
        :type: list[str]
        """
        self._watermark_template_ids = watermark_template_ids

    @property
    def description(self):
        """Gets the description of this TransTemplateGroup.

        模板介绍<br/> 

        :return: The description of this TransTemplateGroup.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TransTemplateGroup.

        模板介绍<br/> 

        :param description: The description of this TransTemplateGroup.
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
        if not isinstance(other, TransTemplateGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
