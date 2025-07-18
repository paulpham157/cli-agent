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


from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist
from pieces._vendor.pieces_os_client.models.paddle_checkout_customer import PaddleCheckoutCustomer
from pieces._vendor.pieces_os_client.models.paddle_checkout_item import PaddleCheckoutItem
from pieces._vendor.pieces_os_client.models.paddle_checkout_payment import PaddleCheckoutPayment
from pieces._vendor.pieces_os_client.models.paddle_checkout_settings import PaddleCheckoutSettings
from pieces._vendor.pieces_os_client.models.paddle_checkout_totals import PaddleCheckoutTotals

class PaddleCheckoutLoadedEventData(BaseModel):
    """
    PaddleCheckoutLoadedEventData
    """
    id: StrictStr = Field(...)
    transaction_id: StrictStr = Field(...)
    status: StrictStr = Field(...)
    custom_data: Optional[Dict[str, Any]] = None
    currency_code: StrictStr = Field(...)
    customer: PaddleCheckoutCustomer = Field(...)
    items: conlist(PaddleCheckoutItem) = Field(...)
    totals: PaddleCheckoutTotals = Field(...)
    payment: PaddleCheckoutPayment = Field(...)
    settings: PaddleCheckoutSettings = Field(...)
    recurring_totals: PaddleCheckoutTotals = Field(...)
    __properties = ["id", "transaction_id", "status", "custom_data", "currency_code", "customer", "items", "totals", "payment", "settings", "recurring_totals"]

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
    def from_json(cls, json_str: str) -> PaddleCheckoutLoadedEventData:
        """Create an instance of PaddleCheckoutLoadedEventData from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic.v1 by calling `to_dict()` of customer
        if self.customer:
            _dict['customer'] = self.customer.to_dict()
        # override the default output from pydantic.v1 by calling `to_dict()` of each item in items (list)
        _items = []
        if self.items:
            for _item in self.items:
                if _item:
                    _items.append(_item.to_dict())
            _dict['items'] = _items
        # override the default output from pydantic.v1 by calling `to_dict()` of totals
        if self.totals:
            _dict['totals'] = self.totals.to_dict()
        # override the default output from pydantic.v1 by calling `to_dict()` of payment
        if self.payment:
            _dict['payment'] = self.payment.to_dict()
        # override the default output from pydantic.v1 by calling `to_dict()` of settings
        if self.settings:
            _dict['settings'] = self.settings.to_dict()
        # override the default output from pydantic.v1 by calling `to_dict()` of recurring_totals
        if self.recurring_totals:
            _dict['recurring_totals'] = self.recurring_totals.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PaddleCheckoutLoadedEventData:
        """Create an instance of PaddleCheckoutLoadedEventData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PaddleCheckoutLoadedEventData.parse_obj(obj)

        _obj = PaddleCheckoutLoadedEventData.parse_obj({
            "id": obj.get("id"),
            "transaction_id": obj.get("transaction_id"),
            "status": obj.get("status"),
            "custom_data": obj.get("custom_data"),
            "currency_code": obj.get("currency_code"),
            "customer": PaddleCheckoutCustomer.from_dict(obj.get("customer")) if obj.get("customer") is not None else None,
            "items": [PaddleCheckoutItem.from_dict(_item) for _item in obj.get("items")] if obj.get("items") is not None else None,
            "totals": PaddleCheckoutTotals.from_dict(obj.get("totals")) if obj.get("totals") is not None else None,
            "payment": PaddleCheckoutPayment.from_dict(obj.get("payment")) if obj.get("payment") is not None else None,
            "settings": PaddleCheckoutSettings.from_dict(obj.get("settings")) if obj.get("settings") is not None else None,
            "recurring_totals": PaddleCheckoutTotals.from_dict(obj.get("recurring_totals")) if obj.get("recurring_totals") is not None else None
        })
        return _obj


