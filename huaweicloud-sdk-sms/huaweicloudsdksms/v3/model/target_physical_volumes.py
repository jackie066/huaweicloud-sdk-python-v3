# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TargetPhysicalVolumes:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'device_use': 'str',
        'file_system': 'str',
        'index': 'int',
        'mount_point': 'str',
        'name': 'str',
        'size': 'int',
        'used_size': 'int',
        'uuid': 'str'
    }

    attribute_map = {
        'device_use': 'device_use',
        'file_system': 'file_system',
        'index': 'index',
        'mount_point': 'mount_point',
        'name': 'name',
        'size': 'size',
        'used_size': 'used_size',
        'uuid': 'uuid'
    }

    def __init__(self, device_use=None, file_system=None, index=None, mount_point=None, name=None, size=None, used_size=None, uuid=None):
        """TargetPhysicalVolumes

        The model defined in huaweicloud sdk

        :param device_use: 分区类型
        :type device_use: str
        :param file_system: 文件系统
        :type file_system: str
        :param index: 编号
        :type index: int
        :param mount_point: 挂载点
        :type mount_point: str
        :param name: 名称
        :type name: str
        :param size: 大小
        :type size: int
        :param used_size: 使用大小
        :type used_size: int
        :param uuid: uuid
        :type uuid: str
        """
        
        

        self._device_use = None
        self._file_system = None
        self._index = None
        self._mount_point = None
        self._name = None
        self._size = None
        self._used_size = None
        self._uuid = None
        self.discriminator = None

        if device_use is not None:
            self.device_use = device_use
        if file_system is not None:
            self.file_system = file_system
        if index is not None:
            self.index = index
        if mount_point is not None:
            self.mount_point = mount_point
        if name is not None:
            self.name = name
        if size is not None:
            self.size = size
        if used_size is not None:
            self.used_size = used_size
        if uuid is not None:
            self.uuid = uuid

    @property
    def device_use(self):
        """Gets the device_use of this TargetPhysicalVolumes.

        分区类型

        :return: The device_use of this TargetPhysicalVolumes.
        :rtype: str
        """
        return self._device_use

    @device_use.setter
    def device_use(self, device_use):
        """Sets the device_use of this TargetPhysicalVolumes.

        分区类型

        :param device_use: The device_use of this TargetPhysicalVolumes.
        :type device_use: str
        """
        self._device_use = device_use

    @property
    def file_system(self):
        """Gets the file_system of this TargetPhysicalVolumes.

        文件系统

        :return: The file_system of this TargetPhysicalVolumes.
        :rtype: str
        """
        return self._file_system

    @file_system.setter
    def file_system(self, file_system):
        """Sets the file_system of this TargetPhysicalVolumes.

        文件系统

        :param file_system: The file_system of this TargetPhysicalVolumes.
        :type file_system: str
        """
        self._file_system = file_system

    @property
    def index(self):
        """Gets the index of this TargetPhysicalVolumes.

        编号

        :return: The index of this TargetPhysicalVolumes.
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this TargetPhysicalVolumes.

        编号

        :param index: The index of this TargetPhysicalVolumes.
        :type index: int
        """
        self._index = index

    @property
    def mount_point(self):
        """Gets the mount_point of this TargetPhysicalVolumes.

        挂载点

        :return: The mount_point of this TargetPhysicalVolumes.
        :rtype: str
        """
        return self._mount_point

    @mount_point.setter
    def mount_point(self, mount_point):
        """Sets the mount_point of this TargetPhysicalVolumes.

        挂载点

        :param mount_point: The mount_point of this TargetPhysicalVolumes.
        :type mount_point: str
        """
        self._mount_point = mount_point

    @property
    def name(self):
        """Gets the name of this TargetPhysicalVolumes.

        名称

        :return: The name of this TargetPhysicalVolumes.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TargetPhysicalVolumes.

        名称

        :param name: The name of this TargetPhysicalVolumes.
        :type name: str
        """
        self._name = name

    @property
    def size(self):
        """Gets the size of this TargetPhysicalVolumes.

        大小

        :return: The size of this TargetPhysicalVolumes.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this TargetPhysicalVolumes.

        大小

        :param size: The size of this TargetPhysicalVolumes.
        :type size: int
        """
        self._size = size

    @property
    def used_size(self):
        """Gets the used_size of this TargetPhysicalVolumes.

        使用大小

        :return: The used_size of this TargetPhysicalVolumes.
        :rtype: int
        """
        return self._used_size

    @used_size.setter
    def used_size(self, used_size):
        """Sets the used_size of this TargetPhysicalVolumes.

        使用大小

        :param used_size: The used_size of this TargetPhysicalVolumes.
        :type used_size: int
        """
        self._used_size = used_size

    @property
    def uuid(self):
        """Gets the uuid of this TargetPhysicalVolumes.

        uuid

        :return: The uuid of this TargetPhysicalVolumes.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this TargetPhysicalVolumes.

        uuid

        :param uuid: The uuid of this TargetPhysicalVolumes.
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
        if not isinstance(other, TargetPhysicalVolumes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
