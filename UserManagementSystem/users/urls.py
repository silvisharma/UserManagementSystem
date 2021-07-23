from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy
from django.views.generic.base import RedirectView

urlpatterns = [
    # path('', RedirectView.as_view(url=reverse_lazy('admin:index'))),
    path('', views.base, name='base'),
    path('register/', views.index, name='register'),
    path('login/', views.user_login, name='login'),
    path('home/', views.home, name='home'),
    path('logout/', views.user_logout, name='logout'),
    path('changepass/', views.change_pass, name='changepass'),
    path('changepwd/', views.change_pwd, name='changepwd'),
    path('userdetail/<int:id>', views.user_detail, name='detail'),
    path('show/', views.user_display, name='show'),
    path('profile/', views.edit_profile, name='profile'),
    path('delete/<int:id>', views.user_delete, name='deleteuser'),
    path('<int:id>', views.user_edit, name='edituser'),
    path('add/', views.user_add, name='adduser'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='forgotpassword/password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='forgotpassword/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='forgotpassword/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='forgotpassword/password_reset_complete.html'), name='password_reset_complete'),
    path('addpost/', views.add_post, name='addpost'),
    path('editpost/<int:id>', views.edit_post, name='editpost'),
    path('delpost/<int:id>', views.delete_post, name='delpost'),
]


