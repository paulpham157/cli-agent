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





class FilterOperationTypeEnum(str, Enum):
    """
    FilterOperationTypeEnum
    """

    """
    allowed enum values
    """
    UNKNOWN = 'UNKNOWN'
    AND = 'AND'
    OR = 'OR'

    @classmethod
    def from_json(cls, json_str: str) -> FilterOperationTypeEnum:
        """Create an instance of FilterOperationTypeEnum from a JSON string"""
        return FilterOperationTypeEnum(json.loads(json_str))


