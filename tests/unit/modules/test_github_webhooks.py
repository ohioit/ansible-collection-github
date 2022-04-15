from __future__ import (absolute_import, division, print_function)
from venv import create
__metaclass__ = type

from ansible.module_utils import basic
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.common.text.converters import jsonify
from ansible.module_utils._text import to_bytes
import json
import collections
import unittest


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


def get_webhooks(g, repo):
    hooks = []

    if repo == 'org_name/one_webhook':
        hooks = [{
            "active": True,
            "config": {
                "content_type": "json",
                "insecure_ssl": "0",
                "url": "http://test.com"
            },
            "events": [
                "member",
                "create"
            ],
            "id": 0,
            "name": "web",
            "ping_url": "https://api.github.com/repos/" + repo + "/hooks/0/pings",
            "test_url": "https://api.github.com/repos/" + repo + "/hooks/0/test",
            "url": "https://api.github.com/repos/" + repo + "/hooks/0"
        }]
    elif repo == 'org_name/two_webhook':
        hooks = [{
            "active": True,
            "config": {
                "content_type": "json",
                "insecure_ssl": "0",
                "url": "http://test.com"
            },
            "events": [
                "gollum",
                "pull_request"
            ],
            "id": 1,
            "name": "web",
            "ping_url": "https://api.github.com/repos/" + repo + "/hooks/1/pings",
            "test_url": "https://api.github.com/repos/" + repo + "/hooks/1/test",
            "url": "https://api.github.com/repos/" + repo + "/hooks/1"
        },
            {
                "active": True,
                "config": {
                    "content_type": "json",
                    "insecure_ssl": "0",
                    "url": "http://test.com"
                },
                "events": [
                    "gollum",
                    "pull_request"
                ],
                "id": 2,
                "name": "web",
                "ping_url": "https://api.github.com/repos/" + repo + "/hooks/2/pings",
                "test_url": "https://api.github.com/repos/" + repo + "/hooks/2/test",
                "url": "https://api.github.com/repos/" + repo + "/hooks/2"
        }]

    return hooks


def create_webhook(g, repo, events, url, content_type):

    hooks = g.copy()
    config = {"url": url, "content_type": content_type if content_type else "json"}

    for current_hook in hooks:
        if (config["url"] == current_hook['config']["url"]):
            current_hook['events'] = events
            return hooks

    new_hook = {
        "active": True,
        "config": {
            "content_type": content_type,
            "insecure_ssl": "0",
            "url": url
        },
        "events": events,
        "id": 999,
        "name": "web",
        "ping_url": "https://api.github.com/repos/" + repo + "/hooks/999/pings",
        "test_url": "https://api.github.com/repos/" + repo + "/hooks/999/test",
        "url": "https://api.github.com/repos/" + repo + "/hooks/999"
    }
    hooks.append(new_hook)
    return hooks


def delete_webhook(g, repo, url):
    hooks = g.copy()
    for current_hook in hooks:
        if url == current_hook['config']["url"]:
            hooks.remove(current_hook)

    return hooks


