# coding: utf-8

"""
    edu-sharing Repository REST API

    The public restful API of the edu-sharing repository.

    The version of the OpenAPI document: 1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from edu_sharing_client.models.menu_entry import MenuEntry

class TestMenuEntry(unittest.TestCase):
    """MenuEntry unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MenuEntry:
        """Test MenuEntry
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MenuEntry`
        """
        model = MenuEntry()
        if include_optional:
            return MenuEntry(
                position = 56,
                icon = '',
                name = '',
                url = '',
                is_disabled = True,
                open_in_new = True,
                is_separate = True,
                is_separate_bottom = True,
                only_desktop = True,
                only_web = True,
                path = '',
                scope = ''
            )
        else:
            return MenuEntry(
        )
        """

    def testMenuEntry(self):
        """Test MenuEntry"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
