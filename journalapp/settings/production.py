import os
from journalapp.settings.common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# HOSTS Settings
ALLOWED_HOSTS = []

# Email Settings
EMAIL_HOST=''
EMAIL_HOST_USER=''
EMAIL_HOST_PASSWORD=''
EMAIL_PORT=''
EMAIL_USE_TLS=False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['DJANGO_SECRET_KEY']