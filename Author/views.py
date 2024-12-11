from django.shortcuts import render, redirect, get_object_or_404

from Author.forms import AuthorForm, EditAuthorForm
from Author.models import Author


def index(request):
    return render(request, 'index.html')


def author_create(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = AuthorForm()

    context = {'form': form}

    return render(request, 'create-author.html', context)


def author_details(request):
    author = Author.objects.first()
    context = {'author': author}
    return render(request, 'details-author.html', context)


def author_edit(request):
    author = Author.objects.first()
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('author_details')

    else:
        form = EditAuthorForm(instance=author)

    context = {'form': form}
    return render(request, 'edit-author.html', context)


def author_delete(request):
    author = Author.objects.first()
    if request.method == 'POST':
        author.delete()
        return redirect('index')

    context = {'author': author}

    return render(request, 'delete-author.html', context)

