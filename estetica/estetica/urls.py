"""estetica URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import path
from citas import views as base_views
from django.conf.urls import url, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('new/', base_views.new, name="new"),
    path('show/', base_views.show, name="show"),
    path('show/<int:pk>', base_views.show, name="show"),
    url(r'^$', base_views.home, name='home'),
    url(r'^login/$', auth_views.LoginView, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.LogoutView, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', base_views.signup, name='signup'),
]
