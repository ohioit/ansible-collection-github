#!/usr/bin/python

import collections
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.common.text.converters import jsonify
from github import Github
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
    token:
        description:
            - GitHub API token used to retrieve information about collaborators in repositories a user has access to
        required: true
        type: str

    enterprise_url:
        description:
            - If using a token from a GitHub Enterprise account, the user must pass an enterprise URL. This URL should be in the format of "https://github.<ENTERPRISE DOMAIN>/api/v3".
        required: false
        default: null
        type: str

    organization_name:
        description:
            - The organization that the information is within the scope of.
        required: true
        type: str

    repos:
        description:
            - The list of repositories that will be managed.
        required: true
        type: str

    collaborators_to_add:
        description:
            - The list of collaborators that will be added to the list of repos.
        required: false
        default: null
        type: str

    collaborators_to_remove:
        description:
            - The list of collaborators that will be removed to the list of repos.
        required: false
        default: null
        type: str

    check_collaborator:
        description:
            - The list of collaborators to check their permissions
        required: false
        default: null
        type: str

    collaborators_to_change:
        description:
            - The list of collaborators to change permissions
        required: false
        default: null
        type: str

author:
    - Jacob Eicher (@jacobeicher)
    - Tyler Zwolenik (@TylerZwolenik)
    - Bradley Golski (@bgolski)
    - Nolan Khounborin (@Khounborinn)
'''

EXAMPLES = '''
# Pass in an github API token and organization name

- name: "Listing collaborators from enterprise GitHub account"
    ohioit.github.collaborator_information:
      token: "12345"
      organization_name: "SSEP"
      enterprise_url: "https://github.<ENTERPRISE DOMAIN>/api/v3"
      repos:
        - "testing-repo-private"
        - "testing-repo-internal"
        - "testing-repo-public"

- name: "Adding collaborators from enterprise GitHub account"
    ohioit.github.collaborator_information:
      token: "12345"
      organization_name: "SSEP"
      enterprise_url: "https://github.<ENTERPRISE DOMAIN>/api/v3"
      repos:
        - "testing-repo-private"
        - "testing-repo-internal"
        - "testing-repo-public"
      collaborators_to_add:
        <GITHUB USERNAME>: "push"
        <ANOTHER GITHUB USERNAME>: "pull"

- name: "Change permissions of collaborators from enterprise GitHub account"
    ohioit.github.collaborator_information:
      token: "12345"
      organization_name: "SSEP"
      enterprise_url: "https://github.<ENTERPRISE DOMAIN>/api/v3"
      repos:
        - "testing-repo-private"
        - "testing-repo-internal"
        - "testing-repo-public"
      collaborators_to_change:
        <GITHUB USERNAME>: "admin"
        <ANOTHER GITHUB USERNAME>: "triage"

- name: "Remove permissions of collaborators from enterprise GitHub account"
    ohioit.github.collaborator_information:
      token: "12345"
      organization_name: "SSEP"
      enterprise_url: "https://github.<ENTERPRISE DOMAIN>/api/v3"
      repos:
        - "testing-repo-private"
        - "testing-repo-internal"
        - "testing-repo-public"
        collaborators_to_remove:
          - "<GITHUB USERNAME>"
          - "<ANOTHER GITHUB USERNAME>"
'''

RETURN = '''
collaborators:
    description: Dictionary contains all names of repositories requested and their collaborators. 
    type: dict
    returned: if GitHub API token connects
    
collaborators['<ORG NAME>/<REPO NAME>']:
    description: List contains dicts of each collaborator's information (that are in that repository).
    type: list
    returned: if at least one collaborator is within repository

collaborators['<ORG NAME>/<REPO NAME>'].<INDEX>:
    description: This index provides access to a dictionary containing information about a single collaborator.
    type: dict
    returned: if at least one collaborator is within repository

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
    description: Will return true if triage rights are given to collaborator. Users with the triage role can request reviews on pull requests, mark issues and pull requests as duplicates, and add or remove milestones on issues and pull requests. NO WRITE ACCESS.
    type: bool
    returned: only if at least one collaborator is contained within repository

collaborators['<ORG NAME>/<REPO NAME>'].<INDEX>.site_admin:
    description: Will return true if collaborator is a site admin. This permission gives the collaborator the ability to manage users, organizations, and repositories.
    type: bool
    returned: only if at least one collaborator is contained within repository

collaborators['<ORG NAME>/<REPO NAME>'].<INDEX>.type:
    description: This will return what type of collaborator the user is. 
    type: str
    returned: only if at least one collaborator is contained within repository
