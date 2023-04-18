from django.contrib import admin
from learning_logs.models import Topic, Entry

# Register your models here.

# 让Django通过管理网站管理我们的模型
admin.site.register(Topic)
admin.site.register(Entry)
