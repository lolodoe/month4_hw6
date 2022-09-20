from django.http import HttpResponse
from django.shortcuts import render

from posts.models import Post, Comment


def main(request):
    posts = Post.objects.all()

    data = {
        'posts': posts
    }

    return render(request, 'main.html', context=data)


def post_detail(request, id):
    post = Post.objects.get(id=id)
    comments = Comment.objects.filter(post=post)

    data = {
        'post': post,
        'comments': comments
    }

    return render(request, 'detail.html', context=data)
