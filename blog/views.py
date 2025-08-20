"""
blogアプリ
表示用の機能作成

Filename:views.py
Date:2025/6/18
Written by Sho Yamada

"""
from django.shortcuts import render
from django.views.generic import View, DetailView
from django.utils import timezone
from .models import Post

class PostListView(View):
    def get(self, request, *args, **kwargs):
        """
        Get request用の処理
        ブログ記事一覧を表示する
        """
        context = {}
        # 記事データを取得
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
        context['posts'] = posts
        return render(request, "blog/post_list.html", context)

post_list = PostListView.as_view()

class PostDetailView(DetailView):
    model = Post # 詳細を表示させたいモデルのクラス名を指定。今回はPost
    template_name = "blog/post_detail.html" # 表示するときに使用するテンプレートの名前。

post_detail = PostDetailView.as_view()
