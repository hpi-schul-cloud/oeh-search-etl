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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from edu_sharing_client.models.job_detail import JobDetail
from edu_sharing_client.models.job_detail_job_data_map import JobDetailJobDataMap
from edu_sharing_client.models.level import Level
from edu_sharing_client.models.log_entry import LogEntry
from typing import Optional, Set
from typing_extensions import Self

class JobInfo(BaseModel):
    """
    JobInfo
    """ # noqa: E501
    job_data_map: Optional[JobDetailJobDataMap] = Field(default=None, alias="jobDataMap")
    job_name: Optional[StrictStr] = Field(default=None, alias="jobName")
    job_group: Optional[StrictStr] = Field(default=None, alias="jobGroup")
    start_time: Optional[StrictInt] = Field(default=None, alias="startTime")
    finish_time: Optional[StrictInt] = Field(default=None, alias="finishTime")
    status: Optional[StrictStr] = None
    worst_level: Optional[Level] = Field(default=None, alias="worstLevel")
    log: Optional[List[LogEntry]] = None
    job_detail: Optional[JobDetail] = Field(default=None, alias="jobDetail")
    __properties: ClassVar[List[str]] = ["jobDataMap", "jobName", "jobGroup", "startTime", "finishTime", "status", "worstLevel", "log", "jobDetail"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Running', 'Failed', 'Aborted', 'Finished']):
            raise ValueError("must be one of enum values ('Running', 'Failed', 'Aborted', 'Finished')")
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
        """Create an instance of JobInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of job_data_map
        if self.job_data_map:
            _dict['jobDataMap'] = self.job_data_map.to_dict()
        # override the default output from pydantic by calling `to_dict()` of worst_level
        if self.worst_level:
            _dict['worstLevel'] = self.worst_level.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in log (list)
        _items = []
        if self.log:
            for _item_log in self.log:
                if _item_log:
                    _items.append(_item_log.to_dict())
            _dict['log'] = _items
        # override the default output from pydantic by calling `to_dict()` of job_detail
        if self.job_detail:
            _dict['jobDetail'] = self.job_detail.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of JobInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "jobDataMap": JobDetailJobDataMap.from_dict(obj["jobDataMap"]) if obj.get("jobDataMap") is not None else None,
            "jobName": obj.get("jobName"),
            "jobGroup": obj.get("jobGroup"),
            "startTime": obj.get("startTime"),
            "finishTime": obj.get("finishTime"),
            "status": obj.get("status"),
            "worstLevel": Level.from_dict(obj["worstLevel"]) if obj.get("worstLevel") is not None else None,
            "log": [LogEntry.from_dict(_item) for _item in obj["log"]] if obj.get("log") is not None else None,
            "jobDetail": JobDetail.from_dict(obj["jobDetail"]) if obj.get("jobDetail") is not None else None
        })
        return _obj


