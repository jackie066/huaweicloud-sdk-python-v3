# coding: utf-8

import pprint
import re

import six





class CreateWatermarkTemplateReq:


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
        'watermark_type': 'str',
        'image_process': 'str',
        'dx': 'str',
        'dy': 'str',
        'position': 'str',
        'width': 'str',
        'height': 'str',
        'timeline_start': 'str',
        'timeline_duration': 'str',
        'type': 'str',
        'md5': 'str'
    }

    attribute_map = {
        'name': 'name',
        'watermark_type': 'watermark_type',
        'image_process': 'image_process',
        'dx': 'dx',
        'dy': 'dy',
        'position': 'position',
        'width': 'width',
        'height': 'height',
        'timeline_start': 'timeline_start',
        'timeline_duration': 'timeline_duration',
        'type': 'type',
        'md5': 'md5'
    }

    def __init__(self, name=None, watermark_type=None, image_process=None, dx=None, dy=None, position=None, width=None, height=None, timeline_start=None, timeline_duration=None, type=None, md5=None):
        """CreateWatermarkTemplateReq - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._watermark_type = None
        self._image_process = None
        self._dx = None
        self._dy = None
        self._position = None
        self._width = None
        self._height = None
        self._timeline_start = None
        self._timeline_duration = None
        self._type = None
        self._md5 = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if watermark_type is not None:
            self.watermark_type = watermark_type
        if image_process is not None:
            self.image_process = image_process
        if dx is not None:
            self.dx = dx
        if dy is not None:
            self.dy = dy
        if position is not None:
            self.position = position
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if timeline_start is not None:
            self.timeline_start = timeline_start
        if timeline_duration is not None:
            self.timeline_duration = timeline_duration
        if type is not None:
            self.type = type
        if md5 is not None:
            self.md5 = md5

    @property
    def name(self):
        """Gets the name of this CreateWatermarkTemplateReq.

        水印模板名称<br/> 

        :return: The name of this CreateWatermarkTemplateReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateWatermarkTemplateReq.

        水印模板名称<br/> 

        :param name: The name of this CreateWatermarkTemplateReq.
        :type: str
        """
        self._name = name

    @property
    def watermark_type(self):
        """Gets the watermark_type of this CreateWatermarkTemplateReq.

        水印类型，当前只支持Image（图片水印）<br/> 

        :return: The watermark_type of this CreateWatermarkTemplateReq.
        :rtype: str
        """
        return self._watermark_type

    @watermark_type.setter
    def watermark_type(self, watermark_type):
        """Sets the watermark_type of this CreateWatermarkTemplateReq.

        水印类型，当前只支持Image（图片水印）<br/> 

        :param watermark_type: The watermark_type of this CreateWatermarkTemplateReq.
        :type: str
        """
        self._watermark_type = watermark_type

    @property
    def image_process(self):
        """Gets the image_process of this CreateWatermarkTemplateReq.

        type设置为Image时有效，目前包括Original（只做简单缩放，不做其他处理），Transparent（图片底色透明），Grayed（彩色图片变灰）<br/> 

        :return: The image_process of this CreateWatermarkTemplateReq.
        :rtype: str
        """
        return self._image_process

    @image_process.setter
    def image_process(self, image_process):
        """Sets the image_process of this CreateWatermarkTemplateReq.

        type设置为Image时有效，目前包括Original（只做简单缩放，不做其他处理），Transparent（图片底色透明），Grayed（彩色图片变灰）<br/> 

        :param image_process: The image_process of this CreateWatermarkTemplateReq.
        :type: str
        """
        self._image_process = image_process

    @property
    def dx(self):
        """Gets the dx of this CreateWatermarkTemplateReq.

        水印图片相对输出视频的水平偏移量，默认值是0<br/> 

        :return: The dx of this CreateWatermarkTemplateReq.
        :rtype: str
        """
        return self._dx

    @dx.setter
    def dx(self, dx):
        """Sets the dx of this CreateWatermarkTemplateReq.

        水印图片相对输出视频的水平偏移量，默认值是0<br/> 

        :param dx: The dx of this CreateWatermarkTemplateReq.
        :type: str
        """
        self._dx = dx

    @property
    def dy(self):
        """Gets the dy of this CreateWatermarkTemplateReq.

        水印图片相对输出视频的垂直偏移量，默认值是0<br/> 

        :return: The dy of this CreateWatermarkTemplateReq.
        :rtype: str
        """
        return self._dy

    @dy.setter
    def dy(self, dy):
        """Sets the dy of this CreateWatermarkTemplateReq.

        水印图片相对输出视频的垂直偏移量，默认值是0<br/> 

        :param dy: The dy of this CreateWatermarkTemplateReq.
        :type: str
        """
        self._dy = dy

    @property
    def position(self):
        """Gets the position of this CreateWatermarkTemplateReq.

        水印的位置<br/> 

        :return: The position of this CreateWatermarkTemplateReq.
        :rtype: str
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this CreateWatermarkTemplateReq.

        水印的位置<br/> 

        :param position: The position of this CreateWatermarkTemplateReq.
        :type: str
        """
        self._position = position

    @property
    def width(self):
        """Gets the width of this CreateWatermarkTemplateReq.

        水印图片宽<br/> 

        :return: The width of this CreateWatermarkTemplateReq.
        :rtype: str
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this CreateWatermarkTemplateReq.

        水印图片宽<br/> 

        :param width: The width of this CreateWatermarkTemplateReq.
        :type: str
        """
        self._width = width

    @property
    def height(self):
        """Gets the height of this CreateWatermarkTemplateReq.

        水印图片高<br/> 

        :return: The height of this CreateWatermarkTemplateReq.
        :rtype: str
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this CreateWatermarkTemplateReq.

        水印图片高<br/> 

        :param height: The height of this CreateWatermarkTemplateReq.
        :type: str
        """
        self._height = height

    @property
    def timeline_start(self):
        """Gets the timeline_start of this CreateWatermarkTemplateReq.

        水印开始时间<br/> 

        :return: The timeline_start of this CreateWatermarkTemplateReq.
        :rtype: str
        """
        return self._timeline_start

    @timeline_start.setter
    def timeline_start(self, timeline_start):
        """Sets the timeline_start of this CreateWatermarkTemplateReq.

        水印开始时间<br/> 

        :param timeline_start: The timeline_start of this CreateWatermarkTemplateReq.
        :type: str
        """
        self._timeline_start = timeline_start

    @property
    def timeline_duration(self):
        """Gets the timeline_duration of this CreateWatermarkTemplateReq.

        水印持续时间<br/> 

        :return: The timeline_duration of this CreateWatermarkTemplateReq.
        :rtype: str
        """
        return self._timeline_duration

    @timeline_duration.setter
    def timeline_duration(self, timeline_duration):
        """Sets the timeline_duration of this CreateWatermarkTemplateReq.

        水印持续时间<br/> 

        :param timeline_duration: The timeline_duration of this CreateWatermarkTemplateReq.
        :type: str
        """
        self._timeline_duration = timeline_duration

    @property
    def type(self):
        """Gets the type of this CreateWatermarkTemplateReq.

        水印图片格式类型<br/> 

        :return: The type of this CreateWatermarkTemplateReq.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateWatermarkTemplateReq.

        水印图片格式类型<br/> 

        :param type: The type of this CreateWatermarkTemplateReq.
        :type: str
        """
        self._type = type

    @property
    def md5(self):
        """Gets the md5 of this CreateWatermarkTemplateReq.

        水印图片MD5值<br/> 

        :return: The md5 of this CreateWatermarkTemplateReq.
        :rtype: str
        """
        return self._md5

    @md5.setter
    def md5(self, md5):
        """Sets the md5 of this CreateWatermarkTemplateReq.

        水印图片MD5值<br/> 

        :param md5: The md5 of this CreateWatermarkTemplateReq.
        :type: str
        """
        self._md5 = md5

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
        if not isinstance(other, CreateWatermarkTemplateReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
