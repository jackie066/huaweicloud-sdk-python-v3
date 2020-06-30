# coding: utf-8

from __future__ import absolute_import

# import MeetingClient
from huaweicloudsdkmeeting.v1.meeting_client import MeetingClient
from huaweicloudsdkmeeting.v1.meeting_async_client import MeetingAsyncClient
# import models into sdk package
from huaweicloudsdkmeeting.v1.model.active_dto import ActiveDTO
from huaweicloudsdkmeeting.v1.model.add_corp_admin_request import AddCorpAdminRequest
from huaweicloudsdkmeeting.v1.model.add_corp_admin_response import AddCorpAdminResponse
from huaweicloudsdkmeeting.v1.model.add_corp_dto import AddCorpDTO
from huaweicloudsdkmeeting.v1.model.add_corp_request import AddCorpRequest
from huaweicloudsdkmeeting.v1.model.add_corp_res_dto import AddCorpResDTO
from huaweicloudsdkmeeting.v1.model.add_corp_response import AddCorpResponse
from huaweicloudsdkmeeting.v1.model.add_department_request import AddDepartmentRequest
from huaweicloudsdkmeeting.v1.model.add_department_response import AddDepartmentResponse
from huaweicloudsdkmeeting.v1.model.add_device_dto import AddDeviceDTO
from huaweicloudsdkmeeting.v1.model.add_device_request import AddDeviceRequest
from huaweicloudsdkmeeting.v1.model.add_device_response import AddDeviceResponse
from huaweicloudsdkmeeting.v1.model.add_resource_request import AddResourceRequest
from huaweicloudsdkmeeting.v1.model.add_resource_response import AddResourceResponse
from huaweicloudsdkmeeting.v1.model.add_user_dto import AddUserDTO
from huaweicloudsdkmeeting.v1.model.add_user_request import AddUserRequest
from huaweicloudsdkmeeting.v1.model.add_user_response import AddUserResponse
from huaweicloudsdkmeeting.v1.model.admin_dto import AdminDTO
from huaweicloudsdkmeeting.v1.model.admin_reset_pwd_req_dto import AdminResetPwdReqDTO
from huaweicloudsdkmeeting.v1.model.associate_vmr_request import AssociateVmrRequest
from huaweicloudsdkmeeting.v1.model.associate_vmr_response import AssociateVmrResponse
from huaweicloudsdkmeeting.v1.model.batch_delete_corp_admins_request import BatchDeleteCorpAdminsRequest
from huaweicloudsdkmeeting.v1.model.batch_delete_corp_admins_response import BatchDeleteCorpAdminsResponse
from huaweicloudsdkmeeting.v1.model.batch_delete_devices_request import BatchDeleteDevicesRequest
from huaweicloudsdkmeeting.v1.model.batch_delete_devices_response import BatchDeleteDevicesResponse
from huaweicloudsdkmeeting.v1.model.batch_delete_users_request import BatchDeleteUsersRequest
from huaweicloudsdkmeeting.v1.model.batch_delete_users_response import BatchDeleteUsersResponse
from huaweicloudsdkmeeting.v1.model.batch_update_devices_status_request import BatchUpdateDevicesStatusRequest
from huaweicloudsdkmeeting.v1.model.batch_update_devices_status_response import BatchUpdateDevicesStatusResponse
from huaweicloudsdkmeeting.v1.model.batch_update_user_status_request import BatchUpdateUserStatusRequest
from huaweicloudsdkmeeting.v1.model.batch_update_user_status_response import BatchUpdateUserStatusResponse
from huaweicloudsdkmeeting.v1.model.check_slide_verify_code_request import CheckSlideVerifyCodeRequest
from huaweicloudsdkmeeting.v1.model.check_slide_verify_code_response import CheckSlideVerifyCodeResponse
from huaweicloudsdkmeeting.v1.model.check_token_request import CheckTokenRequest
from huaweicloudsdkmeeting.v1.model.check_token_response import CheckTokenResponse
from huaweicloudsdkmeeting.v1.model.check_veri_code_for_update_user_info_request import CheckVeriCodeForUpdateUserInfoRequest
from huaweicloudsdkmeeting.v1.model.check_veri_code_for_update_user_info_response import CheckVeriCodeForUpdateUserInfoResponse
from huaweicloudsdkmeeting.v1.model.check_verify_code_request import CheckVerifyCodeRequest
from huaweicloudsdkmeeting.v1.model.check_verify_code_response import CheckVerifyCodeResponse
from huaweicloudsdkmeeting.v1.model.corp_admin_dto import CorpAdminDTO
from huaweicloudsdkmeeting.v1.model.corp_basic_dto import CorpBasicDTO
from huaweicloudsdkmeeting.v1.model.corp_basic_info_dto import CorpBasicInfoDTO
from huaweicloudsdkmeeting.v1.model.delete_corp_request import DeleteCorpRequest
from huaweicloudsdkmeeting.v1.model.delete_corp_response import DeleteCorpResponse
from huaweicloudsdkmeeting.v1.model.delete_corp_vmr_request import DeleteCorpVmrRequest
from huaweicloudsdkmeeting.v1.model.delete_corp_vmr_response import DeleteCorpVmrResponse
from huaweicloudsdkmeeting.v1.model.delete_department_request import DeleteDepartmentRequest
from huaweicloudsdkmeeting.v1.model.delete_department_response import DeleteDepartmentResponse
from huaweicloudsdkmeeting.v1.model.delete_resource_request import DeleteResourceRequest
from huaweicloudsdkmeeting.v1.model.delete_resource_response import DeleteResourceResponse
from huaweicloudsdkmeeting.v1.model.dept_basic_dto import DeptBasicDTO
from huaweicloudsdkmeeting.v1.model.dept_dto import DeptDTO
from huaweicloudsdkmeeting.v1.model.disassociate_vmr_request import DisassociateVmrRequest
from huaweicloudsdkmeeting.v1.model.disassociate_vmr_response import DisassociateVmrResponse
from huaweicloudsdkmeeting.v1.model.empty_dto import EmptyDTO
from huaweicloudsdkmeeting.v1.model.id_mark_dto import IdMarkDTO
from huaweicloudsdkmeeting.v1.model.mod_admin_dto import ModAdminDTO
from huaweicloudsdkmeeting.v1.model.mod_corp_basic_dto import ModCorpBasicDTO
from huaweicloudsdkmeeting.v1.model.mod_corp_basic_info_dto import ModCorpBasicInfoDTO
from huaweicloudsdkmeeting.v1.model.mod_corp_dto import ModCorpDTO
from huaweicloudsdkmeeting.v1.model.mod_dept_dto import ModDeptDTO
from huaweicloudsdkmeeting.v1.model.mod_device_dto import ModDeviceDTO
from huaweicloudsdkmeeting.v1.model.mod_member_dto import ModMemberDTO
from huaweicloudsdkmeeting.v1.model.mod_pwd_req_dto import ModPwdReqDTO
from huaweicloudsdkmeeting.v1.model.mod_resource_dto import ModResourceDTO
from huaweicloudsdkmeeting.v1.model.mod_user_dto import ModUserDTO
from huaweicloudsdkmeeting.v1.model.mod_vmr_dto import ModVmrDTO
from huaweicloudsdkmeeting.v1.model.pages import Pages
from huaweicloudsdkmeeting.v1.model.query_admin_result_dto import QueryAdminResultDTO
from huaweicloudsdkmeeting.v1.model.query_corp_admin_result_dto import QueryCorpAdminResultDTO
from huaweicloudsdkmeeting.v1.model.query_corp_basic_result_dto import QueryCorpBasicResultDTO
from huaweicloudsdkmeeting.v1.model.query_corp_res_result_dto import QueryCorpResResultDTO
from huaweicloudsdkmeeting.v1.model.query_corp_result_dto import QueryCorpResultDTO
from huaweicloudsdkmeeting.v1.model.query_corp_vc_res_result_dto import QueryCorpVcResResultDTO
from huaweicloudsdkmeeting.v1.model.query_dept_result_dto import QueryDeptResultDTO
from huaweicloudsdkmeeting.v1.model.query_device_result_dto import QueryDeviceResultDTO
from huaweicloudsdkmeeting.v1.model.query_device_type_result_dto import QueryDeviceTypeResultDTO
from huaweicloudsdkmeeting.v1.model.query_org_vmr_result_dto import QueryOrgVmrResultDTO
from huaweicloudsdkmeeting.v1.model.query_resource_result_dto import QueryResourceResultDTO
from huaweicloudsdkmeeting.v1.model.query_vmr_pkg_res_result_dto import QueryVmrPkgResResultDTO
from huaweicloudsdkmeeting.v1.model.query_vmr_result_dto import QueryVmrResultDTO
from huaweicloudsdkmeeting.v1.model.res_detail_dto import ResDetailDTO
from huaweicloudsdkmeeting.v1.model.reset_activecode_request import ResetActivecodeRequest
from huaweicloudsdkmeeting.v1.model.reset_activecode_response import ResetActivecodeResponse
from huaweicloudsdkmeeting.v1.model.reset_pwd_by_admin_request import ResetPwdByAdminRequest
from huaweicloudsdkmeeting.v1.model.reset_pwd_by_admin_response import ResetPwdByAdminResponse
from huaweicloudsdkmeeting.v1.model.reset_pwd_req_dtov1 import ResetPwdReqDTOV1
from huaweicloudsdkmeeting.v1.model.reset_pwd_request import ResetPwdRequest
from huaweicloudsdkmeeting.v1.model.reset_pwd_response import ResetPwdResponse
from huaweicloudsdkmeeting.v1.model.resource_dto import ResourceDTO
from huaweicloudsdkmeeting.v1.model.search_corp_admins_request import SearchCorpAdminsRequest
from huaweicloudsdkmeeting.v1.model.search_corp_admins_response import SearchCorpAdminsResponse
from huaweicloudsdkmeeting.v1.model.search_corp_dir_request import SearchCorpDirRequest
from huaweicloudsdkmeeting.v1.model.search_corp_dir_response import SearchCorpDirResponse
from huaweicloudsdkmeeting.v1.model.search_corp_request import SearchCorpRequest
from huaweicloudsdkmeeting.v1.model.search_corp_response import SearchCorpResponse
from huaweicloudsdkmeeting.v1.model.search_corp_vmr_request import SearchCorpVmrRequest
from huaweicloudsdkmeeting.v1.model.search_corp_vmr_response import SearchCorpVmrResponse
from huaweicloudsdkmeeting.v1.model.search_department_by_name_request import SearchDepartmentByNameRequest
from huaweicloudsdkmeeting.v1.model.search_department_by_name_response import SearchDepartmentByNameResponse
from huaweicloudsdkmeeting.v1.model.search_devices_request import SearchDevicesRequest
from huaweicloudsdkmeeting.v1.model.search_devices_response import SearchDevicesResponse
from huaweicloudsdkmeeting.v1.model.search_member_vmr_request import SearchMemberVmrRequest
from huaweicloudsdkmeeting.v1.model.search_member_vmr_response import SearchMemberVmrResponse
from huaweicloudsdkmeeting.v1.model.search_resource_op_record_request import SearchResourceOpRecordRequest
from huaweicloudsdkmeeting.v1.model.search_resource_op_record_response import SearchResourceOpRecordResponse
from huaweicloudsdkmeeting.v1.model.search_resource_request import SearchResourceRequest
from huaweicloudsdkmeeting.v1.model.search_resource_response import SearchResourceResponse
from huaweicloudsdkmeeting.v1.model.search_user_result_dto import SearchUserResultDTO
from huaweicloudsdkmeeting.v1.model.search_users_request import SearchUsersRequest
from huaweicloudsdkmeeting.v1.model.search_users_response import SearchUsersResponse
from huaweicloudsdkmeeting.v1.model.send_slide_verify_code_request import SendSlideVerifyCodeRequest
from huaweicloudsdkmeeting.v1.model.send_slide_verify_code_response import SendSlideVerifyCodeResponse
from huaweicloudsdkmeeting.v1.model.send_veri_code_for_change_pwd_request import SendVeriCodeForChangePwdRequest
from huaweicloudsdkmeeting.v1.model.send_veri_code_for_change_pwd_response import SendVeriCodeForChangePwdResponse
from huaweicloudsdkmeeting.v1.model.send_veri_code_for_update_user_info_request import SendVeriCodeForUpdateUserInfoRequest
from huaweicloudsdkmeeting.v1.model.send_veri_code_for_update_user_info_response import SendVeriCodeForUpdateUserInfoResponse
from huaweicloudsdkmeeting.v1.model.show_corp_admin_request import ShowCorpAdminRequest
from huaweicloudsdkmeeting.v1.model.show_corp_admin_response import ShowCorpAdminResponse
from huaweicloudsdkmeeting.v1.model.show_corp_basic_info_request import ShowCorpBasicInfoRequest
from huaweicloudsdkmeeting.v1.model.show_corp_basic_info_response import ShowCorpBasicInfoResponse
from huaweicloudsdkmeeting.v1.model.show_corp_request import ShowCorpRequest
from huaweicloudsdkmeeting.v1.model.show_corp_resource_request import ShowCorpResourceRequest
from huaweicloudsdkmeeting.v1.model.show_corp_resource_response import ShowCorpResourceResponse
from huaweicloudsdkmeeting.v1.model.show_corp_response import ShowCorpResponse
from huaweicloudsdkmeeting.v1.model.show_dept_and_child_dept_request import ShowDeptAndChildDeptRequest
from huaweicloudsdkmeeting.v1.model.show_dept_and_child_dept_response import ShowDeptAndChildDeptResponse
from huaweicloudsdkmeeting.v1.model.show_device_detail_request import ShowDeviceDetailRequest
from huaweicloudsdkmeeting.v1.model.show_device_detail_response import ShowDeviceDetailResponse
from huaweicloudsdkmeeting.v1.model.show_device_status_request import ShowDeviceStatusRequest
from huaweicloudsdkmeeting.v1.model.show_device_status_response import ShowDeviceStatusResponse
from huaweicloudsdkmeeting.v1.model.show_device_types_request import ShowDeviceTypesRequest
from huaweicloudsdkmeeting.v1.model.show_device_types_response import ShowDeviceTypesResponse
from huaweicloudsdkmeeting.v1.model.show_my_info_request import ShowMyInfoRequest
from huaweicloudsdkmeeting.v1.model.show_my_info_response import ShowMyInfoResponse
from huaweicloudsdkmeeting.v1.model.show_user_detail_request import ShowUserDetailRequest
from huaweicloudsdkmeeting.v1.model.show_user_detail_response import ShowUserDetailResponse
from huaweicloudsdkmeeting.v1.model.slide_verify_code_check_dto import SlideVerifyCodeCheckDTO
from huaweicloudsdkmeeting.v1.model.slide_verify_code_send_dto import SlideVerifyCodeSendDTO
from huaweicloudsdkmeeting.v1.model.update_contact_request import UpdateContactRequest
from huaweicloudsdkmeeting.v1.model.update_contact_response import UpdateContactResponse
from huaweicloudsdkmeeting.v1.model.update_corp_basic_info_request import UpdateCorpBasicInfoRequest
from huaweicloudsdkmeeting.v1.model.update_corp_basic_info_response import UpdateCorpBasicInfoResponse
from huaweicloudsdkmeeting.v1.model.update_corp_request import UpdateCorpRequest
from huaweicloudsdkmeeting.v1.model.update_corp_response import UpdateCorpResponse
from huaweicloudsdkmeeting.v1.model.update_department_request import UpdateDepartmentRequest
from huaweicloudsdkmeeting.v1.model.update_department_response import UpdateDepartmentResponse
from huaweicloudsdkmeeting.v1.model.update_device_request import UpdateDeviceRequest
from huaweicloudsdkmeeting.v1.model.update_device_response import UpdateDeviceResponse
from huaweicloudsdkmeeting.v1.model.update_member_vmr_request import UpdateMemberVmrRequest
from huaweicloudsdkmeeting.v1.model.update_member_vmr_response import UpdateMemberVmrResponse
from huaweicloudsdkmeeting.v1.model.update_my_info_request import UpdateMyInfoRequest
from huaweicloudsdkmeeting.v1.model.update_my_info_response import UpdateMyInfoResponse
from huaweicloudsdkmeeting.v1.model.update_pwd_request import UpdatePwdRequest
from huaweicloudsdkmeeting.v1.model.update_pwd_response import UpdatePwdResponse
from huaweicloudsdkmeeting.v1.model.update_resource_request import UpdateResourceRequest
from huaweicloudsdkmeeting.v1.model.update_resource_response import UpdateResourceResponse
from huaweicloudsdkmeeting.v1.model.update_token_request import UpdateTokenRequest
from huaweicloudsdkmeeting.v1.model.update_token_response import UpdateTokenResponse
from huaweicloudsdkmeeting.v1.model.update_user_request import UpdateUserRequest
from huaweicloudsdkmeeting.v1.model.update_user_response import UpdateUserResponse
from huaweicloudsdkmeeting.v1.model.user_dto import UserDTO
from huaweicloudsdkmeeting.v1.model.user_function_dto import UserFunctionDTO
from huaweicloudsdkmeeting.v1.model.user_info import UserInfo
from huaweicloudsdkmeeting.v1.model.user_status_dto import UserStatusDTO
from huaweicloudsdkmeeting.v1.model.user_vmr_dto import UserVmrDTO
from huaweicloudsdkmeeting.v1.model.validate_token_req_dto import ValidateTokenReqDTO
from huaweicloudsdkmeeting.v1.model.verification_code_dto import VerificationCodeDTO
from huaweicloudsdkmeeting.v1.model.verify_code_check_dto import VerifyCodeCheckDTO
from huaweicloudsdkmeeting.v1.model.verify_code_send_dtov1 import VerifyCodeSendDTOV1

