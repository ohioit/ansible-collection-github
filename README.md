# Ansible Collection for GitHub

### The OHIO IT collection of Ansible modules for GitHub.

The collection includes a variety of Ansible modules to help automate the management of organizations, repositories, and user permissions in GitHub.

---

## Version Compatibility

Tested against:
`Ansible Version >=2.11`
`Python >=3.8`
`PyGitHub >=1.55`

## Installation

Install this collection via [Ansible Galaxy](https://galaxy.ansible.com/ohioit/github):

```bash
ansible-galaxy collection install ohioit.github
```

Content in this collection requires the [PyGitHub package](https://github.com/PyGithub/PyGithub) to interact with [GitHub REST API](https://docs.github.com/en/rest). You can install it with:

```bash
pip install PyGithub
```

## Included Content

### Modules

| Name                                                                                                                                             | Description                                                                            |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------- |
| [repository_information](https://github.com/ohioit/ansible-collection-github/blob/main/docs/repository_information.rst) | Output repositories along with vital information from an (user specified) organization |
| [collaborator_information](https://github.com/ohioit/ansible-collection-github/blob/main/docs/collaborator_information.rst) | View and manage repository collaborators |
| [repository_webhooks](https://github.com/ohioit/ansible-collection-github/blob/main/docs/repository_webhooks.rst) | A module that manages a repository's webhooks |
| [branch_protection](https://github.com/ohioit/ansible-collection-github/blob/main/docs/branch_protection.rst) | A module that allows the modification of branch protections. |
| [general_repository](https://github.com/ohioit/ansible-collection-github/blob/main/docs/general_repository.rst) | A module that manages a repository in an organization. |

## Usage

### Repository Information

```
  - name: "List GitHub repositories within a non-enterprise organization"
    ohioit.github.repository_information:
      token: "<API TOKEN>"
      organization_name: "<ORGANIZATION NAME>"
    register: result

  - name: "List GitHub repositories within an enterprise organization"
    ohioit.github.repository_information:
      token: "<TOKEN>"
      organization_name: "<ORGANIZATION NAME>"
      enterprise_url: "https://github.<ENTERPRISE DOMAIN>/api/v3/"
    register: result    
```
### Collaborator Information

```
    - name: "Functions of Collaborator information module"
      ohioit.github.collaborator_information:
        access_token: "<API TOKEN>"
        organization: "<ORGANIZATION NAME>"
        api_url: "https://github.<ENTERPRISE DOMAIN>/api/v3/"
        repository: "<REPOSITORY NAME>"
        collaborator: "<VALID GITHUB USERNAME>"
        permission: <pull, push, or admin>
        state: <present or absent> 
```
### Webhook
```
    - name: "Add/Modify webhook to GitHub repository MOD 3"
      ohioit.github.repository_webhooks:
        state: <present or absent> 
        access_token: "<API TOKEN>"
        organization: "<ORGANIZATION NAME>"
        api_url: "https://github.<ENTERPRISE DOMAIN>/api/v3/"
        repository: "<REPOSITORY NAME>"
        url: "<RECEIVING URL>"
        events:
          - "<LIST EVENT 1>"
          - "<LIST EVENT 2>"
        content_type: <json or form>
```
### Branch Protection

```
    - name: "Modify branch protections to a branch"
      ohioit.github.branch_protection:
        access_token: "<API TOKEN>"
        organization: "<ORGANIZATION NAME>"
        api_url: "https://github.<ENTERPRISE DOMAIN>/api/v3/"
        repository: "<REPOSITORY NAME>"
        branch: "<BRANCH NAME>"
        state: "<present or absent>"
        branch_protections:
          strict: <true or false>
          contexts: ["<EXAMPLE: default or ci-test>", ...]
          enforce_admins: <true or false>
          dismissal_users: ["<GITHUB USERNAMES>", ...]
          dismissal_teams: ["<GITHUB TEAMS>", ...]
          dismiss_stale_reviews: <true or false>
          require_code_owner_reviews: <true or false>
          required_approving_review_count: <INTEGER>
          user_push_restrictions: ["<GITHUB USERNAMES>", ...]
          team_push_restrictions: ["<GITHUB TEAMS>", ...]
```
### General Repository

```
    - name: "Create repository within enterprise organization"
      ohioit.github.general_repository:
        access_token: "<API TOKEN>"
        organization: "<ORGANIZATION NAME>"
        api_url: "https://github.<ENTERPRISE DOMAIN>/api/v3/"
        repository: "<REPOSITORY NAME>"
        private: <true or false>
        description: "<DESCRIPTION OF REPOSITORY>"
        homepage: "<HOMEPAGE NAME>"
        has_issues: <true or false>
        has_wiki: <true or false>
        has_downloads: <true or false>
        has_projects: <true or false>
        team_id: <INTEGER>
        auto_init: <true or false>
        license_template: "<LICENSING GUIDLINES example: gpl-3.0>"
        gitignore_template: "<SUPPORTED PROGRAMMING LANGUAGE>"
        allow_squash_merge: <true or false>
        allow_merge_commit: <true or false>
        allow_rebase_merge: <true or false>
        delete_branch_on_merge: <true or false>
        state: <present or absent>
```

###### _**NOTE**: Tokens should be encrypted and only decrypted at runtime_

## Testing with 'ansible-test'

Testing has been made available using the [ansible-test](https://docs.ansible.com/ansible/latest/dev_guide/testing_integration.html). These tests include [unit](https://github.com/senior-design-21-22/ansible-collection-github/blob/development/docs/unit_testing.rst), [sanity](https://github.com/senior-design-21-22/ansible-collection-github/tree/repo-information-module/unit/sanity), [integration](https://github.com/senior-design-21-22/ansible-collection-github/blob/development/docs/integration_testing.rst).

The tests are runnable using the following commands:

```bash
ansible-test units --python 3.<YOUR PYTHON VERSION> --venv
ansible-test sanity --python 3.<YOUR PYTHON VERSION> plugins/modules/*
ansible-test integration --python 3.<YOUR PYTHON VERSION>
```
