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


class AdminStatistics(object):
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
        'active_sessions': 'int',
        'number_of_previews': 'int',
        'max_memory': 'int',
        'allocated_memory': 'int',
        'preview_cache_size': 'int',
        'active_locks': 'list[Node]'
    }

    attribute_map = {
        'active_sessions': 'activeSessions',
        'number_of_previews': 'numberOfPreviews',
        'max_memory': 'maxMemory',
        'allocated_memory': 'allocatedMemory',
        'preview_cache_size': 'previewCacheSize',
        'active_locks': 'activeLocks'
    }

    def __init__(self, active_sessions=None, number_of_previews=None, max_memory=None, allocated_memory=None, preview_cache_size=None, active_locks=None):  # noqa: E501
        """AdminStatistics - a model defined in Swagger"""  # noqa: E501
        self._active_sessions = None
        self._number_of_previews = None
        self._max_memory = None
        self._allocated_memory = None
        self._preview_cache_size = None
        self._active_locks = None
        self.discriminator = None
        if active_sessions is not None:
            self.active_sessions = active_sessions
        if number_of_previews is not None:
            self.number_of_previews = number_of_previews
        if max_memory is not None:
            self.max_memory = max_memory
        if allocated_memory is not None:
            self.allocated_memory = allocated_memory
        if preview_cache_size is not None:
            self.preview_cache_size = preview_cache_size
        if active_locks is not None:
            self.active_locks = active_locks

    @property
    def active_sessions(self):
        """Gets the active_sessions of this AdminStatistics.  # noqa: E501


        :return: The active_sessions of this AdminStatistics.  # noqa: E501
        :rtype: int
        """
        return self._active_sessions

    @active_sessions.setter
    def active_sessions(self, active_sessions):
        """Sets the active_sessions of this AdminStatistics.


        :param active_sessions: The active_sessions of this AdminStatistics.  # noqa: E501
        :type: int
        """

        self._active_sessions = active_sessions

    @property
    def number_of_previews(self):
        """Gets the number_of_previews of this AdminStatistics.  # noqa: E501


        :return: The number_of_previews of this AdminStatistics.  # noqa: E501
        :rtype: int
        """
        return self._number_of_previews

    @number_of_previews.setter
    def number_of_previews(self, number_of_previews):
        """Sets the number_of_previews of this AdminStatistics.


        :param number_of_previews: The number_of_previews of this AdminStatistics.  # noqa: E501
        :type: int
        """

        self._number_of_previews = number_of_previews

    @property
    def max_memory(self):
        """Gets the max_memory of this AdminStatistics.  # noqa: E501


        :return: The max_memory of this AdminStatistics.  # noqa: E501
        :rtype: int
        """
        return self._max_memory

    @max_memory.setter
    def max_memory(self, max_memory):
        """Sets the max_memory of this AdminStatistics.


        :param max_memory: The max_memory of this AdminStatistics.  # noqa: E501
        :type: int
        """

        self._max_memory = max_memory

    @property
    def allocated_memory(self):
        """Gets the allocated_memory of this AdminStatistics.  # noqa: E501


        :return: The allocated_memory of this AdminStatistics.  # noqa: E501
        :rtype: int
        """
        return self._allocated_memory

    @allocated_memory.setter
    def allocated_memory(self, allocated_memory):
        """Sets the allocated_memory of this AdminStatistics.


        :param allocated_memory: The allocated_memory of this AdminStatistics.  # noqa: E501
        :type: int
        """

        self._allocated_memory = allocated_memory

    @property
    def preview_cache_size(self):
        """Gets the preview_cache_size of this AdminStatistics.  # noqa: E501


        :return: The preview_cache_size of this AdminStatistics.  # noqa: E501
        :rtype: int
        """
        return self._preview_cache_size

    @preview_cache_size.setter
    def preview_cache_size(self, preview_cache_size):
        """Sets the preview_cache_size of this AdminStatistics.


        :param preview_cache_size: The preview_cache_size of this AdminStatistics.  # noqa: E501
        :type: int
        """

        self._preview_cache_size = preview_cache_size

    @property
    def active_locks(self):
        """Gets the active_locks of this AdminStatistics.  # noqa: E501


        :return: The active_locks of this AdminStatistics.  # noqa: E501
        :rtype: list[Node]
        """
        return self._active_locks

    @active_locks.setter
    def active_locks(self, active_locks):
        """Sets the active_locks of this AdminStatistics.


        :param active_locks: The active_locks of this AdminStatistics.  # noqa: E501
        :type: list[Node]
        """

        self._active_locks = active_locks

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
        if issubclass(AdminStatistics, dict):
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
        if not isinstance(other, AdminStatistics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other