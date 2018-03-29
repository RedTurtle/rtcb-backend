# -*- coding: utf-8 -*-

from .base import *  # noqa
from .omissis import *  # noqa

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
]


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rtcb',

    'graphene_django',
]

GRAPHENE = {
    'SCHEMA': 'rtcb.schema.schema',
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'rtcbproj.urls'


# sqlite3 database - dev
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# CUSTOM USER MODEL
AUTH_USER_MODEL = 'rtcb.User'
