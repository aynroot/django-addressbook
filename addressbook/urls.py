from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static

from contacts import urls as contacts_urls


urlpatterns = [
    url(r'^', include(contacts_urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
