# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ShowBugsPerDeveloperResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'dividend_value': 'str',
        'divisor_value': 'str',
        'metric_name': 'str',
        'metric_value': 'str',
        'project_id': 'str',
        'project_name': 'str'
    }

    attribute_map = {
        'dividend_value': 'dividend_value',
        'divisor_value': 'divisor_value',
        'metric_name': 'metric_name',
        'metric_value': 'metric_value',
        'project_id': 'project_id',
        'project_name': 'project_name'
    }

    def __init__(self, dividend_value=None, divisor_value=None, metric_name=None, metric_value=None, project_id=None, project_name=None):
        """ShowBugsPerDeveloperResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._dividend_value = None
        self._divisor_value = None
        self._metric_name = None
        self._metric_value = None
        self._project_id = None
        self._project_name = None
        self.discriminator = None

        if dividend_value is not None:
            self.dividend_value = dividend_value
        if divisor_value is not None:
            self.divisor_value = divisor_value
        if metric_name is not None:
            self.metric_name = metric_name
        if metric_value is not None:
            self.metric_value = metric_value
        if project_id is not None:
            self.project_id = project_id
        if project_name is not None:
            self.project_name = project_name

    @property
    def dividend_value(self):
        """Gets the dividend_value of this ShowBugsPerDeveloperResponse.

        指标分子数值

        :return: The dividend_value of this ShowBugsPerDeveloperResponse.
        :rtype: str
        """
        return self._dividend_value

    @dividend_value.setter
    def dividend_value(self, dividend_value):
        """Sets the dividend_value of this ShowBugsPerDeveloperResponse.

        指标分子数值

        :param dividend_value: The dividend_value of this ShowBugsPerDeveloperResponse.
        :type: str
        """
        self._dividend_value = dividend_value

    @property
    def divisor_value(self):
        """Gets the divisor_value of this ShowBugsPerDeveloperResponse.

        指标分母数值

        :return: The divisor_value of this ShowBugsPerDeveloperResponse.
        :rtype: str
        """
        return self._divisor_value

    @divisor_value.setter
    def divisor_value(self, divisor_value):
        """Sets the divisor_value of this ShowBugsPerDeveloperResponse.

        指标分母数值

        :param divisor_value: The divisor_value of this ShowBugsPerDeveloperResponse.
        :type: str
        """
        self._divisor_value = divisor_value

    @property
    def metric_name(self):
        """Gets the metric_name of this ShowBugsPerDeveloperResponse.

        指标名称

        :return: The metric_name of this ShowBugsPerDeveloperResponse.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        """Sets the metric_name of this ShowBugsPerDeveloperResponse.

        指标名称

        :param metric_name: The metric_name of this ShowBugsPerDeveloperResponse.
        :type: str
        """
        self._metric_name = metric_name

    @property
    def metric_value(self):
        """Gets the metric_value of this ShowBugsPerDeveloperResponse.

        指标数值

        :return: The metric_value of this ShowBugsPerDeveloperResponse.
        :rtype: str
        """
        return self._metric_value

    @metric_value.setter
    def metric_value(self, metric_value):
        """Sets the metric_value of this ShowBugsPerDeveloperResponse.

        指标数值

        :param metric_value: The metric_value of this ShowBugsPerDeveloperResponse.
        :type: str
        """
        self._metric_value = metric_value

    @property
    def project_id(self):
        """Gets the project_id of this ShowBugsPerDeveloperResponse.

        项目ID

        :return: The project_id of this ShowBugsPerDeveloperResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ShowBugsPerDeveloperResponse.

        项目ID

        :param project_id: The project_id of this ShowBugsPerDeveloperResponse.
        :type: str
        """
        self._project_id = project_id

    @property
    def project_name(self):
        """Gets the project_name of this ShowBugsPerDeveloperResponse.

        项目名称

        :return: The project_name of this ShowBugsPerDeveloperResponse.
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this ShowBugsPerDeveloperResponse.

        项目名称

        :param project_name: The project_name of this ShowBugsPerDeveloperResponse.
        :type: str
        """
        self._project_name = project_name

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
        if not isinstance(other, ShowBugsPerDeveloperResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
