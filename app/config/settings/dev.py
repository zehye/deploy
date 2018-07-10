from .base import *

secrets = json.load(open(os.path.join(SECRET_DIR, 'dev.json')))
# secrets = json.loads(open(SECRET_DIR, 'dev.json').read())

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Static
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(ROOT_DIR, '.static')

MEDIA_ROOT = os.path.join(ROOT_DIR, '.media')
MEDIA_URL = '/media/'

# WSGI
WSGI_APPLICATION = 'config.wsgi.dev.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
DATABASES = secrets['DATABASES']
print(DATABASES)

