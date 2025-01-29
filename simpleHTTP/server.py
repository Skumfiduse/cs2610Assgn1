import socket
from decoder import decode, encode
from router import router
from middleware import loggingMiddlewareFactory, notFoundMessageMiddlewareFactory

# HTTP Request format:
# <start line>
# header1
# header2
# header3
#
# body

# headers
# key: value
# Content-Type: application/json

# Start Line:
# <verb> <uri> <http version>
# GET POST PUT PATCH DELETE
# GET / HTTP/1.1
# GET /exports/data HTTP/1.1

# HTTP Response format:
# <start line>
# header1
# header2
# header3
#
# body

# Start Line:
# <http version> <status code> <status message|reason>
# HTTP/1.1 200 Ok
# HTTP/1.1 404 Not Found

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

            # Parse the request
            parsed = decode(data)
            print(f"Method: {parsed.method}\nuri: {parsed.uri}\nversion: {parsed.version}\n body: {parsed.body}")

            #TODO: parse the request, send through middleware and encode the response
            res = "HTTP/1.1 200 Ok\nConnection: close\n\n<h1>Hello, world!</h1>"

            connection.send(bytes(res, "UTF-8"))


# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.bind(("127.0.0.1", 8000))
#     s.listen()
#     print("listening on port 8000")

#     while True:
#         print("connected: 1")
#         connection, addr = s.accept()
#         with connection:
#             print("connected: 2")
#             data = connection.recv(8192)
#             print("connected: 3")

#             if not data:
#                 continue
#             print("connected: 4")

#             request = decode(data)
#             print(request.method)
#             print(request.uri)
#             print(request.version)
#             print(request.body)
#             print(request.headers)
#             middlewareChain = notFoundMessageMiddlewareFactory(router)
#             response = middlewareChain(request)
#             responseBytes = encode(response)
#             print("connected: 5")

#             connection.send(responseBytes)