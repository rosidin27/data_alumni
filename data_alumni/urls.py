"""data_alumni URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from login import views as login_view
from index import views as index_view
from admin import views as admin_view
from alumni import views as alumni_view

urlpatterns = [
    path('',index_view.index),
    path('admin/', admin_view.index),
    path('alumni/', alumni_view.index),
    path('alumni/view/', alumni_view.view),
    path('alumni/password/', alumni_view.password),
    path('alumni/profil/', alumni_view.profil),
    path('admin/alumni/input/', admin_view.input),
    path('admin/alumni/view/', admin_view.view),
    path('admin/alumni/edit/', admin_view.edit),
    path('admin/password/', admin_view.password),
    path('login/', login_view.index),
    path('logout/', login_view.logout),
]
