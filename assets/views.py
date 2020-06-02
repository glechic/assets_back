from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

from .serializers import AssetSerializer, RequestSerializer
from .models import Asset, Request


class AssetViewSet(viewsets.ModelViewSet):
    serializer_class = AssetSerializer
    queryset = Asset.objects.all()

    def get_queryset(self):
        user = self.request.user
        isAdmin = user.groups.filter(name='admin').exists()
        return Asset.objects.all() if isAdmin else user.asset_set.all()


class RequestViewSet(viewsets.ModelViewSet):
    serializer_class = RequestSerializer
    queryset = Request.objects.all()

    def create(self, request):
        type = request.data['type']
        asset = get_object_or_404(Asset.objects.all(), pk=request.data['asset_id'])
        res = Request(**{
            'asset': asset,
            'author': request.user,
            'title': f'<{asset.name}> - {type}',
            'description': f'Asset <{asset.name}> requested to {type}',
        } )
        res.save()
        serializer = self.serializer_class(res)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
