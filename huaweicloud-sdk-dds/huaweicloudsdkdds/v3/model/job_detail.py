# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobDetail:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'created': 'str',
        'ended': 'str',
        'progress': 'str',
        'instance': 'JobInstanceInfo'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'created': 'created',
        'ended': 'ended',
        'progress': 'progress',
        'instance': 'instance'
    }

    def __init__(self, id=None, name=None, created=None, ended=None, progress=None, instance=None):
        """JobDetail - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._name = None
        self._created = None
        self._ended = None
        self._progress = None
        self._instance = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.created = created
        self.ended = ended
        self.progress = progress
        self.instance = instance

    @property
    def id(self):
        """Gets the id of this JobDetail.

        任务ID

        :return: The id of this JobDetail.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this JobDetail.

        任务ID

        :param id: The id of this JobDetail.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this JobDetail.

        任务名称。

        :return: The name of this JobDetail.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this JobDetail.

        任务名称。

        :param name: The name of this JobDetail.
        :type: str
        """
        self._name = name

    @property
    def created(self):
        """Gets the created of this JobDetail.

        任务创建时间，格式为yyyy-mm-ddThh:mm:ssZ。

        :return: The created of this JobDetail.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this JobDetail.

        任务创建时间，格式为yyyy-mm-ddThh:mm:ssZ。

        :param created: The created of this JobDetail.
        :type: str
        """
        self._created = created

    @property
    def ended(self):
        """Gets the ended of this JobDetail.

        任务结束时间，格式为yyyy-mm-ddThh:mm:ssZ。

        :return: The ended of this JobDetail.
        :rtype: str
        """
        return self._ended

    @ended.setter
    def ended(self, ended):
        """Sets the ended of this JobDetail.

        任务结束时间，格式为yyyy-mm-ddThh:mm:ssZ。

        :param ended: The ended of this JobDetail.
        :type: str
        """
        self._ended = ended

    @property
    def progress(self):
        """Gets the progress of this JobDetail.

        任务执行进度。

        :return: The progress of this JobDetail.
        :rtype: str
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this JobDetail.

        任务执行进度。

        :param progress: The progress of this JobDetail.
        :type: str
        """
        self._progress = progress

    @property
    def instance(self):
        """Gets the instance of this JobDetail.


        :return: The instance of this JobDetail.
        :rtype: JobInstanceInfo
        """
        return self._instance

    @instance.setter
    def instance(self, instance):
        """Sets the instance of this JobDetail.


        :param instance: The instance of this JobDetail.
        :type: JobInstanceInfo
        """
        self._instance = instance

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
        if not isinstance(other, JobDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
