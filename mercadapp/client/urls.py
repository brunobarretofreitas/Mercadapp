from django.conf.urls import url
from .views import *

urlpatterns = [
	url(r'^$', UserCreate.as_view()),
	url(r'^(?P<pk>[0-9]+)/', UserDetail.as_view()),
	url(r'^logged/orders/$', UserOrders.as_view()),
	url(r'^logged/carts/$', UserCarts.as_view()),
]