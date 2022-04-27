from django.db import models
from django.utils import timezone


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200, unique=True)
    pub_date = models.DateTimeField('date published')
    content = models.TextField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    Article = models.ForeignKey(Article, on_delete=models.CASCADE)
    c_content = models.TextField()
    c_time = models.DateTimeField('date published',default=timezone.now())

    def __str__(self):
        return self.c_content
