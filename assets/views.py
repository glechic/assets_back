from django.shortcuts import render
from rest_framework import viewsets

from .serializers import AssetSerializer, RequestSerializer
from .models import Asset, Request


class AssetViewSet(viewsets.ModelViewSet):
    serializer_class = AssetSerializer
    queryset = Asset.objects.all()


class RequestViewSet(viewsets.ModelViewSet):
    serializer_class = RequestSerializer
    queryset = Request.objects.all()
