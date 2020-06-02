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
        types_dict = {
            'repair': Asset.ON_REPAIR,
            'service': Asset.ON_REPAIR,
            'upgrade': Asset.RETIRED,
        }
        asset.status = types_dict[type]
        asset.save()
        serializer = self.serializer_class(res)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, request):
        instance = self.get_object()
        asset = instance.asset
        asset.status = Asset.ASSIGNED
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
