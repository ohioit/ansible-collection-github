import unittest
from github import Github
import sys


class TestAPIConnection(unittest.TestCase):
    API_KEY = 'token'
    ORGANIZATION_NAME = 'Organzation Name'

    def test_check_to_see_repo_returns_correctly_regular(self):
        g = Github(self.API_KEY)
        output = []

        for repo in g.get_organization(self.ORGANIZATION_NAME).get_repos():
            output.append(repo.name)

        self.assertEqual(['kegz', 'ansible-collection-github'], output)
        self.assertEqual(type(output), list)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        TestAPIConnection.ORGANIZATION_NAME = sys.argv.pop()
        TestAPIConnection.API_KEY = sys.argv.pop()

    unittest.main()
    
