from django.urls import path
from . import views

urlpatterns = [
    # 主页
    path("", views.index, name='index'),

    # 显示所有主题
    path("topics/", views.topics, name='topics'),

    path("topics/<int:topic_id>/", views.topic, name='topic'),
]
