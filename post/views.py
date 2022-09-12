from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import PostForm
# Create your views here.
@login_required
def create(request):
    error = ''
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')
        else:
            error = 'Uncorrect form'
    form = PostForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'post/post_create.html')