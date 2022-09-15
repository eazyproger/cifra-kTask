from rest_framework import generics

from .models import News, NewsType
from .serializers import NewsSerializer, NewsTypeSerializer


class NewsList(generics.ListCreateAPIView):
    serializer_class = NewsSerializer

    def get_queryset(self):
        queryset = News.objects.all()
        news_type = self.request.query_params.get('news_type')
        if news_type is not None:
            queryset = queryset.filter(newsType=news_type)
        return queryset


class NewsDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NewsSerializer
    queryset = News.objects.all()


class NewsTypeList(generics.ListCreateAPIView,):
    serializer_class = NewsTypeSerializer
    queryset = NewsType.objects.all()


class NewsTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NewsTypeSerializer
    queryset = NewsType.objects.all()
