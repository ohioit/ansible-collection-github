#!/usr/bin/python

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import copy
import collections
from github import Github
from ansible.module_utils.common.text.converters import jsonify
from ansible.module_utils.basic import AnsibleModule
import json
ANSIBLE_METADATA = {
    'metadata_version': '1.0',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
---

module: collaborator_information

short_description: A module that manages collaborators on repositories

description:
  - "A module that fetches information about collaborators in repositories that a GitHub user provides that are inside of an organization."

options:
    access_token:
        description:
            - GitHub API token used to retrieve information about collaborators in repositories to which a user has access.
        required: true
        type: str

    api_url:
        description:
            - If using a token from a GitHub Enterprise account, the user must pass an enterprise URL.
              This URL should be in the format of "https://github.<ENTERPRISE DOMAIN>/api/v3".
        required: false
        default: null
        type: str

    organization:
        description:
            - The organization whose repository's collaborators will be managed.
        required: true
        type: str

    repository:
        description:
            - The repository whose collaborators will be managed.
        required: true
        type: str

    collaborator:
        description:
            - The collaborator that will be added, deleted, or changed.
        required: True
        type: str

    permission:
        description:
            - The permission the collaborator will have in the repository (push, pull, or admin).
        required: False
        default: pull
        type: str

    state:
        description:
            - The option to have the collaborator being present or absent in the repository.
        required: False
        type: str
        default: present


author:
    - Jacob Eicher (@jacobeicher)
    - Tyler Zwolenik (@TylerZwolenik)
    - Bradley Golski (@bgolski)
    - Nolan Khounborin (@Khounborinn)
'''

EXAMPLES = '''
# Pass in an github API token and organization name
- name: "Adding/modifying collaborator in enterprise GitHub account"
  ohioit.github.collaborator_information:
    access_token: "12345"
    organization: "SSEP"
    api_url: "https://github.<ENTERPRISE DOMAIN>/api/v3"
    repository: "testing-repo-private"
    collaborator: <VALID GITHUB USERNAME>
    permission: pull
    state: present


- name: "Delete collaborator in enterprise GitHub account"
  ohioit.github.collaborator_information:
    access_token: "12345"
    organization: "SSEP"
    api_url: "https://github.<ENTERPRISE DOMAIN>/api/v3"
    repository: "testing-repo-private"
    collaborator: <VALID GITHUB USERNAME>
    state: absent
'''

RETURN = '''
collaborators:
    description: Dictionary contains all names of repositories requested and their collaborators.
    type: dict
    returned: if GitHub API token connects

collaborators['<ORG NAME>/<REPO NAME>']:
    description: List contains dicts of each collaborator's information (that are in that repository).
    type: list
    returned: if at least one collaborator is contained within repository

collaborators['<ORG NAME>/<REPO NAME>'].<INDEX>:
    description: This index provides access to a dictionary containing information about a single collaborator.
    type: dict
    returned: if at least one collaborator is contained within repository

collaborators['<ORG NAME>/<REPO NAME>'].<INDEX>.id:
    description: Collaborator's id number.
    type: int
    returned: only if at least one collaborator is contained within repository

collaborators['<ORG NAME>/<REPO NAME>'].<INDEX>.login:
    description: Collaborator's login. This is their GitHub username.
    type: str
    returned: only if at least one collaborator is contained within repository

collaborators['<ORG NAME>/<REPO NAME>'].<INDEX>.permissions:
    description: Dictionary of statuses of permissions including admin, pull, push, and triage.
    type: dict
    returned: only if at least one collaborator is contained within repository

collaborators['<ORG NAME>/<REPO NAME>'].<INDEX>.permissions.admin:
    description: Will return true if admin rights are given to collaborator. Read, clone, push, and add collaborators permissions to repository.
    type: bool
    returned: only if at least one collaborator is contained within repository

collaborators['<ORG NAME>/<REPO NAME>'].<INDEX>.permissions.push:
    description: Will return true if push rights are given to collaborator. Read, clone, and push to repository.
    type: bool
    returned: only if at least one collaborator is contained within repository

collaborators['<ORG NAME>/<REPO NAME>'].<INDEX>.permissions.pull:
    description: Will return true if pull rights are given to collaborator. Read and clone repository.
    type: bool
    returned: only if at least one collaborator is contained within repository

collaborators['<ORG NAME>/<REPO NAME>'].<INDEX>.permissions.triage:
    description: Will return true if triage rights are given to collaborator.
                 Triage role can request reviews on pull requests (PRs), mark issues and PRs as duplicates, and add or remove milestones on issues and PRs.
                 NO WRITE ACCESS.
    type: bool
    returned: only if at least one collaborator is contained within repository

collaborators['<ORG NAME>/<REPO NAME>'].<INDEX>.site_admin:
    description: Will return true if collaborator is a site admin.
                 This permission gives the collaborator the ability to manage users, organizations, and repositories.
    type: bool
    returned: only if at least one collaborator is contained within repository

collaborators['<ORG NAME>/<REPO NAME>'].<INDEX>.type:
    description: This will return what type of collaborator the user is.
    type: str
    returned: only if at least one collaborator is contained within repository
'''


def present_collaborator(g, repo, collaborator, permission):
    r = g.get_repo(repo)
    r.add_to_collaborators(collaborator, permission=permission)


def absent_collaborator(g, repo, collaborator):
    r = g.get_repo(repo)
    r.remove_from_collaborators(collaborator)


def get_collaborators(g, repo):
    repos = list()
    collab_output = dict()
    collaborators = g.get_repo(
        repo).get_collaborators(affiliation="direct")
    for collaborator in collaborators:
        collab_output['login'] = collaborator.login
        collab_output['id'] = collaborator.id
        collab_output['type'] = collaborator.type
        collab_output['site_admin'] = collaborator.site_admin
        permissions = {
            'triage': collaborator.permissions.triage,
            'push': collaborator.permissions.push,
            'pull': collaborator.permissions.pull,
            'admin': collaborator.permissions.admin
        }
        collab_output['permissions'] = permissions

        repos.append(collab_output.copy())

    return repos


def present_collaborator_check_mode(collaborator, permission, current_collaborators):
    output_collaborators = copy.deepcopy(current_collaborators)
    collaborator_position = next((position for position, output_collaborators in enumerate(
        output_collaborators) if output_collaborators["login"] == collaborator), None)
    permissions = {}
    if permission == 'admin':
        permissions = {
            'triage': True,
            'push': True,
            'pull': True,
            'admin': True,
        }
    elif permission == 'pull':
        permissions = {
            'triage': False,
            'push': False,
            'pull': True,
            'admin': False,
        }
    else:
        permissions = {
            'triage': True,
            'push': True,
            'pull': True,
            'admin': False,
        }

    if collaborator_position is None:
        # adding
        collaborator_to_add = {
            'login': collaborator,
            'id': -1,
            'type': 'User',
            'site_admin': True if permission == 'admin' else False,
            'permissions': permissions.copy()
        }
        output_collaborators.append(collaborator_to_add)

    else:
        # changing
        if collaborator == output_collaborators[collaborator_position]['login']:
            output_collaborators[collaborator_position]['permissions'] = permissions.copy(
            )
            if permission == 'admin':
                output_collaborators[collaborator_position]['site_admin'] = True

    return output_collaborators


def absent_collaborator_check_mode(collaborator, current_collaborators):
    collaborator_position = next((position for position, current_collaborator in enumerate(
        current_collaborators) if current_collaborator["login"] == collaborator), None)
    output_collaborators = current_collaborators.copy()
    if collaborator_position is not None:
        output_collaborators.pop(collaborator_position)

    return output_collaborators


def run_module():
    module_args = dict(
        access_token=dict(type='str', required=True, no_log=True),
        organization=dict(type='str', required=True),
        api_url=dict(type='str', default=''),
        repository=dict(type='str', required=True),
        collaborator=dict(type='str', required=True),
        permission=dict(type='str', required=False, default="pull"),
        state=dict(type='str', default='present'),
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    result = dict(
        changed=False,
        fact=''
    )

    valid_permissions = ["push", "pull", "admin"]

    if(module.params['api_url'] == ''):
        g = Github(module.params['access_token'])
    else:
        g = Github(module.params['access_token'],
                   base_url=module.params['api_url'])

    if len(module.params['repository']):
        module.params['repository'] = module.params['organization'] + \
            "/" + module.params['repository']

    current_collaborators = get_collaborators(g, module.params['repository'])

    output = []

    if module.params['state'] not in ["absent", "present"]:
        module.exit_json(changed=False, failed=True, msg="Invalid state: " +
                         module.params['state'] +
                         ". State must be 'present' or 'absent'")
    else:
        if module.params['state'] == 'present':
            if module.params['permission'].lower() in valid_permissions:
                if module.check_mode is False:
                    present_collaborator(
                        g, module.params['repository'], module.params['collaborator'], module.params['permission'])
                else:
                    output = present_collaborator_check_mode(
                        module.params['collaborator'], module.params['permission'], current_collaborators.copy())
            else:
                module.exit_json(changed=False, failed=True, msg="Invalid permission: " +
                                 module.params['permission'] +
                                 ". Permissions must be 'push' 'pull' or 'admin'")

        elif module.params['state'] == 'absent':
            if module.check_mode is False:
                absent_collaborator(
                    g, module.params['repository'], module.params['collaborator'])
            else:
                output = absent_collaborator_check_mode(
                    module.params['collaborator'], current_collaborators)
    if module.check_mode is False:
        output = get_collaborators(g, module.params['repository'])

    module.exit_json(changed=json.dumps(current_collaborators)
                     != json.dumps(output), collaborators=output)


def main():
    run_module()


if __name__ == '__main__':
    main()
