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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ContextMenuEntry(BaseModel):
    """
    ContextMenuEntry
    """ # noqa: E501
    position: Optional[StrictInt] = None
    icon: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    url: Optional[StrictStr] = None
    is_disabled: Optional[StrictBool] = Field(default=None, alias="isDisabled")
    open_in_new: Optional[StrictBool] = Field(default=None, alias="openInNew")
    is_separate: Optional[StrictBool] = Field(default=None, alias="isSeparate")
    is_separate_bottom: Optional[StrictBool] = Field(default=None, alias="isSeparateBottom")
    only_desktop: Optional[StrictBool] = Field(default=None, alias="onlyDesktop")
    only_web: Optional[StrictBool] = Field(default=None, alias="onlyWeb")
    mode: Optional[StrictStr] = None
    scopes: Optional[List[StrictStr]] = None
    ajax: Optional[StrictBool] = None
    group: Optional[StrictStr] = None
    permission: Optional[StrictStr] = None
    toolpermission: Optional[StrictStr] = None
    is_directory: Optional[StrictBool] = Field(default=None, alias="isDirectory")
    show_as_action: Optional[StrictBool] = Field(default=None, alias="showAsAction")
    multiple: Optional[StrictBool] = None
    change_strategy: Optional[StrictStr] = Field(default=None, alias="changeStrategy")
    __properties: ClassVar[List[str]] = ["position", "icon", "name", "url", "isDisabled", "openInNew", "isSeparate", "isSeparateBottom", "onlyDesktop", "onlyWeb", "mode", "scopes", "ajax", "group", "permission", "toolpermission", "isDirectory", "showAsAction", "multiple", "changeStrategy"]

    @field_validator('scopes')
    def scopes_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['Render', 'Search', 'CollectionsReferences', 'CollectionsCollection', 'WorkspaceList', 'WorkspaceTree', 'Oer', 'CreateMenu']):
                raise ValueError("each list item must be one of ('Render', 'Search', 'CollectionsReferences', 'CollectionsCollection', 'WorkspaceList', 'WorkspaceTree', 'Oer', 'CreateMenu')")
        return value

    @field_validator('change_strategy')
    def change_strategy_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['update', 'remove']):
            raise ValueError("must be one of enum values ('update', 'remove')")
        return value

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
        """Create an instance of ContextMenuEntry from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ContextMenuEntry from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "position": obj.get("position"),
            "icon": obj.get("icon"),
            "name": obj.get("name"),
            "url": obj.get("url"),
            "isDisabled": obj.get("isDisabled"),
            "openInNew": obj.get("openInNew"),
            "isSeparate": obj.get("isSeparate"),
            "isSeparateBottom": obj.get("isSeparateBottom"),
            "onlyDesktop": obj.get("onlyDesktop"),
            "onlyWeb": obj.get("onlyWeb"),
            "mode": obj.get("mode"),
            "scopes": obj.get("scopes"),
            "ajax": obj.get("ajax"),
            "group": obj.get("group"),
            "permission": obj.get("permission"),
            "toolpermission": obj.get("toolpermission"),
            "isDirectory": obj.get("isDirectory"),
            "showAsAction": obj.get("showAsAction"),
            "multiple": obj.get("multiple"),
            "changeStrategy": obj.get("changeStrategy")
        })
        return _obj


