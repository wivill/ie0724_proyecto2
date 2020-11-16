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
# from django.contrib.auth import views as auth_views
from django.urls import path
from citas import views as base_views
from accounts import views as auth_views
# from django.conf.urls import url
from django.views.generic.base import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('new_user/', views.new_user, name="new_user"),
    path('show_user/', views.show_user, name="show_user"),
    path('show_user/<int:pk>', views.show_user, name="show_user"),
    path('new_appointment/', views.new_appointment, name="new_appointment"),
    path('new_appointment/<str:name>', views.new_appointment, name="new_appointment"),
    path('show_appointments/', views.show_appointments, name="show_appointments"),
    path('show_appointments/<str:name>', views.show_appointments, name="show_appointments"),
    path('new_stylist/', views.new_stylist, name="new_stylist"),
    path('show_stylist/', views.show_stylist, name="show_stylist"),
    path('show_stylist/<str:name>', views.show_stylist, name="show_stylist"),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('login/', auth_views.login, name='login'),
    path('logout/', auth_views.logout, name='logout'),
    path('signup/', auth_views.signup, name='signup'),
]
