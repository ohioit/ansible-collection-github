from math import perm
from ansible.module_utils import basic
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils._text import to_bytes
import unittest
import json


class Collaborator:
    def __init__(self):
        self.login = None
        self.id = None
        self.type = None
        self.site_admin = None
        self.permissions = None

    def __init__(self, repository):
        if repository == 'Hello-World':
            self.login = 'Test_User'
            self.id = -1
            self.type = 'User'
            self.site_admin = False
            self.permissions = {
                'triage': True,
                'push': True,
                'pull': True,
                'admin': False
            }
    
    def add_to_collaborators(collaborator, permission):
        permissions = {
            'triage': False,
            'push': False,
            'pull': False,
            'admin': False
        }
        if permission == 'pull':
            permissions = {
                'triage': False,
                'push': False,
                'pull': False,
                'admin': False
            }
        elif permission == 'push':
            permissions = {
                'triage': False,
                'push': False,
                'pull': False,
                'admin': False
            }
        elif permission == 'admin':
            permissions = {
                'triage': False,
                'push': False,
                'pull': False,
                'admin': False
            }
            collaborator.site_admin = True
        collaborator.permissions = permissions
        


class Repository:
    def __init__(self):
        self.archived = None
        self.clone_url = None
        self.default_branch = None
        self.description =  None
        self.full_name = None
        self.hooks_url = None
        self.language = None
        self.name = None
        self.owner = None
        self.private = None
        self.url = None
        self.raw_data = None
        self.collaborators = None
    
    def __init__(self, name):
        if name == 'Hello-World':
            self.archived = False
            self.clone_url = 'https://api.github.com/github/' + name + '.git'
            self.default_branch = "main"
            self.description =  ""
            self.full_name = 'github/' + name
            self.hooks_url = 'https://api.github.com/github/repos/' + name + '/hooks'
            self.language = None
            self.name = name
            self.owner = {
                'login': 'github'
            }
            self.private = True
            self.url = "https://api.github.com/orgs/github/repos/" + name
            self.raw_data = {
                'visibility': 'public',
                'is_template': False
            }
            self.collaborators = [
                Collaborator(name='Hello-World')
            ]
    

class Organization:
    def __init__(self):
        self.login = "login"
        self.id = 1
        self.node_id = -1
        self.url = "https://api.github.com/orgs/github"
        self.repos_url = "https://api.github.com/orgs/github/repos"
        self.description = "A great organization"
        self.name = "github"
        self.type = "Organization"

    def __init__(self, name):
        self.name = name
        self.login = "login"
        self.id = 1
        self.node_id = -1
        self.url = "https://api.github.com/orgs/" + name
        self.repos_url = "https://api.github.com/orgs/" + name + "/repos"
        self.description = "A great organization"
        self.type = "Organization"

    def get_repos(self):
        repositories = []
        if self.name == 'github':
            repositories = [
                Repository(name='Hello-World'),
                Repository(name='Goodbye-Chat')
            ]

        return repositories

    def get_repo(self):
        repository = Repository()
        if self.name == 'github':
            repository = Repository(name='Hello-World')
    
        return repository



class Github:
    def __init__(self, access_token, base_url=''):
        self.access_token = access_token
        self.base_url = base_url

    def get_organization(self, organization):
        if self.access_token == 'token':
            organization = Organization(name=organization)
        return organization


def set_module_args(args):
    if '_ansible_remote_tmp' not in args:
        args['_ansible_remote_tmp'] = '/tmp'
    if '_ansible_keep_remote_files' not in args:
        args['_ansible_keep_remote_files'] = False

    args = json.dumps({'ANSIBLE_MODULE_ARGS': args})
    basic._ANSIBLE_ARGS = to_bytes(args)


class AnsibleExitJson(Exception):
    pass


class AnsibleFailJson(Exception):
    pass


def exit_json(*args, **kwargs):
    if 'changed' not in kwargs:
        kwargs['changed'] = False
    raise AnsibleExitJson(kwargs)


