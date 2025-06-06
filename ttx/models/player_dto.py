# coding: utf-8

"""
    TTX.Api

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List
from ttx.models.loot_box_dto import LootBoxDto
from ttx.models.player_share_dto import PlayerShareDto
from ttx.models.player_transaction_dto import PlayerTransactionDto
from ttx.models.player_type import PlayerType
from ttx.models.portfolio_snapshot_dto import PortfolioSnapshotDto
from typing import Optional, Set
from typing_extensions import Self

class PlayerDto(BaseModel):
    """
    PlayerDto
    """ # noqa: E501
    id: StrictInt
    created_at: datetime
    updated_at: datetime
    name: StrictStr
    slug: StrictStr
    twitch_id: StrictStr
    url: StrictStr
    avatar_url: StrictStr
    credits: StrictInt
    portfolio: StrictInt
    value: StrictInt
    type: PlayerType
    transactions: List[PlayerTransactionDto]
    loot_boxes: List[LootBoxDto]
    shares: List[PlayerShareDto]
    history: List[PortfolioSnapshotDto]
    __properties: ClassVar[List[str]] = ["id", "created_at", "updated_at", "name", "slug", "twitch_id", "url", "avatar_url", "credits", "portfolio", "value", "type", "transactions", "loot_boxes", "shares", "history"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of PlayerDto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "url",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in transactions (list)
        _items = []
        if self.transactions:
            for _item_transactions in self.transactions:
                if _item_transactions:
                    _items.append(_item_transactions.to_dict())
            _dict['transactions'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in loot_boxes (list)
        _items = []
        if self.loot_boxes:
            for _item_loot_boxes in self.loot_boxes:
                if _item_loot_boxes:
                    _items.append(_item_loot_boxes.to_dict())
            _dict['loot_boxes'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in shares (list)
        _items = []
        if self.shares:
            for _item_shares in self.shares:
                if _item_shares:
                    _items.append(_item_shares.to_dict())
            _dict['shares'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in history (list)
        _items = []
        if self.history:
            for _item_history in self.history:
                if _item_history:
                    _items.append(_item_history.to_dict())
            _dict['history'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PlayerDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "name": obj.get("name"),
            "slug": obj.get("slug"),
            "twitch_id": obj.get("twitch_id"),
            "url": obj.get("url"),
            "avatar_url": obj.get("avatar_url"),
            "credits": obj.get("credits"),
            "portfolio": obj.get("portfolio"),
            "value": obj.get("value"),
            "type": obj.get("type"),
            "transactions": [PlayerTransactionDto.from_dict(_item) for _item in obj["transactions"]] if obj.get("transactions") is not None else None,
            "loot_boxes": [LootBoxDto.from_dict(_item) for _item in obj["loot_boxes"]] if obj.get("loot_boxes") is not None else None,
            "shares": [PlayerShareDto.from_dict(_item) for _item in obj["shares"]] if obj.get("shares") is not None else None,
            "history": [PortfolioSnapshotDto.from_dict(_item) for _item in obj["history"]] if obj.get("history") is not None else None
        })
        return _obj


