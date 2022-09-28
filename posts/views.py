from django.http import HttpResponse
from django.shortcuts import render, redirect

from posts.forms import PostForm
from posts.models import Post, Comment


def main(request):
    if request.method == 'GET':
        posts = Post.objects.all()

        data = {
            'posts': posts
        }

        return render(request, 'posts.html', context=data)


def post_detail(request, id):
    post = Post.objects.get(id=id)
    comments = Comment.objects.filter(post=post)

    data = {
        'post': post,
        'comments': comments
    }

    return render(request, 'detail.html', context=data)


def create_post(request):
    if request.method == "GET":
        return render(request, 'create_post.html', context={
            'post_form': PostForm
        })

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            Post.objects.create(
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description'),
                stars=form.cleaned_data.get('stars'),
                type=form.cleaned_data.get('type')
            )
            return redirect('/')
        else:
            return render(request, 'create_post.html', context={
                'post_form': form
            })
