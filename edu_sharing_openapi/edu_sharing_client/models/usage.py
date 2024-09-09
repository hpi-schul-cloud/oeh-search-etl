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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from edu_sharing_client.models.parameters import Parameters
from typing import Optional, Set
from typing_extensions import Self

class Usage(BaseModel):
    """
    Usage
    """ # noqa: E501
    from_used: Optional[datetime] = Field(default=None, alias="fromUsed")
    to_used: Optional[datetime] = Field(default=None, alias="toUsed")
    usage_counter: Optional[StrictInt] = Field(default=None, alias="usageCounter")
    app_subtype: Optional[StrictStr] = Field(default=None, alias="appSubtype")
    app_type: Optional[StrictStr] = Field(default=None, alias="appType")
    type: Optional[StrictStr] = None
    created: Optional[datetime] = None
    modified: Optional[datetime] = None
    app_user: StrictStr = Field(alias="appUser")
    app_user_mail: StrictStr = Field(alias="appUserMail")
    course_id: StrictStr = Field(alias="courseId")
    distinct_persons: Optional[StrictInt] = Field(default=None, alias="distinctPersons")
    app_id: StrictStr = Field(alias="appId")
    node_id: StrictStr = Field(alias="nodeId")
    parent_node_id: StrictStr = Field(alias="parentNodeId")
    usage_version: StrictStr = Field(alias="usageVersion")
    usage_xml_params: Optional[Parameters] = Field(default=None, alias="usageXmlParams")
    usage_xml_params_raw: Optional[StrictStr] = Field(default=None, alias="usageXmlParamsRaw")
    resource_id: StrictStr = Field(alias="resourceId")
    guid: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["fromUsed", "toUsed", "usageCounter", "appSubtype", "appType", "type", "created", "modified", "appUser", "appUserMail", "courseId", "distinctPersons", "appId", "nodeId", "parentNodeId", "usageVersion", "usageXmlParams", "usageXmlParamsRaw", "resourceId", "guid"]

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
        """Create an instance of Usage from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of usage_xml_params
        if self.usage_xml_params:
            _dict['usageXmlParams'] = self.usage_xml_params.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Usage from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "fromUsed": obj.get("fromUsed"),
            "toUsed": obj.get("toUsed"),
            "usageCounter": obj.get("usageCounter"),
            "appSubtype": obj.get("appSubtype"),
            "appType": obj.get("appType"),
            "type": obj.get("type"),
            "created": obj.get("created"),
            "modified": obj.get("modified"),
            "appUser": obj.get("appUser"),
            "appUserMail": obj.get("appUserMail"),
            "courseId": obj.get("courseId"),
            "distinctPersons": obj.get("distinctPersons"),
            "appId": obj.get("appId"),
            "nodeId": obj.get("nodeId"),
            "parentNodeId": obj.get("parentNodeId"),
            "usageVersion": obj.get("usageVersion"),
            "usageXmlParams": Parameters.from_dict(obj["usageXmlParams"]) if obj.get("usageXmlParams") is not None else None,
            "usageXmlParamsRaw": obj.get("usageXmlParamsRaw"),
            "resourceId": obj.get("resourceId"),
            "guid": obj.get("guid")
        })
        return _obj


