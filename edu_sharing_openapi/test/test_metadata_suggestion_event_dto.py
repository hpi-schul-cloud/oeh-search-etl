# coding: utf-8

"""
    edu-sharing Repository REST API

    The public restful API of the edu-sharing repository.

    The version of the OpenAPI document: 1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from edu_sharing_client.models.metadata_suggestion_event_dto import MetadataSuggestionEventDTO

class TestMetadataSuggestionEventDTO(unittest.TestCase):
    """MetadataSuggestionEventDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MetadataSuggestionEventDTO:
        """Test MetadataSuggestionEventDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MetadataSuggestionEventDTO`
        """
        model = MetadataSuggestionEventDTO()
        if include_optional:
            return MetadataSuggestionEventDTO(
                node = edu_sharing_client.models.node_data_dto.NodeDataDTO(
                    type = '', 
                    aspects = [
                        ''
                        ], 
                    properties = {
                        'key' : None
                        }, ),
                caption_id = '',
                caption = '',
                parent_id = '',
                parent_caption = '',
                widget = edu_sharing_client.models.widget_data_dto.WidgetDataDTO(
                    id = '', 
                    caption = '', )
            )
        else:
            return MetadataSuggestionEventDTO(
        )
        """

    def testMetadataSuggestionEventDTO(self):
        """Test MetadataSuggestionEventDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
