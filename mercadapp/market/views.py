# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status

from django.shortcuts import render
from .serializers import StoreSerializer, StoreInformationsSerializer
from .models import Store

# Create your views here.

#class StoreListView(APIView):
#	serializer_class = StoreSerializer
#	def get(self, request, format=None):
#		serializer = self.serializer_class(Store.objects.all(), many=True)
#		return Response(serializer.data)

@api_view(['GET', 'POST'])
@permission_classes((AllowAny,))
def list_or_create_stores(request, format=None):
	if request.method == 'GET':
		stores = Store.objects.all()
		serializer = StoreSerializer(stores, many=True)
		return Response(serializer.data)
	elif request.method == 'POST':
		serializer = StoreInformationsSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes((AllowAny,))
def list_stores_to_deliver(request, user_location, format=None):
	stores = Store.objects.all()


@api_view(['GET'])
@permission_classes((AllowAny,))
def store_informations(request, pk, format=None):
	try:
		store = Store.objects.get(pk=pk)
	except Store.DoesNotExist:
		return Response(status=404)
	content = {
		'store': StoreInformationsSerializer(store).data
	}
	return Response(content)

