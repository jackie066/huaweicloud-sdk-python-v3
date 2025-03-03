# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDatasourceConnectionRespAvailableQueueInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'name': 'str',
        'err_msg': 'str',
        'update_time': 'int',
        'uuid': 'str'
    }

    attribute_map = {
        'status': 'status',
        'name': 'name',
        'err_msg': 'err_msg',
        'update_time': 'update_time',
        'uuid': 'uuid'
    }

    def __init__(self, status=None, name=None, err_msg=None, update_time=None, uuid=None):
        """ShowDatasourceConnectionRespAvailableQueueInfo

        The model defined in huaweicloud sdk

        :param status: 连接状态，状态码请参考表连接状态：  - CREATING： 跨源连接正在创建中  - ACTIVE： 跨源连接创建成功，与目的地址连接正常  - FAILED： 跨源连接创建失败  - DELETED： 跨源连接已被删除 
        :type status: str
        :param name: 队列名称。
        :type name: str
        :param err_msg: 状态为失败时的详细报错信息。
        :type err_msg: str
        :param update_time: 更新时间。
        :type update_time: int
        :param uuid: 跨源连接ID。
        :type uuid: str
        """
        
        

        self._status = None
        self._name = None
        self._err_msg = None
        self._update_time = None
        self._uuid = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if name is not None:
            self.name = name
        if err_msg is not None:
            self.err_msg = err_msg
        if update_time is not None:
            self.update_time = update_time
        if uuid is not None:
            self.uuid = uuid

    @property
    def status(self):
        """Gets the status of this ShowDatasourceConnectionRespAvailableQueueInfo.

        连接状态，状态码请参考表连接状态：  - CREATING： 跨源连接正在创建中  - ACTIVE： 跨源连接创建成功，与目的地址连接正常  - FAILED： 跨源连接创建失败  - DELETED： 跨源连接已被删除 

        :return: The status of this ShowDatasourceConnectionRespAvailableQueueInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowDatasourceConnectionRespAvailableQueueInfo.

        连接状态，状态码请参考表连接状态：  - CREATING： 跨源连接正在创建中  - ACTIVE： 跨源连接创建成功，与目的地址连接正常  - FAILED： 跨源连接创建失败  - DELETED： 跨源连接已被删除 

        :param status: The status of this ShowDatasourceConnectionRespAvailableQueueInfo.
        :type status: str
        """
        self._status = status

    @property
    def name(self):
        """Gets the name of this ShowDatasourceConnectionRespAvailableQueueInfo.

        队列名称。

        :return: The name of this ShowDatasourceConnectionRespAvailableQueueInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowDatasourceConnectionRespAvailableQueueInfo.

        队列名称。

        :param name: The name of this ShowDatasourceConnectionRespAvailableQueueInfo.
        :type name: str
        """
        self._name = name

    @property
    def err_msg(self):
        """Gets the err_msg of this ShowDatasourceConnectionRespAvailableQueueInfo.

        状态为失败时的详细报错信息。

        :return: The err_msg of this ShowDatasourceConnectionRespAvailableQueueInfo.
        :rtype: str
        """
        return self._err_msg

    @err_msg.setter
    def err_msg(self, err_msg):
        """Sets the err_msg of this ShowDatasourceConnectionRespAvailableQueueInfo.

        状态为失败时的详细报错信息。

        :param err_msg: The err_msg of this ShowDatasourceConnectionRespAvailableQueueInfo.
        :type err_msg: str
        """
        self._err_msg = err_msg

    @property
    def update_time(self):
        """Gets the update_time of this ShowDatasourceConnectionRespAvailableQueueInfo.

        更新时间。

        :return: The update_time of this ShowDatasourceConnectionRespAvailableQueueInfo.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this ShowDatasourceConnectionRespAvailableQueueInfo.

        更新时间。

        :param update_time: The update_time of this ShowDatasourceConnectionRespAvailableQueueInfo.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def uuid(self):
        """Gets the uuid of this ShowDatasourceConnectionRespAvailableQueueInfo.

        跨源连接ID。

        :return: The uuid of this ShowDatasourceConnectionRespAvailableQueueInfo.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this ShowDatasourceConnectionRespAvailableQueueInfo.

        跨源连接ID。

        :param uuid: The uuid of this ShowDatasourceConnectionRespAvailableQueueInfo.
        :type uuid: str
        """
        self._uuid = uuid

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
        if not isinstance(other, ShowDatasourceConnectionRespAvailableQueueInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
