# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportCertificateResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'private_key': 'str',
        'certificate': 'str',
        'certificate_chain': 'str'
    }

    attribute_map = {
        'private_key': 'private_key',
        'certificate': 'certificate',
        'certificate_chain': 'certificate_chain'
    }

    def __init__(self, private_key=None, certificate=None, certificate_chain=None):
        """ExportCertificateResponse

        The model defined in huaweicloud sdk

        :param private_key: 私钥内容。
        :type private_key: str
        :param certificate: 证书内容。
        :type certificate: str
        :param certificate_chain: 证书链内容。
        :type certificate_chain: str
        """
        
        super(ExportCertificateResponse, self).__init__()

        self._private_key = None
        self._certificate = None
        self._certificate_chain = None
        self.discriminator = None

        if private_key is not None:
            self.private_key = private_key
        if certificate is not None:
            self.certificate = certificate
        if certificate_chain is not None:
            self.certificate_chain = certificate_chain

    @property
    def private_key(self):
        """Gets the private_key of this ExportCertificateResponse.

        私钥内容。

        :return: The private_key of this ExportCertificateResponse.
        :rtype: str
        """
        return self._private_key

    @private_key.setter
    def private_key(self, private_key):
        """Sets the private_key of this ExportCertificateResponse.

        私钥内容。

        :param private_key: The private_key of this ExportCertificateResponse.
        :type private_key: str
        """
        self._private_key = private_key

    @property
    def certificate(self):
        """Gets the certificate of this ExportCertificateResponse.

        证书内容。

        :return: The certificate of this ExportCertificateResponse.
        :rtype: str
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        """Sets the certificate of this ExportCertificateResponse.

        证书内容。

        :param certificate: The certificate of this ExportCertificateResponse.
        :type certificate: str
        """
        self._certificate = certificate

    @property
    def certificate_chain(self):
        """Gets the certificate_chain of this ExportCertificateResponse.

        证书链内容。

        :return: The certificate_chain of this ExportCertificateResponse.
        :rtype: str
        """
        return self._certificate_chain

    @certificate_chain.setter
    def certificate_chain(self, certificate_chain):
        """Sets the certificate_chain of this ExportCertificateResponse.

        证书链内容。

        :param certificate_chain: The certificate_chain of this ExportCertificateResponse.
        :type certificate_chain: str
        """
        self._certificate_chain = certificate_chain

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
        if not isinstance(other, ExportCertificateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
