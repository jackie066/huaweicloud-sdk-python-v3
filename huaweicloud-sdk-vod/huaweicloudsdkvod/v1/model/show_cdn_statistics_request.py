# coding: utf-8

import pprint
import re

import six





class ShowCdnStatisticsRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'start_time': 'str',
        'end_time': 'str',
        'stat_type': 'str',
        'domain': 'str',
        'interval': 'int'
    }

    attribute_map = {
        'start_time': 'start_time',
        'end_time': 'end_time',
        'stat_type': 'stat_type',
        'domain': 'domain',
        'interval': 'interval'
    }

    def __init__(self, start_time=None, end_time=None, stat_type=None, domain=None, interval=None):
        """ShowCdnStatisticsRequest - a model defined in huaweicloud sdk"""
        
        

        self._start_time = None
        self._end_time = None
        self._stat_type = None
        self._domain = None
        self._interval = None
        self.discriminator = None

        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        self.stat_type = stat_type
        self.domain = domain
        if interval is not None:
            self.interval = interval

    @property
    def start_time(self):
        """Gets the start_time of this ShowCdnStatisticsRequest.

        开始时间 

        :return: The start_time of this ShowCdnStatisticsRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ShowCdnStatisticsRequest.

        开始时间 

        :param start_time: The start_time of this ShowCdnStatisticsRequest.
        :type: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ShowCdnStatisticsRequest.

        结束时间 

        :return: The end_time of this ShowCdnStatisticsRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ShowCdnStatisticsRequest.

        结束时间 

        :param end_time: The end_time of this ShowCdnStatisticsRequest.
        :type: str
        """
        self._end_time = end_time

    @property
    def stat_type(self):
        """Gets the stat_type of this ShowCdnStatisticsRequest.

        支持的参数类型 cdn_bw：CDN峰值带宽cdn_flux：CDN流量req_num：请求总数req_hit_rate：请求命中率flux_hit_rate：流量命中率 

        :return: The stat_type of this ShowCdnStatisticsRequest.
        :rtype: str
        """
        return self._stat_type

    @stat_type.setter
    def stat_type(self, stat_type):
        """Sets the stat_type of this ShowCdnStatisticsRequest.

        支持的参数类型 cdn_bw：CDN峰值带宽cdn_flux：CDN流量req_num：请求总数req_hit_rate：请求命中率flux_hit_rate：流量命中率 

        :param stat_type: The stat_type of this ShowCdnStatisticsRequest.
        :type: str
        """
        self._stat_type = stat_type

    @property
    def domain(self):
        """Gets the domain of this ShowCdnStatisticsRequest.

        域名列表，多个域名以逗号（半角）分隔 

        :return: The domain of this ShowCdnStatisticsRequest.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this ShowCdnStatisticsRequest.

        域名列表，多个域名以逗号（半角）分隔 

        :param domain: The domain of this ShowCdnStatisticsRequest.
        :type: str
        """
        self._domain = domain

    @property
    def interval(self):
        """Gets the interval of this ShowCdnStatisticsRequest.

        采样间隔，单位：秒，取值说明： 时间跨度1天：5分钟、1小时、4小时、8小时，分别对应300秒、3600秒、14400秒和28800秒。 时间跨度2~7天：1小时、4小时、8小时、1天，分别对应3600秒、14400秒、28800秒和86400秒。 时间跨度8~31天：4小时、8小时、1天，分别对应14400秒、28800秒和86400秒。 如果不传，默认取对应时间跨度的最小间隔。 

        :return: The interval of this ShowCdnStatisticsRequest.
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this ShowCdnStatisticsRequest.

        采样间隔，单位：秒，取值说明： 时间跨度1天：5分钟、1小时、4小时、8小时，分别对应300秒、3600秒、14400秒和28800秒。 时间跨度2~7天：1小时、4小时、8小时、1天，分别对应3600秒、14400秒、28800秒和86400秒。 时间跨度8~31天：4小时、8小时、1天，分别对应14400秒、28800秒和86400秒。 如果不传，默认取对应时间跨度的最小间隔。 

        :param interval: The interval of this ShowCdnStatisticsRequest.
        :type: int
        """
        self._interval = interval

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
        if not isinstance(other, ShowCdnStatisticsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
