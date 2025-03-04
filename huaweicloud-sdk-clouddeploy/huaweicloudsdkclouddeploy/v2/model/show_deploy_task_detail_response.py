# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDeployTaskDetailResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'task_id': 'str',
        'name': 'str',
        'project_id': 'str',
        'project_name': 'str',
        'deploy_system': 'str',
        'create_time': 'str',
        'update_time': 'str',
        'state': 'str',
        'execution_time': 'str',
        'description': 'str',
        'is_defaut_permission': 'bool',
        'template_id': 'str',
        'owner': 'str',
        'nick_name': 'str',
        'owner_id': 'str',
        'tenant_id': 'str',
        'tenant_name': 'str',
        'slave_cluster_id': 'str',
        'is_care': 'bool',
        'can_modify': 'bool',
        'can_delete': 'bool',
        'can_view': 'bool',
        'can_execute': 'bool',
        'can_copy': 'bool',
        'can_manage': 'bool',
        'app_component_list': 'list[AppComponentDao]',
        'role_id': 'int'
    }

    attribute_map = {
        'task_id': 'task_id',
        'name': 'name',
        'project_id': 'project_id',
        'project_name': 'project_name',
        'deploy_system': 'deploy_system',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'state': 'state',
        'execution_time': 'execution_time',
        'description': 'description',
        'is_defaut_permission': 'is_defaut_permission',
        'template_id': 'template_id',
        'owner': 'owner',
        'nick_name': 'nick_name',
        'owner_id': 'owner_id',
        'tenant_id': 'tenant_id',
        'tenant_name': 'tenant_name',
        'slave_cluster_id': 'slave_cluster_id',
        'is_care': 'is_care',
        'can_modify': 'can_modify',
        'can_delete': 'can_delete',
        'can_view': 'can_view',
        'can_execute': 'can_execute',
        'can_copy': 'can_copy',
        'can_manage': 'can_manage',
        'app_component_list': 'app_component_list',
        'role_id': 'role_id'
    }

    def __init__(self, task_id=None, name=None, project_id=None, project_name=None, deploy_system=None, create_time=None, update_time=None, state=None, execution_time=None, description=None, is_defaut_permission=None, template_id=None, owner=None, nick_name=None, owner_id=None, tenant_id=None, tenant_name=None, slave_cluster_id=None, is_care=None, can_modify=None, can_delete=None, can_view=None, can_execute=None, can_copy=None, can_manage=None, app_component_list=None, role_id=None):
        """ShowDeployTaskDetailResponse

        The model defined in huaweicloud sdk

        :param task_id: 部署任务id
        :type task_id: str
        :param name: 部署任务名称
        :type name: str
        :param project_id: devcloud项目id
        :type project_id: str
        :param project_name: devcloud项目名称
        :type project_name: str
        :param deploy_system: 部署类型模式，包括deployTemplate，ansible，shell
        :type deploy_system: str
        :param create_time: 创建时间
        :type create_time: str
        :param update_time: 修改时间
        :type update_time: str
        :param state: 部署任务状态，Draft表示草稿状态，Available表示可用状态
        :type state: str
        :param execution_time: 最后一次执行时间
        :type execution_time: str
        :param description: 描述
        :type description: str
        :param is_defaut_permission: 是否使用默认权限矩阵
        :type is_defaut_permission: bool
        :param template_id: 模板id
        :type template_id: str
        :param owner: 部署任务创建者用户名
        :type owner: str
        :param nick_name: 部署任务创建者昵称
        :type nick_name: str
        :param owner_id: 部署任务创建者用户ID
        :type owner_id: str
        :param tenant_id: 部署任务创建者租户ID
        :type tenant_id: str
        :param tenant_name: 部署任务创建者租户名
        :type tenant_name: str
        :param slave_cluster_id: slave集群id，默认为null时使用devcloud八爪鱼slave集群，用户自定义slave时为slave集群id
        :type slave_cluster_id: str
        :param is_care: 当前用户是否已收藏
        :type is_care: bool
        :param can_modify: 是否有编辑权限
        :type can_modify: bool
        :param can_delete: 是否有删除的权限
        :type can_delete: bool
        :param can_view: 是否有查看权限
        :type can_view: bool
        :param can_execute: 是否有执行权限
        :type can_execute: bool
        :param can_copy: 是否有复制权限
        :type can_copy: bool
        :param can_manage: 是否有管理权限，包含增删改查执行以及权限修改
        :type can_manage: bool
        :param app_component_list: 部署任务和应用组件对应关系
        :type app_component_list: list[:class:`huaweicloudsdkclouddeploy.v2.AppComponentDao`]
        :param role_id: 角色ID,0：部署任务创建者，-1：项目创建者，3：项目经理，4：开发人员，5：测试经理，6：测试人员，7：参与者，8：浏览者
        :type role_id: int
        """
        
        super(ShowDeployTaskDetailResponse, self).__init__()

        self._task_id = None
        self._name = None
        self._project_id = None
        self._project_name = None
        self._deploy_system = None
        self._create_time = None
        self._update_time = None
        self._state = None
        self._execution_time = None
        self._description = None
        self._is_defaut_permission = None
        self._template_id = None
        self._owner = None
        self._nick_name = None
        self._owner_id = None
        self._tenant_id = None
        self._tenant_name = None
        self._slave_cluster_id = None
        self._is_care = None
        self._can_modify = None
        self._can_delete = None
        self._can_view = None
        self._can_execute = None
        self._can_copy = None
        self._can_manage = None
        self._app_component_list = None
        self._role_id = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if name is not None:
            self.name = name
        if project_id is not None:
            self.project_id = project_id
        if project_name is not None:
            self.project_name = project_name
        if deploy_system is not None:
            self.deploy_system = deploy_system
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if state is not None:
            self.state = state
        if execution_time is not None:
            self.execution_time = execution_time
        if description is not None:
            self.description = description
        if is_defaut_permission is not None:
            self.is_defaut_permission = is_defaut_permission
        if template_id is not None:
            self.template_id = template_id
        if owner is not None:
            self.owner = owner
        if nick_name is not None:
            self.nick_name = nick_name
        if owner_id is not None:
            self.owner_id = owner_id
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if tenant_name is not None:
            self.tenant_name = tenant_name
        if slave_cluster_id is not None:
            self.slave_cluster_id = slave_cluster_id
        if is_care is not None:
            self.is_care = is_care
        if can_modify is not None:
            self.can_modify = can_modify
        if can_delete is not None:
            self.can_delete = can_delete
        if can_view is not None:
            self.can_view = can_view
        if can_execute is not None:
            self.can_execute = can_execute
        if can_copy is not None:
            self.can_copy = can_copy
        if can_manage is not None:
            self.can_manage = can_manage
        if app_component_list is not None:
            self.app_component_list = app_component_list
        if role_id is not None:
            self.role_id = role_id

    @property
    def task_id(self):
        """Gets the task_id of this ShowDeployTaskDetailResponse.

        部署任务id

        :return: The task_id of this ShowDeployTaskDetailResponse.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this ShowDeployTaskDetailResponse.

        部署任务id

        :param task_id: The task_id of this ShowDeployTaskDetailResponse.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def name(self):
        """Gets the name of this ShowDeployTaskDetailResponse.

        部署任务名称

        :return: The name of this ShowDeployTaskDetailResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowDeployTaskDetailResponse.

        部署任务名称

        :param name: The name of this ShowDeployTaskDetailResponse.
        :type name: str
        """
        self._name = name

    @property
    def project_id(self):
        """Gets the project_id of this ShowDeployTaskDetailResponse.

        devcloud项目id

        :return: The project_id of this ShowDeployTaskDetailResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ShowDeployTaskDetailResponse.

        devcloud项目id

        :param project_id: The project_id of this ShowDeployTaskDetailResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def project_name(self):
        """Gets the project_name of this ShowDeployTaskDetailResponse.

        devcloud项目名称

        :return: The project_name of this ShowDeployTaskDetailResponse.
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this ShowDeployTaskDetailResponse.

        devcloud项目名称

        :param project_name: The project_name of this ShowDeployTaskDetailResponse.
        :type project_name: str
        """
        self._project_name = project_name

    @property
    def deploy_system(self):
        """Gets the deploy_system of this ShowDeployTaskDetailResponse.

        部署类型模式，包括deployTemplate，ansible，shell

        :return: The deploy_system of this ShowDeployTaskDetailResponse.
        :rtype: str
        """
        return self._deploy_system

    @deploy_system.setter
    def deploy_system(self, deploy_system):
        """Sets the deploy_system of this ShowDeployTaskDetailResponse.

        部署类型模式，包括deployTemplate，ansible，shell

        :param deploy_system: The deploy_system of this ShowDeployTaskDetailResponse.
        :type deploy_system: str
        """
        self._deploy_system = deploy_system

    @property
    def create_time(self):
        """Gets the create_time of this ShowDeployTaskDetailResponse.

        创建时间

        :return: The create_time of this ShowDeployTaskDetailResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ShowDeployTaskDetailResponse.

        创建时间

        :param create_time: The create_time of this ShowDeployTaskDetailResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this ShowDeployTaskDetailResponse.

        修改时间

        :return: The update_time of this ShowDeployTaskDetailResponse.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this ShowDeployTaskDetailResponse.

        修改时间

        :param update_time: The update_time of this ShowDeployTaskDetailResponse.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def state(self):
        """Gets the state of this ShowDeployTaskDetailResponse.

        部署任务状态，Draft表示草稿状态，Available表示可用状态

        :return: The state of this ShowDeployTaskDetailResponse.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ShowDeployTaskDetailResponse.

        部署任务状态，Draft表示草稿状态，Available表示可用状态

        :param state: The state of this ShowDeployTaskDetailResponse.
        :type state: str
        """
        self._state = state

    @property
    def execution_time(self):
        """Gets the execution_time of this ShowDeployTaskDetailResponse.

        最后一次执行时间

        :return: The execution_time of this ShowDeployTaskDetailResponse.
        :rtype: str
        """
        return self._execution_time

    @execution_time.setter
    def execution_time(self, execution_time):
        """Sets the execution_time of this ShowDeployTaskDetailResponse.

        最后一次执行时间

        :param execution_time: The execution_time of this ShowDeployTaskDetailResponse.
        :type execution_time: str
        """
        self._execution_time = execution_time

    @property
    def description(self):
        """Gets the description of this ShowDeployTaskDetailResponse.

        描述

        :return: The description of this ShowDeployTaskDetailResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ShowDeployTaskDetailResponse.

        描述

        :param description: The description of this ShowDeployTaskDetailResponse.
        :type description: str
        """
        self._description = description

    @property
    def is_defaut_permission(self):
        """Gets the is_defaut_permission of this ShowDeployTaskDetailResponse.

        是否使用默认权限矩阵

        :return: The is_defaut_permission of this ShowDeployTaskDetailResponse.
        :rtype: bool
        """
        return self._is_defaut_permission

    @is_defaut_permission.setter
    def is_defaut_permission(self, is_defaut_permission):
        """Sets the is_defaut_permission of this ShowDeployTaskDetailResponse.

        是否使用默认权限矩阵

        :param is_defaut_permission: The is_defaut_permission of this ShowDeployTaskDetailResponse.
        :type is_defaut_permission: bool
        """
        self._is_defaut_permission = is_defaut_permission

    @property
    def template_id(self):
        """Gets the template_id of this ShowDeployTaskDetailResponse.

        模板id

        :return: The template_id of this ShowDeployTaskDetailResponse.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this ShowDeployTaskDetailResponse.

        模板id

        :param template_id: The template_id of this ShowDeployTaskDetailResponse.
        :type template_id: str
        """
        self._template_id = template_id

    @property
    def owner(self):
        """Gets the owner of this ShowDeployTaskDetailResponse.

        部署任务创建者用户名

        :return: The owner of this ShowDeployTaskDetailResponse.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this ShowDeployTaskDetailResponse.

        部署任务创建者用户名

        :param owner: The owner of this ShowDeployTaskDetailResponse.
        :type owner: str
        """
        self._owner = owner

    @property
    def nick_name(self):
        """Gets the nick_name of this ShowDeployTaskDetailResponse.

        部署任务创建者昵称

        :return: The nick_name of this ShowDeployTaskDetailResponse.
        :rtype: str
        """
        return self._nick_name

    @nick_name.setter
    def nick_name(self, nick_name):
        """Sets the nick_name of this ShowDeployTaskDetailResponse.

        部署任务创建者昵称

        :param nick_name: The nick_name of this ShowDeployTaskDetailResponse.
        :type nick_name: str
        """
        self._nick_name = nick_name

    @property
    def owner_id(self):
        """Gets the owner_id of this ShowDeployTaskDetailResponse.

        部署任务创建者用户ID

        :return: The owner_id of this ShowDeployTaskDetailResponse.
        :rtype: str
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this ShowDeployTaskDetailResponse.

        部署任务创建者用户ID

        :param owner_id: The owner_id of this ShowDeployTaskDetailResponse.
        :type owner_id: str
        """
        self._owner_id = owner_id

    @property
    def tenant_id(self):
        """Gets the tenant_id of this ShowDeployTaskDetailResponse.

        部署任务创建者租户ID

        :return: The tenant_id of this ShowDeployTaskDetailResponse.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this ShowDeployTaskDetailResponse.

        部署任务创建者租户ID

        :param tenant_id: The tenant_id of this ShowDeployTaskDetailResponse.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def tenant_name(self):
        """Gets the tenant_name of this ShowDeployTaskDetailResponse.

        部署任务创建者租户名

        :return: The tenant_name of this ShowDeployTaskDetailResponse.
        :rtype: str
        """
        return self._tenant_name

    @tenant_name.setter
    def tenant_name(self, tenant_name):
        """Sets the tenant_name of this ShowDeployTaskDetailResponse.

        部署任务创建者租户名

        :param tenant_name: The tenant_name of this ShowDeployTaskDetailResponse.
        :type tenant_name: str
        """
        self._tenant_name = tenant_name

    @property
    def slave_cluster_id(self):
        """Gets the slave_cluster_id of this ShowDeployTaskDetailResponse.

        slave集群id，默认为null时使用devcloud八爪鱼slave集群，用户自定义slave时为slave集群id

        :return: The slave_cluster_id of this ShowDeployTaskDetailResponse.
        :rtype: str
        """
        return self._slave_cluster_id

    @slave_cluster_id.setter
    def slave_cluster_id(self, slave_cluster_id):
        """Sets the slave_cluster_id of this ShowDeployTaskDetailResponse.

        slave集群id，默认为null时使用devcloud八爪鱼slave集群，用户自定义slave时为slave集群id

        :param slave_cluster_id: The slave_cluster_id of this ShowDeployTaskDetailResponse.
        :type slave_cluster_id: str
        """
        self._slave_cluster_id = slave_cluster_id

    @property
    def is_care(self):
        """Gets the is_care of this ShowDeployTaskDetailResponse.

        当前用户是否已收藏

        :return: The is_care of this ShowDeployTaskDetailResponse.
        :rtype: bool
        """
        return self._is_care

    @is_care.setter
    def is_care(self, is_care):
        """Sets the is_care of this ShowDeployTaskDetailResponse.

        当前用户是否已收藏

        :param is_care: The is_care of this ShowDeployTaskDetailResponse.
        :type is_care: bool
        """
        self._is_care = is_care

    @property
    def can_modify(self):
        """Gets the can_modify of this ShowDeployTaskDetailResponse.

        是否有编辑权限

        :return: The can_modify of this ShowDeployTaskDetailResponse.
        :rtype: bool
        """
        return self._can_modify

    @can_modify.setter
    def can_modify(self, can_modify):
        """Sets the can_modify of this ShowDeployTaskDetailResponse.

        是否有编辑权限

        :param can_modify: The can_modify of this ShowDeployTaskDetailResponse.
        :type can_modify: bool
        """
        self._can_modify = can_modify

    @property
    def can_delete(self):
        """Gets the can_delete of this ShowDeployTaskDetailResponse.

        是否有删除的权限

        :return: The can_delete of this ShowDeployTaskDetailResponse.
        :rtype: bool
        """
        return self._can_delete

    @can_delete.setter
    def can_delete(self, can_delete):
        """Sets the can_delete of this ShowDeployTaskDetailResponse.

        是否有删除的权限

        :param can_delete: The can_delete of this ShowDeployTaskDetailResponse.
        :type can_delete: bool
        """
        self._can_delete = can_delete

    @property
    def can_view(self):
        """Gets the can_view of this ShowDeployTaskDetailResponse.

        是否有查看权限

        :return: The can_view of this ShowDeployTaskDetailResponse.
        :rtype: bool
        """
        return self._can_view

    @can_view.setter
    def can_view(self, can_view):
        """Sets the can_view of this ShowDeployTaskDetailResponse.

        是否有查看权限

        :param can_view: The can_view of this ShowDeployTaskDetailResponse.
        :type can_view: bool
        """
        self._can_view = can_view

    @property
    def can_execute(self):
        """Gets the can_execute of this ShowDeployTaskDetailResponse.

        是否有执行权限

        :return: The can_execute of this ShowDeployTaskDetailResponse.
        :rtype: bool
        """
        return self._can_execute

    @can_execute.setter
    def can_execute(self, can_execute):
        """Sets the can_execute of this ShowDeployTaskDetailResponse.

        是否有执行权限

        :param can_execute: The can_execute of this ShowDeployTaskDetailResponse.
        :type can_execute: bool
        """
        self._can_execute = can_execute

    @property
    def can_copy(self):
        """Gets the can_copy of this ShowDeployTaskDetailResponse.

        是否有复制权限

        :return: The can_copy of this ShowDeployTaskDetailResponse.
        :rtype: bool
        """
        return self._can_copy

    @can_copy.setter
    def can_copy(self, can_copy):
        """Sets the can_copy of this ShowDeployTaskDetailResponse.

        是否有复制权限

        :param can_copy: The can_copy of this ShowDeployTaskDetailResponse.
        :type can_copy: bool
        """
        self._can_copy = can_copy

    @property
    def can_manage(self):
        """Gets the can_manage of this ShowDeployTaskDetailResponse.

        是否有管理权限，包含增删改查执行以及权限修改

        :return: The can_manage of this ShowDeployTaskDetailResponse.
        :rtype: bool
        """
        return self._can_manage

    @can_manage.setter
    def can_manage(self, can_manage):
        """Sets the can_manage of this ShowDeployTaskDetailResponse.

        是否有管理权限，包含增删改查执行以及权限修改

        :param can_manage: The can_manage of this ShowDeployTaskDetailResponse.
        :type can_manage: bool
        """
        self._can_manage = can_manage

    @property
    def app_component_list(self):
        """Gets the app_component_list of this ShowDeployTaskDetailResponse.

        部署任务和应用组件对应关系

        :return: The app_component_list of this ShowDeployTaskDetailResponse.
        :rtype: list[:class:`huaweicloudsdkclouddeploy.v2.AppComponentDao`]
        """
        return self._app_component_list

    @app_component_list.setter
    def app_component_list(self, app_component_list):
        """Sets the app_component_list of this ShowDeployTaskDetailResponse.

        部署任务和应用组件对应关系

        :param app_component_list: The app_component_list of this ShowDeployTaskDetailResponse.
        :type app_component_list: list[:class:`huaweicloudsdkclouddeploy.v2.AppComponentDao`]
        """
        self._app_component_list = app_component_list

    @property
    def role_id(self):
        """Gets the role_id of this ShowDeployTaskDetailResponse.

        角色ID,0：部署任务创建者，-1：项目创建者，3：项目经理，4：开发人员，5：测试经理，6：测试人员，7：参与者，8：浏览者

        :return: The role_id of this ShowDeployTaskDetailResponse.
        :rtype: int
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id):
        """Sets the role_id of this ShowDeployTaskDetailResponse.

        角色ID,0：部署任务创建者，-1：项目创建者，3：项目经理，4：开发人员，5：测试经理，6：测试人员，7：参与者，8：浏览者

        :param role_id: The role_id of this ShowDeployTaskDetailResponse.
        :type role_id: int
        """
        self._role_id = role_id

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
        if not isinstance(other, ShowDeployTaskDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