def fail_json(*args, **kwargs):
    kwargs['failed'] = True
    raise AnsibleFailJson(kwargs)


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
    collaborator_position = next((position for position, current_collaborator in enumerate(
        current_collaborators) if current_collaborator["login"] == collaborator), None)
    permissions = {}
    if permission == 'admin':
        permissions = {
            'admin': True,
            'pull': True,
            'push': True,
            'triage': True
        }
    elif permission == 'pull':
        permissions = {
            'admin': False,
            'pull': True,
            'push': False,
            'triage': False
        }
    else:
        permissions = {
            'admin': False,
            'pull': True,
            'push': True,
            'triage': True
        }

    output_collaborators = current_collaborators.copy()
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
            output_collaborators[collaborator_position]['permissions'] = permissions.copy()
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

    if module.params['state'] == 'present':
        if len(module.params['collaborator']) and len(module.params['repository']) and module.params['permission'].lower() in valid_permissions:
            if module.check_mode is False:
                present_collaborator(
                    g, module.params['repository'], module.params['collaborator'], module.params['permission'])
            else:
                output = present_collaborator_check_mode(
                    module.params['collaborator'], module.params['permission'], current_collaborators)
        elif module.params['permission'].lower() not in valid_permissions:
            module.exit_json(changed=False, failed=True, msg="Invalid permission: " +
                             module.params['permission'] +
                             ". Permissions must be 'push' 'pull' or 'admin'")

    elif module.params['state'] == 'absent' and len(module.params['repository']):
        if module.check_mode is False:
            absent_collaborator(
                g, module.params['repository'], module.params['collaborator'])
        else:
            output = absent_collaborator_check_mode(
                module.params['collaborator'], current_collaborators)
    elif module.params['state'] not in ["absent", "present"]:
        module.exit_json(changed=False, failed=True, msg="Invalid state: " +
                         module.params['state'] +
                         ". State must be 'present' or 'absent'")
    if module.check_mode is False:
        output = get_collaborators(g, module.params['repository'])

    module.exit_json(changed=json.dumps(current_collaborators)
                     != json.dumps(output), collaborators=output)


