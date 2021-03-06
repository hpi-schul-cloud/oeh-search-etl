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


class Body2(object):
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
        'excel': 'str'
    }

    attribute_map = {
        'excel': 'excel'
    }

    def __init__(self, excel=None):  # noqa: E501
        """Body2 - a model defined in Swagger"""  # noqa: E501
        self._excel = None
        self.discriminator = None
        self.excel = excel

    @property
    def excel(self):
        """Gets the excel of this Body2.  # noqa: E501

        Excel file to import  # noqa: E501

        :return: The excel of this Body2.  # noqa: E501
        :rtype: str
        """
        return self._excel

    @excel.setter
    def excel(self, excel):
        """Sets the excel of this Body2.

        Excel file to import  # noqa: E501

        :param excel: The excel of this Body2.  # noqa: E501
        :type: str
        """
        if excel is None:
            raise ValueError("Invalid value for `excel`, must not be `None`")  # noqa: E501

        self._excel = excel

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
        if issubclass(Body2, dict):
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
        if not isinstance(other, Body2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
