# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GeneralTextRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'image': 'str',
        'url': 'str',
        'detect_direction': 'bool',
        'quick_mode': 'bool'
    }

    attribute_map = {
        'image': 'image',
        'url': 'url',
        'detect_direction': 'detect_direction',
        'quick_mode': 'quick_mode'
    }

    def __init__(self, image=None, url=None, detect_direction=None, quick_mode=None):
        """GeneralTextRequestBody

        The model defined in huaweicloud sdk

        :param image: 与url二选一  图像数据，base64编码，要求base64编码后大小不超过10MB。图片最小边不小于15px，最长边不超过4096px。支持JPEG、JPG、PNG、BMP、TIFF格式。  图片文件Base64编码字符串，点击[这里](https://support.huaweicloud.com/ocr_faq/ocr_01_0032.html)查看详细获取方式。   
        :type image: str
        :param url: 与image二选一  图片的URL路径，目前支持：  - 公网http/https url  - OBS提供的url，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权，详情参见[配置OBS访问权限](https://support.huaweicloud.com/api-ocr/ocr_03_0132.html)。  &gt; 说明：  - 接口响应时间依赖于图片的下载时间，如果图片下载时间过长，会返回接口调用失败。  - 请保证被检测图片所在的存储服务稳定可靠，推荐使用OBS服务存储图片数据。 
        :type url: str
        :param detect_direction: 图片朝向检测开关，可选值包括：  - true：检测图片朝向;  - false：不检测图片朝向。  &gt; 说明：  - 支持任意角度的图片朝向检测。未传入该参数时默认为false，即不检测图片朝向。 
        :type detect_direction: bool
        :param quick_mode: 快速模式开关，针对单行文字图片（要求图片只包含一行文字，且文字区域占比超过50%），打开时可以更快返回识别。可选值包括：  - true：打开快速模式；  - false：关闭快速模式。  &gt; 说明：  - 未传入该参数时默认为false，即关闭快速模式。 
        :type quick_mode: bool
        """
        
        

        self._image = None
        self._url = None
        self._detect_direction = None
        self._quick_mode = None
        self.discriminator = None

        if image is not None:
            self.image = image
        if url is not None:
            self.url = url
        if detect_direction is not None:
            self.detect_direction = detect_direction
        if quick_mode is not None:
            self.quick_mode = quick_mode

    @property
    def image(self):
        """Gets the image of this GeneralTextRequestBody.

        与url二选一  图像数据，base64编码，要求base64编码后大小不超过10MB。图片最小边不小于15px，最长边不超过4096px。支持JPEG、JPG、PNG、BMP、TIFF格式。  图片文件Base64编码字符串，点击[这里](https://support.huaweicloud.com/ocr_faq/ocr_01_0032.html)查看详细获取方式。   

        :return: The image of this GeneralTextRequestBody.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this GeneralTextRequestBody.

        与url二选一  图像数据，base64编码，要求base64编码后大小不超过10MB。图片最小边不小于15px，最长边不超过4096px。支持JPEG、JPG、PNG、BMP、TIFF格式。  图片文件Base64编码字符串，点击[这里](https://support.huaweicloud.com/ocr_faq/ocr_01_0032.html)查看详细获取方式。   

        :param image: The image of this GeneralTextRequestBody.
        :type image: str
        """
        self._image = image

    @property
    def url(self):
        """Gets the url of this GeneralTextRequestBody.

        与image二选一  图片的URL路径，目前支持：  - 公网http/https url  - OBS提供的url，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权，详情参见[配置OBS访问权限](https://support.huaweicloud.com/api-ocr/ocr_03_0132.html)。  > 说明：  - 接口响应时间依赖于图片的下载时间，如果图片下载时间过长，会返回接口调用失败。  - 请保证被检测图片所在的存储服务稳定可靠，推荐使用OBS服务存储图片数据。 

        :return: The url of this GeneralTextRequestBody.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this GeneralTextRequestBody.

        与image二选一  图片的URL路径，目前支持：  - 公网http/https url  - OBS提供的url，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权，详情参见[配置OBS访问权限](https://support.huaweicloud.com/api-ocr/ocr_03_0132.html)。  > 说明：  - 接口响应时间依赖于图片的下载时间，如果图片下载时间过长，会返回接口调用失败。  - 请保证被检测图片所在的存储服务稳定可靠，推荐使用OBS服务存储图片数据。 

        :param url: The url of this GeneralTextRequestBody.
        :type url: str
        """
        self._url = url

    @property
    def detect_direction(self):
        """Gets the detect_direction of this GeneralTextRequestBody.

        图片朝向检测开关，可选值包括：  - true：检测图片朝向;  - false：不检测图片朝向。  > 说明：  - 支持任意角度的图片朝向检测。未传入该参数时默认为false，即不检测图片朝向。 

        :return: The detect_direction of this GeneralTextRequestBody.
        :rtype: bool
        """
        return self._detect_direction

    @detect_direction.setter
    def detect_direction(self, detect_direction):
        """Sets the detect_direction of this GeneralTextRequestBody.

        图片朝向检测开关，可选值包括：  - true：检测图片朝向;  - false：不检测图片朝向。  > 说明：  - 支持任意角度的图片朝向检测。未传入该参数时默认为false，即不检测图片朝向。 

        :param detect_direction: The detect_direction of this GeneralTextRequestBody.
        :type detect_direction: bool
        """
        self._detect_direction = detect_direction

    @property
    def quick_mode(self):
        """Gets the quick_mode of this GeneralTextRequestBody.

        快速模式开关，针对单行文字图片（要求图片只包含一行文字，且文字区域占比超过50%），打开时可以更快返回识别。可选值包括：  - true：打开快速模式；  - false：关闭快速模式。  > 说明：  - 未传入该参数时默认为false，即关闭快速模式。 

        :return: The quick_mode of this GeneralTextRequestBody.
        :rtype: bool
        """
        return self._quick_mode

    @quick_mode.setter
    def quick_mode(self, quick_mode):
        """Sets the quick_mode of this GeneralTextRequestBody.

        快速模式开关，针对单行文字图片（要求图片只包含一行文字，且文字区域占比超过50%），打开时可以更快返回识别。可选值包括：  - true：打开快速模式；  - false：关闭快速模式。  > 说明：  - 未传入该参数时默认为false，即关闭快速模式。 

        :param quick_mode: The quick_mode of this GeneralTextRequestBody.
        :type quick_mode: bool
        """
        self._quick_mode = quick_mode

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
        if not isinstance(other, GeneralTextRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
