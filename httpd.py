import argparse
import configparser
import os
import socket

import sys

from core.settings import DEFAULT_ROOT_DIR
from src.handler import CustomHttpRequestHandler
from src.server import CustomHttpServer

DEFAULT_CONFIG = 'config.ini'


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-C', '--config', default=DEFAULT_CONFIG, help='Configuration file')
    parser.add_argument(
        '-r', '--root', default=DEFAULT_ROOT_DIR, help='Root directory for reading files')
    parser.add_argument(
        '-c', '--ncpu', default=3, type=int, help='Number of cpu')

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()
    config = configparser.RawConfigParser()
    config.read(args.config)

    if not os.path.exists(args.root):
        print("Please, check root directory.")
        sys.exit()

    server = CustomHttpServer(args.root, CustomHttpRequestHandler, config.get('server', 'host'),
                              int(config.get('server', 'port')), args.ncpu, int(config.get('server', 'listeners')),
                              int(config.get('server', 'recv_msg_size')))
    server.start()
