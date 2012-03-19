from settings import *

DEBUG = TEMPLATE_DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'deone_voicebank',
	'USER': 'deone_voicebank',
        'PASSWORD': 'v01ce',
        'HOST': '',
        'PORT': '',
    }
}

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.staticfiles',
    'sorl.thumbnail',
    'accounts',
    'core',
)

STATICFILE_DIRS = (
    "/home/deone/webapps/voicebank/voicebank/static"
)
STATIC_URL = "/static/"
STATIC_ROOT = "/home/deone/webapps/voicebank_static/"
STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
)

ADMIN_MEDIA_PREFIX = "/static/admin/"

EMAIL_HOST = 'smtp.webfaction.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = 'deone'
EMAIL_HOST_PASSWORD = '@dune369'
