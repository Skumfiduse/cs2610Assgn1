import socket
from decoder import decode, encode
from router import router
from middleware import notFoundMessageMiddlewareFactory, responseMiddlewareFactory, staticMiddlewareFactory, compose, loggingMiddlewareFactory


import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(("127.0.0.1", 8000))
    s.listen()
    print("listening on port 8000")

    while True:
        connection, addr = s.accept()
        with connection:
            data = connection.recv(8192)
            if not data:
                connection.close()
                continue

            parsed = decode(data)

            middlewareList = [responseMiddlewareFactory, notFoundMessageMiddlewareFactory, staticMiddlewareFactory, loggingMiddlewareFactory]
            middlewareChain = compose(router, middlewareList)
            response = middlewareChain(parsed)
            res = encode(response)

            
            connection.send(res)