def run_module():
    module_args = dict(
        state=dict(type="str", default="present"),
        access_token=dict(type="str", required=True, no_log=True),
        organization=dict(type="str", required=True),
        api_url=dict(type="str", default=""),
        repository=dict(type="str", required=True),
        url=dict(type="str", default=""),
        events=dict(type="list", elements="str"),
        content_type=dict(type="str", default="json"),
        check_mode=dict(type='bool', default=False)
    )

    valid_content_types = ["json", "form"]
    valid_actions = ["absent", "present"]
    valid_events = [
        "branch_protection_rule",
        "check_run",
        "check_suite",
        "code_scanning_alert",
        "commit_comment",
        "content_reference",
        "create",
        "delete",
        "deploy_key",
        "deployment",
        "deployment_status",
        "discussion",
        "discussion_comment",
        "fork",
        "github_app_authorization",
        "gollum",
        "installation",
        "installation_repositories",
        "issue_comment",
        "issues",
        "label",
        "marketplace_purchase",
        "member",
        "membership",
        "meta",
        "milestone",
        "organization",
        "org_block",
        "package",
        "page_build",
        "ping",
        "project_card",
        "project_column",
        "project",
        "public",
        "pull_request",
        "pull_request_review",
        "pull_request_review_comment",
        "push",
        "release",
        "repository_dispatch",
        "repository",
        "repository_import",
        "repository_vulnerability_alert",
        "secret_scanning_alert",
        "security_advisory",
        "sponsorship",
        "star",
        "status",
        "team",
        "team_add",
        "watch",
        "workflow_dispatch",
        "workflow_job",
    ]

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    changed = False

    if module.params["state"] not in valid_actions:
        error_message = "Invalid action: " + module.params["state"]
        return error_message, changed

    if module.params["api_url"] == "":
        g = 'Token'
    else:
        g = 'Github Token with api_url'

    if len(module.params["repository"]):
        module.params["repository"] = (
            module.params["organization"] + "/" + module.params["repository"]
        )

    initial = get_webhooks(g, module.params["repository"])
    output = initial.copy()

    if module.params["url"]:
        if module.params["events"]:
            for event in module.params["events"]:
                if event not in valid_events:
                    error_message = "Invalid event name: " + event
                    return error_message, changed
        if module.params["state"].lower() == "absent":
            if module.params['check_mode']:
                for hooks in output:
                    if hooks['config']['url'] == module.params['url']:
                        output.remove(hooks)
            else:
                output = delete_webhook(initial, module.params["repository"], module.params["url"])
        elif module.params["state"].lower() == "present":
            if module.params["content_type"] not in valid_content_types:
                error_message = "Invalid content type: " + \
                    module.params["content_type"]
                return error_message, changed
            if module.params['check_mode']:
                found = False
                for hooks in output:
                    if hooks['config']['url'] == module.params['url']:
                        hooks['events'] = module.params['events']
                        found = True
                if not found:
                    if module.params["api_url"] != "":
                        urlBase = module.params["api_url"]
                    else:
                        urlBase = "https://github.com/api/v3%s" % (
                            module.params['organization'])
                    output.append({
                        "active": True,
                        "config": {
                            "content_type": module.params['content_type'],
                            "insecure_ssl": "0",
                            "url": module.params['url']
                        },
                        "events": module.params['events'],
                        "id": 999,
                        "name": "web",
                        "ping_url": "https://api.github.com/repos/" + module.params['repository'] + "/hooks/999/pings",
                        "test_url": "https://api.github.com/repos/" + module.params['repository'] + "/hooks/999/test",
                        "url": "https://api.github.com/repos/" + module.params['repository'] + "/hooks/999"
                    })
            else:
                output = create_webhook(
                    initial,
                    module.params["repository"],
                    module.params["events"],
                    module.params["url"],
                    module.params["content_type"],
                )

    initial = get_webhooks(g, module.params['repository'])

    if initial != output:
        changed = True

    return output, changed


