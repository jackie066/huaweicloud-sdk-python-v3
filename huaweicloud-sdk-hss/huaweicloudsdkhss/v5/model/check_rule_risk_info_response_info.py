# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckRuleRiskInfoResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'severity': 'str',
        'check_type': 'str',
        'standard': 'str',
        'check_rule_name': 'str',
        'check_rule_id': 'str',
        'host_num': 'int',
        'scan_result': 'str',
        'status': 'str'
    }

    attribute_map = {
        'severity': 'severity',
        'check_type': 'check_type',
        'standard': 'standard',
        'check_rule_name': 'check_rule_name',
        'check_rule_id': 'check_rule_id',
        'host_num': 'host_num',
        'scan_result': 'scan_result',
        'status': 'status'
    }

    def __init__(self, severity=None, check_type=None, standard=None, check_rule_name=None, check_rule_id=None, host_num=None, scan_result=None, status=None):
        """CheckRuleRiskInfoResponseInfo

        The model defined in huaweicloud sdk

        :param severity: 风险等级，包含如下:   - Low : 低危   - Medium : 中危   - High : 高危
        :type severity: str
        :param check_type: 基线名称
        :type check_type: str
        :param standard: 标准类型，包含如下:   - cn_standard : 等保合规标准   - hw_standard : 华为标准   - qt_standard : 青腾标准
        :type standard: str
        :param check_rule_name: 检查项
        :type check_rule_name: str
        :param check_rule_id: 检查项ID
        :type check_rule_id: str
        :param host_num: 影响服务器数量
        :type host_num: int
        :param scan_result: 检测结果，包含如下：   - pass   - failed
        :type scan_result: str
        :param status: 状态，包含如下：   - safe : 无需处理   - ignored : 已忽略   - unhandled : 未处理
        :type status: str
        """
        
        

        self._severity = None
        self._check_type = None
        self._standard = None
        self._check_rule_name = None
        self._check_rule_id = None
        self._host_num = None
        self._scan_result = None
        self._status = None
        self.discriminator = None

        if severity is not None:
            self.severity = severity
        if check_type is not None:
            self.check_type = check_type
        if standard is not None:
            self.standard = standard
        if check_rule_name is not None:
            self.check_rule_name = check_rule_name
        if check_rule_id is not None:
            self.check_rule_id = check_rule_id
        if host_num is not None:
            self.host_num = host_num
        if scan_result is not None:
            self.scan_result = scan_result
        if status is not None:
            self.status = status

    @property
    def severity(self):
        """Gets the severity of this CheckRuleRiskInfoResponseInfo.

        风险等级，包含如下:   - Low : 低危   - Medium : 中危   - High : 高危

        :return: The severity of this CheckRuleRiskInfoResponseInfo.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this CheckRuleRiskInfoResponseInfo.

        风险等级，包含如下:   - Low : 低危   - Medium : 中危   - High : 高危

        :param severity: The severity of this CheckRuleRiskInfoResponseInfo.
        :type severity: str
        """
        self._severity = severity

    @property
    def check_type(self):
        """Gets the check_type of this CheckRuleRiskInfoResponseInfo.

        基线名称

        :return: The check_type of this CheckRuleRiskInfoResponseInfo.
        :rtype: str
        """
        return self._check_type

    @check_type.setter
    def check_type(self, check_type):
        """Sets the check_type of this CheckRuleRiskInfoResponseInfo.

        基线名称

        :param check_type: The check_type of this CheckRuleRiskInfoResponseInfo.
        :type check_type: str
        """
        self._check_type = check_type

    @property
    def standard(self):
        """Gets the standard of this CheckRuleRiskInfoResponseInfo.

        标准类型，包含如下:   - cn_standard : 等保合规标准   - hw_standard : 华为标准   - qt_standard : 青腾标准

        :return: The standard of this CheckRuleRiskInfoResponseInfo.
        :rtype: str
        """
        return self._standard

    @standard.setter
    def standard(self, standard):
        """Sets the standard of this CheckRuleRiskInfoResponseInfo.

        标准类型，包含如下:   - cn_standard : 等保合规标准   - hw_standard : 华为标准   - qt_standard : 青腾标准

        :param standard: The standard of this CheckRuleRiskInfoResponseInfo.
        :type standard: str
        """
        self._standard = standard

    @property
    def check_rule_name(self):
        """Gets the check_rule_name of this CheckRuleRiskInfoResponseInfo.

        检查项

        :return: The check_rule_name of this CheckRuleRiskInfoResponseInfo.
        :rtype: str
        """
        return self._check_rule_name

    @check_rule_name.setter
    def check_rule_name(self, check_rule_name):
        """Sets the check_rule_name of this CheckRuleRiskInfoResponseInfo.

        检查项

        :param check_rule_name: The check_rule_name of this CheckRuleRiskInfoResponseInfo.
        :type check_rule_name: str
        """
        self._check_rule_name = check_rule_name

    @property
    def check_rule_id(self):
        """Gets the check_rule_id of this CheckRuleRiskInfoResponseInfo.

        检查项ID

        :return: The check_rule_id of this CheckRuleRiskInfoResponseInfo.
        :rtype: str
        """
        return self._check_rule_id

    @check_rule_id.setter
    def check_rule_id(self, check_rule_id):
        """Sets the check_rule_id of this CheckRuleRiskInfoResponseInfo.

        检查项ID

        :param check_rule_id: The check_rule_id of this CheckRuleRiskInfoResponseInfo.
        :type check_rule_id: str
        """
        self._check_rule_id = check_rule_id

    @property
    def host_num(self):
        """Gets the host_num of this CheckRuleRiskInfoResponseInfo.

        影响服务器数量

        :return: The host_num of this CheckRuleRiskInfoResponseInfo.
        :rtype: int
        """
        return self._host_num

    @host_num.setter
    def host_num(self, host_num):
        """Sets the host_num of this CheckRuleRiskInfoResponseInfo.

        影响服务器数量

        :param host_num: The host_num of this CheckRuleRiskInfoResponseInfo.
        :type host_num: int
        """
        self._host_num = host_num

    @property
    def scan_result(self):
        """Gets the scan_result of this CheckRuleRiskInfoResponseInfo.

        检测结果，包含如下：   - pass   - failed

        :return: The scan_result of this CheckRuleRiskInfoResponseInfo.
        :rtype: str
        """
        return self._scan_result

    @scan_result.setter
    def scan_result(self, scan_result):
        """Sets the scan_result of this CheckRuleRiskInfoResponseInfo.

        检测结果，包含如下：   - pass   - failed

        :param scan_result: The scan_result of this CheckRuleRiskInfoResponseInfo.
        :type scan_result: str
        """
        self._scan_result = scan_result

    @property
    def status(self):
        """Gets the status of this CheckRuleRiskInfoResponseInfo.

        状态，包含如下：   - safe : 无需处理   - ignored : 已忽略   - unhandled : 未处理

        :return: The status of this CheckRuleRiskInfoResponseInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CheckRuleRiskInfoResponseInfo.

        状态，包含如下：   - safe : 无需处理   - ignored : 已忽略   - unhandled : 未处理

        :param status: The status of this CheckRuleRiskInfoResponseInfo.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, CheckRuleRiskInfoResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
