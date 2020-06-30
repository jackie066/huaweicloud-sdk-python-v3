# coding: utf-8

from __future__ import absolute_import

# import models into model package
from huaweicloudsdkiotda.v5.model.action_device_alarm import ActionDeviceAlarm
from huaweicloudsdkiotda.v5.model.action_device_command import ActionDeviceCommand
from huaweicloudsdkiotda.v5.model.action_dis_forwarding import ActionDisForwarding
from huaweicloudsdkiotda.v5.model.action_io_ta_forwarding import ActionIoTAForwarding
from huaweicloudsdkiotda.v5.model.action_kafka_forwarding import ActionKafkaForwarding
from huaweicloudsdkiotda.v5.model.action_obs_forwarding import ActionObsForwarding
from huaweicloudsdkiotda.v5.model.action_roma_forwarding import ActionRomaForwarding
from huaweicloudsdkiotda.v5.model.action_smn_forwarding import ActionSmnForwarding
from huaweicloudsdkiotda.v5.model.add_certificate_request import AddCertificateRequest
from huaweicloudsdkiotda.v5.model.add_certificate_response import AddCertificateResponse
from huaweicloudsdkiotda.v5.model.add_device import AddDevice
from huaweicloudsdkiotda.v5.model.add_device_group_dto import AddDeviceGroupDTO
from huaweicloudsdkiotda.v5.model.add_device_group_request import AddDeviceGroupRequest
from huaweicloudsdkiotda.v5.model.add_device_group_response import AddDeviceGroupResponse
from huaweicloudsdkiotda.v5.model.add_device_request import AddDeviceRequest
from huaweicloudsdkiotda.v5.model.add_device_response import AddDeviceResponse
from huaweicloudsdkiotda.v5.model.add_product import AddProduct
from huaweicloudsdkiotda.v5.model.auth_info import AuthInfo
from huaweicloudsdkiotda.v5.model.auth_info_without_secret import AuthInfoWithoutSecret
from huaweicloudsdkiotda.v5.model.bind_tags_dto import BindTagsDTO
from huaweicloudsdkiotda.v5.model.certificates_rsp_dto import CertificatesRspDTO
from huaweicloudsdkiotda.v5.model.change_rule_status_request import ChangeRuleStatusRequest
from huaweicloudsdkiotda.v5.model.change_rule_status_response import ChangeRuleStatusResponse
from huaweicloudsdkiotda.v5.model.check_certificate_request import CheckCertificateRequest
from huaweicloudsdkiotda.v5.model.check_certificate_response import CheckCertificateResponse
from huaweicloudsdkiotda.v5.model.cmd import Cmd
from huaweicloudsdkiotda.v5.model.condition_group import ConditionGroup
from huaweicloudsdkiotda.v5.model.create_batch_task import CreateBatchTask
from huaweicloudsdkiotda.v5.model.create_batch_task_request import CreateBatchTaskRequest
from huaweicloudsdkiotda.v5.model.create_batch_task_response import CreateBatchTaskResponse
from huaweicloudsdkiotda.v5.model.create_certificate_dto import CreateCertificateDTO
from huaweicloudsdkiotda.v5.model.create_command_request import CreateCommandRequest
from huaweicloudsdkiotda.v5.model.create_command_response import CreateCommandResponse
from huaweicloudsdkiotda.v5.model.create_message_request import CreateMessageRequest
from huaweicloudsdkiotda.v5.model.create_message_response import CreateMessageResponse
from huaweicloudsdkiotda.v5.model.create_or_delete_device_in_group_request import CreateOrDeleteDeviceInGroupRequest
from huaweicloudsdkiotda.v5.model.create_or_delete_device_in_group_response import CreateOrDeleteDeviceInGroupResponse
from huaweicloudsdkiotda.v5.model.create_product_request import CreateProductRequest
from huaweicloudsdkiotda.v5.model.create_product_response import CreateProductResponse
from huaweicloudsdkiotda.v5.model.create_rule_request import CreateRuleRequest
from huaweicloudsdkiotda.v5.model.create_rule_response import CreateRuleResponse
from huaweicloudsdkiotda.v5.model.create_sub_req import CreateSubReq
from huaweicloudsdkiotda.v5.model.create_subscription_request import CreateSubscriptionRequest
from huaweicloudsdkiotda.v5.model.create_subscription_response import CreateSubscriptionResponse
from huaweicloudsdkiotda.v5.model.daily_timer_type import DailyTimerType
from huaweicloudsdkiotda.v5.model.delete_certificate_request import DeleteCertificateRequest
from huaweicloudsdkiotda.v5.model.delete_certificate_response import DeleteCertificateResponse
from huaweicloudsdkiotda.v5.model.delete_device_group_request import DeleteDeviceGroupRequest
from huaweicloudsdkiotda.v5.model.delete_device_group_response import DeleteDeviceGroupResponse
from huaweicloudsdkiotda.v5.model.delete_device_request import DeleteDeviceRequest
from huaweicloudsdkiotda.v5.model.delete_device_response import DeleteDeviceResponse
from huaweicloudsdkiotda.v5.model.delete_product_request import DeleteProductRequest
from huaweicloudsdkiotda.v5.model.delete_product_response import DeleteProductResponse
from huaweicloudsdkiotda.v5.model.delete_rule_request import DeleteRuleRequest
from huaweicloudsdkiotda.v5.model.delete_rule_response import DeleteRuleResponse
from huaweicloudsdkiotda.v5.model.delete_subscription_request import DeleteSubscriptionRequest
from huaweicloudsdkiotda.v5.model.delete_subscription_response import DeleteSubscriptionResponse
from huaweicloudsdkiotda.v5.model.device_command_request import DeviceCommandRequest
from huaweicloudsdkiotda.v5.model.device_command_v5 import DeviceCommandV5
from huaweicloudsdkiotda.v5.model.device_data_condition import DeviceDataCondition
from huaweicloudsdkiotda.v5.model.device_group_response_dto import DeviceGroupResponseDTO
from huaweicloudsdkiotda.v5.model.device_message import DeviceMessage
from huaweicloudsdkiotda.v5.model.device_message_condition import DeviceMessageCondition
from huaweicloudsdkiotda.v5.model.device_message_request import DeviceMessageRequest
from huaweicloudsdkiotda.v5.model.device_properties_request import DevicePropertiesRequest
from huaweicloudsdkiotda.v5.model.device_shadow_data import DeviceShadowData
from huaweicloudsdkiotda.v5.model.device_shadow_properties import DeviceShadowProperties
from huaweicloudsdkiotda.v5.model.device_status_condition import DeviceStatusCondition
from huaweicloudsdkiotda.v5.model.error_info import ErrorInfo
from huaweicloudsdkiotda.v5.model.freeze_device_request import FreezeDeviceRequest
from huaweicloudsdkiotda.v5.model.freeze_device_response import FreezeDeviceResponse
from huaweicloudsdkiotda.v5.model.initial_desired import InitialDesired
from huaweicloudsdkiotda.v5.model.list_batch_tasks_request import ListBatchTasksRequest
from huaweicloudsdkiotda.v5.model.list_batch_tasks_response import ListBatchTasksResponse
from huaweicloudsdkiotda.v5.model.list_certificates_request import ListCertificatesRequest
from huaweicloudsdkiotda.v5.model.list_certificates_response import ListCertificatesResponse
from huaweicloudsdkiotda.v5.model.list_commands_request import ListCommandsRequest
from huaweicloudsdkiotda.v5.model.list_commands_response import ListCommandsResponse
from huaweicloudsdkiotda.v5.model.list_device_groups_request import ListDeviceGroupsRequest
from huaweicloudsdkiotda.v5.model.list_device_groups_response import ListDeviceGroupsResponse
from huaweicloudsdkiotda.v5.model.list_device_messages_request import ListDeviceMessagesRequest
from huaweicloudsdkiotda.v5.model.list_device_messages_response import ListDeviceMessagesResponse
from huaweicloudsdkiotda.v5.model.list_devices_request import ListDevicesRequest
from huaweicloudsdkiotda.v5.model.list_devices_response import ListDevicesResponse
from huaweicloudsdkiotda.v5.model.list_products_request import ListProductsRequest
from huaweicloudsdkiotda.v5.model.list_products_response import ListProductsResponse
from huaweicloudsdkiotda.v5.model.list_properties_request import ListPropertiesRequest
from huaweicloudsdkiotda.v5.model.list_properties_response import ListPropertiesResponse
from huaweicloudsdkiotda.v5.model.list_resources_by_tags_request import ListResourcesByTagsRequest
from huaweicloudsdkiotda.v5.model.list_resources_by_tags_response import ListResourcesByTagsResponse
from huaweicloudsdkiotda.v5.model.list_rules_request import ListRulesRequest
from huaweicloudsdkiotda.v5.model.list_rules_response import ListRulesResponse
from huaweicloudsdkiotda.v5.model.list_subscriptions_request import ListSubscriptionsRequest
from huaweicloudsdkiotda.v5.model.list_subscriptions_response import ListSubscriptionsResponse
from huaweicloudsdkiotda.v5.model.message_result import MessageResult
from huaweicloudsdkiotda.v5.model.net_address import NetAddress
from huaweicloudsdkiotda.v5.model.page import Page
from huaweicloudsdkiotda.v5.model.product_summary import ProductSummary
from huaweicloudsdkiotda.v5.model.property_filter import PropertyFilter
from huaweicloudsdkiotda.v5.model.query_device_simplify import QueryDeviceSimplify
from huaweicloudsdkiotda.v5.model.query_resource_by_tags_dto import QueryResourceByTagsDTO
from huaweicloudsdkiotda.v5.model.reset_device_secret import ResetDeviceSecret
from huaweicloudsdkiotda.v5.model.reset_device_secret_request import ResetDeviceSecretRequest
from huaweicloudsdkiotda.v5.model.reset_device_secret_response import ResetDeviceSecretResponse
from huaweicloudsdkiotda.v5.model.resource_dto import ResourceDTO
from huaweicloudsdkiotda.v5.model.rule import Rule
from huaweicloudsdkiotda.v5.model.rule_action import RuleAction
from huaweicloudsdkiotda.v5.model.rule_condition import RuleCondition
from huaweicloudsdkiotda.v5.model.rule_response import RuleResponse
from huaweicloudsdkiotda.v5.model.rule_status import RuleStatus
from huaweicloudsdkiotda.v5.model.service_capability import ServiceCapability
from huaweicloudsdkiotda.v5.model.service_command import ServiceCommand
from huaweicloudsdkiotda.v5.model.service_command_para import ServiceCommandPara
from huaweicloudsdkiotda.v5.model.service_command_response import ServiceCommandResponse
from huaweicloudsdkiotda.v5.model.service_event import ServiceEvent
from huaweicloudsdkiotda.v5.model.service_property import ServiceProperty
from huaweicloudsdkiotda.v5.model.show_batch_task_request import ShowBatchTaskRequest
from huaweicloudsdkiotda.v5.model.show_batch_task_response import ShowBatchTaskResponse
from huaweicloudsdkiotda.v5.model.show_device_group_request import ShowDeviceGroupRequest
from huaweicloudsdkiotda.v5.model.show_device_group_response import ShowDeviceGroupResponse
from huaweicloudsdkiotda.v5.model.show_device_message_request import ShowDeviceMessageRequest
from huaweicloudsdkiotda.v5.model.show_device_message_response import ShowDeviceMessageResponse
from huaweicloudsdkiotda.v5.model.show_device_request import ShowDeviceRequest
from huaweicloudsdkiotda.v5.model.show_device_response import ShowDeviceResponse
from huaweicloudsdkiotda.v5.model.show_device_shadow_request import ShowDeviceShadowRequest
from huaweicloudsdkiotda.v5.model.show_device_shadow_response import ShowDeviceShadowResponse
from huaweicloudsdkiotda.v5.model.show_devices_in_group_request import ShowDevicesInGroupRequest
from huaweicloudsdkiotda.v5.model.show_devices_in_group_response import ShowDevicesInGroupResponse
from huaweicloudsdkiotda.v5.model.show_product_request import ShowProductRequest
from huaweicloudsdkiotda.v5.model.show_product_response import ShowProductResponse
from huaweicloudsdkiotda.v5.model.show_rule_request import ShowRuleRequest
from huaweicloudsdkiotda.v5.model.show_rule_response import ShowRuleResponse
from huaweicloudsdkiotda.v5.model.show_subscription_request import ShowSubscriptionRequest
from huaweicloudsdkiotda.v5.model.show_subscription_response import ShowSubscriptionResponse
from huaweicloudsdkiotda.v5.model.simple_timer_type import SimpleTimerType
from huaweicloudsdkiotda.v5.model.simplify_device import SimplifyDevice
from huaweicloudsdkiotda.v5.model.strategy import Strategy
from huaweicloudsdkiotda.v5.model.subject import Subject
from huaweicloudsdkiotda.v5.model.subscription_item import SubscriptionItem
from huaweicloudsdkiotda.v5.model.tag_device_request import TagDeviceRequest
from huaweicloudsdkiotda.v5.model.tag_device_response import TagDeviceResponse
from huaweicloudsdkiotda.v5.model.tag_v5_dto import TagV5DTO
from huaweicloudsdkiotda.v5.model.task import Task
from huaweicloudsdkiotda.v5.model.task_detail import TaskDetail
from huaweicloudsdkiotda.v5.model.task_policy import TaskPolicy
from huaweicloudsdkiotda.v5.model.task_progress import TaskProgress
from huaweicloudsdkiotda.v5.model.time_range import TimeRange
from huaweicloudsdkiotda.v5.model.unbind_tags_dto import UnbindTagsDTO
from huaweicloudsdkiotda.v5.model.unfreeze_device_request import UnfreezeDeviceRequest
from huaweicloudsdkiotda.v5.model.unfreeze_device_response import UnfreezeDeviceResponse
from huaweicloudsdkiotda.v5.model.untag_device_request import UntagDeviceRequest
from huaweicloudsdkiotda.v5.model.untag_device_response import UntagDeviceResponse
from huaweicloudsdkiotda.v5.model.update_desired import UpdateDesired
from huaweicloudsdkiotda.v5.model.update_desireds import UpdateDesireds
from huaweicloudsdkiotda.v5.model.update_device import UpdateDevice
from huaweicloudsdkiotda.v5.model.update_device_group_dto import UpdateDeviceGroupDTO
from huaweicloudsdkiotda.v5.model.update_device_group_request import UpdateDeviceGroupRequest
from huaweicloudsdkiotda.v5.model.update_device_group_response import UpdateDeviceGroupResponse
from huaweicloudsdkiotda.v5.model.update_device_request import UpdateDeviceRequest
from huaweicloudsdkiotda.v5.model.update_device_response import UpdateDeviceResponse
from huaweicloudsdkiotda.v5.model.update_device_shadow_desired_data_request import UpdateDeviceShadowDesiredDataRequest
from huaweicloudsdkiotda.v5.model.update_device_shadow_desired_data_response import UpdateDeviceShadowDesiredDataResponse
from huaweicloudsdkiotda.v5.model.update_product import UpdateProduct
from huaweicloudsdkiotda.v5.model.update_product_request import UpdateProductRequest
from huaweicloudsdkiotda.v5.model.update_product_response import UpdateProductResponse
from huaweicloudsdkiotda.v5.model.update_properties_request import UpdatePropertiesRequest
from huaweicloudsdkiotda.v5.model.update_properties_response import UpdatePropertiesResponse
from huaweicloudsdkiotda.v5.model.update_rule_request import UpdateRuleRequest
from huaweicloudsdkiotda.v5.model.update_rule_response import UpdateRuleResponse
from huaweicloudsdkiotda.v5.model.update_sub_req import UpdateSubReq
from huaweicloudsdkiotda.v5.model.update_subscription_request import UpdateSubscriptionRequest
from huaweicloudsdkiotda.v5.model.update_subscription_response import UpdateSubscriptionResponse
from huaweicloudsdkiotda.v5.model.verify_certificate_dto import VerifyCertificateDTO
