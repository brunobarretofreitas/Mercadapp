from django.conf.urls import url
from .views import StoreList, StoreDetail, ProductList, ProductDetail, UserDetail, UserList

urlpatterns = [
	url(r'^users/$', UserList.as_view()),
	url(r'^users/(?P<pk>[0-9]+)/$', UserDetail.as_view()),
	url(r'^stores/$', StoreList.as_view(), name='stores'),
	url(r'^stores/(?P<pk>[0-9]+)/$', StoreDetail.as_view()),
	url(r'^stores/(?P<pk>[0-9]+)/products/$', ProductList.as_view()),
	url(r'^stores/(?P<pk>[0-9]+)/products/(?P<product>[0-9]+)$', ProductDetail.as_view()),
	url(r'^stores/(?P<pk>[0-9]+)/orders/$', ProductDetail.as_view())

]