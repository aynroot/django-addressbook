from django.conf.urls import include, url

from contacts import urls as contacts_urls


urlpatterns = [
    url(r'^', include(contacts_urls))
]
