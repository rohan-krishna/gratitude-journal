import os
from journalapp.settings.common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# HOSTS Settings
ALLOWED_HOSTS = ["*"]

# Email Settings
EMAIL_HOST='0.0.0.0'
EMAIL_HOST_USER=''
EMAIL_HOST_PASSWORD=''
EMAIL_PORT=1025
EMAIL_USE_TLS=False

# SECURITY WARNING: keep the secret key used in production secret!
with open(os.path.join(BASE_DIR, '../django_secret_key.txt')) as f:
    SECRET_KEY = f.read().strip()