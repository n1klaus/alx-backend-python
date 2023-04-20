#!/usr/bin/env python3
"""Unit tests for client module"""

from parameterized import parameterized, parameterized_class
import unittest
from unittest.mock import patch, Mock, MagicMock, PropertyMock
from typing import Any, Dict, Callable, Mapping
from client import GithubOrgClient, get_json
import requests
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """Test case for class `GithubOrgClient`
    """

    @parameterized.expand([
        ("google", {}),
        ("abc", {}),
    ])
    @patch("client.get_json")
    def test_org(self, org_name: str, result: Dict,
                 mock_get_json: MagicMock) -> None:
        """Testing correct output is given using org method"""
        mock_get_json.return_value = MagicMock(return_value=result)
        gh_client = GithubOrgClient(org_name)
        output = gh_client.org()
        self.assertEqual(result, output)
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")

    def test_public_repos_url(self) -> None:
        """Testing correct output is given using _public_repos_url method"""
        with patch.object(GithubOrgClient, "_public_repos_url",
                          new_callable=PropertyMock) as mock_repos:
            mock_repos.return_value = "Nothing"
            gh_client = GithubOrgClient("org_name")
            repo_url = gh_client._public_repos_url
            self.assertEqual(repo_url, "Nothing")
        mock_repos.assert_called_once()

    @patch("client.get_json")
    def test_public_repos(self, mocked_get_json: MagicMock) -> None:
        """Testing correct output is given using public_repos method"""
        with patch.object(GithubOrgClient, "_public_repos_url",
                          new_callable=PropertyMock) as mock_repos_url:
            mock_repos_url.return_value = "No_Repos"
            gh_client = GithubOrgClient("org_name")
            gh_client.public_repos("my_license")
        mocked_get_json.assert_called_once_with("No_Repos")
        mock_repos_url.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo: Mapping,
                         license_key: str, result: bool) -> None:
        """Testing correct output is given using has_license method"""
        with patch.object(GithubOrgClient, "has_license",
                          autospec=True) as mock_method:
            mock_method.return_value = result
            output = mock_method(repo, license_key)
            self.assertEqual(output, result)
            mock_method.assert_called_once_with(repo, license_key)


org_payload, repos_payload, expected_repos, apache2_repos = TEST_PAYLOAD[0]


@parameterized_class(
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

    @classmethod
    def setUpClass(cls) -> None:
        """Sets up class fixtures before running tests."""
        def side_effect(url):
            """Side effect for mock function"""
            if "repos" in url:
                return Mock(**{'json.return_value': repos_payload})
            else:
                return Mock(**{'json.return_value': org_payload})

        cls.get_patcher = patch.object(
            requests, "get", autospec=True, side_effect=side_effect)
        cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls) -> None:
        "Dispose of patches for the class"
        patch.stopall()

    def test_public_repos(self) -> None:
        """Tests the `public_repos` method."""
        self.assertEqual(
            GithubOrgClient("google").public_repos(),
            expected_repos,
        )

    def test_public_repos_with_license(self) -> None:
        """Tests the `public_repos` method with a license."""
        self.assertEqual(
            GithubOrgClient("google").public_repos(license="apache-2.0"),
            apache2_repos,
        )
