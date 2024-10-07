# coding: utf-8

"""
    edu-sharing Repository REST API

    The public restful API of the edu-sharing repository.

    The version of the OpenAPI document: 1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from edu_sharing_client.models.node import Node
from edu_sharing_client.models.tracking_authority import TrackingAuthority
from typing import Optional, Set
from typing_extensions import Self

class TrackingNode(BaseModel):
    """
    TrackingNode
    """ # noqa: E501
    counts: Optional[Dict[str, StrictInt]] = None
    var_date: Optional[StrictStr] = Field(default=None, alias="date")
    fields: Optional[Dict[str, Dict[str, Any]]] = None
    groups: Optional[Dict[str, Dict[str, Dict[str, StrictInt]]]] = None
    node: Optional[Node] = None
    authority: Optional[TrackingAuthority] = None
    __properties: ClassVar[List[str]] = ["counts", "date", "fields", "groups", "node", "authority"]

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
        """Create an instance of TrackingNode from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of node
        if self.node:
            _dict['node'] = self.node.to_dict()
        # override the default output from pydantic by calling `to_dict()` of authority
        if self.authority:
            _dict['authority'] = self.authority.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TrackingNode from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "counts": obj.get("counts"),
            "date": obj.get("date"),
            "fields": obj.get("fields"),
            "groups": obj.get("groups"),
            "node": Node.from_dict(obj["node"]) if obj.get("node") is not None else None,
            "authority": TrackingAuthority.from_dict(obj["authority"]) if obj.get("authority") is not None else None
        })
        return _obj


