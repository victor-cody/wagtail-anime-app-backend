import os
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# DEBUG = 'RENDER' not in os.environ

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = "django-insecure-wciltrm*7p&@fk-#ajm1@h3(xn+0#zby_$3(qopu0h876*++9="

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get(
    'SECRET_KEY', default='django-insecure-wciltrm*7p&@fk-#ajm1@h3(xn+0#zby_$3(qopu0h876*++9=')

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

# RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')

# if RENDER_EXTERNAL_HOSTNAME:
#         ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)


EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


try:
    from .local import *
except ImportError:
    pass
