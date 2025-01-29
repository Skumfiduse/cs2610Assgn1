from request import Request

def decode(requestBytes):
    request = requestBytes.decode("UTF-8")
    lines = request.split("\n")
    startLine = lines[0]
    method, uri, version = startLine.split(" ")
    return Request(
        method=method,
        uri=uri,
        version=version,
        body="",
        headers={},
    )

def encode(response):
    return f"{response.version} {response.code} {response.reason}\nConnection: close\n\n{response.body}".encode("UTF-8")
