# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTaskResqTaskinfoCaseList:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'case_id': 'int',
        'case_name': 'str',
        'case_type': 'int',
        'contents': 'list[ShowTaskResqTaskinfoContents]',
        'for_loop_params': 'list[object]',
        'increase_setting': 'list[object]',
        'stages': 'list[object]',
        'status': 'int',
        'temp_id': 'int'
    }

    attribute_map = {
        'case_id': 'case_id',
        'case_name': 'case_name',
        'case_type': 'case_type',
        'contents': 'contents',
        'for_loop_params': 'for_loop_params',
        'increase_setting': 'increase_setting',
        'stages': 'stages',
        'status': 'status',
        'temp_id': 'temp_id'
    }

    def __init__(self, case_id=None, case_name=None, case_type=None, contents=None, for_loop_params=None, increase_setting=None, stages=None, status=None, temp_id=None):
        """ShowTaskResqTaskinfoCaseList - a model defined in huaweicloud sdk"""
        
        

        self._case_id = None
        self._case_name = None
        self._case_type = None
        self._contents = None
        self._for_loop_params = None
        self._increase_setting = None
        self._stages = None
        self._status = None
        self._temp_id = None
        self.discriminator = None

        if case_id is not None:
            self.case_id = case_id
        if case_name is not None:
            self.case_name = case_name
        if case_type is not None:
            self.case_type = case_type
        if contents is not None:
            self.contents = contents
        if for_loop_params is not None:
            self.for_loop_params = for_loop_params
        if increase_setting is not None:
            self.increase_setting = increase_setting
        if stages is not None:
            self.stages = stages
        if status is not None:
            self.status = status
        if temp_id is not None:
            self.temp_id = temp_id

    @property
    def case_id(self):
        """Gets the case_id of this ShowTaskResqTaskinfoCaseList.

        case_id

        :return: The case_id of this ShowTaskResqTaskinfoCaseList.
        :rtype: int
        """
        return self._case_id

    @case_id.setter
    def case_id(self, case_id):
        """Sets the case_id of this ShowTaskResqTaskinfoCaseList.

        case_id

        :param case_id: The case_id of this ShowTaskResqTaskinfoCaseList.
        :type: int
        """
        self._case_id = case_id

    @property
    def case_name(self):
        """Gets the case_name of this ShowTaskResqTaskinfoCaseList.

        case_name

        :return: The case_name of this ShowTaskResqTaskinfoCaseList.
        :rtype: str
        """
        return self._case_name

    @case_name.setter
    def case_name(self, case_name):
        """Sets the case_name of this ShowTaskResqTaskinfoCaseList.

        case_name

        :param case_name: The case_name of this ShowTaskResqTaskinfoCaseList.
        :type: str
        """
        self._case_name = case_name

    @property
    def case_type(self):
        """Gets the case_type of this ShowTaskResqTaskinfoCaseList.

        case_type

        :return: The case_type of this ShowTaskResqTaskinfoCaseList.
        :rtype: int
        """
        return self._case_type

    @case_type.setter
    def case_type(self, case_type):
        """Sets the case_type of this ShowTaskResqTaskinfoCaseList.

        case_type

        :param case_type: The case_type of this ShowTaskResqTaskinfoCaseList.
        :type: int
        """
        self._case_type = case_type

    @property
    def contents(self):
        """Gets the contents of this ShowTaskResqTaskinfoCaseList.

        contents

        :return: The contents of this ShowTaskResqTaskinfoCaseList.
        :rtype: list[ShowTaskResqTaskinfoContents]
        """
        return self._contents

    @contents.setter
    def contents(self, contents):
        """Sets the contents of this ShowTaskResqTaskinfoCaseList.

        contents

        :param contents: The contents of this ShowTaskResqTaskinfoCaseList.
        :type: list[ShowTaskResqTaskinfoContents]
        """
        self._contents = contents

    @property
    def for_loop_params(self):
        """Gets the for_loop_params of this ShowTaskResqTaskinfoCaseList.

        for_loop_params

        :return: The for_loop_params of this ShowTaskResqTaskinfoCaseList.
        :rtype: list[object]
        """
        return self._for_loop_params

    @for_loop_params.setter
    def for_loop_params(self, for_loop_params):
        """Sets the for_loop_params of this ShowTaskResqTaskinfoCaseList.

        for_loop_params

        :param for_loop_params: The for_loop_params of this ShowTaskResqTaskinfoCaseList.
        :type: list[object]
        """
        self._for_loop_params = for_loop_params

    @property
    def increase_setting(self):
        """Gets the increase_setting of this ShowTaskResqTaskinfoCaseList.

        increase_setting

        :return: The increase_setting of this ShowTaskResqTaskinfoCaseList.
        :rtype: list[object]
        """
        return self._increase_setting

    @increase_setting.setter
    def increase_setting(self, increase_setting):
        """Sets the increase_setting of this ShowTaskResqTaskinfoCaseList.

        increase_setting

        :param increase_setting: The increase_setting of this ShowTaskResqTaskinfoCaseList.
        :type: list[object]
        """
        self._increase_setting = increase_setting

    @property
    def stages(self):
        """Gets the stages of this ShowTaskResqTaskinfoCaseList.

        stages

        :return: The stages of this ShowTaskResqTaskinfoCaseList.
        :rtype: list[object]
        """
        return self._stages

    @stages.setter
    def stages(self, stages):
        """Sets the stages of this ShowTaskResqTaskinfoCaseList.

        stages

        :param stages: The stages of this ShowTaskResqTaskinfoCaseList.
        :type: list[object]
        """
        self._stages = stages

    @property
    def status(self):
        """Gets the status of this ShowTaskResqTaskinfoCaseList.

        status

        :return: The status of this ShowTaskResqTaskinfoCaseList.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowTaskResqTaskinfoCaseList.

        status

        :param status: The status of this ShowTaskResqTaskinfoCaseList.
        :type: int
        """
        self._status = status

    @property
    def temp_id(self):
        """Gets the temp_id of this ShowTaskResqTaskinfoCaseList.

        temp_id

        :return: The temp_id of this ShowTaskResqTaskinfoCaseList.
        :rtype: int
        """
        return self._temp_id

    @temp_id.setter
    def temp_id(self, temp_id):
        """Sets the temp_id of this ShowTaskResqTaskinfoCaseList.

        temp_id

        :param temp_id: The temp_id of this ShowTaskResqTaskinfoCaseList.
        :type: int
        """
        self._temp_id = temp_id

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
        if not isinstance(other, ShowTaskResqTaskinfoCaseList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
