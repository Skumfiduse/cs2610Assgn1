#functions that do things between things
from decoder import decode

def responseMiddlewareFactory(nextMiddleware):
    def middleware(req):
        res = nextMiddleware(req)
               
        # todo: write code to read data from files.
        # todo: add read code to body section of res

        return res
    return middleware

def loggingMiddlewareFactory(nextMiddleware):
    def middleware(req):

        return res

    return middleware

def notFoundMessageMiddlewareFactory(nextMiddleware):
    def middleware(req):
        res = nextMiddleware(req)
        if res.code == 404:
            print("the page you requested does not exist.")

        return res

    return middleware
