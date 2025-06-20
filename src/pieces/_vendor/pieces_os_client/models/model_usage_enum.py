# coding: utf-8

"""
    Pieces Isomorphic OpenAPI

    Endpoints for Assets, Formats, Users, Asset, Format, User.

    The version of the OpenAPI document: 1.0
    Contact: tsavo@pieces.app
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class ModelUsageEnum(str, Enum):
    """
    These are all the possible uses for a model, i.e. code classification, OCR, text vs code,  tagify code, tag-based code search, neural code search, tagify color and code description.
    """

    """
    allowed enum values
    """
    UNKNOWN = 'UNKNOWN'
    OCR = 'OCR'
    CODE_CLASSIFICATION = 'CODE_CLASSIFICATION'
    TEXT_VS_CODE = 'TEXT_VS_CODE'
    TAGIFY_CODE = 'TAGIFY_CODE'
    TLP_TAG_SEARCH = 'TLP_TAG_SEARCH'
    TLP_NEURAL_CODE_SEARCH = 'TLP_NEURAL_CODE_SEARCH'
    TAGIFY_COLOR_FROM_CODE = 'TAGIFY_COLOR_FROM_CODE'
    CODE_DESCRIPTION = 'CODE_DESCRIPTION'
    CODE_TITLE = 'CODE_TITLE'
    CODE_SEARCH_QUERIES = 'CODE_SEARCH_QUERIES'
    CODE_EXTRACTIVE_TAGS = 'CODE_EXTRACTIVE_TAGS'
    CODE_EXTRACTIVE_LINKS = 'CODE_EXTRACTIVE_LINKS'
    CODE_CONVERSATION = 'CODE_CONVERSATION'
    CODE_GENERATION = 'CODE_GENERATION'
    CODE_SEARCH = 'CODE_SEARCH'
    CODE_DISCOVERY = 'CODE_DISCOVERY'
    CODE_RELATED_PEOPLE = 'CODE_RELATED_PEOPLE'
    CODE_FRAMEWORK = 'CODE_FRAMEWORK'
    VIDEO_OCR = 'VIDEO_OCR'
    TEXT_VS_CODE_SEGMENTATION = 'TEXT_VS_CODE_SEGMENTATION'
    TEXT_EMBEDDING = 'TEXT_EMBEDDING'
    TECHNICAL_ERROR = 'TECHNICAL_ERROR'

    @classmethod
    def from_json(cls, json_str: str) -> ModelUsageEnum:
        """Create an instance of ModelUsageEnum from a JSON string"""
        return ModelUsageEnum(json.loads(json_str))


