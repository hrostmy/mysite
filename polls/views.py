from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegistrationForm
from polls.forms import SignInForm


def index(request):
    return render(request, 'polls/index.html')


def main_page(request):
    return HttpResponse('<h1>Головна сторінка</h1>')


def sign_in_view(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
            if user:
                login(request, user)
                return redirect('index')

    form = SignInForm()
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
            return render(request, 'polls/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'polls/register.html', {'user_form': user_form})


@login_required
def profile(request, username: str):
    user_profile = User.objects.filter(username=username).first()
    if user_profile:
        return render(request, 'polls/profile.html', {'user_profile': user_profile})
    else:
        return HttpResponse('This user is not created')
