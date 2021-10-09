from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-3t9el&)0niuu=6od8$s$c!4u)6*xhiljb#)e*mxbkj#yi29kph'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["DJANGO_ALLOWED_HOSTS", "127.0.0.1", 'localhost']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


try:
    from .local import *
except ImportError:
    pass
