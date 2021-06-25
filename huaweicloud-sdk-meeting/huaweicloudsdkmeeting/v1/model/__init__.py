# coding: utf-8

from __future__ import absolute_import

# import models into model package
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
from huaweicloudsdkmeeting.v1.model.add_program_request import AddProgramRequest
from huaweicloudsdkmeeting.v1.model.add_program_response import AddProgramResponse
from huaweicloudsdkmeeting.v1.model.add_publication_request import AddPublicationRequest
from huaweicloudsdkmeeting.v1.model.add_publication_response import AddPublicationResponse
from huaweicloudsdkmeeting.v1.model.add_resource_request import AddResourceRequest
from huaweicloudsdkmeeting.v1.model.add_resource_response import AddResourceResponse
from huaweicloudsdkmeeting.v1.model.add_to_personal_space_request import AddToPersonalSpaceRequest
from huaweicloudsdkmeeting.v1.model.add_to_personal_space_response import AddToPersonalSpaceResponse
from huaweicloudsdkmeeting.v1.model.add_user_dto import AddUserDTO
from huaweicloudsdkmeeting.v1.model.add_user_request import AddUserRequest
from huaweicloudsdkmeeting.v1.model.add_user_request_body import AddUserRequestBody
from huaweicloudsdkmeeting.v1.model.add_user_response import AddUserResponse
from huaweicloudsdkmeeting.v1.model.admin_dto import AdminDTO
from huaweicloudsdkmeeting.v1.model.admin_reset_pwd_req_dto import AdminResetPwdReqDTO
from huaweicloudsdkmeeting.v1.model.allow_guest_unmute_request import AllowGuestUnmuteRequest
from huaweicloudsdkmeeting.v1.model.allow_guest_unmute_response import AllowGuestUnmuteResponse
from huaweicloudsdkmeeting.v1.model.associate_vmr_request import AssociateVmrRequest
from huaweicloudsdkmeeting.v1.model.associate_vmr_response import AssociateVmrResponse
from huaweicloudsdkmeeting.v1.model.attendee import Attendee
from huaweicloudsdkmeeting.v1.model.base_user import BaseUser
from huaweicloudsdkmeeting.v1.model.batch_delete_corp_admins_request import BatchDeleteCorpAdminsRequest
from huaweicloudsdkmeeting.v1.model.batch_delete_corp_admins_response import BatchDeleteCorpAdminsResponse
from huaweicloudsdkmeeting.v1.model.batch_delete_devices_request import BatchDeleteDevicesRequest
from huaweicloudsdkmeeting.v1.model.batch_delete_devices_response import BatchDeleteDevicesResponse
from huaweicloudsdkmeeting.v1.model.batch_delete_materials_request import BatchDeleteMaterialsRequest
from huaweicloudsdkmeeting.v1.model.batch_delete_materials_response import BatchDeleteMaterialsResponse
from huaweicloudsdkmeeting.v1.model.batch_delete_programs_request import BatchDeleteProgramsRequest
from huaweicloudsdkmeeting.v1.model.batch_delete_programs_response import BatchDeleteProgramsResponse
from huaweicloudsdkmeeting.v1.model.batch_delete_publications_request import BatchDeletePublicationsRequest
from huaweicloudsdkmeeting.v1.model.batch_delete_publications_response import BatchDeletePublicationsResponse
from huaweicloudsdkmeeting.v1.model.batch_delete_users_request import BatchDeleteUsersRequest
from huaweicloudsdkmeeting.v1.model.batch_delete_users_response import BatchDeleteUsersResponse
from huaweicloudsdkmeeting.v1.model.batch_update_devices_status_request import BatchUpdateDevicesStatusRequest
from huaweicloudsdkmeeting.v1.model.batch_update_devices_status_response import BatchUpdateDevicesStatusResponse
from huaweicloudsdkmeeting.v1.model.batch_update_user_status_request import BatchUpdateUserStatusRequest
from huaweicloudsdkmeeting.v1.model.batch_update_user_status_response import BatchUpdateUserStatusResponse
from huaweicloudsdkmeeting.v1.model.broadcast_participant_request import BroadcastParticipantRequest
from huaweicloudsdkmeeting.v1.model.broadcast_participant_response import BroadcastParticipantResponse
from huaweicloudsdkmeeting.v1.model.cancel_meeting_request import CancelMeetingRequest
from huaweicloudsdkmeeting.v1.model.cancel_meeting_response import CancelMeetingResponse
from huaweicloudsdkmeeting.v1.model.category_suggestions import CategorySuggestions
from huaweicloudsdkmeeting.v1.model.check_slide_verify_code_request import CheckSlideVerifyCodeRequest
from huaweicloudsdkmeeting.v1.model.check_slide_verify_code_response import CheckSlideVerifyCodeResponse
from huaweicloudsdkmeeting.v1.model.check_token_request import CheckTokenRequest
from huaweicloudsdkmeeting.v1.model.check_token_response import CheckTokenResponse
from huaweicloudsdkmeeting.v1.model.check_veri_code_for_update_user_info_request import CheckVeriCodeForUpdateUserInfoRequest
from huaweicloudsdkmeeting.v1.model.check_veri_code_for_update_user_info_response import CheckVeriCodeForUpdateUserInfoResponse
from huaweicloudsdkmeeting.v1.model.check_verify_code_request import CheckVerifyCodeRequest
from huaweicloudsdkmeeting.v1.model.check_verify_code_response import CheckVerifyCodeResponse
from huaweicloudsdkmeeting.v1.model.conf_attendee_record_info import ConfAttendeeRecordInfo
from huaweicloudsdkmeeting.v1.model.conf_ctl_record_info import ConfCtlRecordInfo
from huaweicloudsdkmeeting.v1.model.conference_info import ConferenceInfo
from huaweicloudsdkmeeting.v1.model.corp_admin_dto import CorpAdminDTO
from huaweicloudsdkmeeting.v1.model.corp_basic_dto import CorpBasicDTO
from huaweicloudsdkmeeting.v1.model.corp_basic_info_dto import CorpBasicInfoDTO
from huaweicloudsdkmeeting.v1.model.create_anonymous_auth_random_request import CreateAnonymousAuthRandomRequest
from huaweicloudsdkmeeting.v1.model.create_anonymous_auth_random_response import CreateAnonymousAuthRandomResponse
from huaweicloudsdkmeeting.v1.model.create_conf_token_request import CreateConfTokenRequest
from huaweicloudsdkmeeting.v1.model.create_conf_token_response import CreateConfTokenResponse
from huaweicloudsdkmeeting.v1.model.create_meeting_request import CreateMeetingRequest
from huaweicloudsdkmeeting.v1.model.create_meeting_response import CreateMeetingResponse
from huaweicloudsdkmeeting.v1.model.create_portal_ref_nonce_request import CreatePortalRefNonceRequest
from huaweicloudsdkmeeting.v1.model.create_portal_ref_nonce_response import CreatePortalRefNonceResponse
from huaweicloudsdkmeeting.v1.model.create_program_request_dto import CreateProgramRequestDTO
from huaweicloudsdkmeeting.v1.model.create_publication_request_dto import CreatePublicationRequestDTO
from huaweicloudsdkmeeting.v1.model.create_vision_active_code_request import CreateVisionActiveCodeRequest
from huaweicloudsdkmeeting.v1.model.create_vision_active_code_response import CreateVisionActiveCodeResponse
from huaweicloudsdkmeeting.v1.model.create_web_socket_token_request import CreateWebSocketTokenRequest
from huaweicloudsdkmeeting.v1.model.create_web_socket_token_response import CreateWebSocketTokenResponse
from huaweicloudsdkmeeting.v1.model.create_webinar_request import CreateWebinarRequest
from huaweicloudsdkmeeting.v1.model.create_webinar_response import CreateWebinarResponse
from huaweicloudsdkmeeting.v1.model.cycle_params import CycleParams
from huaweicloudsdkmeeting.v1.model.del_attend_info import DelAttendInfo
from huaweicloudsdkmeeting.v1.model.delete_attendees_request import DeleteAttendeesRequest
from huaweicloudsdkmeeting.v1.model.delete_attendees_response import DeleteAttendeesResponse
from huaweicloudsdkmeeting.v1.model.delete_corp_request import DeleteCorpRequest
from huaweicloudsdkmeeting.v1.model.delete_corp_response import DeleteCorpResponse
from huaweicloudsdkmeeting.v1.model.delete_corp_vmr_request import DeleteCorpVmrRequest
from huaweicloudsdkmeeting.v1.model.delete_corp_vmr_response import DeleteCorpVmrResponse
from huaweicloudsdkmeeting.v1.model.delete_department_request import DeleteDepartmentRequest
from huaweicloudsdkmeeting.v1.model.delete_department_response import DeleteDepartmentResponse
from huaweicloudsdkmeeting.v1.model.delete_recordings_request import DeleteRecordingsRequest
from huaweicloudsdkmeeting.v1.model.delete_recordings_response import DeleteRecordingsResponse
from huaweicloudsdkmeeting.v1.model.delete_resource_request import DeleteResourceRequest
from huaweicloudsdkmeeting.v1.model.delete_resource_response import DeleteResourceResponse
from huaweicloudsdkmeeting.v1.model.delete_vision_active_code_request import DeleteVisionActiveCodeRequest
from huaweicloudsdkmeeting.v1.model.delete_vision_active_code_response import DeleteVisionActiveCodeResponse
from huaweicloudsdkmeeting.v1.model.delete_webinar_request import DeleteWebinarRequest
from huaweicloudsdkmeeting.v1.model.delete_webinar_response import DeleteWebinarResponse
from huaweicloudsdkmeeting.v1.model.dept_basic_dto import DeptBasicDTO
from huaweicloudsdkmeeting.v1.model.dept_dto import DeptDTO
from huaweicloudsdkmeeting.v1.model.disassociate_vmr_request import DisassociateVmrRequest
from huaweicloudsdkmeeting.v1.model.disassociate_vmr_response import DisassociateVmrResponse
from huaweicloudsdkmeeting.v1.model.hand_request import HandRequest
from huaweicloudsdkmeeting.v1.model.hand_response import HandResponse
from huaweicloudsdkmeeting.v1.model.hang_up_request import HangUpRequest
from huaweicloudsdkmeeting.v1.model.hang_up_response import HangUpResponse
from huaweicloudsdkmeeting.v1.model.id_mark_dto import IdMarkDTO
from huaweicloudsdkmeeting.v1.model.image_moderation_result import ImageModerationResult
from huaweicloudsdkmeeting.v1.model.invite_participant_request import InviteParticipantRequest
from huaweicloudsdkmeeting.v1.model.invite_participant_response import InviteParticipantResponse
from huaweicloudsdkmeeting.v1.model.invite_share_dto import InviteShareDTO
from huaweicloudsdkmeeting.v1.model.invite_share_request import InviteShareRequest
from huaweicloudsdkmeeting.v1.model.invite_share_response import InviteShareResponse
from huaweicloudsdkmeeting.v1.model.invite_user_request import InviteUserRequest
from huaweicloudsdkmeeting.v1.model.invite_user_response import InviteUserResponse
from huaweicloudsdkmeeting.v1.model.invite_with_pwd_request import InviteWithPwdRequest
from huaweicloudsdkmeeting.v1.model.invite_with_pwd_response import InviteWithPwdResponse
from huaweicloudsdkmeeting.v1.model.list_history_webinars_request import ListHistoryWebinarsRequest
from huaweicloudsdkmeeting.v1.model.list_history_webinars_response import ListHistoryWebinarsResponse
from huaweicloudsdkmeeting.v1.model.list_meeting_file_response_dto import ListMeetingFileResponseDTO
from huaweicloudsdkmeeting.v1.model.list_ongoing_webinars_request import ListOngoingWebinarsRequest
from huaweicloudsdkmeeting.v1.model.list_ongoing_webinars_response import ListOngoingWebinarsResponse
from huaweicloudsdkmeeting.v1.model.list_up_coming_webinars_request import ListUpComingWebinarsRequest
from huaweicloudsdkmeeting.v1.model.list_up_coming_webinars_response import ListUpComingWebinarsResponse
from huaweicloudsdkmeeting.v1.model.live_request import LiveRequest
from huaweicloudsdkmeeting.v1.model.live_response import LiveResponse
from huaweicloudsdkmeeting.v1.model.lock_meeting_request import LockMeetingRequest
from huaweicloudsdkmeeting.v1.model.lock_meeting_response import LockMeetingResponse
from huaweicloudsdkmeeting.v1.model.lock_view_request import LockViewRequest
from huaweicloudsdkmeeting.v1.model.lock_view_response import LockViewResponse
from huaweicloudsdkmeeting.v1.model.material import Material
from huaweicloudsdkmeeting.v1.model.meeting_file_base import MeetingFileBase
from huaweicloudsdkmeeting.v1.model.meeting_status import MeetingStatus
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
from huaweicloudsdkmeeting.v1.model.mute_meeting_request import MuteMeetingRequest
from huaweicloudsdkmeeting.v1.model.mute_meeting_response import MuteMeetingResponse
from huaweicloudsdkmeeting.v1.model.mute_participant_request import MuteParticipantRequest
from huaweicloudsdkmeeting.v1.model.mute_participant_response import MuteParticipantResponse
from huaweicloudsdkmeeting.v1.model.open_attendee_entity import OpenAttendeeEntity
from huaweicloudsdkmeeting.v1.model.open_edit_conf_req import OpenEditConfReq
from huaweicloudsdkmeeting.v1.model.open_notify_setting import OpenNotifySetting
from huaweicloudsdkmeeting.v1.model.open_page_info import OpenPageInfo
from huaweicloudsdkmeeting.v1.model.open_room_setting_req import OpenRoomSettingReq
from huaweicloudsdkmeeting.v1.model.open_room_setting_vo import OpenRoomSettingVO
from huaweicloudsdkmeeting.v1.model.open_schedule_conf_req import OpenScheduleConfReq
from huaweicloudsdkmeeting.v1.model.open_upload_file_info import OpenUploadFileInfo
from huaweicloudsdkmeeting.v1.model.open_webinar_base_info import OpenWebinarBaseInfo
from huaweicloudsdkmeeting.v1.model.open_webinar_history_info import OpenWebinarHistoryInfo
from huaweicloudsdkmeeting.v1.model.open_webinar_ongoing_info import OpenWebinarOngoingInfo
from huaweicloudsdkmeeting.v1.model.open_webinar_upcoming_info import OpenWebinarUpcomingInfo
from huaweicloudsdkmeeting.v1.model.org_group_dto import OrgGroupDTO
from huaweicloudsdkmeeting.v1.model.org_property_dto import OrgPropertyDTO
from huaweicloudsdkmeeting.v1.model.page_participant import PageParticipant
from huaweicloudsdkmeeting.v1.model.pages import Pages
from huaweicloudsdkmeeting.v1.model.part_attendee import PartAttendee
from huaweicloudsdkmeeting.v1.model.participant_info import ParticipantInfo
from huaweicloudsdkmeeting.v1.model.password_entry import PasswordEntry
from huaweicloudsdkmeeting.v1.model.pic_layout_info import PicLayoutInfo
from huaweicloudsdkmeeting.v1.model.program_item_request_base import ProgramItemRequestBase
from huaweicloudsdkmeeting.v1.model.program_item_response_base import ProgramItemResponseBase
from huaweicloudsdkmeeting.v1.model.program_request_base import ProgramRequestBase
from huaweicloudsdkmeeting.v1.model.program_response_base import ProgramResponseBase
from huaweicloudsdkmeeting.v1.model.prolong_meeting_request import ProlongMeetingRequest
from huaweicloudsdkmeeting.v1.model.prolong_meeting_response import ProlongMeetingResponse
from huaweicloudsdkmeeting.v1.model.proxy_token_dto import ProxyTokenDTO
from huaweicloudsdkmeeting.v1.model.publication_request_base import PublicationRequestBase
from huaweicloudsdkmeeting.v1.model.publication_response_base import PublicationResponseBase
from huaweicloudsdkmeeting.v1.model.publish_dept_response_dto import PublishDeptResponseDTO
from huaweicloudsdkmeeting.v1.model.publish_device_response_dto import PublishDeviceResponseDTO
from huaweicloudsdkmeeting.v1.model.qos_conference_info import QosConferenceInfo
from huaweicloudsdkmeeting.v1.model.qos_cpu_info import QosCpuInfo
from huaweicloudsdkmeeting.v1.model.qos_data_element import QosDataElement
from huaweicloudsdkmeeting.v1.model.qos_data_no_thr_element import QosDataNoThrElement
from huaweicloudsdkmeeting.v1.model.qos_info import QosInfo
from huaweicloudsdkmeeting.v1.model.qos_participant_info import QosParticipantInfo
from huaweicloudsdkmeeting.v1.model.qos_send_receive_info import QosSendReceiveInfo
from huaweicloudsdkmeeting.v1.model.query_admin_result_dto import QueryAdminResultDTO
from huaweicloudsdkmeeting.v1.model.query_corp_admin_result_dto import QueryCorpAdminResultDTO
from huaweicloudsdkmeeting.v1.model.query_corp_basic_result_dto import QueryCorpBasicResultDTO
from huaweicloudsdkmeeting.v1.model.query_corp_group_dto import QueryCorpGroupDTO
from huaweicloudsdkmeeting.v1.model.query_corp_res_result_dto import QueryCorpResResultDTO
from huaweicloudsdkmeeting.v1.model.query_corp_result_dto import QueryCorpResultDTO
from huaweicloudsdkmeeting.v1.model.query_corp_vc_res_result_dto import QueryCorpVcResResultDTO
from huaweicloudsdkmeeting.v1.model.query_dept_result_dto import QueryDeptResultDTO
from huaweicloudsdkmeeting.v1.model.query_device_info_result_dto import QueryDeviceInfoResultDTO
from huaweicloudsdkmeeting.v1.model.query_device_result_dto import QueryDeviceResultDTO
from huaweicloudsdkmeeting.v1.model.query_device_type_result_dto import QueryDeviceTypeResultDTO
from huaweicloudsdkmeeting.v1.model.query_org_vmr_result_dto import QueryOrgVmrResultDTO
from huaweicloudsdkmeeting.v1.model.query_resource_result_dto import QueryResourceResultDTO
from huaweicloudsdkmeeting.v1.model.query_vision_active_code_result_dto import QueryVisionActiveCodeResultDTO
from huaweicloudsdkmeeting.v1.model.query_vmr_pkg_res_result_dto import QueryVmrPkgResResultDTO
from huaweicloudsdkmeeting.v1.model.query_vmr_result_dto import QueryVmrResultDTO
from huaweicloudsdkmeeting.v1.model.real_time_attendee import RealTimeAttendee
from huaweicloudsdkmeeting.v1.model.real_time_conf_info import RealTimeConfInfo
from huaweicloudsdkmeeting.v1.model.real_time_participant import RealTimeParticipant
from huaweicloudsdkmeeting.v1.model.record_download_info_bo import RecordDownloadInfoBO
from huaweicloudsdkmeeting.v1.model.record_download_url_do import RecordDownloadUrlDO
from huaweicloudsdkmeeting.v1.model.record_request import RecordRequest
from huaweicloudsdkmeeting.v1.model.record_response import RecordResponse
from huaweicloudsdkmeeting.v1.model.record_result_do import RecordResultDO
from huaweicloudsdkmeeting.v1.model.rename_participant_request import RenameParticipantRequest
from huaweicloudsdkmeeting.v1.model.rename_participant_response import RenameParticipantResponse
from huaweicloudsdkmeeting.v1.model.res_detail_dto import ResDetailDTO
from huaweicloudsdkmeeting.v1.model.reset_activecode_request import ResetActivecodeRequest
from huaweicloudsdkmeeting.v1.model.reset_activecode_response import ResetActivecodeResponse
from huaweicloudsdkmeeting.v1.model.reset_pwd_by_admin_request import ResetPwdByAdminRequest
from huaweicloudsdkmeeting.v1.model.reset_pwd_by_admin_response import ResetPwdByAdminResponse
from huaweicloudsdkmeeting.v1.model.reset_pwd_req_dtov1 import ResetPwdReqDTOV1
from huaweicloudsdkmeeting.v1.model.reset_pwd_request import ResetPwdRequest
from huaweicloudsdkmeeting.v1.model.reset_pwd_response import ResetPwdResponse
from huaweicloudsdkmeeting.v1.model.reset_vision_active_code_request import ResetVisionActiveCodeRequest
from huaweicloudsdkmeeting.v1.model.reset_vision_active_code_response import ResetVisionActiveCodeResponse
from huaweicloudsdkmeeting.v1.model.resource_dto import ResourceDTO
from huaweicloudsdkmeeting.v1.model.rest_allow_un_mute_req_body import RestAllowUnMuteReqBody
from huaweicloudsdkmeeting.v1.model.rest_attendee_dto import RestAttendeeDTO
from huaweicloudsdkmeeting.v1.model.rest_bulk_del_attend_req_body import RestBulkDelAttendReqBody
from huaweicloudsdkmeeting.v1.model.rest_bulk_hang_up_req_body import RestBulkHangUpReqBody
from huaweicloudsdkmeeting.v1.model.rest_chair_token_req_body import RestChairTokenReqBody
from huaweicloudsdkmeeting.v1.model.rest_chair_view_req_body import RestChairViewReqBody
from huaweicloudsdkmeeting.v1.model.rest_conf_config_dto import RestConfConfigDTO
from huaweicloudsdkmeeting.v1.model.rest_custom_multi_picture_body import RestCustomMultiPictureBody
from huaweicloudsdkmeeting.v1.model.rest_hands_up_req_body import RestHandsUpReqBody
from huaweicloudsdkmeeting.v1.model.rest_invite_req_body import RestInviteReqBody
from huaweicloudsdkmeeting.v1.model.rest_invite_with_pwd_req_body import RestInviteWithPwdReqBody
from huaweicloudsdkmeeting.v1.model.rest_lock_req_body import RestLockReqBody
from huaweicloudsdkmeeting.v1.model.rest_lock_site_view_req_body import RestLockSiteViewReqBody
from huaweicloudsdkmeeting.v1.model.rest_mixed_picture_body import RestMixedPictureBody
from huaweicloudsdkmeeting.v1.model.rest_mute_participant_req_body import RestMuteParticipantReqBody
from huaweicloudsdkmeeting.v1.model.rest_mute_req_body import RestMuteReqBody
from huaweicloudsdkmeeting.v1.model.rest_participant_view_req_body import RestParticipantViewReqBody
from huaweicloudsdkmeeting.v1.model.rest_prolong_dur_req_body import RestProlongDurReqBody
from huaweicloudsdkmeeting.v1.model.rest_rename_part_req_body import RestRenamePartReqBody
from huaweicloudsdkmeeting.v1.model.rest_schedule_conf_dto import RestScheduleConfDTO
from huaweicloudsdkmeeting.v1.model.rest_set_live_req_body import RestSetLiveReqBody
from huaweicloudsdkmeeting.v1.model.rest_set_record_req_body import RestSetRecordReqBody
from huaweicloudsdkmeeting.v1.model.rest_subscriber_in_pic import RestSubscriberInPic
from huaweicloudsdkmeeting.v1.model.rest_switch_mode_req_body import RestSwitchModeReqBody
from huaweicloudsdkmeeting.v1.model.rollcall_participant_request import RollcallParticipantRequest
from huaweicloudsdkmeeting.v1.model.rollcall_participant_response import RollcallParticipantResponse
from huaweicloudsdkmeeting.v1.model.search_attendance_records_of_his_meeting_request import SearchAttendanceRecordsOfHisMeetingRequest
from huaweicloudsdkmeeting.v1.model.search_attendance_records_of_his_meeting_response import SearchAttendanceRecordsOfHisMeetingResponse
from huaweicloudsdkmeeting.v1.model.search_corp_admins_request import SearchCorpAdminsRequest
from huaweicloudsdkmeeting.v1.model.search_corp_admins_response import SearchCorpAdminsResponse
from huaweicloudsdkmeeting.v1.model.search_corp_dir_request import SearchCorpDirRequest
from huaweicloudsdkmeeting.v1.model.search_corp_dir_response import SearchCorpDirResponse
from huaweicloudsdkmeeting.v1.model.search_corp_request import SearchCorpRequest
from huaweicloudsdkmeeting.v1.model.search_corp_resources_request import SearchCorpResourcesRequest
from huaweicloudsdkmeeting.v1.model.search_corp_resources_response import SearchCorpResourcesResponse
from huaweicloudsdkmeeting.v1.model.search_corp_response import SearchCorpResponse
from huaweicloudsdkmeeting.v1.model.search_corp_vmr_request import SearchCorpVmrRequest
from huaweicloudsdkmeeting.v1.model.search_corp_vmr_response import SearchCorpVmrResponse
from huaweicloudsdkmeeting.v1.model.search_ctl_records_of_his_meeting_request import SearchCtlRecordsOfHisMeetingRequest
from huaweicloudsdkmeeting.v1.model.search_ctl_records_of_his_meeting_response import SearchCtlRecordsOfHisMeetingResponse
from huaweicloudsdkmeeting.v1.model.search_department_by_name_request import SearchDepartmentByNameRequest
from huaweicloudsdkmeeting.v1.model.search_department_by_name_response import SearchDepartmentByNameResponse
from huaweicloudsdkmeeting.v1.model.search_devices_request import SearchDevicesRequest
from huaweicloudsdkmeeting.v1.model.search_devices_response import SearchDevicesResponse
from huaweicloudsdkmeeting.v1.model.search_his_meetings_request import SearchHisMeetingsRequest
from huaweicloudsdkmeeting.v1.model.search_his_meetings_response import SearchHisMeetingsResponse
from huaweicloudsdkmeeting.v1.model.search_materials_request import SearchMaterialsRequest
from huaweicloudsdkmeeting.v1.model.search_materials_response import SearchMaterialsResponse
from huaweicloudsdkmeeting.v1.model.search_meeting_file_list_request import SearchMeetingFileListRequest
from huaweicloudsdkmeeting.v1.model.search_meeting_file_list_response import SearchMeetingFileListResponse
from huaweicloudsdkmeeting.v1.model.search_meetings_request import SearchMeetingsRequest
from huaweicloudsdkmeeting.v1.model.search_meetings_response import SearchMeetingsResponse
from huaweicloudsdkmeeting.v1.model.search_member_vmr_request import SearchMemberVmrRequest
from huaweicloudsdkmeeting.v1.model.search_member_vmr_response import SearchMemberVmrResponse
from huaweicloudsdkmeeting.v1.model.search_online_meetings_request import SearchOnlineMeetingsRequest
from huaweicloudsdkmeeting.v1.model.search_online_meetings_response import SearchOnlineMeetingsResponse
from huaweicloudsdkmeeting.v1.model.search_programs_request import SearchProgramsRequest
from huaweicloudsdkmeeting.v1.model.search_programs_response import SearchProgramsResponse
from huaweicloudsdkmeeting.v1.model.search_publications_request import SearchPublicationsRequest
from huaweicloudsdkmeeting.v1.model.search_publications_response import SearchPublicationsResponse
from huaweicloudsdkmeeting.v1.model.search_qos_history_meetings_request import SearchQosHistoryMeetingsRequest
from huaweicloudsdkmeeting.v1.model.search_qos_history_meetings_response import SearchQosHistoryMeetingsResponse
from huaweicloudsdkmeeting.v1.model.search_qos_online_meetings_request import SearchQosOnlineMeetingsRequest
from huaweicloudsdkmeeting.v1.model.search_qos_online_meetings_response import SearchQosOnlineMeetingsResponse
from huaweicloudsdkmeeting.v1.model.search_qos_participant_detail_request import SearchQosParticipantDetailRequest
from huaweicloudsdkmeeting.v1.model.search_qos_participant_detail_response import SearchQosParticipantDetailResponse
from huaweicloudsdkmeeting.v1.model.search_qos_participants_request import SearchQosParticipantsRequest
from huaweicloudsdkmeeting.v1.model.search_qos_participants_response import SearchQosParticipantsResponse
from huaweicloudsdkmeeting.v1.model.search_recordings_request import SearchRecordingsRequest
from huaweicloudsdkmeeting.v1.model.search_recordings_response import SearchRecordingsResponse
from huaweicloudsdkmeeting.v1.model.search_resource_op_record_request import SearchResourceOpRecordRequest
from huaweicloudsdkmeeting.v1.model.search_resource_op_record_response import SearchResourceOpRecordResponse
from huaweicloudsdkmeeting.v1.model.search_resource_request import SearchResourceRequest
from huaweicloudsdkmeeting.v1.model.search_resource_response import SearchResourceResponse
from huaweicloudsdkmeeting.v1.model.search_user_result_dto import SearchUserResultDTO
from huaweicloudsdkmeeting.v1.model.search_users_request import SearchUsersRequest
from huaweicloudsdkmeeting.v1.model.search_users_response import SearchUsersResponse
from huaweicloudsdkmeeting.v1.model.search_vision_active_code_request import SearchVisionActiveCodeRequest
from huaweicloudsdkmeeting.v1.model.search_vision_active_code_response import SearchVisionActiveCodeResponse
from huaweicloudsdkmeeting.v1.model.send_slide_verify_code_request import SendSlideVerifyCodeRequest
from huaweicloudsdkmeeting.v1.model.send_slide_verify_code_response import SendSlideVerifyCodeResponse
from huaweicloudsdkmeeting.v1.model.send_veri_code_for_change_pwd_request import SendVeriCodeForChangePwdRequest
from huaweicloudsdkmeeting.v1.model.send_veri_code_for_change_pwd_response import SendVeriCodeForChangePwdResponse
from huaweicloudsdkmeeting.v1.model.send_veri_code_for_update_user_info_request import SendVeriCodeForUpdateUserInfoRequest
from huaweicloudsdkmeeting.v1.model.send_veri_code_for_update_user_info_response import SendVeriCodeForUpdateUserInfoResponse
from huaweicloudsdkmeeting.v1.model.set_custom_multi_picture_request import SetCustomMultiPictureRequest
from huaweicloudsdkmeeting.v1.model.set_custom_multi_picture_response import SetCustomMultiPictureResponse
from huaweicloudsdkmeeting.v1.model.set_host_view_request import SetHostViewRequest
from huaweicloudsdkmeeting.v1.model.set_host_view_response import SetHostViewResponse
from huaweicloudsdkmeeting.v1.model.set_multi_picture_request import SetMultiPictureRequest
from huaweicloudsdkmeeting.v1.model.set_multi_picture_response import SetMultiPictureResponse
from huaweicloudsdkmeeting.v1.model.set_participant_view_request import SetParticipantViewRequest
from huaweicloudsdkmeeting.v1.model.set_participant_view_response import SetParticipantViewResponse
from huaweicloudsdkmeeting.v1.model.set_role_request import SetRoleRequest
from huaweicloudsdkmeeting.v1.model.set_role_response import SetRoleResponse
from huaweicloudsdkmeeting.v1.model.show_conf_org_request import ShowConfOrgRequest
from huaweicloudsdkmeeting.v1.model.show_conf_org_response import ShowConfOrgResponse
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
from huaweicloudsdkmeeting.v1.model.show_his_meeting_detail_request import ShowHisMeetingDetailRequest
from huaweicloudsdkmeeting.v1.model.show_his_meeting_detail_response import ShowHisMeetingDetailResponse
from huaweicloudsdkmeeting.v1.model.show_meeting_detail_request import ShowMeetingDetailRequest
from huaweicloudsdkmeeting.v1.model.show_meeting_detail_response import ShowMeetingDetailResponse
from huaweicloudsdkmeeting.v1.model.show_meeting_file_list_request import ShowMeetingFileListRequest
from huaweicloudsdkmeeting.v1.model.show_meeting_file_list_response import ShowMeetingFileListResponse
from huaweicloudsdkmeeting.v1.model.show_meeting_file_request import ShowMeetingFileRequest
from huaweicloudsdkmeeting.v1.model.show_meeting_file_response import ShowMeetingFileResponse
from huaweicloudsdkmeeting.v1.model.show_my_info_request import ShowMyInfoRequest
from huaweicloudsdkmeeting.v1.model.show_my_info_response import ShowMyInfoResponse
from huaweicloudsdkmeeting.v1.model.show_online_meeting_detail_request import ShowOnlineMeetingDetailRequest
from huaweicloudsdkmeeting.v1.model.show_online_meeting_detail_response import ShowOnlineMeetingDetailResponse
from huaweicloudsdkmeeting.v1.model.show_org_res_request import ShowOrgResRequest
from huaweicloudsdkmeeting.v1.model.show_org_res_response import ShowOrgResResponse
from huaweicloudsdkmeeting.v1.model.show_program_request import ShowProgramRequest
from huaweicloudsdkmeeting.v1.model.show_program_response import ShowProgramResponse
from huaweicloudsdkmeeting.v1.model.show_publication_request import ShowPublicationRequest
from huaweicloudsdkmeeting.v1.model.show_publication_response import ShowPublicationResponse
from huaweicloudsdkmeeting.v1.model.show_real_time_info_of_meeting_request import ShowRealTimeInfoOfMeetingRequest
from huaweicloudsdkmeeting.v1.model.show_real_time_info_of_meeting_response import ShowRealTimeInfoOfMeetingResponse
from huaweicloudsdkmeeting.v1.model.show_recording_detail_request import ShowRecordingDetailRequest
from huaweicloudsdkmeeting.v1.model.show_recording_detail_response import ShowRecordingDetailResponse
from huaweicloudsdkmeeting.v1.model.show_recording_file_download_urls_request import ShowRecordingFileDownloadUrlsRequest
from huaweicloudsdkmeeting.v1.model.show_recording_file_download_urls_response import ShowRecordingFileDownloadUrlsResponse
from huaweicloudsdkmeeting.v1.model.show_region_info_of_meeting_request import ShowRegionInfoOfMeetingRequest
from huaweicloudsdkmeeting.v1.model.show_region_info_of_meeting_response import ShowRegionInfoOfMeetingResponse
from huaweicloudsdkmeeting.v1.model.show_room_setting_request import ShowRoomSettingRequest
from huaweicloudsdkmeeting.v1.model.show_room_setting_response import ShowRoomSettingResponse
from huaweicloudsdkmeeting.v1.model.show_sp_res_request import ShowSpResRequest
from huaweicloudsdkmeeting.v1.model.show_sp_res_response import ShowSpResResponse
from huaweicloudsdkmeeting.v1.model.show_sp_resource_request import ShowSpResourceRequest
from huaweicloudsdkmeeting.v1.model.show_sp_resource_response import ShowSpResourceResponse
from huaweicloudsdkmeeting.v1.model.show_user_detail_request import ShowUserDetailRequest
from huaweicloudsdkmeeting.v1.model.show_user_detail_response import ShowUserDetailResponse
from huaweicloudsdkmeeting.v1.model.show_webinar_request import ShowWebinarRequest
from huaweicloudsdkmeeting.v1.model.show_webinar_response import ShowWebinarResponse
from huaweicloudsdkmeeting.v1.model.slide_verify_code_check_dto import SlideVerifyCodeCheckDTO
from huaweicloudsdkmeeting.v1.model.slide_verify_code_send_dto import SlideVerifyCodeSendDTO
from huaweicloudsdkmeeting.v1.model.stop_meeting_request import StopMeetingRequest
from huaweicloudsdkmeeting.v1.model.stop_meeting_response import StopMeetingResponse
from huaweicloudsdkmeeting.v1.model.sub_pic_layout_info import SubPicLayoutInfo
from huaweicloudsdkmeeting.v1.model.subscriber_in_pic import SubscriberInPic
from huaweicloudsdkmeeting.v1.model.switch_mode_request import SwitchModeRequest
from huaweicloudsdkmeeting.v1.model.switch_mode_response import SwitchModeResponse
from huaweicloudsdkmeeting.v1.model.token_info import TokenInfo
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
from huaweicloudsdkmeeting.v1.model.update_material_request import UpdateMaterialRequest
from huaweicloudsdkmeeting.v1.model.update_material_request_dto import UpdateMaterialRequestDTO
from huaweicloudsdkmeeting.v1.model.update_material_response import UpdateMaterialResponse
from huaweicloudsdkmeeting.v1.model.update_meeting_request import UpdateMeetingRequest
from huaweicloudsdkmeeting.v1.model.update_meeting_response import UpdateMeetingResponse
from huaweicloudsdkmeeting.v1.model.update_member_vmr_request import UpdateMemberVmrRequest
from huaweicloudsdkmeeting.v1.model.update_member_vmr_response import UpdateMemberVmrResponse
from huaweicloudsdkmeeting.v1.model.update_my_info_request import UpdateMyInfoRequest
from huaweicloudsdkmeeting.v1.model.update_my_info_response import UpdateMyInfoResponse
from huaweicloudsdkmeeting.v1.model.update_program_request import UpdateProgramRequest
from huaweicloudsdkmeeting.v1.model.update_program_request_dto import UpdateProgramRequestDTO
from huaweicloudsdkmeeting.v1.model.update_program_response import UpdateProgramResponse
from huaweicloudsdkmeeting.v1.model.update_publication_request import UpdatePublicationRequest
from huaweicloudsdkmeeting.v1.model.update_publication_request_dto import UpdatePublicationRequestDTO
from huaweicloudsdkmeeting.v1.model.update_publication_response import UpdatePublicationResponse
from huaweicloudsdkmeeting.v1.model.update_pwd_request import UpdatePwdRequest
from huaweicloudsdkmeeting.v1.model.update_pwd_response import UpdatePwdResponse
from huaweicloudsdkmeeting.v1.model.update_resource_request import UpdateResourceRequest
from huaweicloudsdkmeeting.v1.model.update_resource_response import UpdateResourceResponse
from huaweicloudsdkmeeting.v1.model.update_room_setting_request import UpdateRoomSettingRequest
from huaweicloudsdkmeeting.v1.model.update_room_setting_response import UpdateRoomSettingResponse
from huaweicloudsdkmeeting.v1.model.update_started_conf_config_request import UpdateStartedConfConfigRequest
from huaweicloudsdkmeeting.v1.model.update_started_conf_config_response import UpdateStartedConfConfigResponse
from huaweicloudsdkmeeting.v1.model.update_started_config_req_body import UpdateStartedConfigReqBody
from huaweicloudsdkmeeting.v1.model.update_token_request import UpdateTokenRequest
from huaweicloudsdkmeeting.v1.model.update_token_response import UpdateTokenResponse
from huaweicloudsdkmeeting.v1.model.update_user_request import UpdateUserRequest
from huaweicloudsdkmeeting.v1.model.update_user_response import UpdateUserResponse
from huaweicloudsdkmeeting.v1.model.update_webinar_request import UpdateWebinarRequest
from huaweicloudsdkmeeting.v1.model.update_webinar_response import UpdateWebinarResponse
from huaweicloudsdkmeeting.v1.model.upload_file_request import UploadFileRequest
from huaweicloudsdkmeeting.v1.model.upload_file_request_body import UploadFileRequestBody
from huaweicloudsdkmeeting.v1.model.upload_file_response import UploadFileResponse
from huaweicloudsdkmeeting.v1.model.user_dto import UserDTO
from huaweicloudsdkmeeting.v1.model.user_function_dto import UserFunctionDTO
from huaweicloudsdkmeeting.v1.model.user_info import UserInfo
from huaweicloudsdkmeeting.v1.model.user_status_dto import UserStatusDTO
from huaweicloudsdkmeeting.v1.model.user_vmr_dto import UserVmrDTO
from huaweicloudsdkmeeting.v1.model.validate_token_req_dto import ValidateTokenReqDTO
from huaweicloudsdkmeeting.v1.model.verification_code_dto import VerificationCodeDTO
from huaweicloudsdkmeeting.v1.model.verify_code_check_dto import VerifyCodeCheckDTO
from huaweicloudsdkmeeting.v1.model.verify_code_send_dtov1 import VerifyCodeSendDTOV1
from huaweicloudsdkmeeting.v1.model.vision_active_code_dto import VisionActiveCodeDTO
