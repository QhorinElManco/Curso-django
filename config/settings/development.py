from .base import *  # noqa F401 '.base.*' imported but unused
from .base import INSTALLED_APPS, MIDDLEWARE, env

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY", default="d9fn19p3r#!($+!#_$!%fahfahf(A@(T(A@N@A)(N$T*H$%*")


# Apps specific for development

INSTALLED_APPS += [
    "debug_toolbar",
    "drf_yasg",
]

MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]

ALLOWED_HOSTS = ["localhost", ""]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
]

DEBUG_TOOLBAR_CONFIG = {
    "DISABLE_PANELS": ["debug_toolbar.panels.redirects.RedirectsPanel"],
    "SHOW_TEMPLATE_CONTEXT": True,
}

# INTERNAL_IPS = [ip[:-1] + "1" for ip in ips] + ["127.0.0.1"]

INTERNAL_IPS = ["127.0.0.1"]

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("DB_NAME"),
        "USER": env("DB_USER"),
        "PASSWORD": env("DB_PASS"),
        "HOST": env("DB_HOST"),
        "PORT": env("DB_PORT"),
    }
}
