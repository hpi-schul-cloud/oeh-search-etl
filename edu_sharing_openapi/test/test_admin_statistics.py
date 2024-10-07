# coding: utf-8

"""
    edu-sharing Repository REST API

    The public restful API of the edu-sharing repository.

    The version of the OpenAPI document: 1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from edu_sharing_client.models.admin_statistics import AdminStatistics

class TestAdminStatistics(unittest.TestCase):
    """AdminStatistics unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AdminStatistics:
        """Test AdminStatistics
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AdminStatistics`
        """
        model = AdminStatistics()
        if include_optional:
            return AdminStatistics(
                active_sessions = 56,
                number_of_previews = 56,
                max_memory = 56,
                allocated_memory = 56,
                preview_cache_size = 56,
                active_locks = [
                    edu_sharing_client.models.node.Node(
                        node_lti_deep_link = edu_sharing_client.models.node_lti_deep_link.NodeLTIDeepLink(
                            lti_deep_link_return_url = '', 
                            jwt_deep_link_response = '', ), 
                        remote = edu_sharing_client.models.remote.Remote(
                            repository = edu_sharing_client.models.repo.Repo(
                                repository_type = '', 
                                rendering_supported = True, 
                                id = '', 
                                title = '', 
                                icon = '', 
                                logo = '', 
                                is_home_repo = True, ), 
                            id = '', ), 
                        content = edu_sharing_client.models.content.Content(
                            url = '', 
                            hash = '', 
                            version = '', ), 
                        license = edu_sharing_client.models.license.License(
                            icon = '', 
                            url = '', ), 
                        is_directory = True, 
                        comment_count = 56, 
                        rating = edu_sharing_client.models.rating_details.RatingDetails(
                            overall = edu_sharing_client.models.rating_data.RatingData(
                                sum = 1.337, 
                                count = 56, ), 
                            affiliation = {
                                'key' : edu_sharing_client.models.rating_data.RatingData(
                                    sum = 1.337, 
                                    count = 56, )
                                }, 
                            user = 1.337, ), 
                        used_in_collections = [
                            edu_sharing_client.models.node.Node(
                                is_directory = True, 
                                comment_count = 56, 
                                relations = {
                                    'key' : 
                                    }, 
                                contributors = [
                                    edu_sharing_client.models.contributor.Contributor(
                                        property = '', 
                                        firstname = '', 
                                        lastname = '', 
                                        email = '', 
                                        vcard = '', 
                                        org = '', )
                                    ], 
                                ref = edu_sharing_client.models.node_ref.NodeRef(
                                    repo = '', 
                                    id = '', 
                                    archived = True, 
                                    is_home_repo = True, ), 
                                parent = edu_sharing_client.models.node_ref.NodeRef(
                                    repo = '', 
                                    id = '', 
                                    archived = True, 
                                    is_home_repo = True, ), 
                                type = '', 
                                aspects = [
                                    ''
                                    ], 
                                name = '', 
                                title = '', 
                                metadataset = '', 
                                repository_type = '', 
                                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                created_by = edu_sharing_client.models.person.Person(
                                    profile = edu_sharing_client.models.user_profile.UserProfile(
                                        primary_affiliation = '', 
                                        skills = [
                                            ''
                                            ], 
                                        types = [
                                            ''
                                            ], 
                                        vcard = '', 
                                        type = [
                                            ''
                                            ], 
                                        first_name = '', 
                                        last_name = '', 
                                        email = '', 
                                        avatar = '', 
                                        about = '', ), 
                                    first_name = '', 
                                    last_name = '', 
                                    mailbox = '', ), 
                                modified_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                modified_by = edu_sharing_client.models.person.Person(
                                    first_name = '', 
                                    last_name = '', 
                                    mailbox = '', ), 
                                access = [
                                    ''
                                    ], 
                                download_url = '', 
                                properties = {
                                    'key' : [
                                        ''
                                        ]
                                    }, 
                                mimetype = '', 
                                mediatype = '', 
                                size = '', 
                                preview = edu_sharing_client.models.preview.Preview(
                                    is_icon = True, 
                                    is_generated = True, 
                                    mimetype = '', 
                                    data = 'YQ==', 
                                    url = '', 
                                    width = 56, 
                                    height = 56, ), 
                                icon_url = '', 
                                collection = edu_sharing_client.models.collection.Collection(
                                    scope = '', 
                                    author_freetext = '', 
                                    order_ascending = True, 
                                    level0 = True, 
                                    title = '', 
                                    description = '', 
                                    type = '', 
                                    viewtype = '', 
                                    order_mode = '', 
                                    x = 56, 
                                    y = 56, 
                                    z = 56, 
                                    color = '', 
                                    from_user = True, 
                                    pinned = True, 
                                    child_collections_count = 56, 
                                    child_references_count = 56, ), 
                                owner = , 
                                is_public = True, )
                            ], 
                        relations = {
                            'key' : 
                            }, 
                        contributors = [
                            edu_sharing_client.models.contributor.Contributor(
                                property = '', 
                                firstname = '', 
                                lastname = '', 
                                email = '', 
                                vcard = '', 
                                org = '', )
                            ], 
                        ref = , 
                        parent = , 
                        type = '', 
                        aspects = [
                            ''
                            ], 
                        name = '', 
                        title = '', 
                        metadataset = '', 
                        repository_type = '', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        created_by = , 
                        modified_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        modified_by = , 
                        access = [
                            ''
                            ], 
                        download_url = '', 
                        properties = {
                            'key' : [
                                ''
                                ]
                            }, 
                        mimetype = '', 
                        mediatype = '', 
                        size = '', 
                        preview = edu_sharing_client.models.preview.Preview(
                            is_icon = True, 
                            is_generated = True, 
                            mimetype = '', 
                            data = 'YQ==', 
                            url = '', 
                            width = 56, 
                            height = 56, ), 
                        icon_url = '', 
                        collection = edu_sharing_client.models.collection.Collection(
                            scope = '', 
                            author_freetext = '', 
                            order_ascending = True, 
                            level0 = True, 
                            title = '', 
                            description = '', 
                            type = '', 
                            viewtype = '', 
                            order_mode = '', 
                            x = 56, 
                            y = 56, 
                            z = 56, 
                            color = '', 
                            from_user = True, 
                            pinned = True, 
                            child_collections_count = 56, 
                            child_references_count = 56, ), 
                        owner = , 
                        is_public = True, )
                    ]
            )
        else:
            return AdminStatistics(
        )
        """

    def testAdminStatistics(self):
        """Test AdminStatistics"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
