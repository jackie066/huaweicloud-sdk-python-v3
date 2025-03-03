# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EventManagementResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'event_id': 'str',
        'event_class_id': 'str',
        'event_type': 'int',
        'event_name': 'str',
        'severity': 'str',
        'container_name': 'str',
        'image_name': 'str',
        'host_name': 'str',
        'host_id': 'str',
        'private_ip': 'str',
        'public_ip': 'str',
        'attack_phase': 'str',
        'attack_tag': 'str',
        'occur_time': 'int',
        'handle_time': 'int',
        'handle_status': 'str',
        'handle_method': 'str',
        'handler': 'str',
        'operate_accept_list': 'list[str]',
        'operate_detail_list': 'list[EventDetailResponseInfo]',
        'forensic_info': 'object',
        'resource_info': 'EventResourceResponseInfo',
        'geo_info': 'object',
        'malware_info': 'object',
        'network_info': 'object',
        'app_info': 'object',
        'system_info': 'object',
        'recommendation': 'str',
        'process_info_list': 'list[EventProcessResponseInfo]',
        'user_info_list': 'list[EventUserResponseInfo]',
        'file_info_list': 'list[EventFileResponseInfo]'
    }

    attribute_map = {
        'event_id': 'event_id',
        'event_class_id': 'event_class_id',
        'event_type': 'event_type',
        'event_name': 'event_name',
        'severity': 'severity',
        'container_name': 'container_name',
        'image_name': 'image_name',
        'host_name': 'host_name',
        'host_id': 'host_id',
        'private_ip': 'private_ip',
        'public_ip': 'public_ip',
        'attack_phase': 'attack_phase',
        'attack_tag': 'attack_tag',
        'occur_time': 'occur_time',
        'handle_time': 'handle_time',
        'handle_status': 'handle_status',
        'handle_method': 'handle_method',
        'handler': 'handler',
        'operate_accept_list': 'operate_accept_list',
        'operate_detail_list': 'operate_detail_list',
        'forensic_info': 'forensic_info',
        'resource_info': 'resource_info',
        'geo_info': 'geo_info',
        'malware_info': 'malware_info',
        'network_info': 'network_info',
        'app_info': 'app_info',
        'system_info': 'system_info',
        'recommendation': 'recommendation',
        'process_info_list': 'process_info_list',
        'user_info_list': 'user_info_list',
        'file_info_list': 'file_info_list'
    }

    def __init__(self, event_id=None, event_class_id=None, event_type=None, event_name=None, severity=None, container_name=None, image_name=None, host_name=None, host_id=None, private_ip=None, public_ip=None, attack_phase=None, attack_tag=None, occur_time=None, handle_time=None, handle_status=None, handle_method=None, handler=None, operate_accept_list=None, operate_detail_list=None, forensic_info=None, resource_info=None, geo_info=None, malware_info=None, network_info=None, app_info=None, system_info=None, recommendation=None, process_info_list=None, user_info_list=None, file_info_list=None):
        """EventManagementResponseInfo

        The model defined in huaweicloud sdk

        :param event_id: 事件编号
        :type event_id: str
        :param event_class_id: 事件分类，包含如下:   - container_1001 : 容器命名空间   - container_1002 : 容器开放端口   - container_1003 : 容器安全选项   - container_1004 : 容器挂载目录   - containerescape_0001 : 容器高危系统调用   - containerescape_0002 : Shocker攻击   - containerescape_0003 : DirtCow攻击   - containerescape_0004 : 容器文件逃逸攻击   - dockerfile_001 : 用户自定义容器保护文件被修改   - dockerfile_002 : 容器文件系统可执行文件被修改   - dockerproc_001 : 容器进程异常事件上报   - fileprotect_0001 : 文件提权   - fileprotect_0002 : 关键文件变更   - fileprotect_0003 : AthorizedKeysFile配置路径变化   - fileprotect_0004 : 文件目录变更   - login_0001 : 尝试暴力破解   - login_0002 : 爆破成功   - login_1001 : 登录成功   - login_1002 : 异地登录   - login_1003 : 弱口令   - malware_0001 : shell变更事件上报   - malware_0002 : 反弹shell事件上报   - malware_1001 : 恶意程序   - procdet_0001 : 进程异常行为检测   - procdet_0002 : 进程提权   - procreport_0001 : 危险命令   - user_1001 : 账号变更   - user_1002 : 风险账号   - vmescape_0001 : 虚拟机敏感命令执行   - vmescape_0002 : 虚拟化进程访问敏感文件   - vmescape_0003 : 虚拟机异常端口访问   - webshell_0001 : 网站后门   - network_1001 : 恶意挖矿   - network_1002 : 对外DDoS攻击   - network_1003 : 恶意扫描   - network_1004 : 敏感区域攻击   - crontab_1001 : Crontab可疑任务
        :type event_class_id: str
        :param event_type: 事件类型，包含如下:   - 1001 : 恶意软件   - 1010 : Rootkit   - 1011 : 勒索软件   - 1015 : Webshell   - 1017 : 反弹Shell   - 2001 : 一般漏洞利用   - 3002 : 文件提权   - 3003 : 进程提权   - 3004 : 关键文件变更   - 3005 : 文件/目录变更   - 3007 : 进程异常行为   - 3015 : 高危命令执行   - 3018 : 异常Shell   - 3027 : Crontab可疑任务   - 4002 : 暴力破解   - 4004 : 异常登录   - 4006 : 非法系统账号
        :type event_type: int
        :param event_name: 事件名称
        :type event_name: str
        :param severity: 威胁等级，包含如下:   - Security : 安全   - Low : 低危   - Medium : 中危   - High : 高危   - Critical : 危急
        :type severity: str
        :param container_name: 容器实例名称
        :type container_name: str
        :param image_name: 镜像名称
        :type image_name: str
        :param host_name: 服务器名称
        :type host_name: str
        :param host_id: 服务器ID
        :type host_id: str
        :param private_ip: 服务器私网IP
        :type private_ip: str
        :param public_ip: 弹性公网IP地址
        :type public_ip: str
        :param attack_phase: 攻击阶段，包含如下：   - reconnaissance : 侦查跟踪   - weaponization : 武器构建   - delivery : 载荷投递   - exploit : 漏洞利用   - installation : 安装植入   - command_and_control : 命令与控制   - actions : 目标达成
        :type attack_phase: str
        :param attack_tag: 攻击标识，包含如下：   - attack_success : 攻击成功   - attack_attempt : 攻击尝试   - attack_blocked : 攻击被阻断   - abnormal_behavior : 异常行为   - collapsible_host : 主机失陷   - system_vulnerability : 系统脆弱性
        :type attack_tag: str
        :param occur_time: 发生时间，毫秒
        :type occur_time: int
        :param handle_time: 处理时间，毫秒
        :type handle_time: int
        :param handle_status: 处理状态，包含如下:   - unhandled ：未处理   - handled : 已处理
        :type handle_status: str
        :param handle_method: 处理方式，包含如下:   - mark_as_handled : 手动处理   - ignore : 忽略   - add_to_alarm_whitelist : 加入告警白名单   - add_to_login_whitelist : 加入登录白名单   - isolate_and_kill : 隔离查杀
        :type handle_method: str
        :param handler: 手动处理的备注
        :type handler: str
        :param operate_accept_list: 支持的处理操作
        :type operate_accept_list: list[str]
        :param operate_detail_list: 操作详情信息列表（页面不展示）
        :type operate_detail_list: list[:class:`huaweicloudsdkhss.v5.EventDetailResponseInfo`]
        :param forensic_info: 取证信息，json格式
        :type forensic_info: object
        :param resource_info: 
        :type resource_info: :class:`huaweicloudsdkhss.v5.EventResourceResponseInfo`
        :param geo_info: 地理位置信息，json格式
        :type geo_info: object
        :param malware_info: 恶意软件信息，json格式
        :type malware_info: object
        :param network_info: 网络信息，json格式
        :type network_info: object
        :param app_info: 应用信息，json格式
        :type app_info: object
        :param system_info: 系统信息，json格式
        :type system_info: object
        :param recommendation: 处置建议
        :type recommendation: str
        :param process_info_list: 进程信息列表
        :type process_info_list: list[:class:`huaweicloudsdkhss.v5.EventProcessResponseInfo`]
        :param user_info_list: 用户信息列表
        :type user_info_list: list[:class:`huaweicloudsdkhss.v5.EventUserResponseInfo`]
        :param file_info_list: 文件信息列表
        :type file_info_list: list[:class:`huaweicloudsdkhss.v5.EventFileResponseInfo`]
        """
        
        

        self._event_id = None
        self._event_class_id = None
        self._event_type = None
        self._event_name = None
        self._severity = None
        self._container_name = None
        self._image_name = None
        self._host_name = None
        self._host_id = None
        self._private_ip = None
        self._public_ip = None
        self._attack_phase = None
        self._attack_tag = None
        self._occur_time = None
        self._handle_time = None
        self._handle_status = None
        self._handle_method = None
        self._handler = None
        self._operate_accept_list = None
        self._operate_detail_list = None
        self._forensic_info = None
        self._resource_info = None
        self._geo_info = None
        self._malware_info = None
        self._network_info = None
        self._app_info = None
        self._system_info = None
        self._recommendation = None
        self._process_info_list = None
        self._user_info_list = None
        self._file_info_list = None
        self.discriminator = None

        if event_id is not None:
            self.event_id = event_id
        if event_class_id is not None:
            self.event_class_id = event_class_id
        if event_type is not None:
            self.event_type = event_type
        if event_name is not None:
            self.event_name = event_name
        if severity is not None:
            self.severity = severity
        if container_name is not None:
            self.container_name = container_name
        if image_name is not None:
            self.image_name = image_name
        if host_name is not None:
            self.host_name = host_name
        if host_id is not None:
            self.host_id = host_id
        if private_ip is not None:
            self.private_ip = private_ip
        if public_ip is not None:
            self.public_ip = public_ip
        if attack_phase is not None:
            self.attack_phase = attack_phase
        if attack_tag is not None:
            self.attack_tag = attack_tag
        if occur_time is not None:
            self.occur_time = occur_time
        if handle_time is not None:
            self.handle_time = handle_time
        if handle_status is not None:
            self.handle_status = handle_status
        if handle_method is not None:
            self.handle_method = handle_method
        if handler is not None:
            self.handler = handler
        if operate_accept_list is not None:
            self.operate_accept_list = operate_accept_list
        if operate_detail_list is not None:
            self.operate_detail_list = operate_detail_list
        if forensic_info is not None:
            self.forensic_info = forensic_info
        if resource_info is not None:
            self.resource_info = resource_info
        if geo_info is not None:
            self.geo_info = geo_info
        if malware_info is not None:
            self.malware_info = malware_info
        if network_info is not None:
            self.network_info = network_info
        if app_info is not None:
            self.app_info = app_info
        if system_info is not None:
            self.system_info = system_info
        if recommendation is not None:
            self.recommendation = recommendation
        if process_info_list is not None:
            self.process_info_list = process_info_list
        if user_info_list is not None:
            self.user_info_list = user_info_list
        if file_info_list is not None:
            self.file_info_list = file_info_list

    @property
    def event_id(self):
        """Gets the event_id of this EventManagementResponseInfo.

        事件编号

        :return: The event_id of this EventManagementResponseInfo.
        :rtype: str
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        """Sets the event_id of this EventManagementResponseInfo.

        事件编号

        :param event_id: The event_id of this EventManagementResponseInfo.
        :type event_id: str
        """
        self._event_id = event_id

    @property
    def event_class_id(self):
        """Gets the event_class_id of this EventManagementResponseInfo.

        事件分类，包含如下:   - container_1001 : 容器命名空间   - container_1002 : 容器开放端口   - container_1003 : 容器安全选项   - container_1004 : 容器挂载目录   - containerescape_0001 : 容器高危系统调用   - containerescape_0002 : Shocker攻击   - containerescape_0003 : DirtCow攻击   - containerescape_0004 : 容器文件逃逸攻击   - dockerfile_001 : 用户自定义容器保护文件被修改   - dockerfile_002 : 容器文件系统可执行文件被修改   - dockerproc_001 : 容器进程异常事件上报   - fileprotect_0001 : 文件提权   - fileprotect_0002 : 关键文件变更   - fileprotect_0003 : AthorizedKeysFile配置路径变化   - fileprotect_0004 : 文件目录变更   - login_0001 : 尝试暴力破解   - login_0002 : 爆破成功   - login_1001 : 登录成功   - login_1002 : 异地登录   - login_1003 : 弱口令   - malware_0001 : shell变更事件上报   - malware_0002 : 反弹shell事件上报   - malware_1001 : 恶意程序   - procdet_0001 : 进程异常行为检测   - procdet_0002 : 进程提权   - procreport_0001 : 危险命令   - user_1001 : 账号变更   - user_1002 : 风险账号   - vmescape_0001 : 虚拟机敏感命令执行   - vmescape_0002 : 虚拟化进程访问敏感文件   - vmescape_0003 : 虚拟机异常端口访问   - webshell_0001 : 网站后门   - network_1001 : 恶意挖矿   - network_1002 : 对外DDoS攻击   - network_1003 : 恶意扫描   - network_1004 : 敏感区域攻击   - crontab_1001 : Crontab可疑任务

        :return: The event_class_id of this EventManagementResponseInfo.
        :rtype: str
        """
        return self._event_class_id

    @event_class_id.setter
    def event_class_id(self, event_class_id):
        """Sets the event_class_id of this EventManagementResponseInfo.

        事件分类，包含如下:   - container_1001 : 容器命名空间   - container_1002 : 容器开放端口   - container_1003 : 容器安全选项   - container_1004 : 容器挂载目录   - containerescape_0001 : 容器高危系统调用   - containerescape_0002 : Shocker攻击   - containerescape_0003 : DirtCow攻击   - containerescape_0004 : 容器文件逃逸攻击   - dockerfile_001 : 用户自定义容器保护文件被修改   - dockerfile_002 : 容器文件系统可执行文件被修改   - dockerproc_001 : 容器进程异常事件上报   - fileprotect_0001 : 文件提权   - fileprotect_0002 : 关键文件变更   - fileprotect_0003 : AthorizedKeysFile配置路径变化   - fileprotect_0004 : 文件目录变更   - login_0001 : 尝试暴力破解   - login_0002 : 爆破成功   - login_1001 : 登录成功   - login_1002 : 异地登录   - login_1003 : 弱口令   - malware_0001 : shell变更事件上报   - malware_0002 : 反弹shell事件上报   - malware_1001 : 恶意程序   - procdet_0001 : 进程异常行为检测   - procdet_0002 : 进程提权   - procreport_0001 : 危险命令   - user_1001 : 账号变更   - user_1002 : 风险账号   - vmescape_0001 : 虚拟机敏感命令执行   - vmescape_0002 : 虚拟化进程访问敏感文件   - vmescape_0003 : 虚拟机异常端口访问   - webshell_0001 : 网站后门   - network_1001 : 恶意挖矿   - network_1002 : 对外DDoS攻击   - network_1003 : 恶意扫描   - network_1004 : 敏感区域攻击   - crontab_1001 : Crontab可疑任务

        :param event_class_id: The event_class_id of this EventManagementResponseInfo.
        :type event_class_id: str
        """
        self._event_class_id = event_class_id

    @property
    def event_type(self):
        """Gets the event_type of this EventManagementResponseInfo.

        事件类型，包含如下:   - 1001 : 恶意软件   - 1010 : Rootkit   - 1011 : 勒索软件   - 1015 : Webshell   - 1017 : 反弹Shell   - 2001 : 一般漏洞利用   - 3002 : 文件提权   - 3003 : 进程提权   - 3004 : 关键文件变更   - 3005 : 文件/目录变更   - 3007 : 进程异常行为   - 3015 : 高危命令执行   - 3018 : 异常Shell   - 3027 : Crontab可疑任务   - 4002 : 暴力破解   - 4004 : 异常登录   - 4006 : 非法系统账号

        :return: The event_type of this EventManagementResponseInfo.
        :rtype: int
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this EventManagementResponseInfo.

        事件类型，包含如下:   - 1001 : 恶意软件   - 1010 : Rootkit   - 1011 : 勒索软件   - 1015 : Webshell   - 1017 : 反弹Shell   - 2001 : 一般漏洞利用   - 3002 : 文件提权   - 3003 : 进程提权   - 3004 : 关键文件变更   - 3005 : 文件/目录变更   - 3007 : 进程异常行为   - 3015 : 高危命令执行   - 3018 : 异常Shell   - 3027 : Crontab可疑任务   - 4002 : 暴力破解   - 4004 : 异常登录   - 4006 : 非法系统账号

        :param event_type: The event_type of this EventManagementResponseInfo.
        :type event_type: int
        """
        self._event_type = event_type

    @property
    def event_name(self):
        """Gets the event_name of this EventManagementResponseInfo.

        事件名称

        :return: The event_name of this EventManagementResponseInfo.
        :rtype: str
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        """Sets the event_name of this EventManagementResponseInfo.

        事件名称

        :param event_name: The event_name of this EventManagementResponseInfo.
        :type event_name: str
        """
        self._event_name = event_name

    @property
    def severity(self):
        """Gets the severity of this EventManagementResponseInfo.

        威胁等级，包含如下:   - Security : 安全   - Low : 低危   - Medium : 中危   - High : 高危   - Critical : 危急

        :return: The severity of this EventManagementResponseInfo.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this EventManagementResponseInfo.

        威胁等级，包含如下:   - Security : 安全   - Low : 低危   - Medium : 中危   - High : 高危   - Critical : 危急

        :param severity: The severity of this EventManagementResponseInfo.
        :type severity: str
        """
        self._severity = severity

    @property
    def container_name(self):
        """Gets the container_name of this EventManagementResponseInfo.

        容器实例名称

        :return: The container_name of this EventManagementResponseInfo.
        :rtype: str
        """
        return self._container_name

    @container_name.setter
    def container_name(self, container_name):
        """Sets the container_name of this EventManagementResponseInfo.

        容器实例名称

        :param container_name: The container_name of this EventManagementResponseInfo.
        :type container_name: str
        """
        self._container_name = container_name

    @property
    def image_name(self):
        """Gets the image_name of this EventManagementResponseInfo.

        镜像名称

        :return: The image_name of this EventManagementResponseInfo.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        """Sets the image_name of this EventManagementResponseInfo.

        镜像名称

        :param image_name: The image_name of this EventManagementResponseInfo.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def host_name(self):
        """Gets the host_name of this EventManagementResponseInfo.

        服务器名称

        :return: The host_name of this EventManagementResponseInfo.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """Sets the host_name of this EventManagementResponseInfo.

        服务器名称

        :param host_name: The host_name of this EventManagementResponseInfo.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def host_id(self):
        """Gets the host_id of this EventManagementResponseInfo.

        服务器ID

        :return: The host_id of this EventManagementResponseInfo.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        """Sets the host_id of this EventManagementResponseInfo.

        服务器ID

        :param host_id: The host_id of this EventManagementResponseInfo.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def private_ip(self):
        """Gets the private_ip of this EventManagementResponseInfo.

        服务器私网IP

        :return: The private_ip of this EventManagementResponseInfo.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        """Sets the private_ip of this EventManagementResponseInfo.

        服务器私网IP

        :param private_ip: The private_ip of this EventManagementResponseInfo.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def public_ip(self):
        """Gets the public_ip of this EventManagementResponseInfo.

        弹性公网IP地址

        :return: The public_ip of this EventManagementResponseInfo.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        """Sets the public_ip of this EventManagementResponseInfo.

        弹性公网IP地址

        :param public_ip: The public_ip of this EventManagementResponseInfo.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def attack_phase(self):
        """Gets the attack_phase of this EventManagementResponseInfo.

        攻击阶段，包含如下：   - reconnaissance : 侦查跟踪   - weaponization : 武器构建   - delivery : 载荷投递   - exploit : 漏洞利用   - installation : 安装植入   - command_and_control : 命令与控制   - actions : 目标达成

        :return: The attack_phase of this EventManagementResponseInfo.
        :rtype: str
        """
        return self._attack_phase

    @attack_phase.setter
    def attack_phase(self, attack_phase):
        """Sets the attack_phase of this EventManagementResponseInfo.

        攻击阶段，包含如下：   - reconnaissance : 侦查跟踪   - weaponization : 武器构建   - delivery : 载荷投递   - exploit : 漏洞利用   - installation : 安装植入   - command_and_control : 命令与控制   - actions : 目标达成

        :param attack_phase: The attack_phase of this EventManagementResponseInfo.
        :type attack_phase: str
        """
        self._attack_phase = attack_phase

    @property
    def attack_tag(self):
        """Gets the attack_tag of this EventManagementResponseInfo.

        攻击标识，包含如下：   - attack_success : 攻击成功   - attack_attempt : 攻击尝试   - attack_blocked : 攻击被阻断   - abnormal_behavior : 异常行为   - collapsible_host : 主机失陷   - system_vulnerability : 系统脆弱性

        :return: The attack_tag of this EventManagementResponseInfo.
        :rtype: str
        """
        return self._attack_tag

    @attack_tag.setter
    def attack_tag(self, attack_tag):
        """Sets the attack_tag of this EventManagementResponseInfo.

        攻击标识，包含如下：   - attack_success : 攻击成功   - attack_attempt : 攻击尝试   - attack_blocked : 攻击被阻断   - abnormal_behavior : 异常行为   - collapsible_host : 主机失陷   - system_vulnerability : 系统脆弱性

        :param attack_tag: The attack_tag of this EventManagementResponseInfo.
        :type attack_tag: str
        """
        self._attack_tag = attack_tag

    @property
    def occur_time(self):
        """Gets the occur_time of this EventManagementResponseInfo.

        发生时间，毫秒

        :return: The occur_time of this EventManagementResponseInfo.
        :rtype: int
        """
        return self._occur_time

    @occur_time.setter
    def occur_time(self, occur_time):
        """Sets the occur_time of this EventManagementResponseInfo.

        发生时间，毫秒

        :param occur_time: The occur_time of this EventManagementResponseInfo.
        :type occur_time: int
        """
        self._occur_time = occur_time

    @property
    def handle_time(self):
        """Gets the handle_time of this EventManagementResponseInfo.

        处理时间，毫秒

        :return: The handle_time of this EventManagementResponseInfo.
        :rtype: int
        """
        return self._handle_time

    @handle_time.setter
    def handle_time(self, handle_time):
        """Sets the handle_time of this EventManagementResponseInfo.

        处理时间，毫秒

        :param handle_time: The handle_time of this EventManagementResponseInfo.
        :type handle_time: int
        """
        self._handle_time = handle_time

    @property
    def handle_status(self):
        """Gets the handle_status of this EventManagementResponseInfo.

        处理状态，包含如下:   - unhandled ：未处理   - handled : 已处理

        :return: The handle_status of this EventManagementResponseInfo.
        :rtype: str
        """
        return self._handle_status

    @handle_status.setter
    def handle_status(self, handle_status):
        """Sets the handle_status of this EventManagementResponseInfo.

        处理状态，包含如下:   - unhandled ：未处理   - handled : 已处理

        :param handle_status: The handle_status of this EventManagementResponseInfo.
        :type handle_status: str
        """
        self._handle_status = handle_status

    @property
    def handle_method(self):
        """Gets the handle_method of this EventManagementResponseInfo.

        处理方式，包含如下:   - mark_as_handled : 手动处理   - ignore : 忽略   - add_to_alarm_whitelist : 加入告警白名单   - add_to_login_whitelist : 加入登录白名单   - isolate_and_kill : 隔离查杀

        :return: The handle_method of this EventManagementResponseInfo.
        :rtype: str
        """
        return self._handle_method

    @handle_method.setter
    def handle_method(self, handle_method):
        """Sets the handle_method of this EventManagementResponseInfo.

        处理方式，包含如下:   - mark_as_handled : 手动处理   - ignore : 忽略   - add_to_alarm_whitelist : 加入告警白名单   - add_to_login_whitelist : 加入登录白名单   - isolate_and_kill : 隔离查杀

        :param handle_method: The handle_method of this EventManagementResponseInfo.
        :type handle_method: str
        """
        self._handle_method = handle_method

    @property
    def handler(self):
        """Gets the handler of this EventManagementResponseInfo.

        手动处理的备注

        :return: The handler of this EventManagementResponseInfo.
        :rtype: str
        """
        return self._handler

    @handler.setter
    def handler(self, handler):
        """Sets the handler of this EventManagementResponseInfo.

        手动处理的备注

        :param handler: The handler of this EventManagementResponseInfo.
        :type handler: str
        """
        self._handler = handler

    @property
    def operate_accept_list(self):
        """Gets the operate_accept_list of this EventManagementResponseInfo.

        支持的处理操作

        :return: The operate_accept_list of this EventManagementResponseInfo.
        :rtype: list[str]
        """
        return self._operate_accept_list

    @operate_accept_list.setter
    def operate_accept_list(self, operate_accept_list):
        """Sets the operate_accept_list of this EventManagementResponseInfo.

        支持的处理操作

        :param operate_accept_list: The operate_accept_list of this EventManagementResponseInfo.
        :type operate_accept_list: list[str]
        """
        self._operate_accept_list = operate_accept_list

    @property
    def operate_detail_list(self):
        """Gets the operate_detail_list of this EventManagementResponseInfo.

        操作详情信息列表（页面不展示）

        :return: The operate_detail_list of this EventManagementResponseInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.EventDetailResponseInfo`]
        """
        return self._operate_detail_list

    @operate_detail_list.setter
    def operate_detail_list(self, operate_detail_list):
        """Sets the operate_detail_list of this EventManagementResponseInfo.

        操作详情信息列表（页面不展示）

        :param operate_detail_list: The operate_detail_list of this EventManagementResponseInfo.
        :type operate_detail_list: list[:class:`huaweicloudsdkhss.v5.EventDetailResponseInfo`]
        """
        self._operate_detail_list = operate_detail_list

    @property
    def forensic_info(self):
        """Gets the forensic_info of this EventManagementResponseInfo.

        取证信息，json格式

        :return: The forensic_info of this EventManagementResponseInfo.
        :rtype: object
        """
        return self._forensic_info

    @forensic_info.setter
    def forensic_info(self, forensic_info):
        """Sets the forensic_info of this EventManagementResponseInfo.

        取证信息，json格式

        :param forensic_info: The forensic_info of this EventManagementResponseInfo.
        :type forensic_info: object
        """
        self._forensic_info = forensic_info

    @property
    def resource_info(self):
        """Gets the resource_info of this EventManagementResponseInfo.


        :return: The resource_info of this EventManagementResponseInfo.
        :rtype: :class:`huaweicloudsdkhss.v5.EventResourceResponseInfo`
        """
        return self._resource_info

    @resource_info.setter
    def resource_info(self, resource_info):
        """Sets the resource_info of this EventManagementResponseInfo.


        :param resource_info: The resource_info of this EventManagementResponseInfo.
        :type resource_info: :class:`huaweicloudsdkhss.v5.EventResourceResponseInfo`
        """
        self._resource_info = resource_info

    @property
    def geo_info(self):
        """Gets the geo_info of this EventManagementResponseInfo.

        地理位置信息，json格式

        :return: The geo_info of this EventManagementResponseInfo.
        :rtype: object
        """
        return self._geo_info

    @geo_info.setter
    def geo_info(self, geo_info):
        """Sets the geo_info of this EventManagementResponseInfo.

        地理位置信息，json格式

        :param geo_info: The geo_info of this EventManagementResponseInfo.
        :type geo_info: object
        """
        self._geo_info = geo_info

    @property
    def malware_info(self):
        """Gets the malware_info of this EventManagementResponseInfo.

        恶意软件信息，json格式

        :return: The malware_info of this EventManagementResponseInfo.
        :rtype: object
        """
        return self._malware_info

    @malware_info.setter
    def malware_info(self, malware_info):
        """Sets the malware_info of this EventManagementResponseInfo.

        恶意软件信息，json格式

        :param malware_info: The malware_info of this EventManagementResponseInfo.
        :type malware_info: object
        """
        self._malware_info = malware_info

    @property
    def network_info(self):
        """Gets the network_info of this EventManagementResponseInfo.

        网络信息，json格式

        :return: The network_info of this EventManagementResponseInfo.
        :rtype: object
        """
        return self._network_info

    @network_info.setter
    def network_info(self, network_info):
        """Sets the network_info of this EventManagementResponseInfo.

        网络信息，json格式

        :param network_info: The network_info of this EventManagementResponseInfo.
        :type network_info: object
        """
        self._network_info = network_info

    @property
    def app_info(self):
        """Gets the app_info of this EventManagementResponseInfo.

        应用信息，json格式

        :return: The app_info of this EventManagementResponseInfo.
        :rtype: object
        """
        return self._app_info

    @app_info.setter
    def app_info(self, app_info):
        """Sets the app_info of this EventManagementResponseInfo.

        应用信息，json格式

        :param app_info: The app_info of this EventManagementResponseInfo.
        :type app_info: object
        """
        self._app_info = app_info

    @property
    def system_info(self):
        """Gets the system_info of this EventManagementResponseInfo.

        系统信息，json格式

        :return: The system_info of this EventManagementResponseInfo.
        :rtype: object
        """
        return self._system_info

    @system_info.setter
    def system_info(self, system_info):
        """Sets the system_info of this EventManagementResponseInfo.

        系统信息，json格式

        :param system_info: The system_info of this EventManagementResponseInfo.
        :type system_info: object
        """
        self._system_info = system_info

    @property
    def recommendation(self):
        """Gets the recommendation of this EventManagementResponseInfo.

        处置建议

        :return: The recommendation of this EventManagementResponseInfo.
        :rtype: str
        """
        return self._recommendation

    @recommendation.setter
    def recommendation(self, recommendation):
        """Sets the recommendation of this EventManagementResponseInfo.

        处置建议

        :param recommendation: The recommendation of this EventManagementResponseInfo.
        :type recommendation: str
        """
        self._recommendation = recommendation

    @property
    def process_info_list(self):
        """Gets the process_info_list of this EventManagementResponseInfo.

        进程信息列表

        :return: The process_info_list of this EventManagementResponseInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.EventProcessResponseInfo`]
        """
        return self._process_info_list

    @process_info_list.setter
    def process_info_list(self, process_info_list):
        """Sets the process_info_list of this EventManagementResponseInfo.

        进程信息列表

        :param process_info_list: The process_info_list of this EventManagementResponseInfo.
        :type process_info_list: list[:class:`huaweicloudsdkhss.v5.EventProcessResponseInfo`]
        """
        self._process_info_list = process_info_list

    @property
    def user_info_list(self):
        """Gets the user_info_list of this EventManagementResponseInfo.

        用户信息列表

        :return: The user_info_list of this EventManagementResponseInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.EventUserResponseInfo`]
        """
        return self._user_info_list

    @user_info_list.setter
    def user_info_list(self, user_info_list):
        """Sets the user_info_list of this EventManagementResponseInfo.

        用户信息列表

        :param user_info_list: The user_info_list of this EventManagementResponseInfo.
        :type user_info_list: list[:class:`huaweicloudsdkhss.v5.EventUserResponseInfo`]
        """
        self._user_info_list = user_info_list

    @property
    def file_info_list(self):
        """Gets the file_info_list of this EventManagementResponseInfo.

        文件信息列表

        :return: The file_info_list of this EventManagementResponseInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.EventFileResponseInfo`]
        """
        return self._file_info_list

    @file_info_list.setter
    def file_info_list(self, file_info_list):
        """Sets the file_info_list of this EventManagementResponseInfo.

        文件信息列表

        :param file_info_list: The file_info_list of this EventManagementResponseInfo.
        :type file_info_list: list[:class:`huaweicloudsdkhss.v5.EventFileResponseInfo`]
        """
        self._file_info_list = file_info_list

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
        if not isinstance(other, EventManagementResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
