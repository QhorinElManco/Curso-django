from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DEBUG")

# ALLOWED_HOSTS = ['192.168.1.9']
ALLOWED_HOSTS = []


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
