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


from typing import Optional, Union
from pydantic.v1 import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from pieces._vendor.pieces_os_client.models.asset import Asset
from pieces._vendor.pieces_os_client.models.embedded_model_schema import EmbeddedModelSchema
from pieces._vendor.pieces_os_client.models.searched_match_enum import SearchedMatchEnum

class SearchedAsset(BaseModel):
    """
    This is a modle that will represent a searched asset!  # noqa: E501
    """
    var_schema: Optional[EmbeddedModelSchema] = Field(default=None, alias="schema")
    asset: Optional[Asset] = None
    exact: StrictBool = Field(...)
    score: Union[StrictFloat, StrictInt] = Field(...)
    match: SearchedMatchEnum = Field(...)
    identifier: StrictStr = Field(default=..., description="This is the uuid of the asset.")
    pseudo: Optional[StrictBool] = Field(default=None, description="If this is a pseudo asset that was also returned.")
    __properties = ["schema", "asset", "exact", "score", "match", "identifier", "pseudo"]

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
    def from_json(cls, json_str: str) -> SearchedAsset:
        """Create an instance of SearchedAsset from a JSON string"""
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
        # override the default output from pydantic.v1 by calling `to_dict()` of asset
        if self.asset:
            _dict['asset'] = self.asset.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SearchedAsset:
        """Create an instance of SearchedAsset from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SearchedAsset.parse_obj(obj)

        _obj = SearchedAsset.parse_obj({
            "var_schema": EmbeddedModelSchema.from_dict(obj.get("schema")) if obj.get("schema") is not None else None,
            "asset": Asset.from_dict(obj.get("asset")) if obj.get("asset") is not None else None,
            "exact": obj.get("exact"),
            "score": obj.get("score"),
            "match": obj.get("match"),
            "identifier": obj.get("identifier"),
            "pseudo": obj.get("pseudo")
        })
        return _obj


