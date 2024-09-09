# coding: utf-8

"""
    edu-sharing Repository REST API

    The public restful API of the edu-sharing repository.

    The version of the OpenAPI document: 1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from edu_sharing_client.models.connector import Connector

class TestConnector(unittest.TestCase):
    """Connector unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Connector:
        """Test Connector
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Connector`
        """
        model = Connector()
        if include_optional:
            return Connector(
                id = '',
                icon = '',
                show_new = True,
                parameters = [
                    ''
                    ],
                filetypes = [
                    edu_sharing_client.models.connector_file_type.ConnectorFileType(
                        ccressourceversion = '', 
                        ccressourcetype = '', 
                        ccresourcesubtype = '', 
                        editor_type = '', 
                        mimetype = '', 
                        filetype = '', 
                        creatable = True, 
                        editable = True, )
                    ],
                only_desktop = True,
                has_view_mode = True
            )
        else:
            return Connector(
                show_new = True,
        )
        """

    def testConnector(self):
        """Test Connector"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
