from .utils import get_version

_VERSION = get_version()


def version(request):
    if _VERSION["name"] or _VERSION["revision"]:
        return {"VERSION": _VERSION}

    return {"VERSION": None}
