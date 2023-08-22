from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from .serializers import *
from .models import *
from rest_framework import viewsets, filters, status, generics

class GatherItemView(viewsets.ModelViewSet):
    queryset = GatherItem.objects.all()
    serializer_class = GatherItemSerializer
    authentication_classes = []
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['created_at']