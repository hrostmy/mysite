from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import UpdateView, DeleteView, DetailView

from accounts.models import User
from .forms import PostForm
from .models import Post
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect


def create(request):
    error = None
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = Post.objects.create(photo=form.data['photo'] if form.data['photo'] else None, text=form.data['text'],
                                       author=request.user)
            post.save()
            return redirect('index')
        else:
            error = 'Uncorrect form'
    form = PostForm()

    data = {
        'form': form,
    }
    if error:
        data['error'] = error

    return render(request, 'post/post_create.html', context=data)


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'post/post_update.html'

    fields = ['photo', 'text']

    # form_class = PostForm


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post/post_delete.html'
    success_url = '/'

    fields = ['photo', 'text']


class PostDetailView(DetailView):
    model = Post
    template_name = 'post/detail_view.html'
    context_object_name = 'post_view'


def like_view(request, pk):
    post = get_object_or_404(Post, id=pk)
    if request.user not in post.likes.all():
        post.likes.add(request.user)
    else:
        post.likes.remove(request.user)
    return redirect(to='post_detail', **{'pk': pk})
