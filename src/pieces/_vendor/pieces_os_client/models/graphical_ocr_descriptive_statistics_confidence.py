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



from pydantic.v1 import BaseModel, Field, StrictStr

class GraphicalOCRDescriptiveStatisticsConfidence(BaseModel):
    """
    GraphicalOCRDescriptiveStatisticsConfidence
    """
    mean: StrictStr = Field(...)
    __properties = ["mean"]

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
    def from_json(cls, json_str: str) -> GraphicalOCRDescriptiveStatisticsConfidence:
        """Create an instance of GraphicalOCRDescriptiveStatisticsConfidence from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GraphicalOCRDescriptiveStatisticsConfidence:
        """Create an instance of GraphicalOCRDescriptiveStatisticsConfidence from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GraphicalOCRDescriptiveStatisticsConfidence.parse_obj(obj)

        _obj = GraphicalOCRDescriptiveStatisticsConfidence.parse_obj({
            "mean": obj.get("mean")
        })
        return _obj


