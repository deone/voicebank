import os
import sys
import django.core.handlers.wsgi

sys.stdout = sys.stderr

sys.path.append("/usr/local/www")
sys.path.append("/usr/local/www/voicebank")

os.environ["DJANGO_SETTINGS_MODULE"] = "voicebank.settings_live"

application = django.core.handlers.wsgi.WSGIHandler()
