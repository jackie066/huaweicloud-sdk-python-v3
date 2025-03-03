# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePremiumHostRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'certificateid': 'str',
        'certificatename': 'str',
        'hostname': 'str',
        'proxy': 'bool',
        'policyid': 'str',
        'server': 'list[PremiumWafServer]'
    }

    attribute_map = {
        'certificateid': 'certificateid',
        'certificatename': 'certificatename',
        'hostname': 'hostname',
        'proxy': 'proxy',
        'policyid': 'policyid',
        'server': 'server'
    }

    def __init__(self, certificateid=None, certificatename=None, hostname=None, proxy=None, policyid=None, server=None):
        """CreatePremiumHostRequestBody

        The model defined in huaweicloud sdk

        :param certificateid: 证书id，通过查询证书列表接口（ListCertificates）接口获取证书id   - 对外协议为HTTP时不需要填写   - 对外协议HTTPS时为必填参数
        :type certificateid: str
        :param certificatename: 证书名   - 对外协议为HTTP时不需要填写   - 对外协议HTTPS时为必填参数
        :type certificatename: str
        :param hostname: 防护域名或IP（可带端口）
        :type hostname: str
        :param proxy: 是否使用代理
        :type proxy: bool
        :param policyid: 防护域名初始绑定的策略ID,可以通过策略名称调用查询防护策略列表（ListPolicy）接口查询到对应的策略id
        :type policyid: str
        :param server: 服务器配置
        :type server: list[:class:`huaweicloudsdkwaf.v1.PremiumWafServer`]
        """
        
        

        self._certificateid = None
        self._certificatename = None
        self._hostname = None
        self._proxy = None
        self._policyid = None
        self._server = None
        self.discriminator = None

        if certificateid is not None:
            self.certificateid = certificateid
        if certificatename is not None:
            self.certificatename = certificatename
        self.hostname = hostname
        self.proxy = proxy
        if policyid is not None:
            self.policyid = policyid
        self.server = server

    @property
    def certificateid(self):
        """Gets the certificateid of this CreatePremiumHostRequestBody.

        证书id，通过查询证书列表接口（ListCertificates）接口获取证书id   - 对外协议为HTTP时不需要填写   - 对外协议HTTPS时为必填参数

        :return: The certificateid of this CreatePremiumHostRequestBody.
        :rtype: str
        """
        return self._certificateid

    @certificateid.setter
    def certificateid(self, certificateid):
        """Sets the certificateid of this CreatePremiumHostRequestBody.

        证书id，通过查询证书列表接口（ListCertificates）接口获取证书id   - 对外协议为HTTP时不需要填写   - 对外协议HTTPS时为必填参数

        :param certificateid: The certificateid of this CreatePremiumHostRequestBody.
        :type certificateid: str
        """
        self._certificateid = certificateid

    @property
    def certificatename(self):
        """Gets the certificatename of this CreatePremiumHostRequestBody.

        证书名   - 对外协议为HTTP时不需要填写   - 对外协议HTTPS时为必填参数

        :return: The certificatename of this CreatePremiumHostRequestBody.
        :rtype: str
        """
        return self._certificatename

    @certificatename.setter
    def certificatename(self, certificatename):
        """Sets the certificatename of this CreatePremiumHostRequestBody.

        证书名   - 对外协议为HTTP时不需要填写   - 对外协议HTTPS时为必填参数

        :param certificatename: The certificatename of this CreatePremiumHostRequestBody.
        :type certificatename: str
        """
        self._certificatename = certificatename

    @property
    def hostname(self):
        """Gets the hostname of this CreatePremiumHostRequestBody.

        防护域名或IP（可带端口）

        :return: The hostname of this CreatePremiumHostRequestBody.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this CreatePremiumHostRequestBody.

        防护域名或IP（可带端口）

        :param hostname: The hostname of this CreatePremiumHostRequestBody.
        :type hostname: str
        """
        self._hostname = hostname

    @property
    def proxy(self):
        """Gets the proxy of this CreatePremiumHostRequestBody.

        是否使用代理

        :return: The proxy of this CreatePremiumHostRequestBody.
        :rtype: bool
        """
        return self._proxy

    @proxy.setter
    def proxy(self, proxy):
        """Sets the proxy of this CreatePremiumHostRequestBody.

        是否使用代理

        :param proxy: The proxy of this CreatePremiumHostRequestBody.
        :type proxy: bool
        """
        self._proxy = proxy

    @property
    def policyid(self):
        """Gets the policyid of this CreatePremiumHostRequestBody.

        防护域名初始绑定的策略ID,可以通过策略名称调用查询防护策略列表（ListPolicy）接口查询到对应的策略id

        :return: The policyid of this CreatePremiumHostRequestBody.
        :rtype: str
        """
        return self._policyid

    @policyid.setter
    def policyid(self, policyid):
        """Sets the policyid of this CreatePremiumHostRequestBody.

        防护域名初始绑定的策略ID,可以通过策略名称调用查询防护策略列表（ListPolicy）接口查询到对应的策略id

        :param policyid: The policyid of this CreatePremiumHostRequestBody.
        :type policyid: str
        """
        self._policyid = policyid

    @property
    def server(self):
        """Gets the server of this CreatePremiumHostRequestBody.

        服务器配置

        :return: The server of this CreatePremiumHostRequestBody.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.PremiumWafServer`]
        """
        return self._server

    @server.setter
    def server(self, server):
        """Sets the server of this CreatePremiumHostRequestBody.

        服务器配置

        :param server: The server of this CreatePremiumHostRequestBody.
        :type server: list[:class:`huaweicloudsdkwaf.v1.PremiumWafServer`]
        """
        self._server = server

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
        if not isinstance(other, CreatePremiumHostRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
