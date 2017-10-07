from django.conf.urls import url
from .views import *

urlpatterns = [
	url(r'^$', StoreList.as_view(), name='stores'),
	url(r'^deliver/(?P<location>\w{0,50})$', StoresDeliverable.as_view()),
	url(r'^(?P<pk>[0-9]+)/$', StoreDetail.as_view()),
	url(r'^(?P<pk>[0-9]+)/products/$', StoreProductsList.as_view()),
	url(r'^(?P<pk>[0-9]+)/delivery/$', StoreDeliveryList.as_view()),
	url(r'^(?P<pk>[0-9]+)/delivery/days/$', StoreDeliveryDay.as_view()),
	url(r'^(?P<store>[0-9]+)/delivery/days/(?P<pk>[0-9]+)/hours/$', StoreDeliveryHour.as_view()),
]