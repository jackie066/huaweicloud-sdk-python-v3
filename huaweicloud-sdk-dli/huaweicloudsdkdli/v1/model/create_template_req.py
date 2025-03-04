# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateTemplateReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'desc': 'str',
        'sql_body': 'str',
        'job_type': 'str',
        'tags': 'list[JobsTags]'
    }

    attribute_map = {
        'name': 'name',
        'desc': 'desc',
        'sql_body': 'sql_body',
        'job_type': 'job_type',
        'tags': 'tags'
    }

    def __init__(self, name=None, desc=None, sql_body=None, job_type=None, tags=None):
        """CreateTemplateReq

        The model defined in huaweicloud sdk

        :param name: 模块名称，长度限制：0-57个字符 。
        :type name: str
        :param desc: 模板描述，长度限制：0-2048个字符。
        :type desc: str
        :param sql_body: Stream SQL语句，至少包含source，query，sink三个部分, 长度限制：0-2048个字符。
        :type sql_body: str
        :param job_type: Flink作业模板类型。默认值为\&quot;flink_sql_job\&quot;，若填写则只能为\&quot;flink_sql_job\&quot;或者\&quot;flink_opensource_sql_job\&quot;。
        :type job_type: str
        :param tags: Flink作业模板的标签。具体请参考表tags。
        :type tags: list[:class:`huaweicloudsdkdli.v1.JobsTags`]
        """
        
        

        self._name = None
        self._desc = None
        self._sql_body = None
        self._job_type = None
        self._tags = None
        self.discriminator = None

        self.name = name
        if desc is not None:
            self.desc = desc
        if sql_body is not None:
            self.sql_body = sql_body
        if job_type is not None:
            self.job_type = job_type
        if tags is not None:
            self.tags = tags

    @property
    def name(self):
        """Gets the name of this CreateTemplateReq.

        模块名称，长度限制：0-57个字符 。

        :return: The name of this CreateTemplateReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateTemplateReq.

        模块名称，长度限制：0-57个字符 。

        :param name: The name of this CreateTemplateReq.
        :type name: str
        """
        self._name = name

    @property
    def desc(self):
        """Gets the desc of this CreateTemplateReq.

        模板描述，长度限制：0-2048个字符。

        :return: The desc of this CreateTemplateReq.
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        """Sets the desc of this CreateTemplateReq.

        模板描述，长度限制：0-2048个字符。

        :param desc: The desc of this CreateTemplateReq.
        :type desc: str
        """
        self._desc = desc

    @property
    def sql_body(self):
        """Gets the sql_body of this CreateTemplateReq.

        Stream SQL语句，至少包含source，query，sink三个部分, 长度限制：0-2048个字符。

        :return: The sql_body of this CreateTemplateReq.
        :rtype: str
        """
        return self._sql_body

    @sql_body.setter
    def sql_body(self, sql_body):
        """Sets the sql_body of this CreateTemplateReq.

        Stream SQL语句，至少包含source，query，sink三个部分, 长度限制：0-2048个字符。

        :param sql_body: The sql_body of this CreateTemplateReq.
        :type sql_body: str
        """
        self._sql_body = sql_body

    @property
    def job_type(self):
        """Gets the job_type of this CreateTemplateReq.

        Flink作业模板类型。默认值为\"flink_sql_job\"，若填写则只能为\"flink_sql_job\"或者\"flink_opensource_sql_job\"。

        :return: The job_type of this CreateTemplateReq.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        """Sets the job_type of this CreateTemplateReq.

        Flink作业模板类型。默认值为\"flink_sql_job\"，若填写则只能为\"flink_sql_job\"或者\"flink_opensource_sql_job\"。

        :param job_type: The job_type of this CreateTemplateReq.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def tags(self):
        """Gets the tags of this CreateTemplateReq.

        Flink作业模板的标签。具体请参考表tags。

        :return: The tags of this CreateTemplateReq.
        :rtype: list[:class:`huaweicloudsdkdli.v1.JobsTags`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateTemplateReq.

        Flink作业模板的标签。具体请参考表tags。

        :param tags: The tags of this CreateTemplateReq.
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
        if not isinstance(other, CreateTemplateReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
