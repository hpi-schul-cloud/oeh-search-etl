# coding: utf-8

"""
    edu-sharing Repository REST API

    The public restful API of the edu-sharing repository.

    The version of the OpenAPI document: 1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from edu_sharing_client.models.contributor import Contributor

class TestContributor(unittest.TestCase):
    """Contributor unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Contributor:
        """Test Contributor
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Contributor`
        """
        model = Contributor()
        if include_optional:
            return Contributor(
                var_property = '',
                firstname = '',
                lastname = '',
                email = '',
                vcard = '',
                org = ''
            )
        else:
            return Contributor(
        )
        """

    def testContributor(self):
        """Test Contributor"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
