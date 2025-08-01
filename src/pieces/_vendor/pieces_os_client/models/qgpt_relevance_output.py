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
from pieces._vendor.pieces_os_client.models.embedded_model_schema import EmbeddedModelSchema
from pieces._vendor.pieces_os_client.models.qgpt_question_output import QGPTQuestionOutput
from pieces._vendor.pieces_os_client.models.relevant_qgpt_seeds import RelevantQGPTSeeds

class QGPTRelevanceOutput(BaseModel):
    """
    This is the returned value from /code_gpt/relevance.  This will return the snippets that we found are relevant to the query you provided.  (optional) answer: in the case you provided question: true, then we will also return to you the answer to your question.  Note: - relevant: this is required property and will represent the relevant snippets, to your specific query.(NOTE: these snippet will all have respective id's and seed defined. even though id and seed are optional)  # noqa: E501
    """
    var_schema: Optional[EmbeddedModelSchema] = Field(default=None, alias="schema")
    answer: Optional[QGPTQuestionOutput] = None
    relevant: RelevantQGPTSeeds = Field(...)
    __properties = ["schema", "answer", "relevant"]

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
    def from_json(cls, json_str: str) -> QGPTRelevanceOutput:
        """Create an instance of QGPTRelevanceOutput from a JSON string"""
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
        # override the default output from pydantic.v1 by calling `to_dict()` of answer
        if self.answer:
            _dict['answer'] = self.answer.to_dict()
        # override the default output from pydantic.v1 by calling `to_dict()` of relevant
        if self.relevant:
            _dict['relevant'] = self.relevant.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> QGPTRelevanceOutput:
        """Create an instance of QGPTRelevanceOutput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return QGPTRelevanceOutput.parse_obj(obj)

        _obj = QGPTRelevanceOutput.parse_obj({
            "var_schema": EmbeddedModelSchema.from_dict(obj.get("schema")) if obj.get("schema") is not None else None,
            "answer": QGPTQuestionOutput.from_dict(obj.get("answer")) if obj.get("answer") is not None else None,
            "relevant": RelevantQGPTSeeds.from_dict(obj.get("relevant")) if obj.get("relevant") is not None else None
        })
        return _obj


