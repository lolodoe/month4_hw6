from django.shortcuts import render

from posts.models import Post


def main(request):
    posts = Post.objects.all()

    data = {
        'posts': posts
    }

    return render(request, 'main.html', context=data)

