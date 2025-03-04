# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RunModifyPictureRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'instance_name': 'str',
        'body': 'RunModifyPictureReq'
    }

    attribute_map = {
        'instance_name': 'instance_name',
        'body': 'body'
    }

    def __init__(self, instance_name=None, body=None):
        """RunModifyPictureRequest

        The model defined in huaweicloud sdk

        :param instance_name: 实例名称。
        :type instance_name: str
        :param body: Body of the RunModifyPictureRequest
        :type body: :class:`huaweicloudsdkimagesearch.v1.RunModifyPictureReq`
        """
        
        

        self._instance_name = None
        self._body = None
        self.discriminator = None

        self.instance_name = instance_name
        if body is not None:
            self.body = body

    @property
    def instance_name(self):
        """Gets the instance_name of this RunModifyPictureRequest.

        实例名称。

        :return: The instance_name of this RunModifyPictureRequest.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        """Sets the instance_name of this RunModifyPictureRequest.

        实例名称。

        :param instance_name: The instance_name of this RunModifyPictureRequest.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def body(self):
        """Gets the body of this RunModifyPictureRequest.


        :return: The body of this RunModifyPictureRequest.
        :rtype: :class:`huaweicloudsdkimagesearch.v1.RunModifyPictureReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this RunModifyPictureRequest.


        :param body: The body of this RunModifyPictureRequest.
        :type body: :class:`huaweicloudsdkimagesearch.v1.RunModifyPictureReq`
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
        if not isinstance(other, RunModifyPictureRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
