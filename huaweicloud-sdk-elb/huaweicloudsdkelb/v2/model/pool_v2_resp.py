# coding: utf-8

import pprint
import re

import six





class PoolV2Resp:


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
        'project_id': 'str',
        'tenant_id': 'str',
        'name': 'str',
        'description': 'str',
        'admin_state_up': 'bool',
        'loadbalancers': 'list[ResourceList]',
        'listeners': 'list[ResourceList]',
        'members': 'list[ResourceList]',
        'healthmonitor_id': 'str',
        'session_persistence': 'SessionPersistence',
        'protocol': 'str',
        'lb_algorithm': 'str'
    }

    attribute_map = {
        'id': 'id',
        'project_id': 'project_id',
        'tenant_id': 'tenant_id',
        'name': 'name',
        'description': 'description',
        'admin_state_up': 'admin_state_up',
        'loadbalancers': 'loadbalancers',
        'listeners': 'listeners',
        'members': 'members',
        'healthmonitor_id': 'healthmonitor_id',
        'session_persistence': 'session_persistence',
        'protocol': 'protocol',
        'lb_algorithm': 'lb_algorithm'
    }

    def __init__(self, id=None, project_id=None, tenant_id=None, name=None, description=None, admin_state_up=None, loadbalancers=None, listeners=None, members=None, healthmonitor_id=None, session_persistence=None, protocol=None, lb_algorithm=None):
        """PoolV2Resp - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._project_id = None
        self._tenant_id = None
        self._name = None
        self._description = None
        self._admin_state_up = None
        self._loadbalancers = None
        self._listeners = None
        self._members = None
        self._healthmonitor_id = None
        self._session_persistence = None
        self._protocol = None
        self._lb_algorithm = None
        self.discriminator = None

        self.id = id
        self.project_id = project_id
        self.tenant_id = tenant_id
        self.name = name
        self.description = description
        self.admin_state_up = admin_state_up
        self.loadbalancers = loadbalancers
        self.listeners = listeners
        self.members = members
        self.healthmonitor_id = healthmonitor_id
        self.session_persistence = session_persistence
        self.protocol = protocol
        self.lb_algorithm = lb_algorithm

    @property
    def id(self):
        """Gets the id of this PoolV2Resp.

        后端云服务器组的ID

        :return: The id of this PoolV2Resp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PoolV2Resp.

        后端云服务器组的ID

        :param id: The id of this PoolV2Resp.
        :type: str
        """
        self._id = id

    @property
    def project_id(self):
        """Gets the project_id of this PoolV2Resp.

        后端云服务器组所在的项目ID。

        :return: The project_id of this PoolV2Resp.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this PoolV2Resp.

        后端云服务器组所在的项目ID。

        :param project_id: The project_id of this PoolV2Resp.
        :type: str
        """
        self._project_id = project_id

    @property
    def tenant_id(self):
        """Gets the tenant_id of this PoolV2Resp.

        后端云服务器组所在的项目ID。

        :return: The tenant_id of this PoolV2Resp.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this PoolV2Resp.

        后端云服务器组所在的项目ID。

        :param tenant_id: The tenant_id of this PoolV2Resp.
        :type: str
        """
        self._tenant_id = tenant_id

    @property
    def name(self):
        """Gets the name of this PoolV2Resp.

        后端云服务器组的名称。

        :return: The name of this PoolV2Resp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PoolV2Resp.

        后端云服务器组的名称。

        :param name: The name of this PoolV2Resp.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this PoolV2Resp.

        后端云服务器组的描述信息

        :return: The description of this PoolV2Resp.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PoolV2Resp.

        后端云服务器组的描述信息

        :param description: The description of this PoolV2Resp.
        :type: str
        """
        self._description = description

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this PoolV2Resp.

        后端云服务器组的管理状态。只支持设定为true，该字段的值无实际意义。

        :return: The admin_state_up of this PoolV2Resp.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this PoolV2Resp.

        后端云服务器组的管理状态。只支持设定为true，该字段的值无实际意义。

        :param admin_state_up: The admin_state_up of this PoolV2Resp.
        :type: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def loadbalancers(self):
        """Gets the loadbalancers of this PoolV2Resp.

        后端云服务器组绑定的负载均衡器ID的列表。

        :return: The loadbalancers of this PoolV2Resp.
        :rtype: list[ResourceList]
        """
        return self._loadbalancers

    @loadbalancers.setter
    def loadbalancers(self, loadbalancers):
        """Sets the loadbalancers of this PoolV2Resp.

        后端云服务器组绑定的负载均衡器ID的列表。

        :param loadbalancers: The loadbalancers of this PoolV2Resp.
        :type: list[ResourceList]
        """
        self._loadbalancers = loadbalancers

    @property
    def listeners(self):
        """Gets the listeners of this PoolV2Resp.

        后端云服务器组关联的监听器ID的列表。

        :return: The listeners of this PoolV2Resp.
        :rtype: list[ResourceList]
        """
        return self._listeners

    @listeners.setter
    def listeners(self, listeners):
        """Sets the listeners of this PoolV2Resp.

        后端云服务器组关联的监听器ID的列表。

        :param listeners: The listeners of this PoolV2Resp.
        :type: list[ResourceList]
        """
        self._listeners = listeners

    @property
    def members(self):
        """Gets the members of this PoolV2Resp.

        后端云服务器组关联的后端云服务器ID的列表。

        :return: The members of this PoolV2Resp.
        :rtype: list[ResourceList]
        """
        return self._members

    @members.setter
    def members(self, members):
        """Sets the members of this PoolV2Resp.

        后端云服务器组关联的后端云服务器ID的列表。

        :param members: The members of this PoolV2Resp.
        :type: list[ResourceList]
        """
        self._members = members

    @property
    def healthmonitor_id(self):
        """Gets the healthmonitor_id of this PoolV2Resp.

        后端云服务器组关联的健康检查的ID。

        :return: The healthmonitor_id of this PoolV2Resp.
        :rtype: str
        """
        return self._healthmonitor_id

    @healthmonitor_id.setter
    def healthmonitor_id(self, healthmonitor_id):
        """Sets the healthmonitor_id of this PoolV2Resp.

        后端云服务器组关联的健康检查的ID。

        :param healthmonitor_id: The healthmonitor_id of this PoolV2Resp.
        :type: str
        """
        self._healthmonitor_id = healthmonitor_id

    @property
    def session_persistence(self):
        """Gets the session_persistence of this PoolV2Resp.


        :return: The session_persistence of this PoolV2Resp.
        :rtype: SessionPersistence
        """
        return self._session_persistence

    @session_persistence.setter
    def session_persistence(self, session_persistence):
        """Sets the session_persistence of this PoolV2Resp.


        :param session_persistence: The session_persistence of this PoolV2Resp.
        :type: SessionPersistence
        """
        self._session_persistence = session_persistence

    @property
    def protocol(self):
        """Gets the protocol of this PoolV2Resp.

        后端云服务器组的后端协议。

        :return: The protocol of this PoolV2Resp.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this PoolV2Resp.

        后端云服务器组的后端协议。

        :param protocol: The protocol of this PoolV2Resp.
        :type: str
        """
        self._protocol = protocol

    @property
    def lb_algorithm(self):
        """Gets the lb_algorithm of this PoolV2Resp.

        后端云服务器组的负载均衡算法，取值：ROUND_ROBIN：加权轮询算法；LEAST_CONNECTIONS：加权最少连接算法；SOURCE_IP：源IP算法。当该字段的取值为SOURCE_IP时，后端云服务器组绑定的后端云服务器的weight字段无效。

        :return: The lb_algorithm of this PoolV2Resp.
        :rtype: str
        """
        return self._lb_algorithm

    @lb_algorithm.setter
    def lb_algorithm(self, lb_algorithm):
        """Sets the lb_algorithm of this PoolV2Resp.

        后端云服务器组的负载均衡算法，取值：ROUND_ROBIN：加权轮询算法；LEAST_CONNECTIONS：加权最少连接算法；SOURCE_IP：源IP算法。当该字段的取值为SOURCE_IP时，后端云服务器组绑定的后端云服务器的weight字段无效。

        :param lb_algorithm: The lb_algorithm of this PoolV2Resp.
        :type: str
        """
        self._lb_algorithm = lb_algorithm

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
        if not isinstance(other, PoolV2Resp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
