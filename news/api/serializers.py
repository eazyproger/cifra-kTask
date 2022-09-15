from rest_framework import serializers
from .models import News, NewsType


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('__all__')


class NewsTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsType
        fields = ('__all__')
