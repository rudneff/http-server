import socket

from src.request import Request

if __name__ == "__main__":
    sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('127.0.0.1', 8889))
    sock.listen(10)
    while True:
        client_sock, client_addr = sock.accept()
        data = client_sock.recv(2048)
        req = Request(data)
        print(req.url)
        client_sock.close()
    sock.close()

