# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateEndpointServiceRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'approval_enabled': 'bool',
        'service_name': 'str',
        'ports': 'list[PortList]',
        'port_id': 'str',
        'vip_port_id': 'str'
    }

    attribute_map = {
        'approval_enabled': 'approval_enabled',
        'service_name': 'service_name',
        'ports': 'ports',
        'port_id': 'port_id',
        'vip_port_id': 'vip_port_id'
    }

    def __init__(self, approval_enabled=None, service_name=None, ports=None, port_id=None, vip_port_id=None):
        """UpdateEndpointServiceRequestBody

        The model defined in huaweicloud sdk

        :param approval_enabled: 是否需要审批。 ● false：不需审批，创建的终端节点连接直接为accepted状态。 ● true：需审批，创建的终端节点连接需要终端节点服务所属用户审核后方可使用。 默认为true，需要审批。
        :type approval_enabled: bool
        :param service_name: 终端节点服务的名称，长度不大于16，允许传入大小写字母、数字、下划线、中划线。
        :type service_name: str
        :param ports: 服务开放的端口映射列表，详细内容请参见表4-22。 同一个终端节点服务下，不允许重复的端口映射。若多个终端节点服务共用一个port_id，则终端节点之间服务的所有端口映射的server_port和protocol的组合不能重复，单次最多添加200个。
        :type ports: list[:class:`huaweicloudsdkvpcep.v1.PortList`]
        :param port_id: 标识终端节点服务后端资源的ID，格式为通用唯一识别码 （Universally UniqueIdentifier，下文简称UUID）。取值为： ● LB类型：增强型负载均衡器内网IP对应的端口ID。详细内容请参考《弹性负载均衡API参考》中的“查询负载均 衡详情”，详见响应消息中的“vip_port_id”字段。 ● VM类型：弹性云服务器IP地址对应的网卡ID。详细内容请参考《弹性云服务器API参考》中的“查询云服务器网 卡信息”，详见响应消息中的“port_id”字段。 ● VIP类型：虚拟资源所在物理服务器对应的网卡ID。 说明 当后端资源为“LB类型”时，仅支持修改为同类型后端资源的“vip_port_id”。 例如，共享型负载均衡仅支持更换为共享型负载均衡，不支持更换为独享型负载均衡。
        :type port_id: str
        :param vip_port_id: 虚拟IP的网卡ID。
        :type vip_port_id: str
        """
        
        

        self._approval_enabled = None
        self._service_name = None
        self._ports = None
        self._port_id = None
        self._vip_port_id = None
        self.discriminator = None

        if approval_enabled is not None:
            self.approval_enabled = approval_enabled
        if service_name is not None:
            self.service_name = service_name
        if ports is not None:
            self.ports = ports
        if port_id is not None:
            self.port_id = port_id
        if vip_port_id is not None:
            self.vip_port_id = vip_port_id

    @property
    def approval_enabled(self):
        """Gets the approval_enabled of this UpdateEndpointServiceRequestBody.

        是否需要审批。 ● false：不需审批，创建的终端节点连接直接为accepted状态。 ● true：需审批，创建的终端节点连接需要终端节点服务所属用户审核后方可使用。 默认为true，需要审批。

        :return: The approval_enabled of this UpdateEndpointServiceRequestBody.
        :rtype: bool
        """
        return self._approval_enabled

    @approval_enabled.setter
    def approval_enabled(self, approval_enabled):
        """Sets the approval_enabled of this UpdateEndpointServiceRequestBody.

        是否需要审批。 ● false：不需审批，创建的终端节点连接直接为accepted状态。 ● true：需审批，创建的终端节点连接需要终端节点服务所属用户审核后方可使用。 默认为true，需要审批。

        :param approval_enabled: The approval_enabled of this UpdateEndpointServiceRequestBody.
        :type approval_enabled: bool
        """
        self._approval_enabled = approval_enabled

    @property
    def service_name(self):
        """Gets the service_name of this UpdateEndpointServiceRequestBody.

        终端节点服务的名称，长度不大于16，允许传入大小写字母、数字、下划线、中划线。

        :return: The service_name of this UpdateEndpointServiceRequestBody.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        """Sets the service_name of this UpdateEndpointServiceRequestBody.

        终端节点服务的名称，长度不大于16，允许传入大小写字母、数字、下划线、中划线。

        :param service_name: The service_name of this UpdateEndpointServiceRequestBody.
        :type service_name: str
        """
        self._service_name = service_name

    @property
    def ports(self):
        """Gets the ports of this UpdateEndpointServiceRequestBody.

        服务开放的端口映射列表，详细内容请参见表4-22。 同一个终端节点服务下，不允许重复的端口映射。若多个终端节点服务共用一个port_id，则终端节点之间服务的所有端口映射的server_port和protocol的组合不能重复，单次最多添加200个。

        :return: The ports of this UpdateEndpointServiceRequestBody.
        :rtype: list[:class:`huaweicloudsdkvpcep.v1.PortList`]
        """
        return self._ports

    @ports.setter
    def ports(self, ports):
        """Sets the ports of this UpdateEndpointServiceRequestBody.

        服务开放的端口映射列表，详细内容请参见表4-22。 同一个终端节点服务下，不允许重复的端口映射。若多个终端节点服务共用一个port_id，则终端节点之间服务的所有端口映射的server_port和protocol的组合不能重复，单次最多添加200个。

        :param ports: The ports of this UpdateEndpointServiceRequestBody.
        :type ports: list[:class:`huaweicloudsdkvpcep.v1.PortList`]
        """
        self._ports = ports

    @property
    def port_id(self):
        """Gets the port_id of this UpdateEndpointServiceRequestBody.

        标识终端节点服务后端资源的ID，格式为通用唯一识别码 （Universally UniqueIdentifier，下文简称UUID）。取值为： ● LB类型：增强型负载均衡器内网IP对应的端口ID。详细内容请参考《弹性负载均衡API参考》中的“查询负载均 衡详情”，详见响应消息中的“vip_port_id”字段。 ● VM类型：弹性云服务器IP地址对应的网卡ID。详细内容请参考《弹性云服务器API参考》中的“查询云服务器网 卡信息”，详见响应消息中的“port_id”字段。 ● VIP类型：虚拟资源所在物理服务器对应的网卡ID。 说明 当后端资源为“LB类型”时，仅支持修改为同类型后端资源的“vip_port_id”。 例如，共享型负载均衡仅支持更换为共享型负载均衡，不支持更换为独享型负载均衡。

        :return: The port_id of this UpdateEndpointServiceRequestBody.
        :rtype: str
        """
        return self._port_id

    @port_id.setter
    def port_id(self, port_id):
        """Sets the port_id of this UpdateEndpointServiceRequestBody.

        标识终端节点服务后端资源的ID，格式为通用唯一识别码 （Universally UniqueIdentifier，下文简称UUID）。取值为： ● LB类型：增强型负载均衡器内网IP对应的端口ID。详细内容请参考《弹性负载均衡API参考》中的“查询负载均 衡详情”，详见响应消息中的“vip_port_id”字段。 ● VM类型：弹性云服务器IP地址对应的网卡ID。详细内容请参考《弹性云服务器API参考》中的“查询云服务器网 卡信息”，详见响应消息中的“port_id”字段。 ● VIP类型：虚拟资源所在物理服务器对应的网卡ID。 说明 当后端资源为“LB类型”时，仅支持修改为同类型后端资源的“vip_port_id”。 例如，共享型负载均衡仅支持更换为共享型负载均衡，不支持更换为独享型负载均衡。

        :param port_id: The port_id of this UpdateEndpointServiceRequestBody.
        :type port_id: str
        """
        self._port_id = port_id

    @property
    def vip_port_id(self):
        """Gets the vip_port_id of this UpdateEndpointServiceRequestBody.

        虚拟IP的网卡ID。

        :return: The vip_port_id of this UpdateEndpointServiceRequestBody.
        :rtype: str
        """
        return self._vip_port_id

    @vip_port_id.setter
    def vip_port_id(self, vip_port_id):
        """Sets the vip_port_id of this UpdateEndpointServiceRequestBody.

        虚拟IP的网卡ID。

        :param vip_port_id: The vip_port_id of this UpdateEndpointServiceRequestBody.
        :type vip_port_id: str
        """
        self._vip_port_id = vip_port_id

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
        if not isinstance(other, UpdateEndpointServiceRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