class TestCollaboratorModule(unittest.TestCase):
    def test_module_passing_valid_arguments(self):
        set_module_args({'access_token': 'token',
                         'organization': 'org',
                         'repository': 'one_collaborator',
                         'collaborator': 'username',
                         'permission': 'push',
                         'state': 'present'})
        self.assertRaises(AnsibleExitJson)

    # def test_module_returning_collaborator_already_there(self):
    #     set_module_args({'access_token': 'token',
    #                      'organization': 'org',
    #                      'repository': 'one_collaborator',
    #                      'collaborator': 'username',
    #                      'permission': 'push',
    #                      'state': 'present'})

    #     result, changed = run_module()

    #     test = [{
    #         'login': 'username',
    #         'id': 0,
    #         'type': 'user',
    #         'site_admin': False,
    #         'permissions': {
    #             'triage': True,
    #             'push': True,
    #             'pull': False,
    #             'admin': False
    #         }
    #     }]

    #     assert result == test
    #     assert changed is False

    # def test_module_adding_collaborator_to_empty_list(self):
    #     set_module_args({'access_token': 'token',
    #                      'organization': 'org',
    #                      'repository': 'no_collaborator',
    #                      'collaborator': 'new_username',
    #                      'permission': 'push',
    #                      'state': 'present'})

    #     result, changed = run_module()

    #     test = [{
    #         'login': 'new_username',
    #         'id': 0,
    #         'type': 'user',
    #         'site_admin': False,
    #         'permissions': {
    #             'triage': True,
    #             'push': True,
    #             'pull': False,
    #             'admin': False
    #         }
    #     }]

    #     assert result == test
    #     assert changed is True

    # def test_module_adding_collaborator_to_populated_list(self):
    #     set_module_args({'access_token': 'token',
    #                      'organization': 'org',
    #                      'repository': 'one_collaborator',
    #                      'collaborator': 'new_username',
    #                      'permission': 'push',
    #                      'state': 'present'})

    #     result, changed = run_module()

    #     test = [{
    #         'login': 'username',
    #         'id': 0,
    #         'type': 'user',
    #         'site_admin': False,
    #         'permissions': {
    #             'triage': True,
    #             'push': True,
    #             'pull': False,
    #             'admin': False
    #         }
    #     },
    #         {
    #             'login': 'new_username',
    #             'id': 0,
    #             'type': 'user',
    #             'site_admin': False,
    #             'permissions': {
    #                 'triage': True,
    #                 'push': True,
    #                 'pull': False,
    #                 'admin': False
    #             }
    #     }]

    #     assert result == test
    #     assert changed is True

    # def test_module_changing_collaborator_permissions(self):
    #     set_module_args({'access_token': 'token',
    #                      'organization': 'org',
    #                      'repository': 'one_collaborator',
    #                      'collaborator': 'username',
    #                      'permission': 'admin',
    #                      'state': 'present'})

    #     result, changed = run_module()

    #     test = [{
    #         'login': 'username',
    #         'id': 0,
    #         'type': 'user',
    #         'site_admin': True,
    #         'permissions': {
    #             'triage': True,
    #             'push': True,
    #             'pull': True,
    #             'admin': True
    #         }
    #     }]

    #     assert result == test
    #     assert changed is True

    # def test_module_remove_collaborator_from_empty_list(self):
    #     set_module_args({'access_token': 'token',
    #                      'organization': 'org',
    #                      'repository': 'no_collaborator',
    #                      'collaborator': 'username',
    #                      'permission': 'admin',
    #                      'state': 'absent'})

    #     result, changed = run_module()

    #     test = []

    #     assert result == test
    #     assert changed is False

    # def test_module_remove_collaborator_from_populated_list(self):
    #     set_module_args({'access_token': 'token',
    #                      'organization': 'org',
    #                      'repository': 'one_collaborator',
    #                      'collaborator': 'username',
    #                      'permission': 'admin',
    #                      'state': 'absent'})

    #     result, changed = run_module()

    #     test = []

    #     assert result == test
    #     assert changed is True

    # def test_module_incorrect_permission(self):
    #     set_module_args({'access_token': 'token',
    #                      'organization': 'org',
    #                      'repository': 'one_collaborator',
    #                      'collaborator': 'username',
    #                      'permission': 'Not a real permission',
    #                      'state': 'present'})

    #     result, changed = run_module()

    #     test = 'Permissions must be \'push\' \'pull\' or \'admin\''

    #     assert result == test
    #     assert changed is False

    # def test_module_check_mode_adding_collaborator(self):
    #     set_module_args({'access_token': 'token',
    #                      'organization': 'org',
    #                      'repository': 'one_collaborator',
    #                      'collaborator': 'username',
    #                      'permission': 'push',
    #                      'state': 'present',
    #                      'check_mode': True})

    #     result, changed = run_module()

    #     test = [{
    #         'login': 'username',
    #         'id': 0,
    #         'type': 'user',
    #         'site_admin': False,
    #         'permissions': {
    #             'triage': True,
    #             'push': True,
    #             'pull': False,
    #             'admin': False
    #         }
    #     }]

    #     assert result == test
    #     assert changed is False

    # def test_module_check_mode_adding_collaborator_to_empty_list(self):
    #     set_module_args({'access_token': 'token',
    #                      'organization': 'org',
    #                      'repository': 'no_collaborator',
    #                      'collaborator': 'new_username',
    #                      'permission': 'push',
    #                      'state': 'present',
    #                      'check_mode': True})

    #     result, changed = run_module()

    #     test = [{
    #         'login': 'new_username',
    #         'id': 0,
    #         'type': 'user',
    #         'site_admin': False,
    #         'permissions': {
    #             'triage': True,
    #             'push': True,
    #             'pull': False,
    #             'admin': False
    #         }
    #     }]

    #     assert result == test
    #     assert changed is True

    # def test_module_check_mode_adding_collaborator_to_populated_list(self):
    #     set_module_args({'access_token': 'token',
    #                      'organization': 'org',
    #                      'repository': 'one_collaborator',
    #                      'collaborator': 'new_username',
    #                      'permission': 'push',
    #                      'state': 'present',
    #                      'check_mode': True})

    #     result, changed = run_module()

    #     test = [{
    #         'login': 'username',
    #         'id': 0,
    #         'type': 'user',
    #         'site_admin': False,
    #         'permissions': {
    #             'triage': True,
    #             'push': True,
    #             'pull': False,
    #             'admin': False
    #         }
    #     },
    #         {
    #             'login': 'new_username',
    #             'id': 0,
    #             'type': 'user',
    #             'site_admin': False,
    #             'permissions': {
    #                 'triage': True,
    #                 'push': True,
    #                 'pull': False,
    #                 'admin': False
    #             }
    #     }]

    #     assert result == test
    #     assert changed is True

    # def test_module_check_mode_changing_collaborator_permissions(self):
    #     set_module_args({'access_token': 'token',
    #                      'organization': 'org',
    #                      'repository': 'one_collaborator',
    #                      'collaborator': 'username',
    #                      'permission': 'admin',
    #                      'state': 'present',
    #                      'check_mode': True})

    #     result, changed = run_module()

    #     test = [{
    #         'login': 'username',
    #         'id': 0,
    #         'type': 'user',
    #         'site_admin': True,
    #         'permissions': {
    #             'triage': True,
    #             'push': True,
    #             'pull': True,
    #             'admin': True
    #         }
    #     }]

    #     assert result == test
    #     assert changed is True

    # def test_module_check_mode_remove_collaborator_from_empty_list(self):
    #     set_module_args({'access_token': 'token',
    #                      'organization': 'org',
    #                      'repository': 'no_collaborator',
    #                      'collaborator': 'username',
    #                      'permission': 'admin',
    #                      'state': 'absent',
    #                      'check_mode': True})

    #     result, changed = run_module()

    #     test = []

    #     assert result == test
    #     assert changed is False

    # def test_module_check_mode_remove_collaborator_from_populated_list(self):
    #     set_module_args({'access_token': 'token',
    #                      'organization': 'org',
    #                      'repository': 'one_collaborator',
    #                      'collaborator': 'username',
    #                      'permission': 'admin',
    #                      'state': 'absent',
    #                      'check_mode': True})

    #     result, changed = run_module()

    #     test = []

    #     assert result == test
    #     assert changed is True
