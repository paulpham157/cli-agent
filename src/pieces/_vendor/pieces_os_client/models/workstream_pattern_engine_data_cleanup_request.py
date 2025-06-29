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


from typing import List, Optional
from pydantic.v1 import BaseModel, Field, conlist
from pieces._vendor.pieces_os_client.models.anonymous_temporal_range import AnonymousTemporalRange
from pieces._vendor.pieces_os_client.models.embedded_model_schema import EmbeddedModelSchema

class WorkstreamPatternEngineDataCleanupRequest(BaseModel):
    """
    NOTE: if we want to remove all the data the from would be unset, the to will be right now.  from: is always in the past to: is always at least before from in our time.  # noqa: E501
    """
    var_schema: Optional[EmbeddedModelSchema] = Field(default=None, alias="schema")
    ranges: Optional[conlist(AnonymousTemporalRange)] = None
    __properties = ["schema", "ranges"]

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
    def from_json(cls, json_str: str) -> WorkstreamPatternEngineDataCleanupRequest:
        """Create an instance of WorkstreamPatternEngineDataCleanupRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic.v1 by calling `to_dict()` of var_schema
        if self.var_schema:
            _dict['schema'] = self.var_schema.to_dict()
        # override the default output from pydantic.v1 by calling `to_dict()` of each item in ranges (list)
        _items = []
        if self.ranges:
            for _item in self.ranges:
                if _item:
                    _items.append(_item.to_dict())
            _dict['ranges'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> WorkstreamPatternEngineDataCleanupRequest:
        """Create an instance of WorkstreamPatternEngineDataCleanupRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return WorkstreamPatternEngineDataCleanupRequest.parse_obj(obj)

        _obj = WorkstreamPatternEngineDataCleanupRequest.parse_obj({
            "var_schema": EmbeddedModelSchema.from_dict(obj.get("schema")) if obj.get("schema") is not None else None,
            "ranges": [AnonymousTemporalRange.from_dict(_item) for _item in obj.get("ranges")] if obj.get("ranges") is not None else None
        })
        return _obj


