from settings import *

DEBUG = TEMPLATE_DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nvb_voicebank',
	    'USER': 'deone_voicebank',
        'PASSWORD': 'v01ce',
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
    'nvb.ng'
]
SITE_URL = 'http://nigerianvoicebank.com'

EMAIL_HOST = 'smtp.webfaction.com'
EMAIL_HOST_USER = 'deone'
EMAIL_HOST_PASSWORD = os.environ['DEONE_MAILBOX_PASSWORD']
SERVER_EMAIL = 'noreply@nigerianvoicebank.com'