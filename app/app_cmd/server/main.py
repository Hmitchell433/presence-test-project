from http.server import HTTPServer

from internal.api.handler import IssuesHandler
from pkg.logger.logger import Logger
from pkg.config.config import Config
from pkg.constants.info import INFO_SERVER_START

def main():
    log = Logger()
    server_address = ('', Config.SERVER_PORT)

    httpd = HTTPServer(server_address, lambda *args, **kwargs: IssuesHandler(*args, logger=log, **kwargs))

    log.info(INFO_SERVER_START.format(Config.SERVER_PORT))
    httpd.serve_forever()

if __name__ == "__main__":
    main()
