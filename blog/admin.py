"""
blogアプリ
admin用の設定

Filename:admin.py
Date: 2025/6/18
Written by Sho Yamada

"""
from django.contrib import admin
from .models import Post

admin.site.register(Post)
