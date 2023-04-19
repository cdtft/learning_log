from django.urls import path
from . import views

urlpatterns = [
    # 主页
    path("", views.index, name='index'),
    # 显示所有主题
    path("topics/", views.topics, name='topics'),
    # 查询topic
    path("topics/<int:topic_id>/", views.topic, name='topic'),
    # 新建topic
    path("new_topic/", views.new_topic, name='new_topic'),
    # 添加新的条目
    path("new_entry/<int:topic_id>/", views.new_entry, name='new_entry'),
    # 编辑entry
    path("edit_entry/<int:entry_id>/", views.edit_entry, name='edit_entry')


]
