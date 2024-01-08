from . import views
from django.urls import path

urlpatterns = [
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('forms',views.forms,name='forms'),
    path('success',views.success,name='success'),
    path('email',views.email,name='email'),
    path('logged',views.logged,name='logged')



]