'''


def add_collaborators(g, repos, to_add):         
    for repo in repos:
        r = g.get_repo(repo)
        collaborator_list = []
        collaborators = r.get_collaborators(affiliation="direct")
        for collaborator in collaborators:
                collaborator_list.append(collaborator.login)
        for p in to_add:
            r.add_to_collaborators(p, permission=to_add[p])

def check_permissions(g, repos, user_to_check):
    status = True
    for repo in repos:
        r = g.get_repo(repo)
        for user in user_to_check.items():
            if(r.get_collaborator_permission(user[0]) != user[1]):
                status = False
    return status
        

def del_collaborators(g, repos, to_remove):
    for repo in repos:
        r = g.get_repo(repo)
        collaborators = r.get_collaborators(affiliation="direct")
        for collaborator in collaborators:
            if(collaborator.login in to_remove):
                r.remove_from_collaborators(collaborator.login)


def change_collaborator_permissions(g, repos, to_change):
    for repo in repos:
        r = g.get_repo(repo)
        collaborator_list = []
        collaborators = r.get_collaborators(affiliation="direct")
        for collaborator in collaborators:
                collaborator_list.append(collaborator.login)
        for p in to_change:
            if (p in collaborator_list):
                r.add_to_collaborators(p, permission=to_change[p])


def get_collaborators(g, repo_list):

    output = dict()
    for repo in repo_list:
        dict_repo = list()
        collab_output = dict()
        collaborators = g.get_repo(repo).get_collaborators(affiliation="direct")
        for collaborator in collaborators:
             
            collab_output['login'] = collaborator.login
            collab_output['id'] = collaborator.id
            # collab_output['node_id'] = collaborator.node_id
            # collab_output['avatar_url'] = collaborator.avatar_url
            # collab_output['gravatar_id'] = collaborator.gravatar_id
            # collab_output['url'] = collaborator.url
            # collab_output['html_url'] = collaborator.html_url
            # collab_output['followers_url'] = collaborator.followers_url
            # collab_output['following_url'] = collaborator.following_url
            # collab_output['gists_url'] = collaborator.gists_url
            # collab_output['starred_url'] = collaborator.starred_url
            # collab_output['subscriptions_url'] = collaborator.subscriptions_url
            # collab_output['organizations_url'] = collaborator.organizations_url
            # collab_output['repos_url'] = collaborator.repos_url
            # collab_output['events_url'] = collaborator.events_url
            # collab_output['received_events_url'] = collaborator.received_events_url
            collab_output['type'] = collaborator.type
            collab_output['site_admin'] = collaborator.site_admin
            permissions = {
                'triage': collaborator.permissions.triage,
                'push': collaborator.permissions.push,
                'pull': collaborator.permissions.pull,
                'admin': collaborator.permissions.admin
                }
            collab_output['permissions'] = permissions


            dict_repo.append(collab_output.copy())

        output[repo] = dict_repo.copy()

    return output


def run_module():
    changed = True
    module_args = dict(
        token=dict(type='str', default='John Doe'),
        organization_name=dict(type='str', default='default'),
        enterprise_url=dict(type='str', default=''),
        repos=dict(type='list', elements='str'),
        collaborators_to_add=dict(type='dict'),
        check_collaborator=dict(type='dict'),
        collaborators_to_change=dict(type='dict'),
        collaborators_to_remove=dict(type='list', elements='str'),

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

    # token usage retrieved from module's variables from playbook
    if(module.params['enterprise_url'] == ''):
        g = Github(module.params['token'])
    else:
        g = Github(module.params['token'], base_url=module.params['enterprise_url'])

    if len(module.params['repos']):
        for i in range(len(module.params['repos'])):
            module.params['repos'][i] = module.params['organization_name'] + "/" + module.params['repos'][i]

    current_collaborators = get_collaborators(g,  module.params['repos'])

    if(module.params['collaborators_to_add']):
        for permission in module.params['collaborators_to_add']:
            if module.params['collaborators_to_add'][permission].lower() not in valid_permissions:
                module.exit_json(changed=False, failed=True, msg="Invalid permission: " + module.params['collaborators_to_add'][permission] + ". Permissions must be 'push' 'pull' or 'admin'")

        if len(module.params['collaborators_to_add']) and len(module.params['repos']):
            add_collaborators(g, module.params['repos'], module.params['collaborators_to_add'])
            
                


    if(module.params['collaborators_to_remove'] and len(module.params['repos'])):
        del_collaborators(g, module.params['repos'], module.params['collaborators_to_remove'])
    
    if(module.params['check_collaborator'] and len(module.params['repos'])):
        check_permissions(g, module.params['repos'], module.params['check_collaborator'])

    if(module.params['collaborators_to_change'] and len(module.params['repos'])):
        change_collaborator_permissions(g, module.params['repos'], module.params['collaborators_to_change'])


    output = get_collaborators(g,  module.params['repos'])
    if collections.Counter(current_collaborators) == collections.Counter(output):
        changed = False

    if module.check_mode:
        return result

    module.exit_json(changed=changed, collaborators=output)


def main():
    run_module()


if __name__ == '__main__':
    main()
