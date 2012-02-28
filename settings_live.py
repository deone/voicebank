from settings import *

DEBUG = TEMPLATE_DEBUG = False

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

STATIC_URL = "/site_media/"
STATIC_ROOT = "/home/deone/webapps/voicebank_static/"

ADMIN_MEDIA_PREFIX = "/site_media/admin/"
