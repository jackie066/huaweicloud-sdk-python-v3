# coding: utf-8

import pprint
import re

import six


class ListDevicesResponse(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'devices': 'list[QueryDeviceSimplify]',
        'page': 'Page'
    }

    attribute_map = {
        'devices': 'devices',
        'page': 'page'
    }

    def __init__(self, devices=None, page=None):  # noqa: E501
        """ListDevicesResponse - a model defined in huaweicloud sdk"""

        self._devices = None
        self._page = None
        self.discriminator = None

        if devices is not None:
            self.devices = devices
        if page is not None:
            self.page = page

    @property
    def devices(self):
        """Gets the devices of this ListDevicesResponse.

        设备信息列表。

        :return: The devices of this ListDevicesResponse.
        :rtype: list[QueryDeviceSimplify]
        """
        return self._devices

    @devices.setter
    def devices(self, devices):
        """Sets the devices of this ListDevicesResponse.

        设备信息列表。

        :param devices: The devices of this ListDevicesResponse.
        :type: list[QueryDeviceSimplify]
        """
        self._devices = devices

    @property
    def page(self):
        """Gets the page of this ListDevicesResponse.


        :return: The page of this ListDevicesResponse.
        :rtype: Page
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this ListDevicesResponse.


        :param page: The page of this ListDevicesResponse.
        :type: Page
        """
        self._page = page

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
        if not isinstance(other, ListDevicesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
