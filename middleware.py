#functions that do things between things
from decoder import decode
from response import Response
from datetime import date

def responseMiddlewareFactory(nextMiddleware):
    def middleware(req):
        res = nextMiddleware(req)
        if req.uri == '/':
            req.uri = '/index'
        if req.uri == '/info':
            req.uri = res.headers["location"]
        with open(f'./templates{req.uri}.html') as file:
            content = file.read()
            today = date.today()
            today = today.strftime("%Y-%m-%d %H:%M:%S")
            res.body = content
            res.headers["Content-Type:"] = "text/html"
            res.headers["Content-Length:"] = len(res.body)
            res.headers["Connection:"] = "Close"
            res.headers["Cache-Control:"] = "max-age=1"
            res.headers["Server:"] = "Grayson's Server"
            res.headers["Date:"] = f"({today})"
        if res.code == 301:
            req.uri = "/info"
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
        whitelist = ['/', '/broke', '/projects', '/experience', '/about', '/info']
        if req.uri not in whitelist: 
            print("file not found")
            today = date.today()
            today = today.strftime("%Y-%m-%d %H:%M:%S")
            res = Response('HTTP/1.1', 404, 'not found', {}, '')
            res.headers["Content-Type:"] = "text/html"
            res.headers["Connection:"] = "Close"
            res.headers["Cache-Control:"] = "max-age=1"
            res.headers["Server:"] = "Grayson's Server"
            res.headers["Date:"] = f"({today})"
            with open(f'./templates/broke.html') as file:
                    content = file.read()
                    res.body = content
            return res
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
                    type = 'JavaScript' if 'js' in req.uri else 'css'
                    content = file.read()
                    today = date.today()
                    today = today.strftime("%Y-%m-%d %H:%M:%S")
                    res = Response('HTTP/1.1', 200, 'ok', {}, content)
                    res.headers["Content-Type:"] = f"text/{type}"
                    res.headers["Content-Length:"] = (res.body)
                    res.headers["Connection:"] = "Close"
                    res.headers["Cache-Control:"] = "max-age=1"
                    res.headers["Server:"] = "Grayson's Server"
                    res.headers["Date:"] = f"({today})"
                    return res
            except FileNotFoundError:
                print("file not found")
                today = date.today()
                today = today.strftime("%Y-%m-%d %H:%M:%S")
                res = Response('HTTP/1.1', 404, 'not found', {}, '')
                res.headers["Content-Type:"] = "text/html"
                res.headers["Connection:"] = "Close"
                res.headers["Cache-Control:"] = "max-age=1"
                res.headers["Server:"] = "Grayson's Server"
                res.headers["Date:"] = f"({today})"
                return res

        res = nextMiddleware(req)
        return res
        
    return middleware

def compose(router, middlewareList):
    middlewareChain = router
    for mWare in middlewareList:
        middlewareChain = mWare(middlewareChain)
    return middlewareChain