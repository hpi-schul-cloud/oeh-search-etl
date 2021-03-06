# coding: utf-8

"""
    edu-sharing Repository REST API

    The public restful API of the edu-sharing repository.  # noqa: E501

    OpenAPI spec version: 1.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class UserEntry(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'edit_profile': 'bool',
        'person': 'User'
    }

    attribute_map = {
        'edit_profile': 'editProfile',
        'person': 'person'
    }

    def __init__(self, edit_profile=False, person=None):  # noqa: E501
        """UserEntry - a model defined in Swagger"""  # noqa: E501
        self._edit_profile = None
        self._person = None
        self.discriminator = None
        if edit_profile is not None:
            self.edit_profile = edit_profile
        self.person = person

    @property
    def edit_profile(self):
        """Gets the edit_profile of this UserEntry.  # noqa: E501


        :return: The edit_profile of this UserEntry.  # noqa: E501
        :rtype: bool
        """
        return self._edit_profile

    @edit_profile.setter
    def edit_profile(self, edit_profile):
        """Sets the edit_profile of this UserEntry.


        :param edit_profile: The edit_profile of this UserEntry.  # noqa: E501
        :type: bool
        """

        self._edit_profile = edit_profile

    @property
    def person(self):
        """Gets the person of this UserEntry.  # noqa: E501


        :return: The person of this UserEntry.  # noqa: E501
        :rtype: User
        """
        return self._person

    @person.setter
    def person(self, person):
        """Sets the person of this UserEntry.


        :param person: The person of this UserEntry.  # noqa: E501
        :type: User
        """
        if person is None:
            raise ValueError("Invalid value for `person`, must not be `None`")  # noqa: E501

        self._person = person

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(UserEntry, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UserEntry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
