from django.urls import path
from .views import NewsList, NewsTypeList, NewsDetail, NewsTypeDetail

urlpatterns = [
    path('news/', NewsList.as_view()),
    path('news/<int:pk>', NewsDetail.as_view()),
    path('news-types/', NewsTypeList.as_view()),
    path('news-types/<int:pk>', NewsTypeDetail.as_view()),
]
