from settings import *

DEBUG = TEMPLATE_DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nvb_voicebank',
	    'USER': 'deone_voicebank',
        'PASSWORD': 'yR5LIuqdKp6sY5J',
        'HOST': '',
        'PORT': '',
    }
}

STATICFILE_DIRS = (
    os.path.join(PROJECT_DIR, "static"),
)
STATIC_ROOT = os.path.join(PROJECT_DIR, "../../../nvb_static")

ALLOWED_HOSTS = [
    'www.nigerianvoicebank.com',
    'nigerianvoicebank.com',
    'www.nvb.ng',
    'nvb.ng',
    'www.africanvo.com',
    'africanvo.com',
]
SITE_URL = 'http://nigerianvoicebank.com'
