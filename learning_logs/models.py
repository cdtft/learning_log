from django.db import models


# Create your models here.

class Topic(models.Model):
    """用户学习主题"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text
