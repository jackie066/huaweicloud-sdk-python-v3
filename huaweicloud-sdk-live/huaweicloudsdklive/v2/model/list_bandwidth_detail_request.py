# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListBandwidthDetailRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'play_domains': 'list[str]',
        'app': 'str',
        'stream': 'str',
        'country': 'list[str]',
        'region': 'list[str]',
        'isp': 'list[str]',
        'protocol': 'str',
        'interval': 'int',
        'start_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'play_domains': 'play_domains',
        'app': 'app',
        'stream': 'stream',
        'country': 'country',
        'region': 'region',
        'isp': 'isp',
        'protocol': 'protocol',
        'interval': 'interval',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, play_domains=None, app=None, stream=None, country=None, region=None, isp=None, protocol=None, interval=None, start_time=None, end_time=None):
        """ListBandwidthDetailRequest

        The model defined in huaweicloud sdk

        :param play_domains: 播放域名列表，最多支持查询100个域名，多个域名以逗号分隔。 
        :type play_domains: list[str]
        :param app: 应用名称。
        :type app: str
        :param stream: 流名。
        :type stream: str
        :param country: 国家列表。具体取值请参考[国家名称缩写](vod_08_0172.xml)，不填写查询所有国家。 
        :type country: list[str]
        :param region: 区域列表。具体取值请参考[省份名称缩写](live_03_0043.xml)，不填写查询所有区域。 
        :type region: list[str]
        :param isp: 运营商列表，取值如下： - CMCC ：移动 - CTCC ：电信 - CUCC ：联通 - OTHER ：其他  不填写查询所有运营商。 
        :type isp: list[str]
        :param protocol: 请求协议
        :type protocol: str
        :param interval: 查询数据的时间粒度。支持300（默认值）, 3600和86400秒。不传值时，使用默认值300秒。 
        :type interval: int
        :param start_time: 起始时间。日期格式按照ISO8601表示法，并使用UTC时间。  格式为：YYYY-MM-DDThh:mm:ssZ。最大查询跨度31天，最大查询周期一年。  若参数为空，默认查询7天数据。 
        :type start_time: str
        :param end_time: 结束时间。日期格式按照ISO8601表示法，并使用UTC时间。  格式为：YYYY-MM-DDThh:mm:ssZ。  若参数为空，默认为当前时间。结束时间需大于起始时间。 
        :type end_time: str
        """
        
        

        self._play_domains = None
        self._app = None
        self._stream = None
        self._country = None
        self._region = None
        self._isp = None
        self._protocol = None
        self._interval = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        self.play_domains = play_domains
        if app is not None:
            self.app = app
        if stream is not None:
            self.stream = stream
        if country is not None:
            self.country = country
        if region is not None:
            self.region = region
        if isp is not None:
            self.isp = isp
        if protocol is not None:
            self.protocol = protocol
        if interval is not None:
            self.interval = interval
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def play_domains(self):
        """Gets the play_domains of this ListBandwidthDetailRequest.

        播放域名列表，最多支持查询100个域名，多个域名以逗号分隔。 

        :return: The play_domains of this ListBandwidthDetailRequest.
        :rtype: list[str]
        """
        return self._play_domains

    @play_domains.setter
    def play_domains(self, play_domains):
        """Sets the play_domains of this ListBandwidthDetailRequest.

        播放域名列表，最多支持查询100个域名，多个域名以逗号分隔。 

        :param play_domains: The play_domains of this ListBandwidthDetailRequest.
        :type play_domains: list[str]
        """
        self._play_domains = play_domains

    @property
    def app(self):
        """Gets the app of this ListBandwidthDetailRequest.

        应用名称。

        :return: The app of this ListBandwidthDetailRequest.
        :rtype: str
        """
        return self._app

    @app.setter
    def app(self, app):
        """Sets the app of this ListBandwidthDetailRequest.

        应用名称。

        :param app: The app of this ListBandwidthDetailRequest.
        :type app: str
        """
        self._app = app

    @property
    def stream(self):
        """Gets the stream of this ListBandwidthDetailRequest.

        流名。

        :return: The stream of this ListBandwidthDetailRequest.
        :rtype: str
        """
        return self._stream

    @stream.setter
    def stream(self, stream):
        """Sets the stream of this ListBandwidthDetailRequest.

        流名。

        :param stream: The stream of this ListBandwidthDetailRequest.
        :type stream: str
        """
        self._stream = stream

    @property
    def country(self):
        """Gets the country of this ListBandwidthDetailRequest.

        国家列表。具体取值请参考[国家名称缩写](vod_08_0172.xml)，不填写查询所有国家。 

        :return: The country of this ListBandwidthDetailRequest.
        :rtype: list[str]
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this ListBandwidthDetailRequest.

        国家列表。具体取值请参考[国家名称缩写](vod_08_0172.xml)，不填写查询所有国家。 

        :param country: The country of this ListBandwidthDetailRequest.
        :type country: list[str]
        """
        self._country = country

    @property
    def region(self):
        """Gets the region of this ListBandwidthDetailRequest.

        区域列表。具体取值请参考[省份名称缩写](live_03_0043.xml)，不填写查询所有区域。 

        :return: The region of this ListBandwidthDetailRequest.
        :rtype: list[str]
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this ListBandwidthDetailRequest.

        区域列表。具体取值请参考[省份名称缩写](live_03_0043.xml)，不填写查询所有区域。 

        :param region: The region of this ListBandwidthDetailRequest.
        :type region: list[str]
        """
        self._region = region

    @property
    def isp(self):
        """Gets the isp of this ListBandwidthDetailRequest.

        运营商列表，取值如下： - CMCC ：移动 - CTCC ：电信 - CUCC ：联通 - OTHER ：其他  不填写查询所有运营商。 

        :return: The isp of this ListBandwidthDetailRequest.
        :rtype: list[str]
        """
        return self._isp

    @isp.setter
    def isp(self, isp):
        """Sets the isp of this ListBandwidthDetailRequest.

        运营商列表，取值如下： - CMCC ：移动 - CTCC ：电信 - CUCC ：联通 - OTHER ：其他  不填写查询所有运营商。 

        :param isp: The isp of this ListBandwidthDetailRequest.
        :type isp: list[str]
        """
        self._isp = isp

    @property
    def protocol(self):
        """Gets the protocol of this ListBandwidthDetailRequest.

        请求协议

        :return: The protocol of this ListBandwidthDetailRequest.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this ListBandwidthDetailRequest.

        请求协议

        :param protocol: The protocol of this ListBandwidthDetailRequest.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def interval(self):
        """Gets the interval of this ListBandwidthDetailRequest.

        查询数据的时间粒度。支持300（默认值）, 3600和86400秒。不传值时，使用默认值300秒。 

        :return: The interval of this ListBandwidthDetailRequest.
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this ListBandwidthDetailRequest.

        查询数据的时间粒度。支持300（默认值）, 3600和86400秒。不传值时，使用默认值300秒。 

        :param interval: The interval of this ListBandwidthDetailRequest.
        :type interval: int
        """
        self._interval = interval

    @property
    def start_time(self):
        """Gets the start_time of this ListBandwidthDetailRequest.

        起始时间。日期格式按照ISO8601表示法，并使用UTC时间。  格式为：YYYY-MM-DDThh:mm:ssZ。最大查询跨度31天，最大查询周期一年。  若参数为空，默认查询7天数据。 

        :return: The start_time of this ListBandwidthDetailRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ListBandwidthDetailRequest.

        起始时间。日期格式按照ISO8601表示法，并使用UTC时间。  格式为：YYYY-MM-DDThh:mm:ssZ。最大查询跨度31天，最大查询周期一年。  若参数为空，默认查询7天数据。 

        :param start_time: The start_time of this ListBandwidthDetailRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ListBandwidthDetailRequest.

        结束时间。日期格式按照ISO8601表示法，并使用UTC时间。  格式为：YYYY-MM-DDThh:mm:ssZ。  若参数为空，默认为当前时间。结束时间需大于起始时间。 

        :return: The end_time of this ListBandwidthDetailRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListBandwidthDetailRequest.

        结束时间。日期格式按照ISO8601表示法，并使用UTC时间。  格式为：YYYY-MM-DDThh:mm:ssZ。  若参数为空，默认为当前时间。结束时间需大于起始时间。 

        :param end_time: The end_time of this ListBandwidthDetailRequest.
        :type end_time: str
        """
        self._end_time = end_time

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
        if not isinstance(other, ListBandwidthDetailRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
