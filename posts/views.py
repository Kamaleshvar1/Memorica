from django.shortcuts import render, redirect
from .forms import PostCreateForm, CommentForm
from django.contrib.auth.decorators import login_required
from .models import Post
from django.shortcuts import get_object_or_404
from django.http import JsonResponse


# Create your views here.

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostCreateForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.user = request.user
            new_item.save()
            return redirect('feed')
    else:
        form = PostCreateForm(data=request.GET)
    return render(request, 'posts/create.html', {'form': form})


@login_required
def feed(request):
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            post_id = request.POST.get('post_id')
            post = get_object_or_404(Post, id=post_id)
            new_comment.post = post
            new_comment.posted_by = request.user.username
            new_comment.save()
            return redirect('feed')
    else:
        comment_form = CommentForm()

    posts = Post.objects.all().order_by('-created')
    logged_user = request.user

    return render(request, 'posts/feed.html', {
        'posts': posts,
        'logged_user': logged_user,
        'comment_form': comment_form
    })


def like_post(request):
    post_id = request.POST.get('post_id')
    post = get_object_or_404(Post, id=post_id)
    if post.liked_by.filter(id=request.user.id).exists():
        post.liked_by.remove(request.user)
        liked = False
    else:
        post.liked_by.add(request.user)
        liked = True
    return JsonResponse({'liked': liked, 'likes_count': post.liked_by.count()})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'posts/post_detail.html', {'post': post})
