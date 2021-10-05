#!/usr/bin/python

ANSIBLE_METADATA = {
    'metadata_version': '1.0',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: repository_info
short_description: A module that returns information about GitHub repositories
description:
  - "A module that fetches information about repositories that a GitHub user has access to inside an organization."
options:
    token:
        description:
            - GitHub API token used to retrieve information about repositories to which a user has access to
        required: true
        type: str
    enterprise_url:
        description:
            - If using a token from a GitHub Enterprise account, the user must pass an enterprise URL
        required: false
        type: str
    organization_name:
        description:
          - The organization in which the query will be run.
        required: true
        type: str
author:
    - Jacob Eicher (@jacobeicher)
    - Bradley Golski (@bgolski)
    - Tyler Zwolenik (@TylerZwolenik)
    - Nolan Khounborinn (@Khounborinn)
'''

EXAMPLES = '''
# Pass in an organization name and GitHub API token
- name: returns information about 
  repository_info:
    organization: "senior-design-21-22"
    github_token: "12345"


# Pass in an organization name, GitHub API token and enterprise URL
- name: returns information about 
  repository_info:
    organization: "SSEP"
    github_token: "12345"
    enterprise_url: "<ENTERPRISE_URL>"
'''

RETURN = '''
    [
        {
            "name":             name of repository (as string),

            "full_name":        full name of repository (as string),

            "owner":            owner name (as string),

            "description":      description (as string),

            "private":          repo status (bool: true or false),

            "is_template":      if it is template (bool: true or false),

            "archived":         archived status of repository (bool: true or false),

            "language":         language that the repo is using (as string),

            "visibility":       for other users ("private" or "public"),

            "url":              url for repo (as string),

            "default_branch":   default branch of the repo (as string),

            "hooks_url":        url for hooks (as string),

            "clone_url":        url for cloning (as string)
        },
        {
            ...
        },
        {
            ...
        }
    ]
'''

from github import Github
from ansible.module_utils.basic import AnsibleModule

def run_module():
    module_args = dict(
        token=dict(type='str', default='No Token Provided.'),
        organization_name=dict(type='str', default='No Organization Name Provided.'),
        enterprise_url=dict(type='str', default=''),
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    result = dict(
        changed=False,
        fact=''
    )
    #token usage retrieved from module's variables from playbook

    if(module.params['enterprise_url'] == ''):
        g = Github(module.params['token'])
    else:
        g = Github(module.params['token'], base_url=module.params['enterprise_url'])

    output = []

    #organization name retrieved from module's variables from playbook
    org_name = module.params['organization_name']
    
    for repo in g.get_organization(org_name).get_repos():
        current_repo_dict = {
                "name" : repo.name,
                "full_name": repo.full_name,
                "owner": repo.owner.login,
                "description": repo.description,
                "private": repo.private,
                "archived": repo.archived,
                "language": repo.language,
                "url": repo.url,
                "default_branch": repo.default_branch,
                "hooks_url": repo.hooks_url,
                "clone_url": repo.clone_url
                }
        if len(module.params["enterprise_url"]) == 0:
            current_repo_dict["visibility"] = repo.raw_data["visibility"]
            current_repo_dict["is_template"]= repo.raw_data["is_template"]
                
        
        output.append(current_repo_dict)
    if module.check_mode:
        return result

    module.exit_json(repos=output) 



def main():
    run_module()

if __name__ == '__main__':
    main()
