from rest_framework import serializers
from .models import News, NewsType


class NewsTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsType
        fields = ('name', 'color')


class CreateNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('__all__')


class ListNewsSerializer(serializers.ModelSerializer):
    news_type_name = serializers.CharField(source='news_type.name', read_only=True)
    news_type_color = serializers.CharField(source='news_type.color', read_only=True)

    class Meta:
        model = News
        fields = ('name', 'short_description', 'news_type_name', 'news_type_color')


class RetrieveNewsSerializer(serializers.ModelSerializer):
    news_type_name = serializers.CharField(source='news_type.name', read_only=True)
    news_type_color = serializers.CharField(source='news_type.color', read_only=True)

    class Meta:
        model = News
        fields = ('name', 'short_description', 'full_description', 'news_type_name', 'news_type_color')
