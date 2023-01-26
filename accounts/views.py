from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect

from post.models import Post
from .forms import UserRegistrationForm
from .models import User


def index(request):
    return render(request, 'accounts/index.html')


def main_page(request):
    return HttpResponse('<h1>Головна сторінка</h1>')


def sign_in_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user:
            login(request, user)
            return redirect('index')

    form = AuthenticationForm()
    return render(request, 'accounts/sign_in.html', {'form': form})


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


def feed(request, username: str = None):
    if username:
        feed = Post.objects.filter(author__in=User.objects.filter(followers__username=username)).order_by('id')
    else:
        feed = Post.objects.all()
    return render(request, 'accounts/index.html', {'feed': feed[::-1]})


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


def logout_view(request):
    logout(request)
    return redirect('sign_in')


def followers_and_followed(request, username: str):
    if request.path.find('followers')!=-1:
        return render(request, 'accounts/followers_and_followed.html',
                      {'users': User.objects.filter(username=username).first().followers.all(), 'title': 'Followers'})
    elif request.path.find('followed')!=-1:
        return render(request, 'accounts/followers_and_followed.html',
               {'users': User.objects.filter(followers__username=username), 'title': 'Followed'})