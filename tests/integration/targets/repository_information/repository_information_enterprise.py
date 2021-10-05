import unittest
from github import Github
import sys


class TestAPIConnection(unittest.TestCase):
    API_KEY = 'token'
    ORGANIZATION_NAME = 'Organzation Name'
    ENTERPRISE_URL = 'Enterprise Url'

    def test_check_to_see_repo_returns_correctly_enterprise(self):
        g = Github(self.API_KEY, base_url=self.ENTERPRISE_URL)
        output = []

        for repo in g.get_organization(self.ORGANIZATION_NAME).get_repos():
            output.append(repo.name)

        self.assertEqual(['testing-repo-private',
                         'testing-repo-internal',
                         'testing-repo-public'],
                          output)
        self.assertEqual(type(output), list)


if __name__ == '__main__':
    if len(sys.argv) > 2:
        TestAPIConnection.ENTERPRISE_URL = sys.argv.pop()
        TestAPIConnection.ORGANIZATION_NAME = sys.argv.pop()
        TestAPIConnection.API_KEY = sys.argv.pop()

    unittest.main()
    
