#!/usr/bin/python

import unittest
from github import Github
import sys


def add_collaborators(g, repos, to_add, org_name):
    for repo in repos:
        r = g.get_repo(org_name + "/" + repo)
        colab_list = []
        collaborators = r.get_collaborators(affiliation="direct")
        for collaborator in collaborators:
            colab_list.append(collaborator.login)
        for p in to_add:
            if (p not in colab_list):
                r.add_to_collaborators(p, permission=to_add[p])
                print("adding " + p + " to " + repo + " with Permission "  + to_add[p])

def check_permissions(g, repos, user, permission_level, org_name):
    status = False
    for repo in repos:
        r = g.get_repo(org_name + "/" + repo)
        status = (r.get_collaborator_permission(user) == permission_level)

    return status
        

def del_collaborators(g, repos, to_remove, org_name):
    for repo in repos:
        r = g.get_repo(org_name + "/" + repo)
        collaborators = r.get_collaborators(affiliation="direct")
        for collaborator in collaborators:
            if(collaborator.login in to_remove):
                r.remove_from_collaborators(collaborator.login)
                print("removing " + str(collaborator) + " from " + repo)


def change_collaborator_permissions(g, repos, user, permssion_level, org_name):
    for repo in repos:
        r = g.get_repo(org_name + "/" + repo)
        colab_list = []
        collaborators = r.get_collaborators(affiliation="direct")
        for collaborator in collaborators:
            if (user == collaborator.login and permssion_level != r.get_collaborator_permission(user)):
                print("changing " + user + " in " + repo + " from Permission " + r.get_collaborator_permission(user) + " to "  + permssion_level)
                r.add_to_collaborators(user, permission=permssion_level)

def get_collaborators(g, repo_list):

    output = dict()
    for repo in repo_list:
        dict_repo = list()
        collab_output = dict()
        collaborators = g.get_repo(repo).get_collaborators(affiliation="direct")
        for collaborator in collaborators:
             
            collab_output['login'] = collaborator.login
            collab_output['type'] = collaborator.type
            collab_output['site_admin'] = collaborator.site_admin
            collab_output['permissions'] = collaborator.permissions

            dict_repo.append(collab_output.copy())

        output[repo] = dict_repo.copy()

    return output

