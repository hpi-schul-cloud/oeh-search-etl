# coding: utf-8

"""
    edu-sharing Repository REST API

    The public restful API of the edu-sharing repository.

    The version of the OpenAPI document: 1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from edu_sharing_client.models.rating_details import RatingDetails

class TestRatingDetails(unittest.TestCase):
    """RatingDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RatingDetails:
        """Test RatingDetails
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RatingDetails`
        """
        model = RatingDetails()
        if include_optional:
            return RatingDetails(
                overall = edu_sharing_client.models.rating_data.RatingData(
                    sum = 1.337, 
                    count = 56, 
                    rating = 1.337, ),
                affiliation = {
                    'key' : edu_sharing_client.models.rating_data.RatingData(
                        sum = 1.337, 
                        count = 56, 
                        rating = 1.337, )
                    },
                user = 1.337
            )
        else:
            return RatingDetails(
        )
        """

    def testRatingDetails(self):
        """Test RatingDetails"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()