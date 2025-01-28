# Big ol' if statement that only returns endpoints. Pretty easy stuff
from response import Response
from endpoints import home, about

def router(request):
    if request.uri == "/":
        return home(request)
    elif request.uri == "/about":
        return about(request)
    elif request.uri == "experience":
        return about(request)
    elif request.uri == "/projects":
        return about(request)
    elif request.uri == "/info":
        return about(request)
    else:
        return Response(
            code=404,
            reason="Not Found",
            version=request.version,
            headers={},
            body="<h1>router.py says no.<h1>",
        )


