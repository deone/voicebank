from django.conf import settings

def admin_media_prefix(request):
    return {'ADMIN_MEDIA_PREFIX': settings.ADMIN_MEDIA_PREFIX}

def site(request):
    return {'SITE_URL': settings.SITE_URL}
