# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateMysqlReadonlyNodeResponse(SdkResponse):


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
        'node_names': 'list[str]',
        'job_id': 'str',
        'order_id': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'node_names': 'node_names',
        'job_id': 'job_id',
        'order_id': 'order_id'
    }

    def __init__(self, instance_id=None, node_names=None, job_id=None, order_id=None):
        """CreateMysqlReadonlyNodeResponse - a model defined in huaweicloud sdk"""
        
        super(CreateMysqlReadonlyNodeResponse, self).__init__()

        self._instance_id = None
        self._node_names = None
        self._job_id = None
        self._order_id = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if node_names is not None:
            self.node_names = node_names
        if job_id is not None:
            self.job_id = job_id
        if order_id is not None:
            self.order_id = order_id

    @property
    def instance_id(self):
        """Gets the instance_id of this CreateMysqlReadonlyNodeResponse.

        实例ID。

        :return: The instance_id of this CreateMysqlReadonlyNodeResponse.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this CreateMysqlReadonlyNodeResponse.

        实例ID。

        :param instance_id: The instance_id of this CreateMysqlReadonlyNodeResponse.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def node_names(self):
        """Gets the node_names of this CreateMysqlReadonlyNodeResponse.

        节点名称列表。

        :return: The node_names of this CreateMysqlReadonlyNodeResponse.
        :rtype: list[str]
        """
        return self._node_names

    @node_names.setter
    def node_names(self, node_names):
        """Sets the node_names of this CreateMysqlReadonlyNodeResponse.

        节点名称列表。

        :param node_names: The node_names of this CreateMysqlReadonlyNodeResponse.
        :type: list[str]
        """
        self._node_names = node_names

    @property
    def job_id(self):
        """Gets the job_id of this CreateMysqlReadonlyNodeResponse.

        实例创建的任务id。  仅创建按需实例时会返回该参数。

        :return: The job_id of this CreateMysqlReadonlyNodeResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this CreateMysqlReadonlyNodeResponse.

        实例创建的任务id。  仅创建按需实例时会返回该参数。

        :param job_id: The job_id of this CreateMysqlReadonlyNodeResponse.
        :type: str
        """
        self._job_id = job_id

    @property
    def order_id(self):
        """Gets the order_id of this CreateMysqlReadonlyNodeResponse.

        订单号，创建包年包月时返回该参数。

        :return: The order_id of this CreateMysqlReadonlyNodeResponse.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this CreateMysqlReadonlyNodeResponse.

        订单号，创建包年包月时返回该参数。

        :param order_id: The order_id of this CreateMysqlReadonlyNodeResponse.
        :type: str
        """
        self._order_id = order_id

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
        if not isinstance(other, CreateMysqlReadonlyNodeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
