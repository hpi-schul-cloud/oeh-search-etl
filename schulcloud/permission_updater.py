import json
import os.path
import sys
import traceback

from schulcloud.edusharing import EdusharingAPI, Node, RequestFailedException
from schulcloud.util import Environment


ENV_VARS = ['EDU_SHARING_BASE_URL', 'EDU_SHARING_USERNAME_CRAWLER', 'EDU_SHARING_PASSWORD_CRAWLER',
            'EDU_SHARING_USERNAME_ADMIN', 'EDU_SHARING_PASSWORD_ADMIN']


class PermissionUpdater:
    def __init__(self):
        self.env = Environment(env_vars=ENV_VARS)
        self.api_admin = EdusharingAPI(
            self.env['EDU_SHARING_BASE_URL'],
            self.env['EDU_SHARING_USERNAME_ADMIN'],
            self.env['EDU_SHARING_PASSWORD_ADMIN'],
        )
        self.api_crawler = EdusharingAPI(
            self.env['EDU_SHARING_BASE_URL'],
            self.env['EDU_SHARING_USERNAME_CRAWLER'],
            self.env['EDU_SHARING_PASSWORD_CRAWLER'],
        )
        self.node_cache: dict[str, Node] = {}

    def get_node_by_path(self, path: str, api: EdusharingAPI) -> Node:
        """
        Get the node of Edu-Sharing by path.
        @param path: Path to node
        """
        path = os.path.normpath(path)
        try:
            return self.node_cache[path]
        except KeyError:
            pass
        parent_path = os.path.dirname(path)
        if parent_path:
            parent_id = self.get_node_by_path(parent_path, api).id
        else:
            parent_id = '-userhome-'
        node_name = os.path.basename(path)
        node = None
        for child in api.get_children(parent_id, type='folders'):
            self.node_cache[os.path.join(parent_path, child.name)] = child
            if child.name == node_name:
                node = child
        self.node_cache = {}
        if node is None:
            raise PathNotFoundException(path)
        else:
            return node

    def run(self):
        """
        Update the permissions accordingly to 'schulcloud/permissions.json'.
        """
        file = open('schulcloud/permissions.json')
        permissions = json.load(file)['permissions']
        file.close()
        for permission in permissions:
            if permission['path'] == "SYNC_OBJ/FWU" or permission['path'] == "SYNC_OBJ/H5P":
                api = self.api_crawler
            else:
                api = self.api_admin
            try:
                node = self.get_node_by_path(permission['path'], api)
                current_groups, inherited = api.get_permissions_groups(node.id)
                current_groups.sort()
                new_groups: list[str] = permission['permitted_groups']
                new_groups.sort()
                if not (current_groups == new_groups and inherited == permission['inherit']):
                    print(f'{permission["path"]} change {current_groups} -> {new_groups}')
                    api.set_permissions(node.id, permission['permitted_groups'], permission['inherit'])
                else:
                    print(f'Permissions already correct: {permission["path"]}')
            except PathNotFoundException:
                print(f'Warning: Could not find {permission["path"]}', file=sys.stderr)
            except KeyboardInterrupt:
                break
            except Exception:
                print(f'Error: Could not set permission for {permission["path"]}', file=sys.stderr)
                traceback.print_exc()


class PathNotFoundException(Exception):
    def __init__(self, path: str):
        super(PathNotFoundException, self).__init__(f'Path not found: {path}')
        self.path = path


if __name__ == '__main__':
    PermissionUpdater().run()
