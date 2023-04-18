#!/usr/bin/env python3
"""Unit tests for client module"""

import parameterized
import unittest
from unittest.mock import patch, Mock, PropertyMock
from typing import Any, Dict, Callable, Mapping
from client import GithubOrgClient
from utils import get_json
import requests
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """Test case for class `GithubOrgClient`
    """

    @parameterized.expand([
        ("google", {}),
        ("abc", {}),
    ])
    @patch("__main__.get_json")
    def test_org(self, org_name: str, result: Dict,
                 mock_get_json: Mock) -> None:
        """Testing correct output is given using org method"""
        gh_client = GithubOrgClient(org_name)
        with patch.object(gh_client, "org", autospec=True) as mock_org:
            mock_org.return_value = result
            mocked = mock_org()
            self.assertEqual(mock_org, gh_client.org)
            self.assertEqual(mocked, result)
        mock_org.assert_called_once()
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")

    def test_public_repos_url(self) -> None:
        """Testing correct output is given using _public_repos_url method"""
        with patch.object("__main__.GithubOrgClient", "_public_repos_url",
                          autospec=True,
                          new_callable=PropertyMock) as mock_repos:
            mock_repos.return_value = "Nothing"
            gh_client = GithubOrgClient("org_name")
            repo_url = gh_client._public_repos_url
            self.assertEqual(repo_url, "Nothing")
        mock_repos.assert_called_once()

    @patch("__main__.get_json")
    def test_public_repos(self, mocked_get_json: Mock) -> None:
        """Testing correct output is given using public_repos method"""
        with patch.object("__main__.GithubOrgClient", "_public_repos_url",
                          autospec=True,
                          new_callable=PropertyMock) as mock_repos_url:
            mock_repos_url.return_value = "No_Repos"
            with patch.object("__main__.GithubOrgClient", "repos_payload",
                              autospec=True) as mock_repos_payload:
                mock_repos_payload.return_value = {"name": "Empty"}
                with patch.object("__main__.GithubOrgClient", "public_repos",
                                  autospec=True) as mock_public_repos:
                    mock_public_repos.return_value = ["Nothing"]
                    gh_client = GithubOrgClient("org_name")
                    repo = gh_client.public_repos("my_license")
                    self.assertEqual(repo, ["Nothing"])
        mock_public_repos.assert_called_once_with("my_license")
        mock_repos_payload.assert_called_once()
        mocked_get_json.assert_called_once_with("No_Repos")
        mock_repos_url.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo: Mapping,
                         license_key: str, result: bool) -> None:
        """Testing correct output is given using has_license method"""
        with patch.object("__main__.GithubOrgClient", "has_license",
                          autospec=True) as mock_method:
            output = mock_method(repo, license_key)
            self.assertEqual(output, result)
        mock_method.assert_called_once_with(repo, license_key)


org_payload, repos_payload, expected_repos, apache2_repos = TEST_PAYLOAD[0]


@parameterized.parameterized_class(
    [
        {"org_payload": org_payload},
        {"repos_payload": repos_payload},
        {"expected_repos": expected_repos},
        {"apache2_repos": apache2_repos}
    ]
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Itegration Test case for class `GithubOrgClient`
    """
    def side_effect(test_url: str):
        """Side effect for mock function"""
        return org_payload

    def setUpClass(self) -> None:
        """Set up patches for the class"""
        self.get_patcher = patch.object(
            "__main__.requests", "get", autospec=True)
        self.get_patcher.side_effect = self.side_effect
        self.get_patcher.start()

    def tearDownClass(self) -> None:
        "Dispose of patches for the class"
        patch.stopall()
