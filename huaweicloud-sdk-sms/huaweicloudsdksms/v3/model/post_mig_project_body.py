# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PostMigProjectBody:

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
        'description': 'str',
        'isdefault': 'bool',
        'region': 'str',
        'start_target_server': 'bool',
        'speed_limit': 'int',
        'use_public_ip': 'bool',
        'exist_server': 'bool',
        'type': 'str',
        'enterprise_project': 'str',
        'syncing': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'isdefault': 'isdefault',
        'region': 'region',
        'start_target_server': 'start_target_server',
        'speed_limit': 'speed_limit',
        'use_public_ip': 'use_public_ip',
        'exist_server': 'exist_server',
        'type': 'type',
        'enterprise_project': 'enterprise_project',
        'syncing': 'syncing'
    }

    def __init__(self, name=None, description=None, isdefault=None, region=None, start_target_server=None, speed_limit=None, use_public_ip=None, exist_server=None, type=None, enterprise_project=None, syncing=None):
        """PostMigProjectBody

        The model defined in huaweicloud sdk

        :param name: 迁移项目名称
        :type name: str
        :param description: 迁移项目描述
        :type description: str
        :param isdefault: 是否为默认模板
        :type isdefault: bool
        :param region: 区域名称
        :type region: str
        :param start_target_server: 迁移后是否启动目的端虚拟机
        :type start_target_server: bool
        :param speed_limit: 限制迁移速率，单位：Mbps
        :type speed_limit: int
        :param use_public_ip: 是否使用公网IP迁移
        :type use_public_ip: bool
        :param exist_server: 是否是已经存在的服务器
        :type exist_server: bool
        :param type: 迁移项目类型
        :type type: str
        :param enterprise_project: 企业项目名称
        :type enterprise_project: str
        :param syncing: 首次复制或者同步后 是否继续持续同步
        :type syncing: bool
        """
        
        

        self._name = None
        self._description = None
        self._isdefault = None
        self._region = None
        self._start_target_server = None
        self._speed_limit = None
        self._use_public_ip = None
        self._exist_server = None
        self._type = None
        self._enterprise_project = None
        self._syncing = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        if isdefault is not None:
            self.isdefault = isdefault
        self.region = region
        if start_target_server is not None:
            self.start_target_server = start_target_server
        if speed_limit is not None:
            self.speed_limit = speed_limit
        self.use_public_ip = use_public_ip
        self.exist_server = exist_server
        self.type = type
        if enterprise_project is not None:
            self.enterprise_project = enterprise_project
        self.syncing = syncing

    @property
    def name(self):
        """Gets the name of this PostMigProjectBody.

        迁移项目名称

        :return: The name of this PostMigProjectBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PostMigProjectBody.

        迁移项目名称

        :param name: The name of this PostMigProjectBody.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this PostMigProjectBody.

        迁移项目描述

        :return: The description of this PostMigProjectBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PostMigProjectBody.

        迁移项目描述

        :param description: The description of this PostMigProjectBody.
        :type description: str
        """
        self._description = description

    @property
    def isdefault(self):
        """Gets the isdefault of this PostMigProjectBody.

        是否为默认模板

        :return: The isdefault of this PostMigProjectBody.
        :rtype: bool
        """
        return self._isdefault

    @isdefault.setter
    def isdefault(self, isdefault):
        """Sets the isdefault of this PostMigProjectBody.

        是否为默认模板

        :param isdefault: The isdefault of this PostMigProjectBody.
        :type isdefault: bool
        """
        self._isdefault = isdefault

    @property
    def region(self):
        """Gets the region of this PostMigProjectBody.

        区域名称

        :return: The region of this PostMigProjectBody.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this PostMigProjectBody.

        区域名称

        :param region: The region of this PostMigProjectBody.
        :type region: str
        """
        self._region = region

    @property
    def start_target_server(self):
        """Gets the start_target_server of this PostMigProjectBody.

        迁移后是否启动目的端虚拟机

        :return: The start_target_server of this PostMigProjectBody.
        :rtype: bool
        """
        return self._start_target_server

    @start_target_server.setter
    def start_target_server(self, start_target_server):
        """Sets the start_target_server of this PostMigProjectBody.

        迁移后是否启动目的端虚拟机

        :param start_target_server: The start_target_server of this PostMigProjectBody.
        :type start_target_server: bool
        """
        self._start_target_server = start_target_server

    @property
    def speed_limit(self):
        """Gets the speed_limit of this PostMigProjectBody.

        限制迁移速率，单位：Mbps

        :return: The speed_limit of this PostMigProjectBody.
        :rtype: int
        """
        return self._speed_limit

    @speed_limit.setter
    def speed_limit(self, speed_limit):
        """Sets the speed_limit of this PostMigProjectBody.

        限制迁移速率，单位：Mbps

        :param speed_limit: The speed_limit of this PostMigProjectBody.
        :type speed_limit: int
        """
        self._speed_limit = speed_limit

    @property
    def use_public_ip(self):
        """Gets the use_public_ip of this PostMigProjectBody.

        是否使用公网IP迁移

        :return: The use_public_ip of this PostMigProjectBody.
        :rtype: bool
        """
        return self._use_public_ip

    @use_public_ip.setter
    def use_public_ip(self, use_public_ip):
        """Sets the use_public_ip of this PostMigProjectBody.

        是否使用公网IP迁移

        :param use_public_ip: The use_public_ip of this PostMigProjectBody.
        :type use_public_ip: bool
        """
        self._use_public_ip = use_public_ip

    @property
    def exist_server(self):
        """Gets the exist_server of this PostMigProjectBody.

        是否是已经存在的服务器

        :return: The exist_server of this PostMigProjectBody.
        :rtype: bool
        """
        return self._exist_server

    @exist_server.setter
    def exist_server(self, exist_server):
        """Sets the exist_server of this PostMigProjectBody.

        是否是已经存在的服务器

        :param exist_server: The exist_server of this PostMigProjectBody.
        :type exist_server: bool
        """
        self._exist_server = exist_server

    @property
    def type(self):
        """Gets the type of this PostMigProjectBody.

        迁移项目类型

        :return: The type of this PostMigProjectBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PostMigProjectBody.

        迁移项目类型

        :param type: The type of this PostMigProjectBody.
        :type type: str
        """
        self._type = type

    @property
    def enterprise_project(self):
        """Gets the enterprise_project of this PostMigProjectBody.

        企业项目名称

        :return: The enterprise_project of this PostMigProjectBody.
        :rtype: str
        """
        return self._enterprise_project

    @enterprise_project.setter
    def enterprise_project(self, enterprise_project):
        """Sets the enterprise_project of this PostMigProjectBody.

        企业项目名称

        :param enterprise_project: The enterprise_project of this PostMigProjectBody.
        :type enterprise_project: str
        """
        self._enterprise_project = enterprise_project

    @property
    def syncing(self):
        """Gets the syncing of this PostMigProjectBody.

        首次复制或者同步后 是否继续持续同步

        :return: The syncing of this PostMigProjectBody.
        :rtype: bool
        """
        return self._syncing

    @syncing.setter
    def syncing(self, syncing):
        """Sets the syncing of this PostMigProjectBody.

        首次复制或者同步后 是否继续持续同步

        :param syncing: The syncing of this PostMigProjectBody.
        :type syncing: bool
        """
        self._syncing = syncing

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
        if not isinstance(other, PostMigProjectBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
