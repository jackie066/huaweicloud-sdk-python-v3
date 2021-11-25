# coding: utf-8

from __future__ import absolute_import

# import NlpClient
from huaweicloudsdknlp.v2.nlp_client import NlpClient
from huaweicloudsdknlp.v2.nlp_async_client import NlpAsyncClient
# import models into sdk package
from huaweicloudsdknlp.v2.model.aspect_advance_opinion import AspectAdvanceOpinion
from huaweicloudsdknlp.v2.model.aspect_opinion import AspectOpinion
from huaweicloudsdknlp.v2.model.aspect_sentiment_advance_request import AspectSentimentAdvanceRequest
from huaweicloudsdknlp.v2.model.aspect_sentiment_request import AspectSentimentRequest
from huaweicloudsdknlp.v2.model.classification_req import ClassificationReq
from huaweicloudsdknlp.v2.model.classification_result import ClassificationResult
from huaweicloudsdknlp.v2.model.create_poem import CreatePoem
from huaweicloudsdknlp.v2.model.dependency_parser_request import DependencyParserRequest
from huaweicloudsdknlp.v2.model.dependency_parser_word import DependencyParserWord
from huaweicloudsdknlp.v2.model.document_classification_req import DocumentClassificationReq
from huaweicloudsdknlp.v2.model.domain_named_entity import DomainNamedEntity
from huaweicloudsdknlp.v2.model.domain_sentiment_req import DomainSentimentReq
from huaweicloudsdknlp.v2.model.entity_sentiment_req import EntitySentimentReq
from huaweicloudsdknlp.v2.model.event_extraction_response_item import EventExtractionResponseItem
from huaweicloudsdknlp.v2.model.event_extraction_response_item_argument import EventExtractionResponseItemArgument
from huaweicloudsdknlp.v2.model.file_translation_req import FileTranslationReq
from huaweicloudsdknlp.v2.model.hw_cloud_sentiment_req import HWCloudSentimentReq
from huaweicloudsdknlp.v2.model.hw_cloud_sentiment_resp import HWCloudSentimentResp
from huaweicloudsdknlp.v2.model.intent_req import IntentReq
from huaweicloudsdknlp.v2.model.intent_result import IntentResult
from huaweicloudsdknlp.v2.model.keyword_extract_req import KeywordExtractReq
from huaweicloudsdknlp.v2.model.language_detection_req import LanguageDetectionReq
from huaweicloudsdknlp.v2.model.linked_entity import LinkedEntity
from huaweicloudsdknlp.v2.model.named_entity import NamedEntity
from huaweicloudsdknlp.v2.model.ner_request import NerRequest
from huaweicloudsdknlp.v2.model.post_domain_ner_request import PostDomainNerRequest
from huaweicloudsdknlp.v2.model.post_entity_linking_request import PostEntityLinkingRequest
from huaweicloudsdknlp.v2.model.post_event_extraction_req import PostEventExtractionReq
from huaweicloudsdknlp.v2.model.post_multi_gained_segment_response_item import PostMultiGainedSegmentResponseItem
from huaweicloudsdknlp.v2.model.post_multi_gained_segment_response_item_copy import PostMultiGainedSegmentResponseItemCopy
from huaweicloudsdknlp.v2.model.post_multi_grained_segment_req import PostMultiGrainedSegmentReq
from huaweicloudsdknlp.v2.model.post_sentence_embedding_req import PostSentenceEmbeddingReq
from huaweicloudsdknlp.v2.model.run_aspect_sentiment_advance_request import RunAspectSentimentAdvanceRequest
from huaweicloudsdknlp.v2.model.run_aspect_sentiment_advance_response import RunAspectSentimentAdvanceResponse
from huaweicloudsdknlp.v2.model.run_aspect_sentiment_request import RunAspectSentimentRequest
from huaweicloudsdknlp.v2.model.run_aspect_sentiment_response import RunAspectSentimentResponse
from huaweicloudsdknlp.v2.model.run_classification_request import RunClassificationRequest
from huaweicloudsdknlp.v2.model.run_classification_response import RunClassificationResponse
from huaweicloudsdknlp.v2.model.run_dependency_parser_request import RunDependencyParserRequest
from huaweicloudsdknlp.v2.model.run_dependency_parser_response import RunDependencyParserResponse
from huaweicloudsdknlp.v2.model.run_doc_classification_request import RunDocClassificationRequest
from huaweicloudsdknlp.v2.model.run_doc_classification_response import RunDocClassificationResponse
from huaweicloudsdknlp.v2.model.run_domain_sentiment_request import RunDomainSentimentRequest
from huaweicloudsdknlp.v2.model.run_domain_sentiment_response import RunDomainSentimentResponse
from huaweicloudsdknlp.v2.model.run_entity_linking_request import RunEntityLinkingRequest
from huaweicloudsdknlp.v2.model.run_entity_linking_response import RunEntityLinkingResponse
from huaweicloudsdknlp.v2.model.run_entity_sentiment_request import RunEntitySentimentRequest
from huaweicloudsdknlp.v2.model.run_entity_sentiment_response import RunEntitySentimentResponse
from huaweicloudsdknlp.v2.model.run_event_extraction_request import RunEventExtractionRequest
from huaweicloudsdknlp.v2.model.run_event_extraction_response import RunEventExtractionResponse
from huaweicloudsdknlp.v2.model.run_file_translation_request import RunFileTranslationRequest
from huaweicloudsdknlp.v2.model.run_file_translation_response import RunFileTranslationResponse
from huaweicloudsdknlp.v2.model.run_get_file_translation_result_request import RunGetFileTranslationResultRequest
from huaweicloudsdknlp.v2.model.run_get_file_translation_result_response import RunGetFileTranslationResultResponse
from huaweicloudsdknlp.v2.model.run_keyword_extract_request import RunKeywordExtractRequest
from huaweicloudsdknlp.v2.model.run_keyword_extract_response import RunKeywordExtractResponse
from huaweicloudsdknlp.v2.model.run_language_detection_request import RunLanguageDetectionRequest
from huaweicloudsdknlp.v2.model.run_language_detection_response import RunLanguageDetectionResponse
from huaweicloudsdknlp.v2.model.run_multi_grained_segment_request import RunMultiGrainedSegmentRequest
from huaweicloudsdknlp.v2.model.run_multi_grained_segment_response import RunMultiGrainedSegmentResponse
from huaweicloudsdknlp.v2.model.run_ner_domain_request import RunNerDomainRequest
from huaweicloudsdknlp.v2.model.run_ner_domain_response import RunNerDomainResponse
from huaweicloudsdknlp.v2.model.run_ner_request import RunNerRequest
from huaweicloudsdknlp.v2.model.run_ner_response import RunNerResponse
from huaweicloudsdknlp.v2.model.run_poem_request import RunPoemRequest
from huaweicloudsdknlp.v2.model.run_poem_response import RunPoemResponse
from huaweicloudsdknlp.v2.model.run_segment_request import RunSegmentRequest
from huaweicloudsdknlp.v2.model.run_segment_response import RunSegmentResponse
from huaweicloudsdknlp.v2.model.run_semantic_parser_request import RunSemanticParserRequest
from huaweicloudsdknlp.v2.model.run_semantic_parser_response import RunSemanticParserResponse
from huaweicloudsdknlp.v2.model.run_sentence_embedding_request import RunSentenceEmbeddingRequest
from huaweicloudsdknlp.v2.model.run_sentence_embedding_response import RunSentenceEmbeddingResponse
from huaweicloudsdknlp.v2.model.run_sentiment_request import RunSentimentRequest
from huaweicloudsdknlp.v2.model.run_sentiment_response import RunSentimentResponse
from huaweicloudsdknlp.v2.model.run_summary_domain_request import RunSummaryDomainRequest
from huaweicloudsdknlp.v2.model.run_summary_domain_response import RunSummaryDomainResponse
from huaweicloudsdknlp.v2.model.run_summary_request import RunSummaryRequest
from huaweicloudsdknlp.v2.model.run_summary_response import RunSummaryResponse
from huaweicloudsdknlp.v2.model.run_text_similarity_advance_request import RunTextSimilarityAdvanceRequest
from huaweicloudsdknlp.v2.model.run_text_similarity_advance_response import RunTextSimilarityAdvanceResponse
from huaweicloudsdknlp.v2.model.run_text_similarity_request import RunTextSimilarityRequest
from huaweicloudsdknlp.v2.model.run_text_similarity_response import RunTextSimilarityResponse
from huaweicloudsdknlp.v2.model.run_text_translation_request import RunTextTranslationRequest
from huaweicloudsdknlp.v2.model.run_text_translation_response import RunTextTranslationResponse
from huaweicloudsdknlp.v2.model.segment_request import SegmentRequest
from huaweicloudsdknlp.v2.model.slot import Slot
from huaweicloudsdknlp.v2.model.summary_domain_req import SummaryDomainReq
from huaweicloudsdknlp.v2.model.summary_req import SummaryReq
from huaweicloudsdknlp.v2.model.text_similarity_advance_request import TextSimilarityAdvanceRequest
from huaweicloudsdknlp.v2.model.text_similarity_request import TextSimilarityRequest
from huaweicloudsdknlp.v2.model.text_translation_req import TextTranslationReq
from huaweicloudsdknlp.v2.model.word import Word

