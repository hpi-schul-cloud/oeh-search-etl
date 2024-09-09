# coding: utf-8

"""
    edu-sharing Repository REST API

    The public restful API of the edu-sharing repository.

    The version of the OpenAPI document: 1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from edu_sharing_client.api.adminv1_api import ADMINV1Api


class TestADMINV1Api(unittest.TestCase):
    """ADMINV1Api unit test stubs"""

    def setUp(self) -> None:
        self.api = ADMINV1Api()

    def tearDown(self) -> None:
        pass

    def test_add_application(self) -> None:
        """Test case for add_application

        register/add an application via xml file
        """
        pass

    def test_add_application1(self) -> None:
        """Test case for add_application1

        register/add an application
        """
        pass

    def test_add_toolpermission(self) -> None:
        """Test case for add_toolpermission

        add a new toolpermissions
        """
        pass

    def test_apply_template(self) -> None:
        """Test case for apply_template

        apply a folder template
        """
        pass

    def test_cancel_job(self) -> None:
        """Test case for cancel_job

        cancel a running job
        """
        pass

    def test_change_logging(self) -> None:
        """Test case for change_logging

        Change the loglevel for classes at runtime.
        """
        pass

    def test_clear_cache(self) -> None:
        """Test case for clear_cache

        clear cache
        """
        pass

    def test_create_preview(self) -> None:
        """Test case for create_preview

        create preview.
        """
        pass

    def test_delete_person(self) -> None:
        """Test case for delete_person

        delete persons
        """
        pass

    def test_export_by_lucene(self) -> None:
        """Test case for export_by_lucene

        Search for custom lucene query and choose specific properties to load
        """
        pass

    def test_export_lom(self) -> None:
        """Test case for export_lom

        Export Nodes with LOM Metadata Format
        """
        pass

    def test_get_all_jobs(self) -> None:
        """Test case for get_all_jobs

        get all available jobs
        """
        pass

    def test_get_all_toolpermissions(self) -> None:
        """Test case for get_all_toolpermissions

        get all toolpermissions for an authority
        """
        pass

    def test_get_application_xml(self) -> None:
        """Test case for get_application_xml

        list any xml properties (like from homeApplication.properties.xml)
        """
        pass

    def test_get_applications(self) -> None:
        """Test case for get_applications

        list applications
        """
        pass

    def test_get_cache_entries(self) -> None:
        """Test case for get_cache_entries

        Get entries of a cache
        """
        pass

    def test_get_cache_info(self) -> None:
        """Test case for get_cache_info

        Get information about a cache
        """
        pass

    def test_get_catalina_out(self) -> None:
        """Test case for get_catalina_out

        Get last info from catalina out
        """
        pass

    def test_get_cluster(self) -> None:
        """Test case for get_cluster

        Get information about the Cluster
        """
        pass

    def test_get_clusters(self) -> None:
        """Test case for get_clusters

        Get information about the Cluster
        """
        pass

    def test_get_config(self) -> None:
        """Test case for get_config

        get the repository config object
        """
        pass

    def test_get_config_file(self) -> None:
        """Test case for get_config_file

        get a base system config file (e.g. edu-sharing.conf)
        """
        pass

    def test_get_enabled_plugins(self) -> None:
        """Test case for get_enabled_plugins

        get enabled system plugins
        """
        pass

    def test_get_global_groups(self) -> None:
        """Test case for get_global_groups

        Get global groups
        """
        pass

    def test_get_jobs(self) -> None:
        """Test case for get_jobs

        get all running jobs
        """
        pass

    def test_get_lightbend_config(self) -> None:
        """Test case for get_lightbend_config

        """
        pass

    def test_get_logging_runtime(self) -> None:
        """Test case for get_logging_runtime

        get the logger config
        """
        pass

    def test_get_oai_classes(self) -> None:
        """Test case for get_oai_classes

        Get OAI class names
        """
        pass

    def test_get_property_to_mds(self) -> None:
        """Test case for get_property_to_mds

        Get a Mds Valuespace for all values of the given properties
        """
        pass

    def test_get_statistics(self) -> None:
        """Test case for get_statistics

        get statistics
        """
        pass

    def test_get_version(self) -> None:
        """Test case for get_version

        get detailed version information
        """
        pass

    def test_import_collections(self) -> None:
        """Test case for import_collections

        import collections via a xml file
        """
        pass

    def test_import_excel(self) -> None:
        """Test case for import_excel

        Import excel data
        """
        pass

    def test_import_oai(self) -> None:
        """Test case for import_oai

        Import oai data
        """
        pass

    def test_import_oai_xml(self) -> None:
        """Test case for import_oai_xml

        Import single xml via oai (for testing)
        """
        pass

    def test_refresh_app_info(self) -> None:
        """Test case for refresh_app_info

        refresh app info
        """
        pass

    def test_refresh_cache(self) -> None:
        """Test case for refresh_cache

        Refresh cache
        """
        pass

    def test_refresh_edu_group_cache(self) -> None:
        """Test case for refresh_edu_group_cache

        Refresh the Edu Group Cache
        """
        pass

    def test_remove_application(self) -> None:
        """Test case for remove_application

        remove an application
        """
        pass

    def test_remove_cache_entry(self) -> None:
        """Test case for remove_cache_entry

        remove cache entry
        """
        pass

    def test_remove_oai_imports(self) -> None:
        """Test case for remove_oai_imports

        Remove deleted imports
        """
        pass

    def test_search_by_elastic_dsl(self) -> None:
        """Test case for search_by_elastic_dsl

        Search for custom elastic DSL query
        """
        pass

    def test_search_by_lucene(self) -> None:
        """Test case for search_by_lucene

        Search for custom lucene query
        """
        pass

    def test_server_update_list(self) -> None:
        """Test case for server_update_list

        list available update tasks
        """
        pass

    def test_server_update_list1(self) -> None:
        """Test case for server_update_list1

        Run an update tasks
        """
        pass

    def test_set_config(self) -> None:
        """Test case for set_config

        set/update the repository config object
        """
        pass

    def test_set_toolpermissions(self) -> None:
        """Test case for set_toolpermissions

        set toolpermissions for an authority
        """
        pass

    def test_start_job(self) -> None:
        """Test case for start_job

        Start a Job.
        """
        pass

    def test_start_job_sync(self) -> None:
        """Test case for start_job_sync

        Start a Job.
        """
        pass

    def test_switch_authority(self) -> None:
        """Test case for switch_authority

        switch the session to a known authority name
        """
        pass

    def test_test_mail(self) -> None:
        """Test case for test_mail

        Test a mail template
        """
        pass

    def test_update_application_xml(self) -> None:
        """Test case for update_application_xml

        edit any properties xml (like homeApplication.properties.xml)
        """
        pass

    def test_update_config_file(self) -> None:
        """Test case for update_config_file

        update a base system config file (e.g. edu-sharing.conf)
        """
        pass

    def test_upload_temp(self) -> None:
        """Test case for upload_temp

        Upload a file
        """
        pass


if __name__ == '__main__':
    unittest.main()
