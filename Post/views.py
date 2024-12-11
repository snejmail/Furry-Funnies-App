from django.shortcuts import render, redirect, get_object_or_404

from Author.models import Author
from Post.forms import PostForm, DeletePostForm
from Post.models import Post


def dashboard(request):
    author = Author.objects.first()
    posts = Post.objects.all()
    context = {
        'posts': posts,
        'author': author,
    }

    return render(request, 'dashboard.html', context)


def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)

            if request.user.is_authenticated:
                author = Author.objects.filter(user=request.user).first()
                if author is None:
                    author = Author(user=request.user)
                    author.save()
                post.author = author
            else:
                author = Author.objects.first()
                post.author = author

            post.save()
            return redirect('dashboard')
    else:
        form = PostForm()

    return render(request, 'create-post.html', context={'form': form})


def post_details(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'details-post.html', {'post': post})


def post_edit(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = PostForm(instance=post)

    return render(request, 'edit-post.html', {'form': form, 'post': post})


def post_delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == "POST":
        post.delete()
        return redirect('dashboard')

    form = DeletePostForm(instance=post)

    return render(request, 'delete-post.html', {'form': form, 'post': post})

