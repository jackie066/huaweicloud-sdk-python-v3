# coding: utf-8

import pprint
import re

import six


class DeleteCertificateRequest(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'certificate_id': 'str'
    }

    attribute_map = {
        'instance_id': 'Instance-Id',
        'certificate_id': 'certificate_id'
    }

    def __init__(self, instance_id=None, certificate_id=None):  # noqa: E501
        """DeleteCertificateRequest - a model defined in huaweicloud sdk"""

        self._instance_id = None
        self._certificate_id = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        self.certificate_id = certificate_id

    @property
    def instance_id(self):
        """Gets the instance_id of this DeleteCertificateRequest.


        :return: The instance_id of this DeleteCertificateRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this DeleteCertificateRequest.


        :param instance_id: The instance_id of this DeleteCertificateRequest.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def certificate_id(self):
        """Gets the certificate_id of this DeleteCertificateRequest.


        :return: The certificate_id of this DeleteCertificateRequest.
        :rtype: str
        """
        return self._certificate_id

    @certificate_id.setter
    def certificate_id(self, certificate_id):
        """Sets the certificate_id of this DeleteCertificateRequest.


        :param certificate_id: The certificate_id of this DeleteCertificateRequest.
        :type: str
        """
        self._certificate_id = certificate_id

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
        if not isinstance(other, DeleteCertificateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
