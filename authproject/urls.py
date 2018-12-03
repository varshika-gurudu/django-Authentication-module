"""authproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from authapp import views
from django.conf import settings
from django.contrib.auth.views import (PasswordResetView,
                                        PasswordResetDoneView,
                                        PasswordResetConfirmView,
                                        PasswordResetCompleteView)




urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',views.register,name = 'signup'),
    path('home/',views.login_view,name = 'home'),
    path('logout/',views.log_out,name = 'logout'),
    #path('^', include('django.contrib.auth.urls')),
    path('login/',views.index,name = 'login'),
    path(
        'password_reset/',PasswordResetView.as_view(),
        {'template_name':'password_reset_form.html'},
        name = 'password_reset'
        ),
    path(
        'password_reset/done/',PasswordResetDoneView.as_view(),
        {'template_name':'password_reset_done.html'},
         name='password_reset_done'
         ),
    path(
        'password_reset/confirm/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(),
        {'template_name':'password_reset_confirm.html'},
        name='password_reset_confirm'
        ),
    path(
        'reset/done/', PasswordResetCompleteView.as_view(),
        {'template_name':'password_reset_complete.html'},
        name='password_reset_complete'
        ),



]
