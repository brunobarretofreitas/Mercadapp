from rest_framework.permissions import BasePermission
from django.contrib.auth.models import Group

class IsStoreAdmin(BasePermission):
	def has_permission(self,request,view):
		return request.user.groups.filter(name="store_owner").count() > 0