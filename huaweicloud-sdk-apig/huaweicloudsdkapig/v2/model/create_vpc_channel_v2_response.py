# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateVpcChannelV2Response(SdkResponse):

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
        'port': 'int',
        'balance_strategy': 'int',
        'member_type': 'str',
        'create_time': 'datetime',
        'id': 'str',
        'status': 'int',
        'member_groups': 'list[MemberGroupInfo]'
    }

    attribute_map = {
        'name': 'name',
        'port': 'port',
        'balance_strategy': 'balance_strategy',
        'member_type': 'member_type',
        'create_time': 'create_time',
        'id': 'id',
        'status': 'status',
        'member_groups': 'member_groups'
    }

    def __init__(self, name=None, port=None, balance_strategy=None, member_type=None, create_time=None, id=None, status=None, member_groups=None):
        """CreateVpcChannelV2Response

        The model defined in huaweicloud sdk

        :param name: VPC通道的名称。  长度为3 ~ 64位的字符串，字符串由中文、英文字母、数字、中划线、下划线组成，且只能以英文或中文开头。 &gt; 中文字符必须为UTF-8或者unicode编码。
        :type name: str
        :param port: VPC通道中主机的端口号。  取值范围1 ~ 65535，仅VPC通道类型为2时有效。  VPC通道类型为2时必选。
        :type port: int
        :param balance_strategy: 分发算法。 - 1：加权轮询（wrr） - 2：加权最少连接（wleastconn） - 3：源地址哈希（source） - 4：URI哈希（uri）  VPC通道类型为2时必选。
        :type balance_strategy: int
        :param member_type: VPC通道的成员类型。 - ip - ecs  VPC通道类型为2时必选。
        :type member_type: str
        :param create_time: VPC通道的创建时间
        :type create_time: datetime
        :param id: VPC通道的编号
        :type id: str
        :param status: VPC通道的状态。 - 1：正常 - 2：异常
        :type status: int
        :param member_groups: 后端云服务器组列表。  暂不支持
        :type member_groups: list[:class:`huaweicloudsdkapig.v2.MemberGroupInfo`]
        """
        
        super(CreateVpcChannelV2Response, self).__init__()

        self._name = None
        self._port = None
        self._balance_strategy = None
        self._member_type = None
        self._create_time = None
        self._id = None
        self._status = None
        self._member_groups = None
        self.discriminator = None

        self.name = name
        if port is not None:
            self.port = port
        if balance_strategy is not None:
            self.balance_strategy = balance_strategy
        if member_type is not None:
            self.member_type = member_type
        if create_time is not None:
            self.create_time = create_time
        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if member_groups is not None:
            self.member_groups = member_groups

    @property
    def name(self):
        """Gets the name of this CreateVpcChannelV2Response.

        VPC通道的名称。  长度为3 ~ 64位的字符串，字符串由中文、英文字母、数字、中划线、下划线组成，且只能以英文或中文开头。 > 中文字符必须为UTF-8或者unicode编码。

        :return: The name of this CreateVpcChannelV2Response.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateVpcChannelV2Response.

        VPC通道的名称。  长度为3 ~ 64位的字符串，字符串由中文、英文字母、数字、中划线、下划线组成，且只能以英文或中文开头。 > 中文字符必须为UTF-8或者unicode编码。

        :param name: The name of this CreateVpcChannelV2Response.
        :type name: str
        """
        self._name = name

    @property
    def port(self):
        """Gets the port of this CreateVpcChannelV2Response.

        VPC通道中主机的端口号。  取值范围1 ~ 65535，仅VPC通道类型为2时有效。  VPC通道类型为2时必选。

        :return: The port of this CreateVpcChannelV2Response.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this CreateVpcChannelV2Response.

        VPC通道中主机的端口号。  取值范围1 ~ 65535，仅VPC通道类型为2时有效。  VPC通道类型为2时必选。

        :param port: The port of this CreateVpcChannelV2Response.
        :type port: int
        """
        self._port = port

    @property
    def balance_strategy(self):
        """Gets the balance_strategy of this CreateVpcChannelV2Response.

        分发算法。 - 1：加权轮询（wrr） - 2：加权最少连接（wleastconn） - 3：源地址哈希（source） - 4：URI哈希（uri）  VPC通道类型为2时必选。

        :return: The balance_strategy of this CreateVpcChannelV2Response.
        :rtype: int
        """
        return self._balance_strategy

    @balance_strategy.setter
    def balance_strategy(self, balance_strategy):
        """Sets the balance_strategy of this CreateVpcChannelV2Response.

        分发算法。 - 1：加权轮询（wrr） - 2：加权最少连接（wleastconn） - 3：源地址哈希（source） - 4：URI哈希（uri）  VPC通道类型为2时必选。

        :param balance_strategy: The balance_strategy of this CreateVpcChannelV2Response.
        :type balance_strategy: int
        """
        self._balance_strategy = balance_strategy

    @property
    def member_type(self):
        """Gets the member_type of this CreateVpcChannelV2Response.

        VPC通道的成员类型。 - ip - ecs  VPC通道类型为2时必选。

        :return: The member_type of this CreateVpcChannelV2Response.
        :rtype: str
        """
        return self._member_type

    @member_type.setter
    def member_type(self, member_type):
        """Sets the member_type of this CreateVpcChannelV2Response.

        VPC通道的成员类型。 - ip - ecs  VPC通道类型为2时必选。

        :param member_type: The member_type of this CreateVpcChannelV2Response.
        :type member_type: str
        """
        self._member_type = member_type

    @property
    def create_time(self):
        """Gets the create_time of this CreateVpcChannelV2Response.

        VPC通道的创建时间

        :return: The create_time of this CreateVpcChannelV2Response.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this CreateVpcChannelV2Response.

        VPC通道的创建时间

        :param create_time: The create_time of this CreateVpcChannelV2Response.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def id(self):
        """Gets the id of this CreateVpcChannelV2Response.

        VPC通道的编号

        :return: The id of this CreateVpcChannelV2Response.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreateVpcChannelV2Response.

        VPC通道的编号

        :param id: The id of this CreateVpcChannelV2Response.
        :type id: str
        """
        self._id = id

    @property
    def status(self):
        """Gets the status of this CreateVpcChannelV2Response.

        VPC通道的状态。 - 1：正常 - 2：异常

        :return: The status of this CreateVpcChannelV2Response.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CreateVpcChannelV2Response.

        VPC通道的状态。 - 1：正常 - 2：异常

        :param status: The status of this CreateVpcChannelV2Response.
        :type status: int
        """
        self._status = status

    @property
    def member_groups(self):
        """Gets the member_groups of this CreateVpcChannelV2Response.

        后端云服务器组列表。  暂不支持

        :return: The member_groups of this CreateVpcChannelV2Response.
        :rtype: list[:class:`huaweicloudsdkapig.v2.MemberGroupInfo`]
        """
        return self._member_groups

    @member_groups.setter
    def member_groups(self, member_groups):
        """Sets the member_groups of this CreateVpcChannelV2Response.

        后端云服务器组列表。  暂不支持

        :param member_groups: The member_groups of this CreateVpcChannelV2Response.
        :type member_groups: list[:class:`huaweicloudsdkapig.v2.MemberGroupInfo`]
        """
        self._member_groups = member_groups

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
        if not isinstance(other, CreateVpcChannelV2Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
