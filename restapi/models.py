from django.db import models

# Create your models here.

# 测试blog的model类
class Blog(models.Model):

    title = models.CharField(max_length = 50 )
    content = models.TextField()