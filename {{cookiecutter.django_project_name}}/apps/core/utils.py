import json
import os

from django.conf import settings


def get_version():
    try:
        parts = (
            open(os.path.join(settings.BASE_DIR, ".version.txt"), "r")
            .read()
            .strip()
            .split("\n")
        )

        base = {
            "name": parts.pop(0) if len(parts) > 0 else None,
            "revision": parts.pop(0) if len(parts) > 0 else None,
            "url": parts.pop(0) if len(parts) > 0 else None,
        }
        return {**base, "json": json.dumps(base)}
    except IOError:
        pass

    return {"name": None, "revision": None, "url": None, "json": {}}
