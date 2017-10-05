from django.conf.urls import url
from .views import list_or_create_stores, store_informations

urlpatterns = [
	url(r'^stores/$', list_or_create_stores, name='stores'),
	url(r'^stores/(?P<pk>[0-9]+)/$', store_informations),
]