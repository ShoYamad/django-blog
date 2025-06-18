"""
blogアプリ
URL定義

Filename:urls.py
date:2025.6.18
Written by Sho Yamada

"""
from django.urls import path
from . import views

app_name = 'blog' # アプリケーション名
urlpatterns = [
    path('', views.post_list, name='post_list'),
]
