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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from edu_sharing_client.models.collection import Collection
from edu_sharing_client.models.content import Content
from edu_sharing_client.models.contributor import Contributor
from edu_sharing_client.models.license import License
from edu_sharing_client.models.node import Node
from edu_sharing_client.models.node_lti_deep_link import NodeLTIDeepLink
from edu_sharing_client.models.node_ref import NodeRef
from edu_sharing_client.models.person import Person
from edu_sharing_client.models.preview import Preview
from edu_sharing_client.models.rating_details import RatingDetails
from edu_sharing_client.models.remote import Remote
from typing import Optional, Set
from typing_extensions import Self

class NodeCollectionProposalCount(BaseModel):
    """
    NodeCollectionProposalCount
    """ # noqa: E501
    node_lti_deep_link: Optional[NodeLTIDeepLink] = Field(default=None, alias="nodeLTIDeepLink")
    remote: Optional[Remote] = None
    content: Optional[Content] = None
    license: Optional[License] = None
    is_directory: Optional[StrictBool] = Field(default=None, alias="isDirectory")
    comment_count: Optional[StrictInt] = Field(default=None, alias="commentCount")
    rating: Optional[RatingDetails] = None
    used_in_collections: Optional[List[Node]] = Field(default=None, alias="usedInCollections")
    relations: Optional[Dict[str, Node]] = None
    contributors: Optional[List[Contributor]] = None
    proposal_counts: Optional[Dict[str, StrictInt]] = Field(default=None, alias="proposalCounts")
    proposal_count: Optional[Dict[str, StrictInt]] = Field(default=None, alias="proposalCount")
    ref: NodeRef
    parent: Optional[NodeRef] = None
    type: Optional[StrictStr] = None
    aspects: Optional[List[StrictStr]] = None
    name: StrictStr
    title: Optional[StrictStr] = None
    metadataset: Optional[StrictStr] = None
    repository_type: Optional[StrictStr] = Field(default=None, alias="repositoryType")
    created_at: datetime = Field(alias="createdAt")
    created_by: Person = Field(alias="createdBy")
    modified_at: Optional[datetime] = Field(default=None, alias="modifiedAt")
    modified_by: Optional[Person] = Field(default=None, alias="modifiedBy")
    access: List[StrictStr]
    download_url: StrictStr = Field(alias="downloadUrl")
    properties: Optional[Dict[str, List[StrictStr]]] = None
    mimetype: Optional[StrictStr] = None
    mediatype: Optional[StrictStr] = None
    size: Optional[StrictStr] = None
    preview: Optional[Preview] = None
    icon_url: Optional[StrictStr] = Field(default=None, alias="iconURL")
    collection: Collection
    owner: Person
    is_public: Optional[StrictBool] = Field(default=None, alias="isPublic")
    __properties: ClassVar[List[str]] = ["nodeLTIDeepLink", "remote", "content", "license", "isDirectory", "commentCount", "rating", "usedInCollections", "relations", "contributors", "proposalCounts", "proposalCount", "ref", "parent", "type", "aspects", "name", "title", "metadataset", "repositoryType", "createdAt", "createdBy", "modifiedAt", "modifiedBy", "access", "downloadUrl", "properties", "mimetype", "mediatype", "size", "preview", "iconURL", "collection", "owner", "isPublic"]

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
        """Create an instance of NodeCollectionProposalCount from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of node_lti_deep_link
        if self.node_lti_deep_link:
            _dict['nodeLTIDeepLink'] = self.node_lti_deep_link.to_dict()
        # override the default output from pydantic by calling `to_dict()` of remote
        if self.remote:
            _dict['remote'] = self.remote.to_dict()
        # override the default output from pydantic by calling `to_dict()` of content
        if self.content:
            _dict['content'] = self.content.to_dict()
        # override the default output from pydantic by calling `to_dict()` of license
        if self.license:
            _dict['license'] = self.license.to_dict()
        # override the default output from pydantic by calling `to_dict()` of rating
        if self.rating:
            _dict['rating'] = self.rating.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in used_in_collections (list)
        _items = []
        if self.used_in_collections:
            for _item_used_in_collections in self.used_in_collections:
                if _item_used_in_collections:
                    _items.append(_item_used_in_collections.to_dict())
            _dict['usedInCollections'] = _items
        # override the default output from pydantic by calling `to_dict()` of each value in relations (dict)
        _field_dict = {}
        if self.relations:
            for _key_relations in self.relations:
                if self.relations[_key_relations]:
                    _field_dict[_key_relations] = self.relations[_key_relations].to_dict()
            _dict['relations'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each item in contributors (list)
        _items = []
        if self.contributors:
            for _item_contributors in self.contributors:
                if _item_contributors:
                    _items.append(_item_contributors.to_dict())
            _dict['contributors'] = _items
        # override the default output from pydantic by calling `to_dict()` of ref
        if self.ref:
            _dict['ref'] = self.ref.to_dict()
        # override the default output from pydantic by calling `to_dict()` of parent
        if self.parent:
            _dict['parent'] = self.parent.to_dict()
        # override the default output from pydantic by calling `to_dict()` of created_by
        if self.created_by:
            _dict['createdBy'] = self.created_by.to_dict()
        # override the default output from pydantic by calling `to_dict()` of modified_by
        if self.modified_by:
            _dict['modifiedBy'] = self.modified_by.to_dict()
        # override the default output from pydantic by calling `to_dict()` of preview
        if self.preview:
            _dict['preview'] = self.preview.to_dict()
        # override the default output from pydantic by calling `to_dict()` of collection
        if self.collection:
            _dict['collection'] = self.collection.to_dict()
        # override the default output from pydantic by calling `to_dict()` of owner
        if self.owner:
            _dict['owner'] = self.owner.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NodeCollectionProposalCount from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "nodeLTIDeepLink": NodeLTIDeepLink.from_dict(obj["nodeLTIDeepLink"]) if obj.get("nodeLTIDeepLink") is not None else None,
            "remote": Remote.from_dict(obj["remote"]) if obj.get("remote") is not None else None,
            "content": Content.from_dict(obj["content"]) if obj.get("content") is not None else None,
            "license": License.from_dict(obj["license"]) if obj.get("license") is not None else None,
            "isDirectory": obj.get("isDirectory"),
            "commentCount": obj.get("commentCount"),
            "rating": RatingDetails.from_dict(obj["rating"]) if obj.get("rating") is not None else None,
            "usedInCollections": [Node.from_dict(_item) for _item in obj["usedInCollections"]] if obj.get("usedInCollections") is not None else None,
            "relations": dict(
                (_k, Node.from_dict(_v))
                for _k, _v in obj["relations"].items()
            )
            if obj.get("relations") is not None
            else None,
            "contributors": [Contributor.from_dict(_item) for _item in obj["contributors"]] if obj.get("contributors") is not None else None,
            "proposalCounts": obj.get("proposalCounts"),
            "proposalCount": obj.get("proposalCount"),
            "ref": NodeRef.from_dict(obj["ref"]) if obj.get("ref") is not None else None,
            "parent": NodeRef.from_dict(obj["parent"]) if obj.get("parent") is not None else None,
            "type": obj.get("type"),
            "aspects": obj.get("aspects"),
            "name": obj.get("name"),
            "title": obj.get("title"),
            "metadataset": obj.get("metadataset"),
            "repositoryType": obj.get("repositoryType"),
            "createdAt": obj.get("createdAt"),
            "createdBy": Person.from_dict(obj["createdBy"]) if obj.get("createdBy") is not None else None,
            "modifiedAt": obj.get("modifiedAt"),
            "modifiedBy": Person.from_dict(obj["modifiedBy"]) if obj.get("modifiedBy") is not None else None,
            "access": obj.get("access"),
            "downloadUrl": obj.get("downloadUrl"),
            "properties": obj.get("properties"),
            "mimetype": obj.get("mimetype"),
            "mediatype": obj.get("mediatype"),
            "size": obj.get("size"),
            "preview": Preview.from_dict(obj["preview"]) if obj.get("preview") is not None else None,
            "iconURL": obj.get("iconURL"),
            "collection": Collection.from_dict(obj["collection"]) if obj.get("collection") is not None else None,
            "owner": Person.from_dict(obj["owner"]) if obj.get("owner") is not None else None,
            "isPublic": obj.get("isPublic")
        })
        return _obj


