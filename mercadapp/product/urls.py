from django.conf.urls import url
from .views import *

urlpatterns = [
	url(r'^$', ProductList.as_view()),
	url(r'^(?P<pk>[0-9]+)$', ProductDetail.as_view()),
]

