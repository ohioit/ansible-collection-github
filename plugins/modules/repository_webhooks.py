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


ANSIBLE_METADATA = {
    "metadata_version": "1.0",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = '''
---
module: repository_webhooks

short_description: A module that manages webhooks

description:
  - "A module that manages a repository's webhooks."

options:
    access_token:
        description:
            - GitHub API token used to retrieve information about repositories to which a user has access.
        required: true
        type: str
    api_url:
        description:
            - If using a GitHub API token from a GitHub Enterprise account, the user must pass an enterprise URL.
              This URL must be structured as 'https://github.<ENTERPRISE DOMAIN>/api/v3'.
        required: false
        type: str
    organization:
        description:
          - The organization containing the repository whose webhook will be modified or deleted.
        required: true
        type: str
    repository:
        description:
          - The provided repository for which webhooks are being managed.
        required: true
        type: str
    url:
        description:
          - The provided url will be the webhook that is added, deleted, or edited.
            This must be structured as <SCHEME(https://)><HOST(fakewebsite.com)><ENDPOINT(/path/end/here)>
        required: true
        type: str
    events:
        description:
          - The list of provided events will be added to what triggers a webhook.
            The following events are valid "branch_protection_rule", "check_run", "check_suite",
            "code_scanning_alert", "commit_comment", "content_reference", "create", "delete",
            "deploy_key", "deployment", "deployment_status", "discussion", "discussion_comment",
            "fork", "github_app_authorization", "gollum", "installation", "installation_repositories",
            "issue_comment", "issues", "label", "marketplace_purchase", "member", "membership", "meta",
            "milestone", "organization", "org_block", "package", "page_build", "ping", "project_card",
            "project_column", "project", "public", "pull_request", "pull_request_review", "pull_request_review_comment",
            "push", "release", "repository_dispatch", "repository", "repository_import", "repository_vulnerability_alert",
            "secret_scanning_alert", "security_advisory", "sponsorship", "star", "status", "team", "team_add", "watch",
            "workflow_dispatch", or "workflow_job". This is used with the "present" state.
        required: false
        type: list
        elements: str
    content_type:
        description:
          - The provided content type will be the webhook's primary content type.
            This can either be "json" or "form".
            This is used with the "present" state.
        required: false
        type: str
        default: json
    state:
        description:
          - Specifies if the webhook should exist or not in the repository. Can be either "present" or "absent".
        required: False
        type: str
        default: present

author:
    - Jacob Eicher (@jacobeicher)
    - Bradley Golski (@bgolski)
    - Tyler Zwolenik (@TylerZwolenik)
    - Nolan Khounborinn (@Khounborinn)
'''

EXAMPLES = """
- name: "Add/Modify webhook to GitHub repository"
  ohioit.github.repository_webhooks:
    state: present
    access_token: "12345"
    organization: "SSEP"
    api_url: "https://github.<ORGANIZATION DOMAIN>/api/v3"
    repository: "testing-repo-public"
    url: "https://ansiblest.ansible.com/ansible-test"
    events:
      - "public"
      - "gollum"
    content_type: json
  register: result

- name: "Delete webhook in GitHub repository"
  ohioit.github.repository_webhooks:
    state: absent
    access_token: "12345"
    organization: "SSEP"
    api_url: "https://github.<ORGANIZATION DOMAIN>/api/v3"
    repository: "testing-repo-public"
    url: "https://ansiblest.ansible.com/ansible-test"
  register: result
"""

RETURN = """
webhooks:
    description: List contains dictionaries of webhooks and their information.
    type: list
    returned: if GitHub API token connects

webhooks.<ELEMENT INDEX>:
    description: Dictionary contains keys and values of webhooks' information.
    type: dict
    returned: if at least one webhook is contained within organization

webhooks.<ELEMENT INDEX>.active:
    description: Status of whether the webhook is active or not.
    type: bool
    returned: provided per webhook dictionary

webhooks.<ELEMENT INDEX>.config:
    description: dictionary containing the webhook's content type, insecure ssl number, and the url of where to send.
    type: dict
    returned: provided per webhook dictionary

webhooks.<ELEMENT INDEX>.config.content_type:
    description: The format of the webhook being sent to the url.
    type: str
    returned: provided per webhook's configuration

webhooks.<ELEMENT INDEX>.config.insecure_ssl:
    description: The status of the website being sent information. Whether or not it is secure (https vs http).
    type: str
    returned: provided per webhook's configuration

webhooks.<ELEMENT INDEX>.config.url:
    description: The url that the webhook is sending to.
    type: str
    returned: provided per webhook's configuration

webhooks.<ELEMENT INDEX>.events:
    description: List of events that trigger the webhook to send data.
    type: list
    returned: provided per webhook dictionary

webhooks.<ELEMENT INDEX>.id:
    description: Unique identifier for the webhook in the repository.
    type: int
    returned: provided per webhook dictionary

webhooks.<ELEMENT INDEX>.name:
    description: Name of the webhook.
    type: str
    returned: provided per webhook dictionary

webhooks.<ELEMENT INDEX>.ping_url:
    description: The url to ping the webhook.
    type: str
    returned: provided per webhook dictionary

webhooks.<ELEMENT INDEX>.test_url:
    description: The url to test the webhook.
    type: str
    returned: provided per webhook dictionary

webhooks.<ELEMENT INDEX>.url:
    description: The url in which the webhook resides
    type: str
    returned: provided per webhook dictionary
"""

import collections
import json
from operator import mod
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.common.text.converters import jsonify
from github import Github


def get_webhooks(g, repo):
    hooks = []
    current_hook_dict = {}
    for current_hook in g.get_repo(repo).get_hooks():
        current_hook_dict = {
            "id": current_hook.id,
            "config": current_hook.config,
            "name": current_hook.name,
            "url": current_hook.url,
            "active": current_hook.active,
            "test_url": current_hook.test_url,
            "ping_url": current_hook.ping_url,
            "events": current_hook.events,
        }
        hooks.append(current_hook_dict)
    output = [i for n, i in enumerate(hooks) if i not in hooks[n + 1:]]

    return output


def create_or_update_webhook(g, repo, events, url, content_type):

    config = {"url": url, "content_type": content_type if content_type else "json"}

    for current_hook in g.get_repo(repo).get_hooks():
        if (config["url"] == current_hook.config["url"]):
            current_hook.edit("web", config, events, active=True)
            return

    repo = g.get_repo(repo)
    repo.create_hook("web", config, events, active=True)


def delete_webhook(g, repo, url):
    for current_hook in g.get_repo(repo).get_hooks():
        if url == current_hook.config["url"]:
            current_hook.delete()


def run_module():
    module_args = dict(
        state=dict(type="str", default="present"),
        access_token=dict(type="str", required=True, no_log=True),
        organization=dict(type="str", required=True),
        api_url=dict(type="str", default=""),
        repository=dict(type="str", required=True),
        url=dict(type="str", required=True),
        events=dict(type="list", elements="str"),
        content_type=dict(type="str", default="json"),
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

    if module.params["state"] not in valid_actions:
        error_message = "Invalid action: " + module.params["state"]
        module.exit_json(changed=False, err=error_message, failed=True)

    if module.params["events"]:
        for event in module.params["events"]:
            if event not in valid_events:
                error_message = "Invalid event name: " + event
                module.exit_json(
                    changed=False, err=error_message, failed=True)

    if module.params["content_type"] not in valid_content_types:
        error_message = "Invalid content type: " + \
            module.params["content_type"]
        module.exit_json(
            changed=False, err=error_message, failed=True)

    if module.params["api_url"] == "":
        g = Github(module.params["access_token"])
    else:
        g = Github(module.params["access_token"],
                   base_url=module.params["api_url"])

    if len(module.params["repository"]):
        module.params["repository"] = (
            module.params["organization"] + "/" + module.params["repository"]
        )

    initial = get_webhooks(g, module.params["repository"])

    if module.params["url"]:
        if module.params["state"].lower() == "absent":
            if module.check_mode:
                for hooks in initial:
                    if hooks['config']['url'] == module.params['url']:
                        initial.remove(hooks)

            else:
                delete_webhook(g, module.params["repository"], module.params["url"])
        elif module.params["state"].lower() == "present":
            if module.check_mode:
                found = False
                for hooks in initial:
                    if hooks['config']['url'] == module.params['url']:
                        hooks['events'] = module.params['events']
                        found = True
                if not found:
                    if module.params["api_url"] != "":
                        urlBase = module.params["api_url"]
                    else:
                        urlBase = "https://github.com/api/v3%s" % (
                            module.params['organization'])
                    initial.append({
                        "active": True,
                        "config": {
                            "content_type": module.params['content_type'],
                            "insecure_ssl": "0",
                            "url": module.params['url']
                        },
                        "events": module.params['events'],
                        "id": "<WEBHOOK_ID>",
                        "name": "web",
                        "ping_url": "%s/%s/hooks/<WEBHOOK_ID>/pings" % (urlBase, module.params["repository"]),
                        "test_url": "%s/%s/hooks/<WEBHOOK_ID>/test" % (urlBase, module.params["repository"]),
                        "url": "%s/%s/hooks/<WEBHOOK_ID>" % (urlBase, module.params["repository"])
                    })
            else:
                create_or_update_webhook(
                    g,
                    module.params["repository"],
                    module.params["events"],
                    module.params["url"],
                    module.params["content_type"],
                )

    output = get_webhooks(g, module.params["repository"])

    if module.check_mode:
        module.exit_json(webhooks=initial, changed=initial != output)
    else:
        module.exit_json(webhooks=output, changed=initial != output)


def main():
    run_module()


if __name__ == "__main__":
    main()
