import unittest
from github import Github

class TestAPIConnection(unittest.TestCase):
    def test_check_to_see_repo_returns_correctly(self):
        g = Github('token')
        output = []
        org_name = 'Kegz-Tester'

        for repo in g.get_user(org_name).get_repos():
            output.append(repo.name)

        self.assertEqual(['repo1', 'repo2'], output)

if __name__ == '__main__':
    unittest.main()
    