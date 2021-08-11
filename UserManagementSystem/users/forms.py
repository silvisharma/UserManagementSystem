from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from .models import Blog


class SignUpForm(UserCreationForm):
    fullname = forms.CharField(label="Full name")

    class Meta:
        model = User
        fields = ['username', 'fullname', 'email']
        labels = {'email': 'Email', 'password2': 'Confirm Password'}



class EditUserForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'date_joined', 'last_login']
        labels = {'email': 'Email'}


class EditAdminForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'last_login', 'groups', 'user_permissions',
                  'is_superuser', 'is_active', 'date_joined']
        labels = {'email': 'Email'}


class UpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'is_superuser', 'groups', 'user_permissions']
        labels = {'email': 'Email'}


class PostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.Textarea(attrs={'cols': 90, 'rows': 1}))
    desc = forms.CharField(label='Description', widget=forms.Textarea(attrs={'cols': 90, 'rows': 8}))

    class Meta:
        model = Blog
        fields = ['title', 'desc']

