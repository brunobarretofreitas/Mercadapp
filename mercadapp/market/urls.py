from django.conf.urls import url
from .views import StoreList, StoreDetail,StoresDeliverable, OrderInfo, OrderStatusNew, OrderStatusApproved, OrderStatusSent, OrderStatusDelivered, ProductList, OrderDetail, ProductDetail, UserDetail, UserList, UserCarts, CartDetail, PaymentList, CartItems, CartItemDetail, StoreDeliveryList, StoreDeliveryDay, StoreDeliveryHour, OrderList

urlpatterns = [
	url(r'^users/$', UserList.as_view()),
	url(r'^users/(?P<pk>[0-9]+)/$', UserDetail.as_view()),
	url(r'^stores/$', StoreList.as_view(), name='stores'),
	url(r'^stores/deliver/(?P<location>\w{0,50})$', StoresDeliverable.as_view()),
	url(r'^stores/(?P<pk>[0-9]+)/$', StoreDetail.as_view()),
	url(r'^stores/(?P<pk>[0-9]+)/products/$', ProductList.as_view()),
	url(r'^stores/(?P<pk>[0-9]+)/delivery/$', StoreDeliveryList.as_view()),
	url(r'^stores/(?P<pk>[0-9]+)/delivery/days/$', StoreDeliveryDay.as_view()),
	url(r'^stores/(?P<store>[0-9]+)/delivery/days/(?P<pk>[0-9]+)/hours/$', StoreDeliveryHour.as_view()),
	url(r'^stores/(?P<pk>[0-9]+)/orders/$', ProductDetail.as_view()),
	url(r'^products/(?P<pk>[0-9]+)$', ProductDetail.as_view()),
	url(r'^payments/$', PaymentList.as_view()),
	url(r'^carts/$', UserCarts.as_view()),
	url(r'^carts/(?P<pk>[0-9]+)/$', CartDetail.as_view()),
	url(r'^carts/(?P<pk>[0-9]+)/items$', CartItems.as_view()),
	url(r'^carts/(?P<cart>[0-9]+)/items/(?P<pk>[0-9]+)/$', CartItemDetail.as_view()),
	url(r'^orders/$', OrderList.as_view()),
	url(r'^orders/(?P<pk>[0-9]+)/$', OrderDetail.as_view()),
	url(r'^orders/(?P<pk>[0-9]+)/info/$', OrderInfo.as_view()),
	url(r'^orders/new/$', OrderStatusNew.as_view()),
	url(r'^orders/approved/$', OrderStatusApproved.as_view()),
	url(r'^orders/sent/$', OrderStatusSent.as_view()),
	url(r'^orders/delivered/$', OrderStatusDelivered.as_view()),

]