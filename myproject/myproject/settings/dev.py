from .base import *
from decouple import config as cfg

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = cfg('DEBUG')

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = cfg('SECRET_KEY')

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = [cfg('ALLOWED_HOSTS')]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


try:
    from .local import *
except ImportError:
    pass
