import os

from core.settings.settings import *

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

DEBUG = True

ALLOWED_HOSTS = ['*']
