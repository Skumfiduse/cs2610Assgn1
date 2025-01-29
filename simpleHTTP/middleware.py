#functions that do things between things

def responceMiddlewareFactory(nextMiddleware):
    def middleware(req):
        


        return res

def loggingMiddlewareFactory(nextMiddleware):
    def middleware(req):
        # do something request
        print(f"Method: {req.method}, URI: {req.uri}")
        # call the nextMiddleware function
        res = nextMiddleware(req)
        # do something with result of nextMiddlware
        print(f"URI: {res.uri} Code: {res.code}, Reason: {res.reason}")
        # return a Response (not optional!)
        return res

    return middleware

def notFoundMessageMiddlewareFactory(nextMiddleware):
    def middleware(req):
        res = nextMiddleware(req)
        if res.code == 404:
            print("Oh no! You requested something that does not exist!")

        return res

    return middleware
