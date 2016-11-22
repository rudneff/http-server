import socket

from core.settings import DEFAULT_ROOT_DIR
from src.handler import CustomHttpRequestHandler
from src.request import Request

if __name__ == "__main__":
    sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('127.0.0.1', 8080))
    sock.listen(10)
    while True:
        client_sock, client_addr = sock.accept()
        data = client_sock.recv(2048)
        if len(data.strip()) == 0:
            client_sock.close()
            continue
        req = Request(data)
        handler = CustomHttpRequestHandler(req, DEFAULT_ROOT_DIR)
        resp = handler.handle()
        client_sock.sendall(resp.build())
        client_sock.close()
    sock.close()

