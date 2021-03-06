from rest_framework import serializers

from .models import Asset, Request


class AssetSerializer(serializers.ModelSerializer):
    owner = serializers.CharField()
    type = serializers.CharField(source='get_type_display')
    status = serializers.CharField(source='get_status_display')

    class Meta:
        model = Asset
        fields = '__all__'


class RequestSerializer(serializers.ModelSerializer):
    author = serializers.CharField()
    asset = serializers.CharField()

    class Meta:
        model = Request
        fields = '__all__'
