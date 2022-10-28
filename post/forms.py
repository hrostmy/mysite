from django.contrib.auth.forms import PasswordChangeForm
from .models import Post
from django.forms import ModelForm


class MyChangeFormPassword(PasswordChangeForm):
    pass


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['photo', 'text']
