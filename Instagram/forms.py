from django import forms
from .models import UserInfo, Post


class LoginForm(forms.Form):
    model = UserInfo
    username = forms.CharField(widget=forms.TextInput({'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput({'placeholder': 'Password'}))


class RegisterForm(forms.Form):
    model = UserInfo
    name = forms.CharField(widget=forms.TextInput({'placeholder': 'Name'}))
    username = forms.CharField(widget=forms.TextInput({'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput({'placeholder': 'Password'}))


class PostForm(forms.Form):
    model = Post
    title = forms.CharField(min_length=1)
    image = forms.ImageField(required=True)
    description = forms.CharField(widget=forms.Textarea({'palceholder': 'Give description of your image'}))
