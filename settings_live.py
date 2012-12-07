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

STATICFILE_DIRS = (
    os.path.join(PROJECT_DIR, "static"),
)
STATIC_ROOT = os.path.join(PROJECT_DIR, "../../voicebank_static")

EMAIL_HOST = 'smtp.webfaction.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = 'deone'
EMAIL_HOST_PASSWORD = '@dune369'
