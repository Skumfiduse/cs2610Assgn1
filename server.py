import socket
from decoder import decode, encode
from router import router
from middleware import notFoundMessageMiddlewareFactory, responseMiddlewareFactory, staticMiddlewareFactory, compose, loggingMiddlewareFactory

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
            # print(f"Method: {parsed.method}\nuri: {parsed.uri}\nversion: {parsed.version}\n body: {parsed.body}")
            # send it through the middle ware chain reverse order
            # log, staic?, exists?, knit, router

            middlewareList = [responseMiddlewareFactory, notFoundMessageMiddlewareFactory, staticMiddlewareFactory, loggingMiddlewareFactory]
            middlewareChain = compose(router, middlewareList)
            response = middlewareChain(parsed)
            res = encode(response)

            # response = middlewareChain(data)

            # return the response.
            #TODO: parse the request, send through middleware and encode the response
            
            # res = "HTTP/1.1 200 Ok\nConnection: close\n\n<h1>Hello, world!</h1>"
            connection.send(res)
            # connection.send(bytes(res, "UTF-8"))


# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.bind(("127.0.0.1", 8000))
#     s.listen()
#     print("listening on port 8000")

#     while True:
#         connection, addr = s.accept()
#         with connection:
#             data = connection.recv(8192)

#             if not data:
#                 continue

#             request = decode(data)
#             middlewareChain = notFoundMessageMiddlewareFactory(router)
#             response = middlewareChain(request)
#             responseBytes = encode(response)

#             connection.send(responseBytes)