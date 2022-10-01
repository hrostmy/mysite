from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import PostForm
from django.views.generic import UpdateView, DeleteView
from .models import Post


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