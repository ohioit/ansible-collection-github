#!/usr/bin/python
from github import Github
from ansible.module_utils.basic import AnsibleModule

ANSIBLE_METADATA = {
    'metadata_version': '1.0',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: repository_information

short_description: A module that returns information about GitHub repositories

description:

  - "A module that fetches information about repositories
        that a GitHub user has access to inside an organization."

options:
    token:
        description:
            - GitHub API token used to retrieve information
                about repositories to which a user has access to
        required: true
        type: str
    enterprise_url:
        description:
            - If using a token from a GitHub Enterprise account,
                the user must pass an enterprise URL
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
    enterprise_url: "https://github.<ENTERPRISE DOMAIN>/api/v3/repos/<ORGANIZATION NAME>/<REPO NAME>"
'''

RETURN = '''
repos:
    description: List contains dictionaries of repositories and their information.
    type: list
    returned: if GitHub API token connects
    
repos.<ELEMENT INDEX>:
    description: Dictionary contains keys and values of a repository's information.
    type: dict
    returned: only if at least one repo is contained within organization

repos.<ELEMENT INDEX>.name:
    description: Repository's name.
    type: str
    returned: only if organization contains a repository

repos.<ELEMENT INDEX>.full_name:
    description: Repository path name starting from organization.
    type: str
    returned: only if organization contains a repository
    
repos.<ELEMENT INDEX>.owner:
    description: Name of organization that owns the repository.
    type: str
    returned: only if organization contains a repository

repos.<ELEMENT INDEX>.description:
    description: Description of the repository. This field will be null unless previously set.
    type: str
    returned: only if organization contains a repository
    
repos.<ELEMENT INDEX>.private:
    description: Status whether the repository is private or public.
    type: bool
    returned: only if organization contains a repository
    
repos.<ELEMENT INDEX>.archived:
    description: Status of whether the repository is archived or not.
    type: bool
    returned: only if organization contains a repository
    
repos.<ELEMENT INDEX>.language:
    description: Repository language. This can be any language listed in 'https://github.com/github/linguist/blob/master/lib/linguist/languages.yml'.
    type: str
    returned: only if organization contains a repository
    
repos.<ELEMENT INDEX>.url:
    description: URL for repository. The provided URL is the route used for the GitHub API to be connected to Ansible.
                Non-enterprise URLs will be structured as 'https://api.github.com/repos/<ORGANIZATION NAME>/<REPO NAME>'.
                Enterprise URLs are structured as 'https://github.<ENTERPRISE DOMAIN>/api/v3/repos/<ORGANIZATION NAME>/<REPO NAME>'.
    type: str
    returned: only if organization contains a repository
    
repos.<ELEMENT INDEX>.default_branch:
    description: The branch that GitHub displays when anyone visits your repository.
    type: str
    returned: only if organization contains a repository

repos.<ELEMENT INDEX>.hooks_url:
    description: URL location where hooks are located within the repository when connected to the GitHub API.
                Non-enterprise URLs should be structured as 'https://api.github.com/repos/<ORGANIZATION NAME>/<REPO NAME>/hooks'.
                Enterprise URLs should be structured as 'https://github.<ENTERPRISE DOMAIN>/api/v3/repos/<ORGANIZATION NAME>/<REPO NAME>/hooks'. 
    type: str
    returned: only if organization contains a repository

repos.<ELEMENT INDEX>.clone_url:
    description: URL location where repository will be accessible to be cloned. 
                Non-enterprise URLs should be structured as 'https://github.com/<ORGANIZATION NAME>/<REPO NAME>.git'.
                Enterprise URLs should be structured as 'https://github.<ENTERPRISE DOMAIN>/<ORGANIZATION NAME>/<REPO NAME>.git'. 
    type: str
    returned: only if organization contains a repository
    
repos.<ELEMENT INDEX>.visibility:
    description: The repository visibility status will be 'public', 'internal', or 'private'. 
    type: str
    returned: only if organization contains a repository and is not a part of an enterprise account
    
repos.<ELEMENT INDEX>.is_template:
    description: The repository template status will true or false. 
    type: bool
    returned: only if organization contains a repository and is not a part of an enterprise account
'''


def run_module():
    module_args = dict(
        token=dict(type='str', default='No Token Provided.'),
        organization_name=dict(
            type='str', default='No Organization Name Provided.'),
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

    if(module.params['enterprise_url'] == ''):
        g = Github(module.params['token'])
    else:
        g = Github(module.params['token'],
                   base_url=module.params['enterprise_url'])

    output = []

    org_name = module.params['organization_name']

    for repo in g.get_organization(org_name).get_repos():
        current_repo_dict = {
            "name": repo.name,
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
            current_repo_dict["is_template"] = repo.raw_data["is_template"]

        output.append(current_repo_dict)
    if module.check_mode:
        return result

    module.exit_json(repos=output)


def main():
    run_module()


if __name__ == '__main__':
    main()
