import unittest
import json
from unittest.mock import MagicMock, patch
from ansible.module_utils import basic
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.common.text.converters import to_bytes

def set_module_args(args):
    """prepare arguments so that they will be picked up during module creation"""
    args = json.dumps({'ANSIBLE_MODULE_ARGS': args})
    basic._ANSIBLE_ARGS = to_bytes(args)

class AnsibleExitJson(Exception):
    """Exception class to be raised by module.exit_json and caught by the test case"""
    pass


class AnsibleFailJson(Exception):
    """Exception class to be raised by module.fail_json and caught by the test case"""
    pass


def exit_json(*args, **kwargs):
    """function to patch over exit_json; package return data into an exception"""
    if 'changed' not in kwargs:
        kwargs['changed'] = False
    raise AnsibleExitJson(kwargs)


def fail_json(*args, **kwargs):
    """function to patch over fail_json; package return data into an exception"""
    kwargs['failed'] = True
    raise AnsibleFailJson(kwargs)


def get_github_api_call(self, arg, required=False):
    if arg.endswith('token'):
        return 'token'
    else:
        if required:
            fail_json(msg='%r not found !' % arg)
        else:
            return 'Invalid token'

def get_enterprise_url(self, *args, required=False):
    if len(args) == 1:
        return 'no enterprise url'

    if args[1] == 'github.enterprise.com':
        return 'github.enterprise.com'
    else:
        if required:
            fail_json(msg='%r not found !' % arg)
        else:
            return 'Invalid enterprise url'

class Organization:
    organization_dict = {}
    name_list = []

    def get_organization(self, org_name):
        if org_name == 'Good Organization Name':
            self.organization_dict = {"Org_name": 'organization1',
                    "repos": [
                        {'name': 'repo1', 'url': "github.com/repo1"}, 
                        {'name': 'repo2', 'url': "github.com/repo2"}, 
                        {'name': 'repo3', 'url': "github.com/repo3"}
                    ]}
            return self.organization_dict
        else:
            return 'Bad Org Name'

    def get_repos(self):
        if len(self.organization_dict)>0: 
            repo_list = self.organization_dict['repos']
            for repo in repo_list:
                self.name_list.append({'name': repo['name'], 'url': repo['url']})
            return self.name_list
        else:
            return []
        
    

class TestMyModule(unittest.TestCase):

    def setUp(self):
        self.mock_module_helper = patch.multiple(basic.AnsibleModule,
                                                 exit_json=exit_json,
                                                 fail_json=fail_json)
        self.mock_module_helper.start()
        self.addCleanup(self.mock_module_helper.stop)

    def test_module_fail_when_required_args_missing(self):
        set_module_args({})
        self.assertRaises(AnsibleFailJson)

    def test_module_pass_when_required_args_fulfilled_correctly(self):
        set_module_args({'param1': 'token'})
        self.assertRaises(AnsibleExitJson)

    def test_pass_api_call(self):
        assert get_github_api_call(self, arg = 'token', required = True) == 'token'

    def test_pass_enterprise_url_entered_correctly(self):
        assert get_enterprise_url(self, 'token', 'github.enterprise.com', required = False) == 'github.enterprise.com'

    def test_pass_enterprise_url_entered_as_empty(self):
        assert get_enterprise_url(self, 'token', required = False) == 'no enterprise url'

    def test_fail_api_call(self):
        assert get_github_api_call(self, arg = 'token bad', required = False) != 'token'

    def test_fail_enterprise_url_entered_correctly(self):
        assert get_enterprise_url(self, 'token', 'github.enterprise.net', required = False) != 'github.enterprise.com'

    def test_pass_get_organization_returns_correct_output(self):
        test = Organization()
        test.get_organization('Good Organization Name')
        assert test.organization_dict == {'Org_name': 'organization1', 'repos': [{'name': 'repo1', 'url': 'github.com/repo1'}, {'name': 'repo2', 'url': 'github.com/repo2'}, {'name': 'repo3', 'url': 'github.com/repo3'}]}

    def test_fail_get_organization_with_bad_organization_name(self):
        test = Organization()
        test.get_organization('Bad Organization Name')
        assert test.organization_dict != {'Org_name': 'organization1', 'repos': [{'name': 'repo1', 'url': 'github.com/repo1'}, {'name': 'repo2', 'url': 'github.com/repo2'}, {'name': 'repo3', 'url': 'github.com/repo3'}]}

    def test_pass_get_repos_returns_correct_output(self):
        test = Organization()
        test.get_organization('Good Organization Name')
        test.get_repos()
        assert test.name_list == [{'name': 'repo1', 'url': 'github.com/repo1'}, {'name': 'repo2', 'url': 'github.com/repo2'}, {'name': 'repo3', 'url': 'github.com/repo3'}]

    def test_fail_get_repos_returns_incorrect_output(self):
        test = Organization()
        test.get_organization('Bad Organization Name')
        test.get_repos()
        assert test.name_list != [{'name': 'repo1', 'url': 'github.com/repo1'}, {'name': 'repo2', 'url': 'github.com/repo2'}, {'name': 'repo3', 'url': 'github.com/repo3'}]
