#functions that do things between things
from decoder import decode
from response import Response

def responseMiddlewareFactory(nextMiddleware):
    def middleware(req):
        res = nextMiddleware(req)
        if req.uri == '/':
            req.uri = '/index'
        with open(f'./templates{req.uri}.html') as file:
            content = file.read()
            res.body = content
        return res
    return middleware

def loggingMiddlewareFactory(nextMiddleware):
    def middleware(req):
        # read request info
        print(f"Request information: Method: {req.method}, URI: {req.uri}\n")
        res = nextMiddleware(req) # convert request to response
        print(f"Response information: URI: {req.uri} Code: {res.code}, Reason: {res.reason}\n")
        # return the response
        return res

    return middleware

def notFoundMessageMiddlewareFactory(nextMiddleware):
    def middleware(req):
        res = nextMiddleware(req)
        if res.code == 404:
            print(f"the page you requested does not exist. {req.uri}\n")

        return res

    return middleware

def staticMiddlewareFactory(nextMiddleware):
    def middleware(req):
        if '.' in req.uri:
            try:
                with open(f'./static/{req.uri}') as file:
                    content = file.read()
                    res = Response('HTTP/1.1', 200, 'ok', {}, content)
                    return res
            except FileNotFoundError:
                print("file not found")
                res = Response('HTTP/1.1', 404, 'not found', {}, '')
                return res

        res = nextMiddleware(req)
        return res
        
    return middleware

def compose(router, middlewareList):
    middlewareChain = router
    for mWare in middlewareList:
        middlewareChain = mWare(middlewareChain)
    return middlewareChain