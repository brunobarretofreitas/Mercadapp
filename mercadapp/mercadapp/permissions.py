from rest_framework import permissions
from django.contrib.auth.models import Group

class IsStoreAdmin(permissions.BasePermission):
	message = "You are not using a Store Admin account"
	
	def has_permission(self,request,view):
		return request.user.groups.filter(name="store_owner").count() > 0

class IsClient(permissions.BasePermission):
	message = "You are not using a client account"

	def has_permission(self,request,view):
		return request.user.groups.filter(name="client").count() > 0