class TestCollaboratorRepositoryModule(unittest.TestCase):
    API_KEY = 'token'
    ORGANIZATION_NAME = 'Organization Name'
    ENTERPRISE_URL = None
    USER = None

    def test_pass_list_collaborators_enterprise_github(self):
        g = Github(self.API_KEY, base_url=self.ENTERPRISE_URL)
        repo_list = ["testing-repo-private", "testing-repo-internal", "testing-repo-public"]

        if len(repo_list):
            for i in range(len(repo_list)):
                repo_list[i] = self.ORGANIZATION_NAME + "/" + repo_list[i]

        output = get_collaborators(g, repo_list)
        collaborator_list = list()
        for collaborator in output[repo_list[0]]:
            collaborator_list.append(collaborator['login'])

        assert self.USER in collaborator_list

    def test_pass_check_permissions_enterprise_github(self):
        g = Github(self.API_KEY, base_url=self.ENTERPRISE_URL)
        repo_list = ["testing-repo-internal"]

        if len(repo_list):
            for i in range(len(repo_list)):
                repo_list[i] = self.ORGANIZATION_NAME + "/" + repo_list[i]

        output = get_collaborators(g, repo_list)

        collaborator_list = list()
        for collaborator in output[repo_list[0]]:
            collaborator_list.append(collaborator['login'])

        for i in range(0, len(collaborator_list)):
            if output[repo_list[0]][i]['login'] == self.USER:
                collaborator_permission = {'permissions': output[repo_list[0]][i]['permissions']}

        assert 'admin=False' in str(collaborator_permission['permissions'])
        assert 'pull=True' in str(collaborator_permission['permissions'])
        assert 'push=False' in str(collaborator_permission['permissions'])

    def test_pass_add_and_delete_collaborator_to_enterprise_github_repo(self):
        g = Github(self.API_KEY, base_url=self.ENTERPRISE_URL)
        target_repos = ["testing-repo-public"]
        collaborators_to_add = {self.USER:"pull"}
        collaborators_to_remove = [self.USER]

        collaborator_added = False
        collaborator_deleted = False

        #needed from ansible (list of dict [name, permission])
        if(len(collaborators_to_add) > 0):
            if(len(target_repos) > 0):# needed from ansible (list)
                add_collaborators(g, target_repos, collaborators_to_add, self.ORGANIZATION_NAME)

        target_repos_copy = target_repos.copy()
        if len(target_repos_copy):
            for i in range(len(target_repos_copy)):
                target_repos_copy[i] = self.ORGANIZATION_NAME + "/" + target_repos_copy[i]

        output = get_collaborators(g, target_repos_copy)
        collaborator_list = list()
        for collaborator in output[target_repos_copy[0]]:
            collaborator_list.append(collaborator['login'])

        assert self.USER in collaborator_list

        # Remove xuj1 from the repository to return it to the original state

        if(len(collaborators_to_remove) > 0):  # needed from ansible (list)
            if(len(target_repos) > 0):# needed from ansible (list)
                del_collaborators(g, target_repos, collaborators_to_remove, self.ORGANIZATION_NAME)

        output = get_collaborators(g, target_repos_copy)
        collaborator_list = list()
        for collaborator in output[target_repos_copy[0]]:
            collaborator_list.append(collaborator['login'])

        assert self.USER not in collaborator_list

    def test_pass_change_permissions_of_collaborator_enterprise_github(self):
        g = Github(self.API_KEY, base_url=self.ENTERPRISE_URL)
        perms_check = self.USER
        target_repos = ['testing-repo-private']

        target_repos_copy = target_repos.copy()
        if len(target_repos_copy):
            for i in range(len(target_repos_copy)):
                target_repos_copy[i] = self.ORGANIZATION_NAME + "/" + target_repos_copy[i]

        change_collaborator_permissions(g, target_repos, perms_check, "push", self.ORGANIZATION_NAME)

        output = get_collaborators(g, target_repos_copy)

        collaborator_list = list()
        for collaborator in output[target_repos_copy[0]]:
            collaborator_list.append(collaborator['login'])

        for i in range(0, len(collaborator_list)):
            if output[target_repos_copy[0]][i]['login'] == self.USER:
                collaborator_permission = {'permissions': output[target_repos_copy[0]][i]['permissions']}

        assert 'push=True' in str(collaborator_permission['permissions'])

        change_collaborator_permissions(g, target_repos, perms_check, "pull", self.ORGANIZATION_NAME)

        output = get_collaborators(g, target_repos_copy)

        collaborator_list = list()
        for collaborator in output[target_repos_copy[0]]:
            collaborator_list.append(collaborator['login'])

        for i in range(0, len(collaborator_list)):
            if output[target_repos_copy[0]][i]['login'] == self.USER:
                collaborator_permission = {'permissions': output[target_repos_copy[0]][i]['permissions']}

        assert 'push=False' in str(collaborator_permission['permissions'])

    def test_pass_check_for_unrealistic_role(self):
        g = Github(self.API_KEY, base_url=self.ENTERPRISE_URL)
        perms_check = self.USER
        target_repos = ['testing-repo-internal']

        target_repos_copy = target_repos.copy()
        if len(target_repos_copy):
            for i in range(len(target_repos_copy)):
                target_repos_copy[i] = self.ORGANIZATION_NAME + "/" + target_repos_copy[i]

        change_collaborator_permissions(g, target_repos, perms_check, "pizza", self.ORGANIZATION_NAME)

        output = get_collaborators(g, target_repos_copy)

        collaborator_list = list()
        for collaborator in output[target_repos_copy[0]]:
            collaborator_list.append(collaborator['login'])

        for i in range(0, len(collaborator_list)):
            if output[target_repos_copy[0]][i]['login'] == self.USER:
                collaborator_permission = {'permissions': output[target_repos_copy[0]][i]['permissions']}

        assert 'push=False' in str(collaborator_permission['permissions'])
        assert 'pull=True' in str(collaborator_permission['permissions'])

    def test_pass_check_for_no_collaborators(self):

        g = Github(self.API_KEY, base_url=self.ENTERPRISE_URL)
        repo_list = ["test-repo-empty"]

        if len(repo_list):
            for i in range(len(repo_list)):
                repo_list[i] = self.ORGANIZATION_NAME + "/" + repo_list[i]

        output = get_collaborators(g, repo_list)
        collaborator_list = list()
        for collaborator in output[repo_list[0]]:
            collaborator_list.append(collaborator['login'])

        assert not collaborator_list

if __name__ == '__main__':
    if len(sys.argv) > 3:
        TestCollaboratorRepositoryModule.USER = sys.argv.pop()
        TestCollaboratorRepositoryModule.ENTERPRISE_URL = sys.argv.pop()
        TestCollaboratorRepositoryModule.ORGANIZATION_NAME = sys.argv.pop()
        TestCollaboratorRepositoryModule.API_KEY = sys.argv.pop()

    unittest.main()
