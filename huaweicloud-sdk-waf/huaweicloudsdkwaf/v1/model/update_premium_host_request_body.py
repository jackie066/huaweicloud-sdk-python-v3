# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdatePremiumHostRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'proxy': 'bool',
        'certificateid': 'str',
        'certificatename': 'str',
        'tls': 'str',
        'cipher': 'str',
        'mode': 'str',
        'locked': 'int',
        'protect_status': 'int',
        'access_status': 'int',
        'timestamp': 'int',
        'pool_ids': 'list[str]',
        'block_page': 'BlockPage',
        'traffic_mark': 'TrafficMark',
        'flag': 'dict(str, str)',
        'extend': 'dict(str, str)',
        'circuit_breaker': 'CircuitBreaker',
        'timeout_config': 'TimeoutConfig'
    }

    attribute_map = {
        'proxy': 'proxy',
        'certificateid': 'certificateid',
        'certificatename': 'certificatename',
        'tls': 'tls',
        'cipher': 'cipher',
        'mode': 'mode',
        'locked': 'locked',
        'protect_status': 'protect_status',
        'access_status': 'access_status',
        'timestamp': 'timestamp',
        'pool_ids': 'pool_ids',
        'block_page': 'block_page',
        'traffic_mark': 'traffic_mark',
        'flag': 'flag',
        'extend': 'extend',
        'circuit_breaker': 'circuit_breaker',
        'timeout_config': 'timeout_config'
    }

    def __init__(self, proxy=None, certificateid=None, certificatename=None, tls=None, cipher=None, mode=None, locked=None, protect_status=None, access_status=None, timestamp=None, pool_ids=None, block_page=None, traffic_mark=None, flag=None, extend=None, circuit_breaker=None, timeout_config=None):
        """UpdatePremiumHostRequestBody

        The model defined in huaweicloud sdk

        :param proxy: 是否使用代理
        :type proxy: bool
        :param certificateid: https证书id，通过查询证书列表接口（ListCertificates）接口获取证书id
        :type certificateid: str
        :param certificatename: https证书名称，通过查询证书列表接口（ListCertificates）接口获取证书id
        :type certificatename: str
        :param tls: 支持最低的TLS版本
        :type tls: str
        :param cipher: 加密套件（cipher_1，cipher_2，cipher_3，cipher_4，cipher_default）：  cipher_1： 加密算法为ECDHE-ECDSA-AES256-GCM-SHA384:HIGH:!MEDIUM:!LOW:!aNULL:!eNULL:!DES:!MD5:!PSK:!RC4:!kRSA:!SRP:!3DES:!DSS:!EXP:!CAMELLIA:@STRENGTH   cipher_2：加密算法为EECDH+AESGCM:EDH+AESGCM    cipher_3：加密算法为ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384:RC4:HIGH:!MD5:!aNULL:!eNULL:!NULL:!DH:!EDH    cipher_4：加密算法为ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-SHA384:AES256-SHA256:RC4:HIGH:!MD5:!aNULL:!eNULL:!NULL:!EDH    cipher_default： 加密算法为ECDHE-RSA-AES256-SHA384:AES256-SHA256:RC4:HIGH:!MD5:!aNULL:!eNULL:!NULL:!DH:!EDH:!AESGCM
        :type cipher: str
        :param mode: 独享模式特殊域名模式（仅特殊模式需要，如elb）
        :type mode: str
        :param locked: 是否锁定
        :type locked: int
        :param protect_status: 防护状态
        :type protect_status: int
        :param access_status: 接入状态
        :type access_status: int
        :param timestamp: 时间戳
        :type timestamp: int
        :param pool_ids: 域名关联的组ID（仅特殊模式需要，如elb）
        :type pool_ids: list[str]
        :param block_page: 
        :type block_page: :class:`huaweicloudsdkwaf.v1.BlockPage`
        :param traffic_mark: 
        :type traffic_mark: :class:`huaweicloudsdkwaf.v1.TrafficMark`
        :param flag: 域名特殊标识
        :type flag: dict(str, str)
        :param extend: 可扩展字段
        :type extend: dict(str, str)
        :param circuit_breaker: 
        :type circuit_breaker: :class:`huaweicloudsdkwaf.v1.CircuitBreaker`
        :param timeout_config: 
        :type timeout_config: :class:`huaweicloudsdkwaf.v1.TimeoutConfig`
        """
        
        

        self._proxy = None
        self._certificateid = None
        self._certificatename = None
        self._tls = None
        self._cipher = None
        self._mode = None
        self._locked = None
        self._protect_status = None
        self._access_status = None
        self._timestamp = None
        self._pool_ids = None
        self._block_page = None
        self._traffic_mark = None
        self._flag = None
        self._extend = None
        self._circuit_breaker = None
        self._timeout_config = None
        self.discriminator = None

        if proxy is not None:
            self.proxy = proxy
        if certificateid is not None:
            self.certificateid = certificateid
        if certificatename is not None:
            self.certificatename = certificatename
        if tls is not None:
            self.tls = tls
        if cipher is not None:
            self.cipher = cipher
        if mode is not None:
            self.mode = mode
        if locked is not None:
            self.locked = locked
        if protect_status is not None:
            self.protect_status = protect_status
        if access_status is not None:
            self.access_status = access_status
        if timestamp is not None:
            self.timestamp = timestamp
        if pool_ids is not None:
            self.pool_ids = pool_ids
        if block_page is not None:
            self.block_page = block_page
        if traffic_mark is not None:
            self.traffic_mark = traffic_mark
        if flag is not None:
            self.flag = flag
        if extend is not None:
            self.extend = extend
        if circuit_breaker is not None:
            self.circuit_breaker = circuit_breaker
        if timeout_config is not None:
            self.timeout_config = timeout_config

    @property
    def proxy(self):
        """Gets the proxy of this UpdatePremiumHostRequestBody.

        是否使用代理

        :return: The proxy of this UpdatePremiumHostRequestBody.
        :rtype: bool
        """
        return self._proxy

    @proxy.setter
    def proxy(self, proxy):
        """Sets the proxy of this UpdatePremiumHostRequestBody.

        是否使用代理

        :param proxy: The proxy of this UpdatePremiumHostRequestBody.
        :type proxy: bool
        """
        self._proxy = proxy

    @property
    def certificateid(self):
        """Gets the certificateid of this UpdatePremiumHostRequestBody.

        https证书id，通过查询证书列表接口（ListCertificates）接口获取证书id

        :return: The certificateid of this UpdatePremiumHostRequestBody.
        :rtype: str
        """
        return self._certificateid

    @certificateid.setter
    def certificateid(self, certificateid):
        """Sets the certificateid of this UpdatePremiumHostRequestBody.

        https证书id，通过查询证书列表接口（ListCertificates）接口获取证书id

        :param certificateid: The certificateid of this UpdatePremiumHostRequestBody.
        :type certificateid: str
        """
        self._certificateid = certificateid

    @property
    def certificatename(self):
        """Gets the certificatename of this UpdatePremiumHostRequestBody.

        https证书名称，通过查询证书列表接口（ListCertificates）接口获取证书id

        :return: The certificatename of this UpdatePremiumHostRequestBody.
        :rtype: str
        """
        return self._certificatename

    @certificatename.setter
    def certificatename(self, certificatename):
        """Sets the certificatename of this UpdatePremiumHostRequestBody.

        https证书名称，通过查询证书列表接口（ListCertificates）接口获取证书id

        :param certificatename: The certificatename of this UpdatePremiumHostRequestBody.
        :type certificatename: str
        """
        self._certificatename = certificatename

    @property
    def tls(self):
        """Gets the tls of this UpdatePremiumHostRequestBody.

        支持最低的TLS版本

        :return: The tls of this UpdatePremiumHostRequestBody.
        :rtype: str
        """
        return self._tls

    @tls.setter
    def tls(self, tls):
        """Sets the tls of this UpdatePremiumHostRequestBody.

        支持最低的TLS版本

        :param tls: The tls of this UpdatePremiumHostRequestBody.
        :type tls: str
        """
        self._tls = tls

    @property
    def cipher(self):
        """Gets the cipher of this UpdatePremiumHostRequestBody.

        加密套件（cipher_1，cipher_2，cipher_3，cipher_4，cipher_default）：  cipher_1： 加密算法为ECDHE-ECDSA-AES256-GCM-SHA384:HIGH:!MEDIUM:!LOW:!aNULL:!eNULL:!DES:!MD5:!PSK:!RC4:!kRSA:!SRP:!3DES:!DSS:!EXP:!CAMELLIA:@STRENGTH   cipher_2：加密算法为EECDH+AESGCM:EDH+AESGCM    cipher_3：加密算法为ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384:RC4:HIGH:!MD5:!aNULL:!eNULL:!NULL:!DH:!EDH    cipher_4：加密算法为ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-SHA384:AES256-SHA256:RC4:HIGH:!MD5:!aNULL:!eNULL:!NULL:!EDH    cipher_default： 加密算法为ECDHE-RSA-AES256-SHA384:AES256-SHA256:RC4:HIGH:!MD5:!aNULL:!eNULL:!NULL:!DH:!EDH:!AESGCM

        :return: The cipher of this UpdatePremiumHostRequestBody.
        :rtype: str
        """
        return self._cipher

    @cipher.setter
    def cipher(self, cipher):
        """Sets the cipher of this UpdatePremiumHostRequestBody.

        加密套件（cipher_1，cipher_2，cipher_3，cipher_4，cipher_default）：  cipher_1： 加密算法为ECDHE-ECDSA-AES256-GCM-SHA384:HIGH:!MEDIUM:!LOW:!aNULL:!eNULL:!DES:!MD5:!PSK:!RC4:!kRSA:!SRP:!3DES:!DSS:!EXP:!CAMELLIA:@STRENGTH   cipher_2：加密算法为EECDH+AESGCM:EDH+AESGCM    cipher_3：加密算法为ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384:RC4:HIGH:!MD5:!aNULL:!eNULL:!NULL:!DH:!EDH    cipher_4：加密算法为ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-SHA384:AES256-SHA256:RC4:HIGH:!MD5:!aNULL:!eNULL:!NULL:!EDH    cipher_default： 加密算法为ECDHE-RSA-AES256-SHA384:AES256-SHA256:RC4:HIGH:!MD5:!aNULL:!eNULL:!NULL:!DH:!EDH:!AESGCM

        :param cipher: The cipher of this UpdatePremiumHostRequestBody.
        :type cipher: str
        """
        self._cipher = cipher

    @property
    def mode(self):
        """Gets the mode of this UpdatePremiumHostRequestBody.

        独享模式特殊域名模式（仅特殊模式需要，如elb）

        :return: The mode of this UpdatePremiumHostRequestBody.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this UpdatePremiumHostRequestBody.

        独享模式特殊域名模式（仅特殊模式需要，如elb）

        :param mode: The mode of this UpdatePremiumHostRequestBody.
        :type mode: str
        """
        self._mode = mode

    @property
    def locked(self):
        """Gets the locked of this UpdatePremiumHostRequestBody.

        是否锁定

        :return: The locked of this UpdatePremiumHostRequestBody.
        :rtype: int
        """
        return self._locked

    @locked.setter
    def locked(self, locked):
        """Sets the locked of this UpdatePremiumHostRequestBody.

        是否锁定

        :param locked: The locked of this UpdatePremiumHostRequestBody.
        :type locked: int
        """
        self._locked = locked

    @property
    def protect_status(self):
        """Gets the protect_status of this UpdatePremiumHostRequestBody.

        防护状态

        :return: The protect_status of this UpdatePremiumHostRequestBody.
        :rtype: int
        """
        return self._protect_status

    @protect_status.setter
    def protect_status(self, protect_status):
        """Sets the protect_status of this UpdatePremiumHostRequestBody.

        防护状态

        :param protect_status: The protect_status of this UpdatePremiumHostRequestBody.
        :type protect_status: int
        """
        self._protect_status = protect_status

    @property
    def access_status(self):
        """Gets the access_status of this UpdatePremiumHostRequestBody.

        接入状态

        :return: The access_status of this UpdatePremiumHostRequestBody.
        :rtype: int
        """
        return self._access_status

    @access_status.setter
    def access_status(self, access_status):
        """Sets the access_status of this UpdatePremiumHostRequestBody.

        接入状态

        :param access_status: The access_status of this UpdatePremiumHostRequestBody.
        :type access_status: int
        """
        self._access_status = access_status

    @property
    def timestamp(self):
        """Gets the timestamp of this UpdatePremiumHostRequestBody.

        时间戳

        :return: The timestamp of this UpdatePremiumHostRequestBody.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this UpdatePremiumHostRequestBody.

        时间戳

        :param timestamp: The timestamp of this UpdatePremiumHostRequestBody.
        :type timestamp: int
        """
        self._timestamp = timestamp

    @property
    def pool_ids(self):
        """Gets the pool_ids of this UpdatePremiumHostRequestBody.

        域名关联的组ID（仅特殊模式需要，如elb）

        :return: The pool_ids of this UpdatePremiumHostRequestBody.
        :rtype: list[str]
        """
        return self._pool_ids

    @pool_ids.setter
    def pool_ids(self, pool_ids):
        """Sets the pool_ids of this UpdatePremiumHostRequestBody.

        域名关联的组ID（仅特殊模式需要，如elb）

        :param pool_ids: The pool_ids of this UpdatePremiumHostRequestBody.
        :type pool_ids: list[str]
        """
        self._pool_ids = pool_ids

    @property
    def block_page(self):
        """Gets the block_page of this UpdatePremiumHostRequestBody.


        :return: The block_page of this UpdatePremiumHostRequestBody.
        :rtype: :class:`huaweicloudsdkwaf.v1.BlockPage`
        """
        return self._block_page

    @block_page.setter
    def block_page(self, block_page):
        """Sets the block_page of this UpdatePremiumHostRequestBody.


        :param block_page: The block_page of this UpdatePremiumHostRequestBody.
        :type block_page: :class:`huaweicloudsdkwaf.v1.BlockPage`
        """
        self._block_page = block_page

    @property
    def traffic_mark(self):
        """Gets the traffic_mark of this UpdatePremiumHostRequestBody.


        :return: The traffic_mark of this UpdatePremiumHostRequestBody.
        :rtype: :class:`huaweicloudsdkwaf.v1.TrafficMark`
        """
        return self._traffic_mark

    @traffic_mark.setter
    def traffic_mark(self, traffic_mark):
        """Sets the traffic_mark of this UpdatePremiumHostRequestBody.


        :param traffic_mark: The traffic_mark of this UpdatePremiumHostRequestBody.
        :type traffic_mark: :class:`huaweicloudsdkwaf.v1.TrafficMark`
        """
        self._traffic_mark = traffic_mark

    @property
    def flag(self):
        """Gets the flag of this UpdatePremiumHostRequestBody.

        域名特殊标识

        :return: The flag of this UpdatePremiumHostRequestBody.
        :rtype: dict(str, str)
        """
        return self._flag

    @flag.setter
    def flag(self, flag):
        """Sets the flag of this UpdatePremiumHostRequestBody.

        域名特殊标识

        :param flag: The flag of this UpdatePremiumHostRequestBody.
        :type flag: dict(str, str)
        """
        self._flag = flag

    @property
    def extend(self):
        """Gets the extend of this UpdatePremiumHostRequestBody.

        可扩展字段

        :return: The extend of this UpdatePremiumHostRequestBody.
        :rtype: dict(str, str)
        """
        return self._extend

    @extend.setter
    def extend(self, extend):
        """Sets the extend of this UpdatePremiumHostRequestBody.

        可扩展字段

        :param extend: The extend of this UpdatePremiumHostRequestBody.
        :type extend: dict(str, str)
        """
        self._extend = extend

    @property
    def circuit_breaker(self):
        """Gets the circuit_breaker of this UpdatePremiumHostRequestBody.


        :return: The circuit_breaker of this UpdatePremiumHostRequestBody.
        :rtype: :class:`huaweicloudsdkwaf.v1.CircuitBreaker`
        """
        return self._circuit_breaker

    @circuit_breaker.setter
    def circuit_breaker(self, circuit_breaker):
        """Sets the circuit_breaker of this UpdatePremiumHostRequestBody.


        :param circuit_breaker: The circuit_breaker of this UpdatePremiumHostRequestBody.
        :type circuit_breaker: :class:`huaweicloudsdkwaf.v1.CircuitBreaker`
        """
        self._circuit_breaker = circuit_breaker

    @property
    def timeout_config(self):
        """Gets the timeout_config of this UpdatePremiumHostRequestBody.


        :return: The timeout_config of this UpdatePremiumHostRequestBody.
        :rtype: :class:`huaweicloudsdkwaf.v1.TimeoutConfig`
        """
        return self._timeout_config

    @timeout_config.setter
    def timeout_config(self, timeout_config):
        """Sets the timeout_config of this UpdatePremiumHostRequestBody.


        :param timeout_config: The timeout_config of this UpdatePremiumHostRequestBody.
        :type timeout_config: :class:`huaweicloudsdkwaf.v1.TimeoutConfig`
        """
        self._timeout_config = timeout_config

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
        if not isinstance(other, UpdatePremiumHostRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
