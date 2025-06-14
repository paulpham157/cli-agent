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
from pydantic.v1 import BaseModel, Field
from pieces._vendor.pieces_os_client.models.classification_generic_enum import ClassificationGenericEnum
from pieces._vendor.pieces_os_client.models.classification_rendering_enum import ClassificationRenderingEnum
from pieces._vendor.pieces_os_client.models.classification_specific_enum import ClassificationSpecificEnum
from pieces._vendor.pieces_os_client.models.embedded_model_schema import EmbeddedModelSchema

class SeededClassification(BaseModel):
    """
    This is the specific classification of an Asset's Format.(This is on a per format basis b/c an asset could have different formats that are different format representations of the Asset.)  # noqa: E501
    """
    var_schema: Optional[EmbeddedModelSchema] = Field(default=None, alias="schema")
    generic: Optional[ClassificationGenericEnum] = None
    specific: Optional[ClassificationSpecificEnum] = None
    rendering: Optional[ClassificationRenderingEnum] = None
    __properties = ["schema", "generic", "specific", "rendering"]

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
    def from_json(cls, json_str: str) -> SeededClassification:
        """Create an instance of SeededClassification from a JSON string"""
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
    def from_dict(cls, obj: dict) -> SeededClassification:
        """Create an instance of SeededClassification from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SeededClassification.parse_obj(obj)

        _obj = SeededClassification.parse_obj({
            "var_schema": EmbeddedModelSchema.from_dict(obj.get("schema")) if obj.get("schema") is not None else None,
            "generic": obj.get("generic"),
            "specific": obj.get("specific"),
            "rendering": obj.get("rendering")
        })
        return _obj


