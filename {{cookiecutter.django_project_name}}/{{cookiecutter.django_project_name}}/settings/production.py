import dj_database_url
import requests
from django.core.exceptions import ImproperlyConfigured

from .base import *  # NOQA

DEBUG = False
SECRET_KEY = os.environ.get("SECRET_KEY", "")
USE_X_FORWARDED_HOST = True

ALLOWED_HOSTS = [h.strip() for h in os.environ.get("ALLOWED_HOSTS", "").split(",")]

# Load Balancer META
# -------------------------------------------------------------------------

try:
    EC2_PRIVATE_IP = requests.get(
        "http://169.254.169.254/latest/meta-data/local-ipv4", timeout=2
    ).text
    ALLOWED_HOSTS.append(EC2_PRIVATE_IP)  # NOQA
except requests.exceptions.RequestException:
    raise ImproperlyConfigured(
        "You can only run production settings on an AWS EC2 instance"
    )

# Database
# --------------------------------------------------------------------------

if "DATABASE_URL" in os.environ:
    DATABASES["default"] = dj_database_url.parse(
        os.environ.get("DATABASE_URL", ""), conn_max_age=10
    )  # NOQA

# Media & Storage
# --------------------------------------------------------------------------

# AWS_S3_REGION_NAME = os.environ.get("AWS_DEFAULT_REGION", "eu-west-1")
#
# AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID", "")
# AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY", "")
#
# AWS_STORAGE_BUCKET_NAME = os.environ.get("S3_BUCKET_NAME", "")
# AWS_S3_CUSTOM_DOMAIN = os.environ.get("S3_CUSTOM_DOMAIN", AWS_STORAGE_BUCKET_NAME)
#
# # Fixes issue with calling format
# AWS_S3_CALLING_FORMAT = ProtocolIndependentOrdinaryCallingFormat()
#
# STATIC_URL = "https://{0}/static/".format(AWS_S3_CUSTOM_DOMAIN)
# MEDIA_URL = "https://{0}/media/".format(AWS_S3_CUSTOM_DOMAIN)
#
# DEFAULT_FILE_STORAGE = "{{cookiecutter.django_project_name}}.apps.core.storage.MediaStorage"
# STATICFILES_STORAGE = "{{cookiecutter.django_project_name}}.apps.core.storage.StaticStorage"

# SENTRY
# --------------------------------------------------------------------------

if "SENTRY_DSN" in os.environ:
    import sentry_sdk

    SENTRY_DSN = os.environ.get("SENTRY_DSN")

    from sentry_sdk.integrations.django import DjangoIntegration

    sentry_sdk.init(SENTRY_DSN, integrations=[DjangoIntegration()])

# REDIS
# --------------------------------------------------------------------------

# if "REDIS_URL" in os.environ:
#     cache_locations = [os.environ.get("REDIS_URL")]
#     if "REDIS_URL_SLAVE" in os.environ:
#         cache_locations.append(os.environ.get("REDIS_URL_SLAVE"))
#     CACHES = {
#         "default": {
#             "BACKEND": "django_redis.cache.RedisCache",
#             "LOCATION": cache_locations,
#             "KEY_PREFIX": "aws-live",
#             "OPTIONS": {
#                 "CLIENT_CLASS": "django_redis.client.DefaultClient",
#                 "MAX_ENTRIES": 10000000,
#             },
#         }
#     }
#     SESSION_ENGINE = "django.contrib.sessions.backends.cache"
#     SESSION_CACHE_ALIAS = "default"
