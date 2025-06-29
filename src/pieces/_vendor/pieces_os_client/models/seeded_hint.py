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
from pydantic.v1 import BaseModel, Field, StrictStr
from pieces._vendor.pieces_os_client.models.embedded_model_schema import EmbeddedModelSchema
from pieces._vendor.pieces_os_client.models.hint_type_enum import HintTypeEnum
from pieces._vendor.pieces_os_client.models.mechanism_enum import MechanismEnum

class SeededHint(BaseModel):
    """
    SeededHint
    """
    var_schema: Optional[EmbeddedModelSchema] = Field(default=None, alias="schema")
    mechanism: Optional[MechanismEnum] = None
    asset: Optional[StrictStr] = Field(default=None, description="This is an asset id that we are using to link this to an asset.")
    type: HintTypeEnum = Field(...)
    text: StrictStr = Field(default=..., description="This is the text of the hint.")
    model: Optional[StrictStr] = Field(default=None, description="this is a model id. that we are using to link this to a model.")
    __properties = ["schema", "mechanism", "asset", "type", "text", "model"]

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
    def from_json(cls, json_str: str) -> SeededHint:
        """Create an instance of SeededHint from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SeededHint:
        """Create an instance of SeededHint from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SeededHint.parse_obj(obj)

        _obj = SeededHint.parse_obj({
            "var_schema": EmbeddedModelSchema.from_dict(obj.get("schema")) if obj.get("schema") is not None else None,
            "mechanism": obj.get("mechanism"),
            "asset": obj.get("asset"),
            "type": obj.get("type"),
            "text": obj.get("text"),
            "model": obj.get("model")
        })
        return _obj


