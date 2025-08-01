# coding: utf-8

"""
    Pieces Isomorphic OpenAPI

    Endpoints for Assets, Formats, Users, Asset, Format, User.

    The version of the OpenAPI document: 1.0
    Contact: tsavo@pieces.app
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic.v1 import BaseModel

class TemporalRangeGrounding(BaseModel):
    """
    This is used in the QGPT flow as well as within the conversation.  This will let us know grounding's that you want us to use within a given time range(s).  workstreams: is used to describe workstreams context. (specific to the \"workstream mapper\" - name subject to change)  # noqa: E501
    """
    workstreams: Optional[FlattenedRanges] = None
    __properties = ["workstreams"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> TemporalRangeGrounding:
        """Create an instance of TemporalRangeGrounding from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic.v1 by calling `to_dict()` of workstreams
        if self.workstreams:
            _dict['workstreams'] = self.workstreams.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TemporalRangeGrounding:
        """Create an instance of TemporalRangeGrounding from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TemporalRangeGrounding.parse_obj(obj)

        _obj = TemporalRangeGrounding.parse_obj({
            "workstreams": FlattenedRanges.from_dict(obj.get("workstreams")) if obj.get("workstreams") is not None else None
        })
        return _obj

from pieces._vendor.pieces_os_client.models.flattened_ranges import FlattenedRanges
TemporalRangeGrounding.update_forward_refs()

