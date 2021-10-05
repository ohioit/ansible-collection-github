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

class TestCollaboratorRepository(unittest.TestCase):
    API_KEY = 'token'
    ORGANIZATION_NAME = 'Organization Name'

    def test_pass_list_collaborators_regular_github(self):
        g = Github(self.API_KEY)
        repo_list = ['ansible-collection-github']

        if len(repo_list):
            for i in range(len(repo_list)):
                repo_list[i] = self.ORGANIZATION_NAME + "/" + repo_list[i]

        output = get_collaborators(g, repo_list)
        collaborator_list = list()
        for collaborator in output[repo_list[0]]:
            collaborator_list.append(collaborator['login'])

        assert 'Khounborinn' in collaborator_list

    def test_pass_check_permissions_regular_github(self):
        g = Github(self.API_KEY)
        repo_list = ['ansible-collection-github']

        if len(repo_list):
            for i in range(len(repo_list)):
                repo_list[i] = self.ORGANIZATION_NAME + "/" + repo_list[i]

        output = get_collaborators(g, repo_list)

        collaborator_list = list()
        for collaborator in output[repo_list[0]]:
            collaborator_list.append(collaborator['login'])

        for i in range(0, len(collaborator_list)):
            if output[repo_list[0]][i]['login'] == 'Khounborinn':
                collaborator_permission = {'permissions': output[repo_list[0]][i]['permissions']}

        assert 'push=True' in str(collaborator_permission['permissions'])


if __name__ == '__main__':
    if len(sys.argv) > 1:
        TestCollaboratorRepository.ORGANIZATION_NAME = sys.argv.pop()
        TestCollaboratorRepository.API_KEY = sys.argv.pop()
        
    unittest.main()
