from django.contrib import admin
from learning_logs.models import Topic, Entry

# Register your models here.
# 注册自己的模型

admin.site.register(Topic)
admin.site.register(Entry)