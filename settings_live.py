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

EMAIL_HOST = '74.55.86.74'
EMAIL_PORT = 25
EMAIL_HOST_USER = 'deone'
EMAIL_HOST_PASSWORD = '@dune369'

ALLOWED_HOSTS = ['www.nigerianvoicebank.com', 'nigerianvoicebank.com']
SITE_URL = 'http://nigerianvoicebank.com'
