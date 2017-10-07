from django.conf.urls import url
from .views import *

urlpatterns = [
	url(r'^$', CreateCart.as_view()),
	url(r'^(?P<pk>[0-9]+)/$', CartDetail.as_view()),
	url(r'^(?P<pk>[0-9]+)/items$', CartItems.as_view()),
	url(r'^(?P<cart>[0-9]+)/items/(?P<pk>[0-9]+)/$', CartItemDetail.as_view()),
]