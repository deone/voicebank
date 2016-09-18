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

# ALLOWED_HOSTS = ['www.nigerianvoicebank.com', 'nigerianvoicebank.com']
# SITE_URL = 'http://nigerianvoicebank.com'
ALLOWED_HOSTS = ['deone.webfactional.com']
SITE_URL = 'http://deone.webfactional.com'
