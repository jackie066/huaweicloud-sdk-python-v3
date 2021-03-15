# coding: utf-8

import pprint
import re

import six





class ListRemuxTaskRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'task_id': 'list[str]',
        'status': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'input_bucket': 'str',
        'input_object': 'str',
        'page': 'int',
        'size': 'int'
    }

    attribute_map = {
        'task_id': 'task_id',
        'status': 'status',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'input_bucket': 'input_bucket',
        'input_object': 'input_object',
        'page': 'page',
        'size': 'size'
    }

    def __init__(self, task_id=None, status=None, start_time=None, end_time=None, input_bucket=None, input_object=None, page=None, size=None):
        """ListRemuxTaskRequest - a model defined in huaweicloud sdk"""
        
        

        self._task_id = None
        self._status = None
        self._start_time = None
        self._end_time = None
        self._input_bucket = None
        self._input_object = None
        self._page = None
        self._size = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if status is not None:
            self.status = status
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if input_bucket is not None:
            self.input_bucket = input_bucket
        if input_object is not None:
            self.input_object = input_object
        if page is not None:
            self.page = page
        if size is not None:
            self.size = size

    @property
    def task_id(self):
        """Gets the task_id of this ListRemuxTaskRequest.


        :return: The task_id of this ListRemuxTaskRequest.
        :rtype: list[str]
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this ListRemuxTaskRequest.


        :param task_id: The task_id of this ListRemuxTaskRequest.
        :type: list[str]
        """
        self._task_id = task_id

    @property
    def status(self):
        """Gets the status of this ListRemuxTaskRequest.


        :return: The status of this ListRemuxTaskRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListRemuxTaskRequest.


        :param status: The status of this ListRemuxTaskRequest.
        :type: str
        """
        self._status = status

    @property
    def start_time(self):
        """Gets the start_time of this ListRemuxTaskRequest.


        :return: The start_time of this ListRemuxTaskRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ListRemuxTaskRequest.


        :param start_time: The start_time of this ListRemuxTaskRequest.
        :type: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ListRemuxTaskRequest.


        :return: The end_time of this ListRemuxTaskRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListRemuxTaskRequest.


        :param end_time: The end_time of this ListRemuxTaskRequest.
        :type: str
        """
        self._end_time = end_time

    @property
    def input_bucket(self):
        """Gets the input_bucket of this ListRemuxTaskRequest.


        :return: The input_bucket of this ListRemuxTaskRequest.
        :rtype: str
        """
        return self._input_bucket

    @input_bucket.setter
    def input_bucket(self, input_bucket):
        """Sets the input_bucket of this ListRemuxTaskRequest.


        :param input_bucket: The input_bucket of this ListRemuxTaskRequest.
        :type: str
        """
        self._input_bucket = input_bucket

    @property
    def input_object(self):
        """Gets the input_object of this ListRemuxTaskRequest.


        :return: The input_object of this ListRemuxTaskRequest.
        :rtype: str
        """
        return self._input_object

    @input_object.setter
    def input_object(self, input_object):
        """Sets the input_object of this ListRemuxTaskRequest.


        :param input_object: The input_object of this ListRemuxTaskRequest.
        :type: str
        """
        self._input_object = input_object

    @property
    def page(self):
        """Gets the page of this ListRemuxTaskRequest.


        :return: The page of this ListRemuxTaskRequest.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this ListRemuxTaskRequest.


        :param page: The page of this ListRemuxTaskRequest.
        :type: int
        """
        self._page = page

    @property
    def size(self):
        """Gets the size of this ListRemuxTaskRequest.


        :return: The size of this ListRemuxTaskRequest.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ListRemuxTaskRequest.


        :param size: The size of this ListRemuxTaskRequest.
        :type: int
        """
        self._size = size

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
        if not isinstance(other, ListRemuxTaskRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
