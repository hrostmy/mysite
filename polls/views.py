from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse

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
