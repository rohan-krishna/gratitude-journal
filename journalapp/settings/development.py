import os
from journalapp.settings.common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# SECURITY WARNING: keep the secret key used in production secret!
with open(os.path.join(BASE_DIR, '../django_secret_key.txt')) as f:
    SECRET_KEY = f.read().strip()