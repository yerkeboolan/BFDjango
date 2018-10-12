
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404

import datetime
from datetime import timedelta
from .models import Comment, Posts
from .forms import PostForm, CommentForm


def post_list(request):
    post_list = [i for i in Posts.objects.all()]
    context = {
        'post_list': post_list
    }
    return render(request, 'Post/post_list.html', context)


def post_detail(request, id):
    try:
        post = Posts.objects.get(pk=id)
    except Posts.DoesNotExist:
        raise Http404("Post was not found")
    context = {
        'posts': post
    }
    return render(request, 'Post/post_details.html', context)

def new_post(request):
    form = PostForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('post_list')
    context = {
        'form': form
    }
    return render(request, 'Post/post_form.html', context)

def update_post(request, id):
    updated_post = get_object_or_404(Posts, id=id)
    form = PostForm(request.POST or None, instance=updated_post)
    if form.is_valid():
        form.save()
        return redirect(post_list)
    return render(request, 'Post/post_form.html', {'form': form})

def delete_post(request, id):
    deleted_post = Posts.objects.get(pk=id)
    deleted_post.delete()
    return redirect(post_list)

def delete_all_posts(request):
    all_posts = Posts.objects.all()
    all_posts.delete()
    return redirect(post_list)

def create_comment(request, id):
    post = get_object_or_404(Posts, pk=id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save()
            comment.post = post
            comment.save()
            return redirect('post_list')
    else:
        form = CommentForm
    context = {
        'form': form
    }
    return render(request, 'Comment/add_comment.html', context)