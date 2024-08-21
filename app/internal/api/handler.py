import json
from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from http import HTTPStatus

from internal.github.client import fetch_issues
from pkg.logger.logger import Logger
from pkg.constants.error import MISSING_QUERY_PARAMETERS, ERROR_FETCHING_ISSUES
from pkg.constants.info import INFO_HANDLING_REQUEST

class IssuesHandler(BaseHTTPRequestHandler):
    def __init__(self, *args, logger: Logger = None, **kwargs):
        self.logger = logger
        super().__init__(*args, **kwargs)

    def do_GET(self):
        self.logger.info(INFO_HANDLING_REQUEST)

        parsed_path = urlparse(self.path)
        query_params = parse_qs(parsed_path.query)
        owner = query_params.get('owner', [None])[0]
        repo = query_params.get('repo', [None])[0]

        if not owner or not repo:
            self.send_response(HTTPStatus.BAD_REQUEST)
            self.end_headers()
            self.wfile.write(MISSING_QUERY_PARAMETERS.encode())
            return

        try:
            issues = fetch_issues(owner, repo)
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(issues).encode())
        except Exception as e:
            self.logger.error(f"{ERROR_FETCHING_ISSUES}: {e}")
            self.send_response(HTTPStatus.INTERNAL_SERVER_ERROR)
            self.end_headers()
            self.wfile.write(str(e).encode())
