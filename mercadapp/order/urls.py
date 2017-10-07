from django.conf.urls import url

from .views import *

urlpatterns = [
	url(r'^$', OrderList.as_view()),
	url(r'^payments/$', PaymentList.as_view()),
	url(r'^(?P<pk>[0-9]+)/$', OrderDetail.as_view()),
	url(r'^(?P<pk>[0-9]+)/info/$', OrderInfo.as_view()),
	url(r'^new/$', OrderStatusNew.as_view()),
	url(r'^approved/$', OrderStatusApproved.as_view()),
	url(r'^sent/$', OrderStatusSent.as_view()),
	url(r'^delivered/$', OrderStatusDelivered.as_view()),
]
	