# Big ol' if statement that only returns endpoints. Pretty easy stuff
from response import Response
from endpoints import home, about, experience, projects, info
from middleware import staticMiddlewareFactory


def router(request):
    if request.uri == "/":
        return home(request)
    elif request.uri == "/about":
        return about(request)
    elif request.uri == "/experience":
        return experience(request)
    elif request.uri == "/projects":
        return projects(request)
    elif request.uri == "/info":
        return info(request)
    else:
        return Response(
            code=404,
            reason="Not Found",
            version=request.version,
            headers={},
            body="broke",
        )


