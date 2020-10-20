# coding: utf-8

import pprint
import re

import six





class IpGroup:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'created_at': 'str',
        'description': 'str',
        'id': 'str',
        'ip_list': 'list[IpInfo]',
        'listeners': 'list[ListenerRef]',
        'name': 'str',
        'project_id': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'created_at': 'created_at',
        'description': 'description',
        'id': 'id',
        'ip_list': 'ip_list',
        'listeners': 'listeners',
        'name': 'name',
        'project_id': 'project_id',
        'updated_at': 'updated_at'
    }

    def __init__(self, created_at=None, description=None, id=None, ip_list=None, listeners=None, name=None, project_id=None, updated_at=None):
        """IpGroup - a model defined in huaweicloud sdk"""
        
        

        self._created_at = None
        self._description = None
        self._id = None
        self._ip_list = None
        self._listeners = None
        self._name = None
        self._project_id = None
        self._updated_at = None
        self.discriminator = None

        self.created_at = created_at
        self.description = description
        self.id = id
        self.ip_list = ip_list
        self.listeners = listeners
        self.name = name
        self.project_id = project_id
        self.updated_at = updated_at

    @property
    def created_at(self):
        """Gets the created_at of this IpGroup.

        IP地址组的创建时间

        :return: The created_at of this IpGroup.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this IpGroup.

        IP地址组的创建时间

        :param created_at: The created_at of this IpGroup.
        :type: str
        """
        self._created_at = created_at

    @property
    def description(self):
        """Gets the description of this IpGroup.

        IP地址组的更新时间。

        :return: The description of this IpGroup.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this IpGroup.

        IP地址组的更新时间。

        :param description: The description of this IpGroup.
        :type: str
        """
        self._description = description

    @property
    def id(self):
        """Gets the id of this IpGroup.

        IP地址组的id。

        :return: The id of this IpGroup.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IpGroup.

        IP地址组的id。

        :param id: The id of this IpGroup.
        :type: str
        """
        self._id = id

    @property
    def ip_list(self):
        """Gets the ip_list of this IpGroup.

        IP地址组中包含的ip或网段列表。[]表示任意ip。

        :return: The ip_list of this IpGroup.
        :rtype: list[IpInfo]
        """
        return self._ip_list

    @ip_list.setter
    def ip_list(self, ip_list):
        """Sets the ip_list of this IpGroup.

        IP地址组中包含的ip或网段列表。[]表示任意ip。

        :param ip_list: The ip_list of this IpGroup.
        :type: list[IpInfo]
        """
        self._ip_list = ip_list

    @property
    def listeners(self):
        """Gets the listeners of this IpGroup.

        与IP地址组关联的监听器的id列表。

        :return: The listeners of this IpGroup.
        :rtype: list[ListenerRef]
        """
        return self._listeners

    @listeners.setter
    def listeners(self, listeners):
        """Sets the listeners of this IpGroup.

        与IP地址组关联的监听器的id列表。

        :param listeners: The listeners of this IpGroup.
        :type: list[ListenerRef]
        """
        self._listeners = listeners

    @property
    def name(self):
        """Gets the name of this IpGroup.

        IP地址组的名称。

        :return: The name of this IpGroup.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IpGroup.

        IP地址组的名称。

        :param name: The name of this IpGroup.
        :type: str
        """
        self._name = name

    @property
    def project_id(self):
        """Gets the project_id of this IpGroup.

        IP地址组的项目id。

        :return: The project_id of this IpGroup.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this IpGroup.

        IP地址组的项目id。

        :param project_id: The project_id of this IpGroup.
        :type: str
        """
        self._project_id = project_id

    @property
    def updated_at(self):
        """Gets the updated_at of this IpGroup.

        IP地址组的更新时间。

        :return: The updated_at of this IpGroup.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this IpGroup.

        IP地址组的更新时间。

        :param updated_at: The updated_at of this IpGroup.
        :type: str
        """
        self._updated_at = updated_at

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
        if not isinstance(other, IpGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
