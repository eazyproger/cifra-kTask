from django.db import models


class NewsType(models.Model):
    name = models.CharField(max_length=20)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class News(models.Model):
    name = models.CharField(max_length=50)
    short_description = models.CharField(max_length=100)
    full_description = models.TextField()
    news_type = models.ForeignKey(NewsType, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
