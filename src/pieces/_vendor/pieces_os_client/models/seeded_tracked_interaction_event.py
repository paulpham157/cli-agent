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
from pieces._vendor.pieces_os_client.models.seeded_tracked_interaction_event_identifier_description_pairs import SeededTrackedInteractionEventIdentifierDescriptionPairs

class SeededTrackedInteractionEvent(BaseModel):
    """
    This is a model that will hold relavent information in relation to an interaction(ONLY CLICK/TAP) analytics event(usage). If you want to register an event that relates to an interaction with the key then register a Keyboard Event.   # noqa: E501
    """
    var_schema: Optional[EmbeddedModelSchema] = Field(default=None, alias="schema")
    description: StrictStr = Field(default=..., description="These need structure")
    element: Optional[StrictStr] = None
    identifier_description_pair: Optional[SeededTrackedInteractionEventIdentifierDescriptionPairs] = None
    __properties = ["schema", "description", "element", "identifier_description_pair"]

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
    def from_json(cls, json_str: str) -> SeededTrackedInteractionEvent:
        """Create an instance of SeededTrackedInteractionEvent from a JSON string"""
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
        # override the default output from pydantic.v1 by calling `to_dict()` of identifier_description_pair
        if self.identifier_description_pair:
            _dict['identifier_description_pair'] = self.identifier_description_pair.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SeededTrackedInteractionEvent:
        """Create an instance of SeededTrackedInteractionEvent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SeededTrackedInteractionEvent.parse_obj(obj)

        _obj = SeededTrackedInteractionEvent.parse_obj({
            "var_schema": EmbeddedModelSchema.from_dict(obj.get("schema")) if obj.get("schema") is not None else None,
            "description": obj.get("description"),
            "element": obj.get("element"),
            "identifier_description_pair": SeededTrackedInteractionEventIdentifierDescriptionPairs.from_dict(obj.get("identifier_description_pair")) if obj.get("identifier_description_pair") is not None else None
        })
        return _obj