class TestWebhooksModule(unittest.TestCase):
    def test_receive_repository_and_get_webhooks(self):
        set_module_args({
            'access_token': 'token',
            'organization': 'org_name',
            'repository': 'no_webhooks',
            'url': 'https://test.com/test_endpoint',
            'events': ['create', 'delete']
        })
        result, changed = run_module()
        self.assertRaises(AnsibleExitJson)

    def test_adding_webhook_to_populated_list(self):
        set_module_args({
            'access_token': 'token',
            'organization': 'org_name',
            'repository': 'one_webhook',
            'url': 'https://test.com/test_endpoint',
            'events': ['create', 'delete']
        })
        result, changed = run_module()
        test = [{
            "active": True,
            "config": {
                "content_type": "json",
                "insecure_ssl": "0",
                "url": "http://test.com"
            },
            "events": [
                "member",
                "create"
            ],
            "id": 0,
            "name": "web",
            "ping_url": "https://api.github.com/repos/org_name/one_webhook/hooks/0/pings",
            "test_url": "https://api.github.com/repos/org_name/one_webhook/hooks/0/test",
            "url": "https://api.github.com/repos/org_name/one_webhook/hooks/0"
        },
            {
                "active": True,
                "config": {
                    "content_type": "json",
                    "insecure_ssl": "0",
                    "url": "https://test.com/test_endpoint"
                },
                "events": [
                    "create",
                    "delete"
                ],
                "id": 999,
                "name": "web",
                "ping_url": "https://api.github.com/repos/org_name/one_webhook/hooks/999/pings",
                "test_url": "https://api.github.com/repos/org_name/one_webhook/hooks/999/test",
                "url": "https://api.github.com/repos/org_name/one_webhook/hooks/999"
        }]
        assert result == test
        assert changed is True

    def test_adding_webhook_to_empty_list(self):
        set_module_args({
            'access_token': 'token',
            'organization': 'org_name',
            'repository': 'no_webhook',
            'url': 'https://test.com/test_endpoint',
            'events': ['create', 'delete']
        })
        result, changed = run_module()
        test = [{
            "active": True,
            "config": {
                "content_type": "json",
                "insecure_ssl": "0",
                "url": "https://test.com/test_endpoint"
            },
            "events": [
                "create",
                "delete"
            ],
            "id": 999,
            "name": "web",
            "ping_url": "https://api.github.com/repos/org_name/no_webhook/hooks/999/pings",
            "test_url": "https://api.github.com/repos/org_name/no_webhook/hooks/999/test",
            "url": "https://api.github.com/repos/org_name/no_webhook/hooks/999"
        }]
        assert result == test
        assert changed is True

    def test_adding_webhook_that_is_already_there(self):
        set_module_args({
            'access_token': 'token',
            'organization': 'org_name',
            'repository': 'one_webhook',
            'url': 'http://test.com',
            'events': ['member', 'create']
        })
        result, changed = run_module()
        test = [{
            "active": True,
            "config": {
                "content_type": "json",
                "insecure_ssl": "0",
                "url": "http://test.com"
            },
            "events": [
                "member",
                "create"
            ],
            "id": 0,
            "name": "web",
            "ping_url": "https://api.github.com/repos/org_name/one_webhook/hooks/0/pings",
            "test_url": "https://api.github.com/repos/org_name/one_webhook/hooks/0/test",
            "url": "https://api.github.com/repos/org_name/one_webhook/hooks/0"
        }]
        assert result == test
        assert changed is False

    def test_deleting_webhook_from_a_list(self):
        set_module_args({
            'access_token': 'token',
            'organization': 'org_name',
            'repository': 'one_webhook',
            'url': 'http://test.com',
            'events': ['create', 'delete'],
            'state': 'absent'
        })
        result, changed = run_module()
        test = []
        assert result == test
        assert changed is True

    def test_deleting_webhook_that_is_not_in_a_list(self):
        set_module_args({
            'access_token': 'token',
            'organization': 'org_name',
            'repository': 'one_webhook',
            'url': 'http://test_two.com',
            'events': ['create', 'delete'],
            'state': 'absent'
        })
        result, changed = run_module()
        test = [{
            "active": True,
            "config": {
                "content_type": "json",
                "insecure_ssl": "0",
                "url": "http://test.com"
            },
            "events": [
                "member",
                "create"
            ],
            "id": 0,
            "name": "web",
            "ping_url": "https://api.github.com/repos/org_name/one_webhook/hooks/0/pings",
            "test_url": "https://api.github.com/repos/org_name/one_webhook/hooks/0/test",
            "url": "https://api.github.com/repos/org_name/one_webhook/hooks/0"
        }]
        assert result == test
        assert changed is False

    def test_editing_webhook_that_is_in_a_list_by_changing_events(self):
        set_module_args({
            'access_token': 'token',
            'organization': 'org_name',
            'repository': 'one_webhook',
            'url': 'http://test.com',
            'events': ['create', 'delete'],
            'state': 'present'
        })
        result, changed = run_module()
        test = [{
            "active": True,
            "config": {
                "content_type": "json",
                "insecure_ssl": "0",
                "url": "http://test.com"
            },
            "events": [
                "create",
                "delete"
            ],
            "id": 0,
            "name": "web",
            "ping_url": "https://api.github.com/repos/org_name/one_webhook/hooks/0/pings",
            "test_url": "https://api.github.com/repos/org_name/one_webhook/hooks/0/test",
            "url": "https://api.github.com/repos/org_name/one_webhook/hooks/0"
        }]
        assert result == test
        assert changed is True

    def test_editing_webhook_that_is_in_a_list_by_adding_events(self):
        set_module_args({
            'access_token': 'token',
            'organization': 'org_name',
            'repository': 'one_webhook',
            'url': 'http://test.com',
            'events': ['create', 'delete', 'check_run'],
            'state': 'present'
        })
        result, changed = run_module()
        test = [{
            "active": True,
            "config": {
                "content_type": "json",
                "insecure_ssl": "0",
                "url": "http://test.com"
            },
            "events": [
                "create",
                "delete",
                'check_run'
            ],
            "id": 0,
            "name": "web",
            "ping_url": "https://api.github.com/repos/org_name/one_webhook/hooks/0/pings",
            "test_url": "https://api.github.com/repos/org_name/one_webhook/hooks/0/test",
            "url": "https://api.github.com/repos/org_name/one_webhook/hooks/0"
        }]
        assert result == test
        assert changed is True

    def test_editing_webhook_that_is_in_a_list_by_deleting_events(self):
        set_module_args({
            'access_token': 'token',
            'organization': 'org_name',
            'repository': 'one_webhook',
            'url': 'http://test.com',
            'events': ['create'],
            'state': 'present'
        })
        result, changed = run_module()
        test = [{
            "active": True,
            "config": {
                "content_type": "json",
                "insecure_ssl": "0",
                "url": "http://test.com"
            },
            "events": [
                "create"
            ],
            "id": 0,
            "name": "web",
            "ping_url": "https://api.github.com/repos/org_name/one_webhook/hooks/0/pings",
            "test_url": "https://api.github.com/repos/org_name/one_webhook/hooks/0/test",
            "url": "https://api.github.com/repos/org_name/one_webhook/hooks/0"
        }]
        assert result == test
        assert changed is True

    def test_incorrect_events(self):
        set_module_args({
            'access_token': 'token',
            'organization': 'org_name',
            'repository': 'one_webhook',
            'url': 'http://test.com',
            'events': ['create', 'not_an_event'],
            'state': 'present'
        })
        result, changed = run_module()
        test = 'Invalid event name: ' + 'not_an_event'
        assert result == test
        assert changed is False

    def test_incorrect_content_type(self):
        set_module_args({
            'access_token': 'token',
            'organization': 'org_name',
            'repository': 'one_webhook',
            'url': 'http://test.com',
            'events': ['create'],
            'content_type': 'not_a_valid_content_type',
            'state': 'present'
        })
        result, changed = run_module()
        test = "Invalid content type: not_a_valid_content_type"
        assert result == test
        assert changed is False

    def test_adding_webhook_to_populated_list_check_mode(self):
        set_module_args({
            'access_token': 'token',
            'organization': 'org_name',
            'repository': 'one_webhook',
            'url': 'https://test.com/test_endpoint',
            'events': ['create', 'delete'],
            'check_mode': True
        })
        result, changed = run_module()
        test = [{
            "active": True,
            "config": {
                "content_type": "json",
                "insecure_ssl": "0",
                "url": "http://test.com"
            },
            "events": [
                "member",
                "create"
            ],
            "id": 0,
            "name": "web",
            "ping_url": "https://api.github.com/repos/org_name/one_webhook/hooks/0/pings",
            "test_url": "https://api.github.com/repos/org_name/one_webhook/hooks/0/test",
            "url": "https://api.github.com/repos/org_name/one_webhook/hooks/0"
        },
            {
                "active": True,
                "config": {
                    "content_type": "json",
                    "insecure_ssl": "0",
                    "url": "https://test.com/test_endpoint"
                },
                "events": [
                    "create",
                    "delete"
                ],
                "id": 999,
                "name": "web",
                "ping_url": "https://api.github.com/repos/org_name/one_webhook/hooks/999/pings",
                "test_url": "https://api.github.com/repos/org_name/one_webhook/hooks/999/test",
                "url": "https://api.github.com/repos/org_name/one_webhook/hooks/999"
        }]
        assert result == test
        assert changed is True

    def test_adding_webhook_to_empty_list_check_mode(self):
        set_module_args({
            'access_token': 'token',
            'organization': 'org_name',
            'repository': 'no_webhook',
            'url': 'https://test.com/test_endpoint',
            'events': ['create', 'delete'],
            'check_mode': True
        })
        result, changed = run_module()
        test = [{
            "active": True,
            "config": {
                "content_type": "json",
                "insecure_ssl": "0",
                "url": "https://test.com/test_endpoint"
            },
            "events": [
                "create",
                "delete"
            ],
            "id": 999,
            "name": "web",
            "ping_url": "https://api.github.com/repos/org_name/no_webhook/hooks/999/pings",
            "test_url": "https://api.github.com/repos/org_name/no_webhook/hooks/999/test",
            "url": "https://api.github.com/repos/org_name/no_webhook/hooks/999"
        }]
        assert result == test
        assert changed is True

    def test_adding_webhook_that_is_already_there_check_mode(self):
        set_module_args({
            'access_token': 'token',
            'organization': 'org_name',
            'repository': 'one_webhook',
            'url': 'http://test.com',
            'events': ['member', 'create'],
            'check_mode': True
        })
        result, changed = run_module()
        test = [{
            "active": True,
            "config": {
                "content_type": "json",
                "insecure_ssl": "0",
                "url": "http://test.com"
            },
            "events": [
                "member",
                "create"
            ],
            "id": 0,
            "name": "web",
            "ping_url": "https://api.github.com/repos/org_name/one_webhook/hooks/0/pings",
            "test_url": "https://api.github.com/repos/org_name/one_webhook/hooks/0/test",
            "url": "https://api.github.com/repos/org_name/one_webhook/hooks/0"
        }]
        assert result == test
        assert changed is False

    def test_deleting_webhook_from_a_list_check_mode(self):
        set_module_args({
            'access_token': 'token',
            'organization': 'org_name',
            'repository': 'one_webhook',
            'url': 'http://test.com',
            'events': ['create', 'delete'],
            'state': 'absent',
            'check_mode': True
        })
        result, changed = run_module()
        test = []
        assert result == test
        assert changed is True

    def test_deleting_webhook_that_is_not_in_a_list_check_mode(self):
        set_module_args({
            'access_token': 'token',
            'organization': 'org_name',
            'repository': 'one_webhook',
            'url': 'http://test_two.com',
            'events': ['create', 'delete'],
            'state': 'absent',
            'check_mode': True
        })
        result, changed = run_module()
        test = [{
            "active": True,
            "config": {
                "content_type": "json",
                "insecure_ssl": "0",
                "url": "http://test.com"
            },
            "events": [
                "member",
                "create"
            ],
            "id": 0,
            "name": "web",
            "ping_url": "https://api.github.com/repos/org_name/one_webhook/hooks/0/pings",
            "test_url": "https://api.github.com/repos/org_name/one_webhook/hooks/0/test",
            "url": "https://api.github.com/repos/org_name/one_webhook/hooks/0"
        }]
        assert result == test
        assert changed is False

    def test_editing_webhook_that_is_in_a_list_by_changing_events_check_mode(self):
        set_module_args({
            'access_token': 'token',
            'organization': 'org_name',
            'repository': 'one_webhook',
            'url': 'http://test.com',
            'events': ['create', 'delete'],
            'state': 'present',
            'check_mode': True
        })
        result, changed = run_module()
        test = [{
            "active": True,
            "config": {
                "content_type": "json",
                "insecure_ssl": "0",
                "url": "http://test.com"
            },
            "events": [
                "create",
                "delete"
            ],
            "id": 0,
            "name": "web",
            "ping_url": "https://api.github.com/repos/org_name/one_webhook/hooks/0/pings",
            "test_url": "https://api.github.com/repos/org_name/one_webhook/hooks/0/test",
            "url": "https://api.github.com/repos/org_name/one_webhook/hooks/0"
        }]
        assert result == test
        assert changed is True

    def test_editing_webhook_that_is_in_a_list_by_adding_events_check_mode(self):
        set_module_args({
            'access_token': 'token',
            'organization': 'org_name',
            'repository': 'one_webhook',
            'url': 'http://test.com',
            'events': ['create', 'delete', 'check_run'],
            'state': 'present',
            'check_mode': True
        })
        result, changed = run_module()
        test = [{
            "active": True,
            "config": {
                "content_type": "json",
                "insecure_ssl": "0",
                "url": "http://test.com"
            },
            "events": [
                "create",
                "delete",
                'check_run'
            ],
            "id": 0,
            "name": "web",
            "ping_url": "https://api.github.com/repos/org_name/one_webhook/hooks/0/pings",
            "test_url": "https://api.github.com/repos/org_name/one_webhook/hooks/0/test",
            "url": "https://api.github.com/repos/org_name/one_webhook/hooks/0"
        }]
        assert result == test
        assert changed is True

    def test_editing_webhook_that_is_in_a_list_by_deleting_events_check_mode(self):
        set_module_args({
            'access_token': 'token',
            'organization': 'org_name',
            'repository': 'one_webhook',
            'url': 'http://test.com',
            'events': ['create'],
            'state': 'present',
            'check_mode': True
        })
        result, changed = run_module()
        test = [{
            "active": True,
            "config": {
                "content_type": "json",
                "insecure_ssl": "0",
                "url": "http://test.com"
            },
            "events": [
                "create"
            ],
            "id": 0,
            "name": "web",
            "ping_url": "https://api.github.com/repos/org_name/one_webhook/hooks/0/pings",
            "test_url": "https://api.github.com/repos/org_name/one_webhook/hooks/0/test",
            "url": "https://api.github.com/repos/org_name/one_webhook/hooks/0"
        }]
        assert result == test
        assert changed is True
