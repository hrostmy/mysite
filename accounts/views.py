from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView

from post.models import Post
from .forms import UserRegistrationForm
from .models import User


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            login(request, new_user)
            return render(request, 'accounts/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'user_form': user_form})


@login_required
def profile(request, username: str):
    user_profile = User.objects.filter(username=username).first()
    user_posts = Post.objects.filter(author__username=username)
    if user_profile:
        return render(request=request, template_name='accounts/profile.html',
                      context={
                          'user_profile': user_profile,
                          'user_posts': user_posts[::-1],
                          'followed': User.objects.filter(followers__username=user_profile.username).count()
                      })
    else:
        return HttpResponse('This user is not created')


class FeedListView(ListView):
    model = Post
    paginate_by = 5
    queryset = Post.objects.all().order_by('-id')
    template_name = 'accounts/index.html'

    def get_context_data(self, *, object_list=queryset, **kwargs):
        if username := self.kwargs.get('username'):
            if user := User.objects.filter(username=username).first():
                object_list = self.queryset.filter(author__in=user.followed)
        context = super().get_context_data(object_list=object_list, **kwargs)

        return context



@login_required
def follow(request, pk: int):
    if request.user.pk == pk:
        return redirect(to='profile', **{'username': request.user.username})
    followed = User.objects.get(pk=pk)
    if request.user not in followed.followers.all():
        followed.followers.add(request.user)
    else:
        followed.followers.remove(request.user)
    return redirect(to='profile', **{'username': followed.username})


def followers_and_followed(request, username: str):
    if request.path.find('followers') != -1:
        return render(request, 'accounts/followers_and_followed.html',
                      {'users': User.objects.filter(username=username).first().followers.all(), 'title': 'Followers'})
    elif request.path.find('followed') != -1:
        return render(request, 'accounts/followers_and_followed.html',
                      {'users': User.objects.filter(followers__username=username), 'title': 'Followed'})
