import json
import os.path
from dataclasses import dataclass
from typing import List, Set, Literal

from schulcloud.edusharing import EdusharingAPI, NotFoundException
from schulcloud.util import Environment


ENV_VARS = ['EDU_SHARING_BASE_URL', 'EDU_SHARING_USERNAME', 'EDU_SHARING_PASSWORD']


@dataclass
class User:
    name: str
    password: str
    type: Literal['function', 'system']
    groups: List[str]


class EdusharingSetup:
    def __init__(self):
        self.env = Environment(ENV_VARS, ask_for_missing=True)
        self.api = EdusharingAPI(
            self.env['EDU_SHARING_BASE_URL'],
            self.env['EDU_SHARING_USERNAME'],
            self.env['EDU_SHARING_PASSWORD'])

    def _add_metadata_sets(self):
        xml_name = 'homeApplication.properties.xml'
        key, value = 'metadatasetsV2', 'mds,mds_oeh'
        properties = self.api.get_application_properties(xml_name)
        if key not in properties or not properties[key] == value:
            properties[key] = value
            self.api.set_application_properties(xml_name, properties)

    def _add_users_and_groups(self, users: List[User], groups: Set[str]):
        # requirement: all groups within users must also be within groups
        # TODO: change only if users and groups do not exist
        for user in users:
            self.api.create_user(user.name, user.password, user.type)
            print(f'Created user {user.name}')

        for group in groups:
            self.api.create_group(group)

        for user in users:
            for group in user.groups:
                self.api.group_add_user(group, user.name)

    def _upload_color_picker(self):
        # the color picker h5p content contains the color picker library needed for other h5p items
        # which will be installed after upload
        colorpicker_path = 'schulcloud/update_colorpicker.h5p'
        colorpicker_name = os.path.basename(colorpicker_path)
        try:
            self.api.find_node_by_name('-userhome-', colorpicker_name)
        except NotFoundException:
            node = self.api.create_node('-userhome-', colorpicker_name)
            file = open(colorpicker_path, 'rb')
            self.api.upload_content(node.id, colorpicker_name, file)
            file.close()

    def run(self, users: List[User], groups: List[str]):
        groups = set(groups)
        for user in users:
            for group in user.groups:
                groups.add(group)

        self._add_metadata_sets()
        self._add_users_and_groups(users, groups)
        self._upload_color_picker()


def temporary_setup():
    file = open('schulcloud/es_users.json')
    obj = json.load(file)
    file.close()
    json_users = obj['users']
    groups = obj['groups']
    users = []
    for json_user in json_users:
        users.append(User(json_user[0], json_user[1], json_user[2], json_user[3]))
    print(users)
    print(groups)
    EdusharingSetup().run(users, groups)


def example():
    # users and groups should be taken from 1password
    users: List[User] = [
        User('BrandenburgUser', 'test123', 'function', ['Brandenburg-public, Brandenburg-private'])
    ]
    other_groups = ['public']
    EdusharingSetup().run(users, other_groups)


if __name__ == '__main__':
    temporary_setup()
