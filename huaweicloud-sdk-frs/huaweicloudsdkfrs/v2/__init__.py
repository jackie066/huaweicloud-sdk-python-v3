# coding: utf-8

from __future__ import absolute_import

# import FrsClient
from huaweicloudsdkfrs.v2.frs_client import FrsClient
from huaweicloudsdkfrs.v2.frs_async_client import FrsAsyncClient
# import models into sdk package
from huaweicloudsdkfrs.v2.model.actions_list import ActionsList
from huaweicloudsdkfrs.v2.model.add_faces_base64_req import AddFacesBase64Req
from huaweicloudsdkfrs.v2.model.add_faces_by_base64_request import AddFacesByBase64Request
from huaweicloudsdkfrs.v2.model.add_faces_by_base64_response import AddFacesByBase64Response
from huaweicloudsdkfrs.v2.model.add_faces_by_file_request import AddFacesByFileRequest
from huaweicloudsdkfrs.v2.model.add_faces_by_file_request_body import AddFacesByFileRequestBody
from huaweicloudsdkfrs.v2.model.add_faces_by_file_response import AddFacesByFileResponse
from huaweicloudsdkfrs.v2.model.add_faces_by_url_request import AddFacesByUrlRequest
from huaweicloudsdkfrs.v2.model.add_faces_by_url_response import AddFacesByUrlResponse
from huaweicloudsdkfrs.v2.model.add_faces_url_req import AddFacesUrlReq
from huaweicloudsdkfrs.v2.model.attributes import Attributes
from huaweicloudsdkfrs.v2.model.attributes_expression import AttributesExpression
from huaweicloudsdkfrs.v2.model.batch_delete_faces_request import BatchDeleteFacesRequest
from huaweicloudsdkfrs.v2.model.batch_delete_faces_response import BatchDeleteFacesResponse
from huaweicloudsdkfrs.v2.model.bounding_box import BoundingBox
from huaweicloudsdkfrs.v2.model.compare_face import CompareFace
from huaweicloudsdkfrs.v2.model.compare_face_by_base64_request import CompareFaceByBase64Request
from huaweicloudsdkfrs.v2.model.compare_face_by_base64_response import CompareFaceByBase64Response
from huaweicloudsdkfrs.v2.model.compare_face_by_file_request import CompareFaceByFileRequest
from huaweicloudsdkfrs.v2.model.compare_face_by_file_request_body import CompareFaceByFileRequestBody
from huaweicloudsdkfrs.v2.model.compare_face_by_file_response import CompareFaceByFileResponse
from huaweicloudsdkfrs.v2.model.compare_face_by_url_request import CompareFaceByUrlRequest
from huaweicloudsdkfrs.v2.model.compare_face_by_url_response import CompareFaceByUrlResponse
from huaweicloudsdkfrs.v2.model.create_face_set_req import CreateFaceSetReq
from huaweicloudsdkfrs.v2.model.create_face_set_request import CreateFaceSetRequest
from huaweicloudsdkfrs.v2.model.create_face_set_response import CreateFaceSetResponse
from huaweicloudsdkfrs.v2.model.delete_face_by_external_image_id_request import DeleteFaceByExternalImageIdRequest
from huaweicloudsdkfrs.v2.model.delete_face_by_external_image_id_response import DeleteFaceByExternalImageIdResponse
from huaweicloudsdkfrs.v2.model.delete_face_by_face_id_request import DeleteFaceByFaceIdRequest
from huaweicloudsdkfrs.v2.model.delete_face_by_face_id_response import DeleteFaceByFaceIdResponse
from huaweicloudsdkfrs.v2.model.delete_face_set_request import DeleteFaceSetRequest
from huaweicloudsdkfrs.v2.model.delete_face_set_response import DeleteFaceSetResponse
from huaweicloudsdkfrs.v2.model.delete_faces_batch_req import DeleteFacesBatchReq
from huaweicloudsdkfrs.v2.model.detect_face import DetectFace
from huaweicloudsdkfrs.v2.model.detect_face_by_base64_request import DetectFaceByBase64Request
from huaweicloudsdkfrs.v2.model.detect_face_by_base64_response import DetectFaceByBase64Response
from huaweicloudsdkfrs.v2.model.detect_face_by_file_request import DetectFaceByFileRequest
from huaweicloudsdkfrs.v2.model.detect_face_by_file_request_body import DetectFaceByFileRequestBody
from huaweicloudsdkfrs.v2.model.detect_face_by_file_response import DetectFaceByFileResponse
from huaweicloudsdkfrs.v2.model.detect_face_by_url_request import DetectFaceByUrlRequest
from huaweicloudsdkfrs.v2.model.detect_face_by_url_response import DetectFaceByUrlResponse
from huaweicloudsdkfrs.v2.model.detect_live_by_base64_request import DetectLiveByBase64Request
from huaweicloudsdkfrs.v2.model.detect_live_by_base64_response import DetectLiveByBase64Response
from huaweicloudsdkfrs.v2.model.detect_live_by_file_request import DetectLiveByFileRequest
from huaweicloudsdkfrs.v2.model.detect_live_by_file_request_body import DetectLiveByFileRequestBody
from huaweicloudsdkfrs.v2.model.detect_live_by_file_response import DetectLiveByFileResponse
from huaweicloudsdkfrs.v2.model.detect_live_by_url_request import DetectLiveByUrlRequest
from huaweicloudsdkfrs.v2.model.detect_live_by_url_response import DetectLiveByUrlResponse
from huaweicloudsdkfrs.v2.model.detect_live_face_by_base64_request import DetectLiveFaceByBase64Request
from huaweicloudsdkfrs.v2.model.detect_live_face_by_base64_response import DetectLiveFaceByBase64Response
from huaweicloudsdkfrs.v2.model.detect_live_face_by_file_request import DetectLiveFaceByFileRequest
from huaweicloudsdkfrs.v2.model.detect_live_face_by_file_request_body import DetectLiveFaceByFileRequestBody
from huaweicloudsdkfrs.v2.model.detect_live_face_by_file_response import DetectLiveFaceByFileResponse
from huaweicloudsdkfrs.v2.model.detect_live_face_by_url_request import DetectLiveFaceByUrlRequest
from huaweicloudsdkfrs.v2.model.detect_live_face_by_url_response import DetectLiveFaceByUrlResponse
from huaweicloudsdkfrs.v2.model.dress import Dress
from huaweicloudsdkfrs.v2.model.face_compare_base64_req import FaceCompareBase64Req
from huaweicloudsdkfrs.v2.model.face_compare_url_req import FaceCompareUrlReq
from huaweicloudsdkfrs.v2.model.face_detect_base64_req import FaceDetectBase64Req
from huaweicloudsdkfrs.v2.model.face_detect_url_req import FaceDetectUrlReq
from huaweicloudsdkfrs.v2.model.face_quality import FaceQuality
from huaweicloudsdkfrs.v2.model.face_search_base64_req import FaceSearchBase64Req
from huaweicloudsdkfrs.v2.model.face_search_face_id_req import FaceSearchFaceIdReq
from huaweicloudsdkfrs.v2.model.face_search_url_req import FaceSearchUrlReq
from huaweicloudsdkfrs.v2.model.face_set_face import FaceSetFace
from huaweicloudsdkfrs.v2.model.face_set_info import FaceSetInfo
from huaweicloudsdkfrs.v2.model.landmark import Landmark
from huaweicloudsdkfrs.v2.model.live_detect_base64_req import LiveDetectBase64Req
from huaweicloudsdkfrs.v2.model.live_detect_face_base64_req import LiveDetectFaceBase64Req
from huaweicloudsdkfrs.v2.model.live_detect_face_resp_result import LiveDetectFaceRespResult
from huaweicloudsdkfrs.v2.model.live_detect_face_url_req import LiveDetectFaceUrlReq
from huaweicloudsdkfrs.v2.model.live_detect_resp_videoresult import LiveDetectRespVideoresult
from huaweicloudsdkfrs.v2.model.live_detect_url_req import LiveDetectUrlReq
from huaweicloudsdkfrs.v2.model.point import Point
from huaweicloudsdkfrs.v2.model.search_face import SearchFace
from huaweicloudsdkfrs.v2.model.search_face_by_base64_request import SearchFaceByBase64Request
from huaweicloudsdkfrs.v2.model.search_face_by_base64_response import SearchFaceByBase64Response
from huaweicloudsdkfrs.v2.model.search_face_by_face_id_request import SearchFaceByFaceIdRequest
from huaweicloudsdkfrs.v2.model.search_face_by_face_id_response import SearchFaceByFaceIdResponse
from huaweicloudsdkfrs.v2.model.search_face_by_file_request import SearchFaceByFileRequest
from huaweicloudsdkfrs.v2.model.search_face_by_file_request_body import SearchFaceByFileRequestBody
from huaweicloudsdkfrs.v2.model.search_face_by_file_response import SearchFaceByFileResponse
from huaweicloudsdkfrs.v2.model.search_face_by_url_request import SearchFaceByUrlRequest
from huaweicloudsdkfrs.v2.model.search_face_by_url_response import SearchFaceByUrlResponse
from huaweicloudsdkfrs.v2.model.show_all_face_sets_request import ShowAllFaceSetsRequest
from huaweicloudsdkfrs.v2.model.show_all_face_sets_response import ShowAllFaceSetsResponse
from huaweicloudsdkfrs.v2.model.show_face_set_request import ShowFaceSetRequest
from huaweicloudsdkfrs.v2.model.show_face_set_response import ShowFaceSetResponse
from huaweicloudsdkfrs.v2.model.show_faces_by_face_id_request import ShowFacesByFaceIdRequest
from huaweicloudsdkfrs.v2.model.show_faces_by_face_id_response import ShowFacesByFaceIdResponse
from huaweicloudsdkfrs.v2.model.show_faces_by_limit_request import ShowFacesByLimitRequest
from huaweicloudsdkfrs.v2.model.show_faces_by_limit_response import ShowFacesByLimitResponse
from huaweicloudsdkfrs.v2.model.type_info import TypeInfo
from huaweicloudsdkfrs.v2.model.update_face_req import UpdateFaceReq
from huaweicloudsdkfrs.v2.model.update_face_request import UpdateFaceRequest
from huaweicloudsdkfrs.v2.model.update_face_response import UpdateFaceResponse
from huaweicloudsdkfrs.v2.model.warning_list import WarningList

