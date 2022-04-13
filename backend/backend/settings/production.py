from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

# ALLOWED_HOSTS = ['192.168.1.9']
ALLOWED_HOSTS = []


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASS'),
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT'),
        'OPTIONS': {'ssl': {'ca': env('MYSQL_ATTR_SSL_CA')}}
    }
}


'''
DB_NAME=store
DB_USER=j2tp7tp4odx6
DB_PASS=pscale_pw_X468wnapJDUrFL-XKXm49U1mNCDSORF68lvxp9svbbE
DB_HOST=y22l0scq0nzs.us-east-4.psdb.cloud
DB_PORT=3306
MYSQL_ATTR_SSL_CA=/etc/ssl/certs/ca-certificates.crt
'''
