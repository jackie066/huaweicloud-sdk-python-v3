# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CommitJobReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'sql': 'str',
        'currentdb': 'str',
        'queue_name': 'str',
        'conf': 'list[str]',
        'tags': 'list[JobsTags]'
    }

    attribute_map = {
        'sql': 'sql',
        'currentdb': 'currentdb',
        'queue_name': 'queue_name',
        'conf': 'conf',
        'tags': 'tags'
    }

    def __init__(self, sql=None, currentdb=None, queue_name=None, conf=None, tags=None):
        """CommitJobReq

        The model defined in huaweicloud sdk

        :param sql: 待执行的SQL语句。
        :type sql: str
        :param currentdb: SQL语句执行所在的数据库。当创建新数据库时，不需要提供此参数。
        :type currentdb: str
        :param queue_name: 待提交作业的队列名称，名称只能包含数字、英文字母和下划线，但不能是纯数字，且不能以下划线开头。长度限制：1~128个字符。 说明：  队列名称不区分大小写，系统会自动转换为小写。
        :type queue_name: str
        :param conf: 用户以“key/value”的形式设置用于此作业的配置参数。目前支持的配置项请参考表3。
        :type conf: list[str]
        :param tags: 作业的标签。具体请参考表tags。
        :type tags: list[:class:`huaweicloudsdkdli.v1.JobsTags`]
        """
        
        

        self._sql = None
        self._currentdb = None
        self._queue_name = None
        self._conf = None
        self._tags = None
        self.discriminator = None

        self.sql = sql
        if currentdb is not None:
            self.currentdb = currentdb
        if queue_name is not None:
            self.queue_name = queue_name
        if conf is not None:
            self.conf = conf
        if tags is not None:
            self.tags = tags

    @property
    def sql(self):
        """Gets the sql of this CommitJobReq.

        待执行的SQL语句。

        :return: The sql of this CommitJobReq.
        :rtype: str
        """
        return self._sql

    @sql.setter
    def sql(self, sql):
        """Sets the sql of this CommitJobReq.

        待执行的SQL语句。

        :param sql: The sql of this CommitJobReq.
        :type sql: str
        """
        self._sql = sql

    @property
    def currentdb(self):
        """Gets the currentdb of this CommitJobReq.

        SQL语句执行所在的数据库。当创建新数据库时，不需要提供此参数。

        :return: The currentdb of this CommitJobReq.
        :rtype: str
        """
        return self._currentdb

    @currentdb.setter
    def currentdb(self, currentdb):
        """Sets the currentdb of this CommitJobReq.

        SQL语句执行所在的数据库。当创建新数据库时，不需要提供此参数。

        :param currentdb: The currentdb of this CommitJobReq.
        :type currentdb: str
        """
        self._currentdb = currentdb

    @property
    def queue_name(self):
        """Gets the queue_name of this CommitJobReq.

        待提交作业的队列名称，名称只能包含数字、英文字母和下划线，但不能是纯数字，且不能以下划线开头。长度限制：1~128个字符。 说明：  队列名称不区分大小写，系统会自动转换为小写。

        :return: The queue_name of this CommitJobReq.
        :rtype: str
        """
        return self._queue_name

    @queue_name.setter
    def queue_name(self, queue_name):
        """Sets the queue_name of this CommitJobReq.

        待提交作业的队列名称，名称只能包含数字、英文字母和下划线，但不能是纯数字，且不能以下划线开头。长度限制：1~128个字符。 说明：  队列名称不区分大小写，系统会自动转换为小写。

        :param queue_name: The queue_name of this CommitJobReq.
        :type queue_name: str
        """
        self._queue_name = queue_name

    @property
    def conf(self):
        """Gets the conf of this CommitJobReq.

        用户以“key/value”的形式设置用于此作业的配置参数。目前支持的配置项请参考表3。

        :return: The conf of this CommitJobReq.
        :rtype: list[str]
        """
        return self._conf

    @conf.setter
    def conf(self, conf):
        """Sets the conf of this CommitJobReq.

        用户以“key/value”的形式设置用于此作业的配置参数。目前支持的配置项请参考表3。

        :param conf: The conf of this CommitJobReq.
        :type conf: list[str]
        """
        self._conf = conf

    @property
    def tags(self):
        """Gets the tags of this CommitJobReq.

        作业的标签。具体请参考表tags。

        :return: The tags of this CommitJobReq.
        :rtype: list[:class:`huaweicloudsdkdli.v1.JobsTags`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CommitJobReq.

        作业的标签。具体请参考表tags。

        :param tags: The tags of this CommitJobReq.
        :type tags: list[:class:`huaweicloudsdkdli.v1.JobsTags`]
        """
        self._tags = tags

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
        if not isinstance(other, CommitJobReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
