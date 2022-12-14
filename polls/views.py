from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.http import HttpResponse
from post.models import Post
from .forms import UserRegistrationForm
from polls.forms import SignInForm
from .models import User
from django.contrib.auth.forms import AuthenticationForm

def index(request):
    return render(request, 'polls/index.html')


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
    return render(request, 'polls/sign_in.html', {'form': form})


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
            return render(request, 'polls/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'polls/register.html', {'user_form': user_form})


@login_required
def profile(request, username: str):
    user_profile = User.objects.filter(username=username).first()
    user_posts = Post.objects.filter(author__username=username)
    if user_profile:
        return render(request, 'polls/profile.html', {'user_profile': user_profile, 'user_posts': user_posts[::-1]})
    else:
        return HttpResponse('This user is not created')


def feed_home(request):
    feed = Post.objects.all()
    return render(request, 'polls/index.html', {'feed': feed[::-1]})


# def profile(request):
#     user_posts = Post.objects.filter(user=request.user)
#     return render(request, 'profile.html', {'user_posts': user_posts[::-1]})

class PostDetailView(DetailView):
    model = Post
    template_name = 'post/detail_view.html'
    context_object_name = 'post_view'

    # def get_object(self, queryset=None):
    #     obj = super(PostDetailView, self).get_object(queryset)
    #     if obj:
    #         return obj
    #     else:
    #         return None
    #
    # def render_to_response(self, context, **response_kwargs):
    #     if context.get(self.context_object_name):
    #         return render(self.request, self.template_name, context)
    #     else:
    #         return HttpResponse('HAHHAHAAHHAHA LOOOOOOOOH')
    #

def logout_view(request):
    logout(request)
    return redirect('sign_in')
