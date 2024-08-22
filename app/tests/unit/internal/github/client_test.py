import pytest
from unittest.mock import patch, Mock
from internal.github.client import fetch_issues

@patch('internal.github.client.requests.get')
def test_fetch_issues_success(mock_get):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = [{'id': 1, 'title': 'Issue'}]
    mock_get.return_value = mock_response

    issues = fetch_issues("owner", "repo")

    assert len(issues) == 1
    assert issues[0]['title'] == 'Issue'

@patch('internal.github.client.requests.get')
def test_fetch_issues_empty(mock_get):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = []
    mock_get.return_value = mock_response

    issues = fetch_issues("owner", "repo")

    assert len(issues) == 0

@patch('internal.github.client.requests.get')
def test_fetch_issues_not_found(mock_get):
    mock_response = Mock()
    mock_response.status_code = 404
    mock_response.json.return_value = {'message': 'Not Found'}
    mock_get.return_value = mock_response

    with pytest.raises(Exception) as excinfo:
        fetch_issues("owner", "repo")
    assert '404' in str(excinfo.value)

@patch('internal.github.client.requests.get')
def test_fetch_issues_rate_limited(mock_get):
    mock_response = Mock()
    mock_response.status_code = 403
    mock_response.json.return_value = {'message': 'Rate Limit Exceeded'}
    mock_get.return_value = mock_response

    with pytest.raises(Exception) as excinfo:
        fetch_issues("owner", "repo")
    assert '403' in str(excinfo.value)

@patch('internal.github.client.requests.get')
def test_fetch_issues_server_error(mock_get):
    mock_response = Mock()
    mock_response.status_code = 500
    mock_response.json.return_value = {'message': 'Server Error'}
    mock_get.return_value = mock_response

    with pytest.raises(Exception) as excinfo:
        fetch_issues("owner", "repo")
    assert '500' in str(excinfo.value)
