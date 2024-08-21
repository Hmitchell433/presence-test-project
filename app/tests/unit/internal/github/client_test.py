import unittest
from unittest.mock import patch, Mock
from internal.github.client import fetch_issues

class TestGitHubClient(unittest.TestCase):

    @patch('internal.github.client.requests.get')
    def test_fetch_issues_success(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = [{'id': 1, 'title': 'Issue'}]
        mock_get.return_value = mock_response

        issues = fetch_issues("owner", "repo")

        self.assertEqual(len(issues), 1)
        self.assertEqual(issues[0]['title'], 'Issue')

    @patch('internal.github.client.requests.get')
    def test_fetch_issues_empty(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = []
        mock_get.return_value = mock_response

        issues = fetch_issues("owner", "repo")

        self.assertEqual(len(issues), 0)

    @patch('internal.github.client.requests.get')
    def test_fetch_issues_not_found(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 404
        mock_response.json.return_value = {'message': 'Not Found'}
        mock_get.return_value = mock_response

        with self.assertRaises(Exception) as context:
            fetch_issues("owner", "repo")
        self.assertIn('404', str(context.exception))

    @patch('internal.github.client.requests.get')
    def test_fetch_issues_rate_limited(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 403
        mock_response.json.return_value = {'message': 'Rate Limit Exceeded'}
        mock_get.return_value = mock_response

        with self.assertRaises(Exception) as context:
            fetch_issues("owner", "repo")
        self.assertIn('403', str(context.exception))

    @patch('internal.github.client.requests.get')
    def test_fetch_issues_server_error(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 500
        mock_response.json.return_value = {'message': 'Server Error'}
        mock_get.return_value = mock_response

        with self.assertRaises(Exception) as context:
            fetch_issues("owner", "repo")
        self.assertIn('500', str(context.exception))

if __name__ == '__main__':
    unittest.main()
