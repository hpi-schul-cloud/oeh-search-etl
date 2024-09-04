# coding: utf-8

"""
    edu-sharing Repository REST API

    The public restful API of the edu-sharing repository.

    The version of the OpenAPI document: 1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from edu_sharing_client.api.iamv1_api import IAMV1Api


class TestIAMV1Api(unittest.TestCase):
    """IAMV1Api unit test stubs"""

    def setUp(self) -> None:
        self.api = IAMV1Api()

    def tearDown(self) -> None:
        pass

    def test_add_membership(self) -> None:
        """Test case for add_membership

        Add member to the group.
        """
        pass

    def test_add_node_list(self) -> None:
        """Test case for add_node_list

        Add a node to node a list of a user
        """
        pass

    def test_change_group_profile(self) -> None:
        """Test case for change_group_profile

        Set profile of the group.
        """
        pass

    def test_change_user_avatar(self) -> None:
        """Test case for change_user_avatar

        Set avatar of the user.
        """
        pass

    def test_change_user_password(self) -> None:
        """Test case for change_user_password

        Change/Set password of the user.
        """
        pass

    def test_change_user_profile(self) -> None:
        """Test case for change_user_profile

        Set profile of the user.
        """
        pass

    def test_confirm_signup(self) -> None:
        """Test case for confirm_signup

        put the pending user into the group
        """
        pass

    def test_create_group(self) -> None:
        """Test case for create_group

        Create a new group.
        """
        pass

    def test_create_user(self) -> None:
        """Test case for create_user

        Create a new user.
        """
        pass

    def test_delete_group(self) -> None:
        """Test case for delete_group

        Delete the group.
        """
        pass

    def test_delete_membership(self) -> None:
        """Test case for delete_membership

        Delete member from the group.
        """
        pass

    def test_delete_user(self) -> None:
        """Test case for delete_user

        Delete the user.
        """
        pass

    def test_get_group(self) -> None:
        """Test case for get_group

        Get the group.
        """
        pass

    def test_get_membership(self) -> None:
        """Test case for get_membership

        Get all members of the group.
        """
        pass

    def test_get_node_list(self) -> None:
        """Test case for get_node_list

        Get a specific node list for a user
        """
        pass

    def test_get_preferences(self) -> None:
        """Test case for get_preferences

        Get preferences stored for user
        """
        pass

    def test_get_profile_settings(self) -> None:
        """Test case for get_profile_settings

        Get profileSettings configuration
        """
        pass

    def test_get_recently_invited(self) -> None:
        """Test case for get_recently_invited

        Get recently invited authorities.
        """
        pass

    def test_get_subgroup_by_type(self) -> None:
        """Test case for get_subgroup_by_type

        Get a subgroup by the specified type
        """
        pass

    def test_get_user(self) -> None:
        """Test case for get_user

        Get the user.
        """
        pass

    def test_get_user_groups(self) -> None:
        """Test case for get_user_groups

        Get all groups the given user is member of.
        """
        pass

    def test_get_user_stats(self) -> None:
        """Test case for get_user_stats

        Get the user stats.
        """
        pass

    def test_reject_signup(self) -> None:
        """Test case for reject_signup

        reject the pending user
        """
        pass

    def test_remove_node_list(self) -> None:
        """Test case for remove_node_list

        Delete a node of a node list of a user
        """
        pass

    def test_remove_user_avatar(self) -> None:
        """Test case for remove_user_avatar

        Remove avatar of the user.
        """
        pass

    def test_search_authorities(self) -> None:
        """Test case for search_authorities

        Search authorities.
        """
        pass

    def test_search_groups(self) -> None:
        """Test case for search_groups

        Search groups.
        """
        pass

    def test_search_user(self) -> None:
        """Test case for search_user

        Search users.
        """
        pass

    def test_set_preferences(self) -> None:
        """Test case for set_preferences

        Set preferences for user
        """
        pass

    def test_set_profile_settings(self) -> None:
        """Test case for set_profile_settings

        Set profileSettings Configuration
        """
        pass

    def test_signup_group(self) -> None:
        """Test case for signup_group

        let the current user signup to the given group
        """
        pass

    def test_signup_group_details(self) -> None:
        """Test case for signup_group_details

         requires admin rights
        """
        pass

    def test_signup_group_list(self) -> None:
        """Test case for signup_group_list

        list pending users that want to join this group
        """
        pass

    def test_update_user_status(self) -> None:
        """Test case for update_user_status

        update the user status.
        """
        pass


if __name__ == '__main__':
    unittest.main()
