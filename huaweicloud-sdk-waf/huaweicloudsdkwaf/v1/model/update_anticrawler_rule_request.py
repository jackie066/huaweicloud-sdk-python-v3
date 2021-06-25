# coding: utf-8

import pprint
import re

import six





class UpdateAnticrawlerRuleRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'policy_id': 'str',
        'rule_id': 'str',
        'body': 'PolicyAntiCrawlerPutInfo'
    }

    attribute_map = {
        'policy_id': 'policy_id',
        'rule_id': 'rule_id',
        'body': 'body'
    }

    def __init__(self, policy_id=None, rule_id=None, body=None):
        """UpdateAnticrawlerRuleRequest - a model defined in huaweicloud sdk"""
        
        

        self._policy_id = None
        self._rule_id = None
        self._body = None
        self.discriminator = None

        self.policy_id = policy_id
        self.rule_id = rule_id
        if body is not None:
            self.body = body

    @property
    def policy_id(self):
        """Gets the policy_id of this UpdateAnticrawlerRuleRequest.

        policyid

        :return: The policy_id of this UpdateAnticrawlerRuleRequest.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        """Sets the policy_id of this UpdateAnticrawlerRuleRequest.

        policyid

        :param policy_id: The policy_id of this UpdateAnticrawlerRuleRequest.
        :type: str
        """
        self._policy_id = policy_id

    @property
    def rule_id(self):
        """Gets the rule_id of this UpdateAnticrawlerRuleRequest.

        anticrawlerRuleId

        :return: The rule_id of this UpdateAnticrawlerRuleRequest.
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        """Sets the rule_id of this UpdateAnticrawlerRuleRequest.

        anticrawlerRuleId

        :param rule_id: The rule_id of this UpdateAnticrawlerRuleRequest.
        :type: str
        """
        self._rule_id = rule_id

    @property
    def body(self):
        """Gets the body of this UpdateAnticrawlerRuleRequest.


        :return: The body of this UpdateAnticrawlerRuleRequest.
        :rtype: PolicyAntiCrawlerPutInfo
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateAnticrawlerRuleRequest.


        :param body: The body of this UpdateAnticrawlerRuleRequest.
        :type: PolicyAntiCrawlerPutInfo
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
        if not isinstance(other, UpdateAnticrawlerRuleRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
