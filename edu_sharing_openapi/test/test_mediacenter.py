# coding: utf-8

"""
    edu-sharing Repository REST API

    The public restful API of the edu-sharing repository.

    The version of the OpenAPI document: 1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from edu_sharing_client.models.mediacenter import Mediacenter

class TestMediacenter(unittest.TestCase):
    """Mediacenter unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Mediacenter:
        """Test Mediacenter
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Mediacenter`
        """
        model = Mediacenter()
        if include_optional:
            return Mediacenter(
                properties = {
                    'key' : [
                        ''
                        ]
                    },
                editable = True,
                signup_method = 'simple',
                ref = edu_sharing_client.models.node_ref.NodeRef(
                    repo = '', 
                    id = '', 
                    archived = True, 
                    is_home_repo = True, ),
                aspects = [
                    ''
                    ],
                organizations = [
                    edu_sharing_client.models.organization.Organization(
                        properties = {
                            'key' : [
                                ''
                                ]
                            }, 
                        editable = True, 
                        signup_method = 'simple', 
                        ref = edu_sharing_client.models.node_ref.NodeRef(
                            repo = '', 
                            id = '', 
                            archived = True, 
                            is_home_repo = True, ), 
                        aspects = [
                            ''
                            ], 
                        authority_name = '', 
                        authority_type = 'USER', 
                        group_name = '', 
                        profile = edu_sharing_client.models.group_profile.GroupProfile(
                            group_email = '', 
                            display_name = '', 
                            group_type = '', 
                            scope_type = '', ), 
                        administration_access = True, 
                        shared_folder = edu_sharing_client.models.node_ref.NodeRef(
                            repo = '', 
                            id = '', 
                            archived = True, 
                            is_home_repo = True, ), )
                    ],
                authority_name = '',
                authority_type = 'USER',
                group_name = '',
                profile = edu_sharing_client.models.group_profile.GroupProfile(
                    group_email = '', 
                    display_name = '', 
                    group_type = '', 
                    scope_type = '', ),
                administration_access = True
            )
        else:
            return Mediacenter(
                authority_name = '',
        )
        """

    def testMediacenter(self):
        """Test Mediacenter"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
