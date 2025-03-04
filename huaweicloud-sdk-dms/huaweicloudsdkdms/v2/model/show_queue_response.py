# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowQueueResponse(SdkResponse):

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
        'created': 'int',
        'description': 'str',
        'queue_mode': 'str',
        'reservation': 'int',
        'max_msg_size_byte': 'int',
        'produced_messages': 'int',
        'redrive_policy': 'str',
        'max_consume_count': 'int',
        'group_count': 'int',
        'kafka_topic': 'str',
        'eff_date': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'created': 'created',
        'description': 'description',
        'queue_mode': 'queue_mode',
        'reservation': 'reservation',
        'max_msg_size_byte': 'max_msg_size_byte',
        'produced_messages': 'produced_messages',
        'redrive_policy': 'redrive_policy',
        'max_consume_count': 'max_consume_count',
        'group_count': 'group_count',
        'kafka_topic': 'kafka_topic',
        'eff_date': 'eff_date'
    }

    def __init__(self, id=None, name=None, created=None, description=None, queue_mode=None, reservation=None, max_msg_size_byte=None, produced_messages=None, redrive_policy=None, max_consume_count=None, group_count=None, kafka_topic=None, eff_date=None):
        """ShowQueueResponse

        The model defined in huaweicloud sdk

        :param id: 队列ID。
        :type id: str
        :param name: 队列的名称。
        :type name: str
        :param created: 创建队列的时间。
        :type created: int
        :param description: 队列的描述信息。
        :type description: str
        :param queue_mode: 队列类型。
        :type queue_mode: str
        :param reservation: 消息在队列中允许保留的时长（单位分钟）。
        :type reservation: int
        :param max_msg_size_byte: 队列中允许的最大消息大小（单位Byte）。
        :type max_msg_size_byte: int
        :param produced_messages: 队列的消息总数。
        :type produced_messages: int
        :param redrive_policy: 该队列是否开启死信消息。仅当include_deadletter为true时，才有该响应参数。 - enable：表示开启。 - disable：表示不开启。
        :type redrive_policy: str
        :param max_consume_count: 最大确认消费失败的次数，当达到最大确认失败次数后，DMS会将该条消息转存到死信队列中。 仅当include_deadletter为true时，才有该响应参数。
        :type max_consume_count: int
        :param group_count: 该队列下的消费组数量。
        :type group_count: int
        :param kafka_topic: 仅Kafka队列才有该参数。
        :type kafka_topic: str
        :param eff_date: 创建队列的时间。
        :type eff_date: int
        """
        
        super(ShowQueueResponse, self).__init__()

        self._id = None
        self._name = None
        self._created = None
        self._description = None
        self._queue_mode = None
        self._reservation = None
        self._max_msg_size_byte = None
        self._produced_messages = None
        self._redrive_policy = None
        self._max_consume_count = None
        self._group_count = None
        self._kafka_topic = None
        self._eff_date = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if created is not None:
            self.created = created
        if description is not None:
            self.description = description
        if queue_mode is not None:
            self.queue_mode = queue_mode
        if reservation is not None:
            self.reservation = reservation
        if max_msg_size_byte is not None:
            self.max_msg_size_byte = max_msg_size_byte
        if produced_messages is not None:
            self.produced_messages = produced_messages
        if redrive_policy is not None:
            self.redrive_policy = redrive_policy
        if max_consume_count is not None:
            self.max_consume_count = max_consume_count
        if group_count is not None:
            self.group_count = group_count
        if kafka_topic is not None:
            self.kafka_topic = kafka_topic
        if eff_date is not None:
            self.eff_date = eff_date

    @property
    def id(self):
        """Gets the id of this ShowQueueResponse.

        队列ID。

        :return: The id of this ShowQueueResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowQueueResponse.

        队列ID。

        :param id: The id of this ShowQueueResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ShowQueueResponse.

        队列的名称。

        :return: The name of this ShowQueueResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowQueueResponse.

        队列的名称。

        :param name: The name of this ShowQueueResponse.
        :type name: str
        """
        self._name = name

    @property
    def created(self):
        """Gets the created of this ShowQueueResponse.

        创建队列的时间。

        :return: The created of this ShowQueueResponse.
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this ShowQueueResponse.

        创建队列的时间。

        :param created: The created of this ShowQueueResponse.
        :type created: int
        """
        self._created = created

    @property
    def description(self):
        """Gets the description of this ShowQueueResponse.

        队列的描述信息。

        :return: The description of this ShowQueueResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ShowQueueResponse.

        队列的描述信息。

        :param description: The description of this ShowQueueResponse.
        :type description: str
        """
        self._description = description

    @property
    def queue_mode(self):
        """Gets the queue_mode of this ShowQueueResponse.

        队列类型。

        :return: The queue_mode of this ShowQueueResponse.
        :rtype: str
        """
        return self._queue_mode

    @queue_mode.setter
    def queue_mode(self, queue_mode):
        """Sets the queue_mode of this ShowQueueResponse.

        队列类型。

        :param queue_mode: The queue_mode of this ShowQueueResponse.
        :type queue_mode: str
        """
        self._queue_mode = queue_mode

    @property
    def reservation(self):
        """Gets the reservation of this ShowQueueResponse.

        消息在队列中允许保留的时长（单位分钟）。

        :return: The reservation of this ShowQueueResponse.
        :rtype: int
        """
        return self._reservation

    @reservation.setter
    def reservation(self, reservation):
        """Sets the reservation of this ShowQueueResponse.

        消息在队列中允许保留的时长（单位分钟）。

        :param reservation: The reservation of this ShowQueueResponse.
        :type reservation: int
        """
        self._reservation = reservation

    @property
    def max_msg_size_byte(self):
        """Gets the max_msg_size_byte of this ShowQueueResponse.

        队列中允许的最大消息大小（单位Byte）。

        :return: The max_msg_size_byte of this ShowQueueResponse.
        :rtype: int
        """
        return self._max_msg_size_byte

    @max_msg_size_byte.setter
    def max_msg_size_byte(self, max_msg_size_byte):
        """Sets the max_msg_size_byte of this ShowQueueResponse.

        队列中允许的最大消息大小（单位Byte）。

        :param max_msg_size_byte: The max_msg_size_byte of this ShowQueueResponse.
        :type max_msg_size_byte: int
        """
        self._max_msg_size_byte = max_msg_size_byte

    @property
    def produced_messages(self):
        """Gets the produced_messages of this ShowQueueResponse.

        队列的消息总数。

        :return: The produced_messages of this ShowQueueResponse.
        :rtype: int
        """
        return self._produced_messages

    @produced_messages.setter
    def produced_messages(self, produced_messages):
        """Sets the produced_messages of this ShowQueueResponse.

        队列的消息总数。

        :param produced_messages: The produced_messages of this ShowQueueResponse.
        :type produced_messages: int
        """
        self._produced_messages = produced_messages

    @property
    def redrive_policy(self):
        """Gets the redrive_policy of this ShowQueueResponse.

        该队列是否开启死信消息。仅当include_deadletter为true时，才有该响应参数。 - enable：表示开启。 - disable：表示不开启。

        :return: The redrive_policy of this ShowQueueResponse.
        :rtype: str
        """
        return self._redrive_policy

    @redrive_policy.setter
    def redrive_policy(self, redrive_policy):
        """Sets the redrive_policy of this ShowQueueResponse.

        该队列是否开启死信消息。仅当include_deadletter为true时，才有该响应参数。 - enable：表示开启。 - disable：表示不开启。

        :param redrive_policy: The redrive_policy of this ShowQueueResponse.
        :type redrive_policy: str
        """
        self._redrive_policy = redrive_policy

    @property
    def max_consume_count(self):
        """Gets the max_consume_count of this ShowQueueResponse.

        最大确认消费失败的次数，当达到最大确认失败次数后，DMS会将该条消息转存到死信队列中。 仅当include_deadletter为true时，才有该响应参数。

        :return: The max_consume_count of this ShowQueueResponse.
        :rtype: int
        """
        return self._max_consume_count

    @max_consume_count.setter
    def max_consume_count(self, max_consume_count):
        """Sets the max_consume_count of this ShowQueueResponse.

        最大确认消费失败的次数，当达到最大确认失败次数后，DMS会将该条消息转存到死信队列中。 仅当include_deadletter为true时，才有该响应参数。

        :param max_consume_count: The max_consume_count of this ShowQueueResponse.
        :type max_consume_count: int
        """
        self._max_consume_count = max_consume_count

    @property
    def group_count(self):
        """Gets the group_count of this ShowQueueResponse.

        该队列下的消费组数量。

        :return: The group_count of this ShowQueueResponse.
        :rtype: int
        """
        return self._group_count

    @group_count.setter
    def group_count(self, group_count):
        """Sets the group_count of this ShowQueueResponse.

        该队列下的消费组数量。

        :param group_count: The group_count of this ShowQueueResponse.
        :type group_count: int
        """
        self._group_count = group_count

    @property
    def kafka_topic(self):
        """Gets the kafka_topic of this ShowQueueResponse.

        仅Kafka队列才有该参数。

        :return: The kafka_topic of this ShowQueueResponse.
        :rtype: str
        """
        return self._kafka_topic

    @kafka_topic.setter
    def kafka_topic(self, kafka_topic):
        """Sets the kafka_topic of this ShowQueueResponse.

        仅Kafka队列才有该参数。

        :param kafka_topic: The kafka_topic of this ShowQueueResponse.
        :type kafka_topic: str
        """
        self._kafka_topic = kafka_topic

    @property
    def eff_date(self):
        """Gets the eff_date of this ShowQueueResponse.

        创建队列的时间。

        :return: The eff_date of this ShowQueueResponse.
        :rtype: int
        """
        return self._eff_date

    @eff_date.setter
    def eff_date(self, eff_date):
        """Sets the eff_date of this ShowQueueResponse.

        创建队列的时间。

        :param eff_date: The eff_date of this ShowQueueResponse.
        :type eff_date: int
        """
        self._eff_date = eff_date

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
        if not isinstance(other, ShowQueueResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
