from .base import *

DEBUG = True
ALLOWED_HOSTS = ["DJANGO_ALLOWED_HOSTS", "127.0.0.1"]
SECRET_KEY = 'django-insecure-3t9el&)0niuu=6od8$s$c!4u)6*xhiljb#)e*mxbkj#yi29kph'

try:
    from .local import *
except ImportError:
    pass
