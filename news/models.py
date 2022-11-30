from django.db import models

# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=1000)
    author = models.CharField(null=True, max_length=1000)
    description = models.CharField(null=True, max_length=1000)
    url = models.CharField(max_length=1000)
    image_url = models.ImageField(upload_to='news_pics', max_length=1000)
    published_date = models.CharField(max_length=1000)
    content = models.TextField(null=True, max_length=100000)

    def __str__(self):
        return self.title