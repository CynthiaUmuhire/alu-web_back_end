import unittest
from unittest.mock import MagicMock, patch
from parameterized import parameterized
from client import GithubOrgClient
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos

class TestGithubOrgClient(unittest.TestCase):

    @parameterized.expand([
        ("google", {"login": "google"}),
        ("abc", {"login": "abc"}),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, expected_response, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value."""
        mock_get_json.return_value = expected_response

        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, expected_response)

        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test that GithubOrgClient.public_repos returns the correct value."""
        test_payload = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"},
        ]
        mock_get_json.return_value = test_payload

        with patch('client.GithubOrgClient._public_repos_url', new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = "http://some_url.com"
            client = GithubOrgClient("test_org")

            result = client.public_repos()

            # Check the expected result
            self.assertEqual(result, ["repo1", "repo2", "repo3"])

            # Ensure _public_repos_url property was accessed
            mock_public_repos_url.assert_called_once()

            # Ensure get_json was called once with the correct URL
            mock_get_json.assert_called_once_with("http://some_url.com")

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
        ({}, "my_license", False),
        ({"license": {}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test that GithubOrgClient.has_license returns the correct value."""
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)

    @parameterized_class([
    {"org_payload": org_payload, "repos_payload": repos_payload, "expected_repos": expected_repos, "apache2_repos": apache2_repos}
])
    @classmethod
    def setUpClass(cls):
        """Set up class method to patch requests.get"""
        cls.get_patcher = patch('requests.get')

        # Start patcher and set side_effect for requests.get().json()
        cls.mock_get = cls.get_patcher.start()
        cls.mock_get.return_value = MagicMock()

        def get_json(url):
            if url == "https://api.github.com/orgs/test_org":
                return cls.org_payload
            elif url == "https://api.github.com/orgs/test_org/repos":
                return cls.repos_payload
            return None

        cls.mock_get.return_value.json.side_effect = get_json

    @classmethod
    def tearDownClass(cls):
        """Tear down class method to stop patcher"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test public_repos method"""
        client = GithubOrgClient("test_org")
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """Test public_repos method with license"""
        client = GithubOrgClient("test_org")
        self.assertEqual(client.public_repos(license="apache-2.0"), self.apache2_repos)