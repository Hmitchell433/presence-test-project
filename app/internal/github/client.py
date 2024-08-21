import requests
from http import HTTPStatus

from pkg.constants.error import ERROR_RATE_LIMIT_EXCEEDED, ERROR_NOT_FOUND, ERROR_SERVER_ERROR, ERROR_UNEXPECTED
from pkg.constants.constants import GITHUB_API_URL

def fetch_issues(owner, repo):
    url = GITHUB_API_URL.format(owner=owner, repo=repo)
    response = requests.get(url)

    if response.status_code == HTTPStatus.OK:
        return response.json()
    elif response.status_code == HTTPStatus.FORBIDDEN:
        raise Exception(ERROR_RATE_LIMIT_EXCEEDED)
    elif response.status_code == HTTPStatus.NOT_FOUND:
        raise Exception(ERROR_NOT_FOUND)
    elif response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        raise Exception(ERROR_SERVER_ERROR)
    else:
        raise Exception(f"{ERROR_UNEXPECTED}: {response.status_code}")

