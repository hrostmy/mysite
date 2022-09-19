from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import PostForm
# Create your views here.
from .models import Post


def create(request):
    error = None
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = Post.objects.create(photo=form.data['photo'] if form.data['photo'] else None,text=form.data['text'], author=request.user)
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