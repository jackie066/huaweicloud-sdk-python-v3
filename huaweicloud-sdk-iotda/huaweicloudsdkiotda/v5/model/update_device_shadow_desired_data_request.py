# coding: utf-8

import pprint
import re

import six





class UpdateDeviceShadowDesiredDataRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []
    sensitive_list.append('sp_auth_token')
    sensitive_list.append('stage_auth_token')

    openapi_types = {
        'sp_auth_token': 'str',
        'stage_auth_token': 'str',
        'instance_id': 'str',
        'device_id': 'str',
        'body': 'UpdateDesireds'
    }

    attribute_map = {
        'sp_auth_token': 'Sp-Auth-Token',
        'stage_auth_token': 'Stage-Auth-Token',
        'instance_id': 'Instance-Id',
        'device_id': 'device_id',
        'body': 'body'
    }

    def __init__(self, sp_auth_token=None, stage_auth_token=None, instance_id=None, device_id=None, body=None):
        """UpdateDeviceShadowDesiredDataRequest - a model defined in huaweicloud sdk"""
        
        

        self._sp_auth_token = None
        self._stage_auth_token = None
        self._instance_id = None
        self._device_id = None
        self._body = None
        self.discriminator = None

        if sp_auth_token is not None:
            self.sp_auth_token = sp_auth_token
        if stage_auth_token is not None:
            self.stage_auth_token = stage_auth_token
        if instance_id is not None:
            self.instance_id = instance_id
        self.device_id = device_id
        if body is not None:
            self.body = body

    @property
    def sp_auth_token(self):
        """Gets the sp_auth_token of this UpdateDeviceShadowDesiredDataRequest.


        :return: The sp_auth_token of this UpdateDeviceShadowDesiredDataRequest.
        :rtype: str
        """
        return self._sp_auth_token

    @sp_auth_token.setter
    def sp_auth_token(self, sp_auth_token):
        """Sets the sp_auth_token of this UpdateDeviceShadowDesiredDataRequest.


        :param sp_auth_token: The sp_auth_token of this UpdateDeviceShadowDesiredDataRequest.
        :type: str
        """
        self._sp_auth_token = sp_auth_token

    @property
    def stage_auth_token(self):
        """Gets the stage_auth_token of this UpdateDeviceShadowDesiredDataRequest.


        :return: The stage_auth_token of this UpdateDeviceShadowDesiredDataRequest.
        :rtype: str
        """
        return self._stage_auth_token

    @stage_auth_token.setter
    def stage_auth_token(self, stage_auth_token):
        """Sets the stage_auth_token of this UpdateDeviceShadowDesiredDataRequest.


        :param stage_auth_token: The stage_auth_token of this UpdateDeviceShadowDesiredDataRequest.
        :type: str
        """
        self._stage_auth_token = stage_auth_token

    @property
    def instance_id(self):
        """Gets the instance_id of this UpdateDeviceShadowDesiredDataRequest.


        :return: The instance_id of this UpdateDeviceShadowDesiredDataRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this UpdateDeviceShadowDesiredDataRequest.


        :param instance_id: The instance_id of this UpdateDeviceShadowDesiredDataRequest.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def device_id(self):
        """Gets the device_id of this UpdateDeviceShadowDesiredDataRequest.


        :return: The device_id of this UpdateDeviceShadowDesiredDataRequest.
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this UpdateDeviceShadowDesiredDataRequest.


        :param device_id: The device_id of this UpdateDeviceShadowDesiredDataRequest.
        :type: str
        """
        self._device_id = device_id

    @property
    def body(self):
        """Gets the body of this UpdateDeviceShadowDesiredDataRequest.


        :return: The body of this UpdateDeviceShadowDesiredDataRequest.
        :rtype: UpdateDesireds
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateDeviceShadowDesiredDataRequest.


        :param body: The body of this UpdateDeviceShadowDesiredDataRequest.
        :type: UpdateDesireds
        """
        self._body = body

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
        if not isinstance(other, UpdateDeviceShadowDesiredDataRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
