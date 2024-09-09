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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class NotificationIntervals(BaseModel):
    """
    NotificationIntervals
    """ # noqa: E501
    add_to_collection_event: Optional[StrictStr] = Field(default=None, alias="addToCollectionEvent")
    propose_for_collection_event: Optional[StrictStr] = Field(default=None, alias="proposeForCollectionEvent")
    comment_event: Optional[StrictStr] = Field(default=None, alias="commentEvent")
    invite_event: Optional[StrictStr] = Field(default=None, alias="inviteEvent")
    node_issue_event: Optional[StrictStr] = Field(default=None, alias="nodeIssueEvent")
    rating_event: Optional[StrictStr] = Field(default=None, alias="ratingEvent")
    workflow_event: Optional[StrictStr] = Field(default=None, alias="workflowEvent")
    metadata_suggestion_event: Optional[StrictStr] = Field(default=None, alias="metadataSuggestionEvent")
    __properties: ClassVar[List[str]] = ["addToCollectionEvent", "proposeForCollectionEvent", "commentEvent", "inviteEvent", "nodeIssueEvent", "ratingEvent", "workflowEvent", "metadataSuggestionEvent"]

    @field_validator('add_to_collection_event')
    def add_to_collection_event_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['immediately', 'disabled', 'daily', 'weekly']):
            raise ValueError("must be one of enum values ('immediately', 'disabled', 'daily', 'weekly')")
        return value

    @field_validator('propose_for_collection_event')
    def propose_for_collection_event_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['immediately', 'disabled', 'daily', 'weekly']):
            raise ValueError("must be one of enum values ('immediately', 'disabled', 'daily', 'weekly')")
        return value

    @field_validator('comment_event')
    def comment_event_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['immediately', 'disabled', 'daily', 'weekly']):
            raise ValueError("must be one of enum values ('immediately', 'disabled', 'daily', 'weekly')")
        return value

    @field_validator('invite_event')
    def invite_event_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['immediately', 'disabled', 'daily', 'weekly']):
            raise ValueError("must be one of enum values ('immediately', 'disabled', 'daily', 'weekly')")
        return value

    @field_validator('node_issue_event')
    def node_issue_event_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['immediately', 'disabled', 'daily', 'weekly']):
            raise ValueError("must be one of enum values ('immediately', 'disabled', 'daily', 'weekly')")
        return value

    @field_validator('rating_event')
    def rating_event_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['immediately', 'disabled', 'daily', 'weekly']):
            raise ValueError("must be one of enum values ('immediately', 'disabled', 'daily', 'weekly')")
        return value

    @field_validator('workflow_event')
    def workflow_event_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['immediately', 'disabled', 'daily', 'weekly']):
            raise ValueError("must be one of enum values ('immediately', 'disabled', 'daily', 'weekly')")
        return value

    @field_validator('metadata_suggestion_event')
    def metadata_suggestion_event_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['immediately', 'disabled', 'daily', 'weekly']):
            raise ValueError("must be one of enum values ('immediately', 'disabled', 'daily', 'weekly')")
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
        """Create an instance of NotificationIntervals from a JSON string"""
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
        """Create an instance of NotificationIntervals from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "addToCollectionEvent": obj.get("addToCollectionEvent"),
            "proposeForCollectionEvent": obj.get("proposeForCollectionEvent"),
            "commentEvent": obj.get("commentEvent"),
            "inviteEvent": obj.get("inviteEvent"),
            "nodeIssueEvent": obj.get("nodeIssueEvent"),
            "ratingEvent": obj.get("ratingEvent"),
            "workflowEvent": obj.get("workflowEvent"),
            "metadataSuggestionEvent": obj.get("metadataSuggestionEvent")
        })
        return _obj


