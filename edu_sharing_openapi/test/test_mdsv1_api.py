# coding: utf-8

"""
    edu-sharing Repository REST API

    The public restful API of the edu-sharing repository.

    The version of the OpenAPI document: 1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from edu_sharing_client.api.mdsv1_api import MDSV1Api


class TestMDSV1Api(unittest.TestCase):
    """MDSV1Api unit test stubs"""

    def setUp(self) -> None:
        self.api = MDSV1Api()

    def tearDown(self) -> None:
        pass

    def test_get_metadata_set(self) -> None:
        """Test case for get_metadata_set

        Get metadata set new.
        """
        pass

    def test_get_metadata_sets(self) -> None:
        """Test case for get_metadata_sets

        Get metadata sets V2 of repository.
        """
        pass

    def test_get_values(self) -> None:
        """Test case for get_values

        Get values.
        """
        pass

    def test_get_values4_keys(self) -> None:
        """Test case for get_values4_keys

        Get values for keys.
        """
        pass

    def test_suggest_value(self) -> None:
        """Test case for suggest_value

        Suggest a value.
        """
        pass


if __name__ == '__main__':
    unittest.main()
