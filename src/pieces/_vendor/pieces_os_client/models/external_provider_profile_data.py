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
from pydantic.v1 import BaseModel, StrictBool, StrictInt, StrictStr

class ExternalProviderProfileData(BaseModel):
    """
    All of these will be optional.  Will support ProfileData from all our social providers.  # noqa: E501
    """
    name: Optional[StrictStr] = None
    picture: Optional[StrictStr] = None
    nickname: Optional[StrictStr] = None
    email: Optional[StrictStr] = None
    email_verified: Optional[StrictBool] = None
    node_id: Optional[StrictStr] = None
    gravatar_id: Optional[StrictStr] = None
    url: Optional[StrictStr] = None
    html_url: Optional[StrictStr] = None
    followers_url: Optional[StrictStr] = None
    following_url: Optional[StrictStr] = None
    gists_url: Optional[StrictStr] = None
    starred_url: Optional[StrictStr] = None
    subscriptions_url: Optional[StrictStr] = None
    organizations_url: Optional[StrictStr] = None
    repos_url: Optional[StrictStr] = None
    events_url: Optional[StrictStr] = None
    received_events_url: Optional[StrictStr] = None
    type: Optional[StrictStr] = None
    site_admin: Optional[StrictBool] = None
    company: Optional[StrictStr] = None
    blog: Optional[StrictStr] = None
    anchor: Optional[StrictStr] = None
    hireable: Optional[StrictBool] = None
    bio: Optional[StrictStr] = None
    twitter_username: Optional[StrictStr] = None
    public_repos: Optional[StrictInt] = None
    public_gists: Optional[StrictInt] = None
    followers: Optional[StrictInt] = None
    following: Optional[StrictInt] = None
    created_at: Optional[StrictStr] = None
    updated_at: Optional[StrictStr] = None
    private_gists: Optional[StrictInt] = None
    total_private_repos: Optional[StrictInt] = None
    owned_private_repos: Optional[StrictInt] = None
    disk_usage: Optional[StrictInt] = None
    collaborators: Optional[StrictInt] = None
    two_factor_authentication: Optional[StrictBool] = None
    __properties = ["name", "picture", "nickname", "email", "email_verified", "node_id", "gravatar_id", "url", "html_url", "followers_url", "following_url", "gists_url", "starred_url", "subscriptions_url", "organizations_url", "repos_url", "events_url", "received_events_url", "type", "site_admin", "company", "blog", "anchor", "hireable", "bio", "twitter_username", "public_repos", "public_gists", "followers", "following", "created_at", "updated_at", "private_gists", "total_private_repos", "owned_private_repos", "disk_usage", "collaborators", "two_factor_authentication"]

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
    def from_json(cls, json_str: str) -> ExternalProviderProfileData:
        """Create an instance of ExternalProviderProfileData from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ExternalProviderProfileData:
        """Create an instance of ExternalProviderProfileData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ExternalProviderProfileData.parse_obj(obj)

        _obj = ExternalProviderProfileData.parse_obj({
            "name": obj.get("name"),
            "picture": obj.get("picture"),
            "nickname": obj.get("nickname"),
            "email": obj.get("email"),
            "email_verified": obj.get("email_verified"),
            "node_id": obj.get("node_id"),
            "gravatar_id": obj.get("gravatar_id"),
            "url": obj.get("url"),
            "html_url": obj.get("html_url"),
            "followers_url": obj.get("followers_url"),
            "following_url": obj.get("following_url"),
            "gists_url": obj.get("gists_url"),
            "starred_url": obj.get("starred_url"),
            "subscriptions_url": obj.get("subscriptions_url"),
            "organizations_url": obj.get("organizations_url"),
            "repos_url": obj.get("repos_url"),
            "events_url": obj.get("events_url"),
            "received_events_url": obj.get("received_events_url"),
            "type": obj.get("type"),
            "site_admin": obj.get("site_admin"),
            "company": obj.get("company"),
            "blog": obj.get("blog"),
            "anchor": obj.get("anchor"),
            "hireable": obj.get("hireable"),
            "bio": obj.get("bio"),
            "twitter_username": obj.get("twitter_username"),
            "public_repos": obj.get("public_repos"),
            "public_gists": obj.get("public_gists"),
            "followers": obj.get("followers"),
            "following": obj.get("following"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "private_gists": obj.get("private_gists"),
            "total_private_repos": obj.get("total_private_repos"),
            "owned_private_repos": obj.get("owned_private_repos"),
            "disk_usage": obj.get("disk_usage"),
            "collaborators": obj.get("collaborators"),
            "two_factor_authentication": obj.get("two_factor_authentication")
        })
        return _obj


