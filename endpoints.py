from response import Response
from middleware import loggingMiddlewareFactory


def home(req):
    return Response(
        version=req.version,
        code=200,
        reason="Ok",
        headers={},
        body="index",
    )



def about(req):
    return Response(
        version=req.version,
        code=200,
        reason="Ok",
        headers={},
        body="about",
    )


def experience(req):
    return Response(
        version=req.version,
        code=200,
        reason="Ok",
        headers={},
        body="experience",
    )


def projects(req):
    return Response(
        version=req.version,
        code=200,
        reason="Ok",
        headers={},
        body="projects",
    )
