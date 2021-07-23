from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .forms import EditUserForm, EditAdminForm, UpdateForm, SignUpForm, PostForm
from django.contrib.auth.models import User, Group
from django.shortcuts import render, HttpResponseRedirect
from django.db import IntegrityError
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMessage
from .models import Blog


def home(request):
    if request.user.is_authenticated:
        posts = Blog.objects.all()
        if request.method == "POST":
            if request.user.is_superuser == True:
                f = EditAdminForm(request.POST, instance=request.user)
                users = User.objects.all()

            else:
                f = EditUserForm(request.POST, instance=request.user)
                users = None
            if f.is_valid():
                messages.success(request, 'Your Profile is updated')
                f.save()

        else:
            if request.user.is_superuser == True:
                f = EditAdminForm(instance=request.user)
                users = User.objects.all()
            else:
                f = EditUserForm(instance=request.user)
                users = None
        return render(request, 'home.html', {'name': request.user.username, 'form': f, 'users': users, 'posts': posts})
    else:
        return HttpResponseRedirect('/login/')


def user_permission(request):
    if request.user.is_authenticated:
        users = User.objects.all()
        return render(request, 'home.html', {'name': request.user.username}, {'users': users})
    else:
        return HttpResponseRedirect('/login/')


def base(request):
    return render(request, 'base.html')


def index(request):
    if request.method == 'POST':
        f = SignUpForm(request.POST)
        if f.is_valid():
            user = f.save()
            group = Group.objects.get(name='User')
            user.groups.add(group)
            html_template = 'registration/email.html'
            html_message = render_to_string(html_template, {'name': request.POST.get('username'),
                                                            'fullname': request.POST.get('fullname'),
                                                            'email': request.POST.get('email'),
                                                            })
            subject = 'You have successfully registered to User Management System'
            email_from = settings.EMAIL_HOST_USER
            to_list = [User.email, settings.EMAIL_HOST_USER]
            message = EmailMessage(subject, html_message, email_from, to_list)
            message.content_subtype = "html"
            message.send()
            messages.success(request, 'Congratulations! Your account is created successfully')
    else:
        f = SignUpForm()
    return render(request, 'registration/register.html', {"form": f})


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            f = AuthenticationForm(request=request, data=request.POST)
            if f.is_valid():
                username = request.POST['username']
                password = request.POST['password']
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in successfully')
                    return HttpResponseRedirect('/home/')
        else:
            f = UserCreationForm(request.POST)
            f = AuthenticationForm()
        return render(request, 'registration/login.html', {'form': f})
    else:
        return HttpResponseRedirect('/home/')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')


def change_pass(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            f = PasswordChangeForm(user=request.user, data=request.POST)
            if f.is_valid():
                f.save()
                update_session_auth_hash(request, f.user)
                messages.success(request, 'Your password is changed successfully')
                return HttpResponseRedirect('/home')
        else:
            f = PasswordChangeForm(user=request.user)
        return render(request, 'registration/changepass.html', {'form': f})

    else:
        return HttpResponseRedirect('/login/')


def change_pwd(request):
    if request.method == 'POST':
        f = SetPasswordForm(user=request.user, data=request.POST)
        if f.is_valid():
            f.save()
            update_session_auth_hash(request, f.user)
            messages.success(request, 'Your password is changed successfully')
            return HttpResponseRedirect('/home')
    else:
        f = SetPasswordForm(user=request.user)
    return render(request, 'registration/changepwd.html', {'form': f})


def user_detail(request, id):
    if request.user.is_authenticated:
        pi = User.objects.get(pk=id)
        f = EditAdminForm(instance=pi)
        return render(request, 'admin/detail.html', {'form': f})
    else:
        return HttpResponseRedirect('/login')


def user_display(request):
    from .models import ShowUser
    show = User.objects.all()
    return render(request, 'admin/showuser.html', {'ShowUser': show})


def user_edit(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        f = UpdateForm(request.POST, instance=pi)
        if f.is_valid():
            f.save()
            messages.success(request, 'The user is updated successfully')
            return HttpResponseRedirect('/show/')
    else:
        pi = User.objects.get(pk=id)
        f = UpdateForm(instance=pi)
    return render(request, 'admin/edituser.html', {'form': f})


def user_delete(request, id):
    if request.method == "POST":
        pi = User.objects.get(pk=id)
        pi.delete()
        messages.success(request, 'The user is deleted successfully')
        return HttpResponseRedirect('/show/')


def user_add(request):
    if request.method == 'POST':
        f = UpdateForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'The user is added successfully')
            return HttpResponseRedirect('/show/')
    else:
        f = UpdateForm()
    return render(request, 'admin/adduser.html', {'form': f})


def add_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                desc = form.cleaned_data['desc']
                post = Blog(title=title, desc=desc)
                post.save()
                messages.success(request, 'Post is added succesfully')
                return HttpResponseRedirect('/home/')
                form = PostForm
        else:
            form = PostForm()
        return render(request, 'blog/addpost.html', {'form': form})
    else:
        return HttpResponseRedirect('/login/')


def edit_post(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Blog.objects.get(pk=id)
            form = PostForm(request.POST, instance=pi)
            if form.is_valid():
                form.save()
                messages.success(request, 'Post is successfully updated')
                return HttpResponseRedirect('/home/')
        else:
            pi = Blog.objects.get(pk=id)
            form = PostForm(instance=pi)
        return render(request, 'blog/editpost.html', {'form': form})
    else:
        return HttpResponseRedirect('/login/')


def delete_post(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Blog.objects.get(pk=id)
            pi.delete()
            messages.success(request, 'Deleted Successfully')
            return HttpResponseRedirect('/home/')
    else:
        return HttpResponseRedirect('/login/')


def edit_profile(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            if request.user.is_superuser == True:
                f = EditAdminForm(request.POST, instance=request.user)
                users = User.objects.all()

            else:
                f = EditUserForm(request.POST, instance=request.user)
                users = None
            if f.is_valid():
                messages.success(request, 'Your profile is updated successfully')
                f.save()

        else:
            if request.user.is_superuser == True:
                f = EditAdminForm(instance=request.user)
                users = User.objects.all()
            else:
                f = EditUserForm(instance=request.user)
                users = None
        return render(request, 'registration/editprofile.html',
                      {'name': request.user.username, 'form': f, 'users': users})
    else:
        return HttpResponseRedirect('/login/')
