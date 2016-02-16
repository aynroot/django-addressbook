from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.list_contacts, name='list_contacts'),
    url(r'^new$', views.create_new_contact, name='create_new_contact'),
    url(r'^edit/(?P<pk>\d+)$', views.edit_contact, name='edit_contact'),
    url(r'^delete/(?P<pk>\d+)$', views.delete_contact, name='delete_contact'),
    url(r'^view/(?P<pk>\d+)$', views.contact_details, name='contact_details')
]
