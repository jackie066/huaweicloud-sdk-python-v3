# coding: utf-8

import pprint
import re

import six





class ServiceProperty:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'property_name': 'str',
        'data_type': 'str',
        'required': 'bool',
        'enum_list': 'list[str]',
        'min': 'str',
        'max': 'str',
        'max_length': 'int',
        'step': 'float',
        'unit': 'str',
        'method': 'str',
        'description': 'str',
        'default_value': 'object'
    }

    attribute_map = {
        'property_name': 'property_name',
        'data_type': 'data_type',
        'required': 'required',
        'enum_list': 'enum_list',
        'min': 'min',
        'max': 'max',
        'max_length': 'max_length',
        'step': 'step',
        'unit': 'unit',
        'method': 'method',
        'description': 'description',
        'default_value': 'default_value'
    }

    def __init__(self, property_name=None, data_type=None, required=None, enum_list=None, min=None, max=None, max_length=None, step=None, unit=None, method=None, description=None, default_value=None):
        """ServiceProperty - a model defined in huaweicloud sdk"""
        
        

        self._property_name = None
        self._data_type = None
        self._required = None
        self._enum_list = None
        self._min = None
        self._max = None
        self._max_length = None
        self._step = None
        self._unit = None
        self._method = None
        self._description = None
        self._default_value = None
        self.discriminator = None

        self.property_name = property_name
        self.data_type = data_type
        if required is not None:
            self.required = required
        if enum_list is not None:
            self.enum_list = enum_list
        if min is not None:
            self.min = min
        if max is not None:
            self.max = max
        if max_length is not None:
            self.max_length = max_length
        if step is not None:
            self.step = step
        if unit is not None:
            self.unit = unit
        self.method = method
        if description is not None:
            self.description = description
        if default_value is not None:
            self.default_value = default_value

    @property
    def property_name(self):
        """Gets the property_name of this ServiceProperty.

        设备属性名称。

        :return: The property_name of this ServiceProperty.
        :rtype: str
        """
        return self._property_name

    @property_name.setter
    def property_name(self, property_name):
        """Sets the property_name of this ServiceProperty.

        设备属性名称。

        :param property_name: The property_name of this ServiceProperty.
        :type: str
        """
        self._property_name = property_name

    @property
    def data_type(self):
        """Gets the data_type of this ServiceProperty.

        设备属性的数据类型。取值范围：int，long，decimal，string，DateTime，jsonObject，enum，boolean，string list。

        :return: The data_type of this ServiceProperty.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this ServiceProperty.

        设备属性的数据类型。取值范围：int，long，decimal，string，DateTime，jsonObject，enum，boolean，string list。

        :param data_type: The data_type of this ServiceProperty.
        :type: str
        """
        self._data_type = data_type

    @property
    def required(self):
        """Gets the required of this ServiceProperty.

        设备属性是否必选。默认为false。

        :return: The required of this ServiceProperty.
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this ServiceProperty.

        设备属性是否必选。默认为false。

        :param required: The required of this ServiceProperty.
        :type: bool
        """
        self._required = required

    @property
    def enum_list(self):
        """Gets the enum_list of this ServiceProperty.

        设备属性的枚举值列表。

        :return: The enum_list of this ServiceProperty.
        :rtype: list[str]
        """
        return self._enum_list

    @enum_list.setter
    def enum_list(self, enum_list):
        """Sets the enum_list of this ServiceProperty.

        设备属性的枚举值列表。

        :param enum_list: The enum_list of this ServiceProperty.
        :type: list[str]
        """
        self._enum_list = enum_list

    @property
    def min(self):
        """Gets the min of this ServiceProperty.

        设备属性的最小值。

        :return: The min of this ServiceProperty.
        :rtype: str
        """
        return self._min

    @min.setter
    def min(self, min):
        """Sets the min of this ServiceProperty.

        设备属性的最小值。

        :param min: The min of this ServiceProperty.
        :type: str
        """
        self._min = min

    @property
    def max(self):
        """Gets the max of this ServiceProperty.

        设备属性的最大值。

        :return: The max of this ServiceProperty.
        :rtype: str
        """
        return self._max

    @max.setter
    def max(self, max):
        """Sets the max of this ServiceProperty.

        设备属性的最大值。

        :param max: The max of this ServiceProperty.
        :type: str
        """
        self._max = max

    @property
    def max_length(self):
        """Gets the max_length of this ServiceProperty.

        设备属性的最大长度。

        :return: The max_length of this ServiceProperty.
        :rtype: int
        """
        return self._max_length

    @max_length.setter
    def max_length(self, max_length):
        """Sets the max_length of this ServiceProperty.

        设备属性的最大长度。

        :param max_length: The max_length of this ServiceProperty.
        :type: int
        """
        self._max_length = max_length

    @property
    def step(self):
        """Gets the step of this ServiceProperty.

        设备属性的步长。

        :return: The step of this ServiceProperty.
        :rtype: float
        """
        return self._step

    @step.setter
    def step(self, step):
        """Sets the step of this ServiceProperty.

        设备属性的步长。

        :param step: The step of this ServiceProperty.
        :type: float
        """
        self._step = step

    @property
    def unit(self):
        """Gets the unit of this ServiceProperty.

        设备属性的单位。

        :return: The unit of this ServiceProperty.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this ServiceProperty.

        设备属性的单位。

        :param unit: The unit of this ServiceProperty.
        :type: str
        """
        self._unit = unit

    @property
    def method(self):
        """Gets the method of this ServiceProperty.

        设备属性的访问模式。取值范围：RWE，RW，RE，WE，E，W，R。 - R：属性值可读 - W：属性值可写 - E：属性值可订阅，即属性值变化时上报事件 

        :return: The method of this ServiceProperty.
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this ServiceProperty.

        设备属性的访问模式。取值范围：RWE，RW，RE，WE，E，W，R。 - R：属性值可读 - W：属性值可写 - E：属性值可订阅，即属性值变化时上报事件 

        :param method: The method of this ServiceProperty.
        :type: str
        """
        self._method = method

    @property
    def description(self):
        """Gets the description of this ServiceProperty.

        设备属性的描述。

        :return: The description of this ServiceProperty.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ServiceProperty.

        设备属性的描述。

        :param description: The description of this ServiceProperty.
        :type: str
        """
        self._description = description

    @property
    def default_value(self):
        """Gets the default_value of this ServiceProperty.

        设备属性的默认值。如果设置了默认值，使用该产品创建设备时，会将该属性的默认值写入到该设备的设备影子预期数据中，待设备上线时将该属性默认值下发给设备。

        :return: The default_value of this ServiceProperty.
        :rtype: object
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """Sets the default_value of this ServiceProperty.

        设备属性的默认值。如果设置了默认值，使用该产品创建设备时，会将该属性的默认值写入到该设备的设备影子预期数据中，待设备上线时将该属性默认值下发给设备。

        :param default_value: The default_value of this ServiceProperty.
        :type: object
        """
        self._default_value = default_value

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
        if not isinstance(other, ServiceProperty):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
