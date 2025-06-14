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
from pydantic.v1 import BaseModel, Field, StrictStr, conlist
from pieces._vendor.pieces_os_client.models.asset_filter_phrase import AssetFilterPhrase
from pieces._vendor.pieces_os_client.models.asset_filter_timestamp import AssetFilterTimestamp
from pieces._vendor.pieces_os_client.models.classification_specific_enum import ClassificationSpecificEnum
from pieces._vendor.pieces_os_client.models.embedded_model_schema import EmbeddedModelSchema

class AssetFilter(BaseModel):
    """
    ** in the future, consider adding an optional bool's called nextAnd, nextOr which will say that the next filter will be  AND behavor or OR behavior.  \"operations\": here is is an optional property to allow or behavior,(we will only allow 1 level deep of or's), if or is not passed in then it is just simply ignored. If or is passed in then we will be or'd together with the top level filter and considered extras. default behavior for operations is and, however yoour can specifiy OR operations as well.  # noqa: E501
    """
    var_schema: Optional[EmbeddedModelSchema] = Field(default=None, alias="schema")
    classification: Optional[ClassificationSpecificEnum] = None
    tags: Optional[conlist(StrictStr)] = None
    websites: Optional[conlist(StrictStr)] = None
    persons: Optional[conlist(StrictStr)] = None
    phrase: Optional[AssetFilterPhrase] = None
    created: Optional[AssetFilterTimestamp] = None
    updated: Optional[AssetFilterTimestamp] = None
    operations: Optional[AssetFilters] = None
    __properties = ["schema", "classification", "tags", "websites", "persons", "phrase", "created", "updated", "operations"]

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
    def from_json(cls, json_str: str) -> AssetFilter:
        """Create an instance of AssetFilter from a JSON string"""
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
        # override the default output from pydantic.v1 by calling `to_dict()` of phrase
        if self.phrase:
            _dict['phrase'] = self.phrase.to_dict()
        # override the default output from pydantic.v1 by calling `to_dict()` of created
        if self.created:
            _dict['created'] = self.created.to_dict()
        # override the default output from pydantic.v1 by calling `to_dict()` of updated
        if self.updated:
            _dict['updated'] = self.updated.to_dict()
        # override the default output from pydantic.v1 by calling `to_dict()` of operations
        if self.operations:
            _dict['operations'] = self.operations.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AssetFilter:
        """Create an instance of AssetFilter from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AssetFilter.parse_obj(obj)

        _obj = AssetFilter.parse_obj({
            "var_schema": EmbeddedModelSchema.from_dict(obj.get("schema")) if obj.get("schema") is not None else None,
            "classification": obj.get("classification"),
            "tags": obj.get("tags"),
            "websites": obj.get("websites"),
            "persons": obj.get("persons"),
            "phrase": AssetFilterPhrase.from_dict(obj.get("phrase")) if obj.get("phrase") is not None else None,
            "created": AssetFilterTimestamp.from_dict(obj.get("created")) if obj.get("created") is not None else None,
            "updated": AssetFilterTimestamp.from_dict(obj.get("updated")) if obj.get("updated") is not None else None,
            "operations": AssetFilters.from_dict(obj.get("operations")) if obj.get("operations") is not None else None
        })
        return _obj

from pieces._vendor.pieces_os_client.models.asset_filters import AssetFilters
AssetFilter.update_forward_refs()

