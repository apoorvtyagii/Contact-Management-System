from django.http import request
from django.urls import path
from django.conf.urls import url
from .views import *
from django.contrib import admin
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView

# homeClass = HomeClass()

urlpatterns = [
    path("login/", Login, name="login"),
    path("sign_up/", SignUp, name="signup"),
    path("logout/", Logout, name="logout"),

    
    path("my_directory/", MyDirectory, name="base"),
    path("my_directory/", MyDirectory, name="home"),

    path("add_contact/", AddContact, name="addcontact"),
    path("edit_contact/<contact_id>", EditContact, name="editcontact"),
    path("delete_contact/<contact_id>", DeleteContact, name="deletecontact"),
    path("my_directory/", MyDirectory, name="mydirectory"),
]
    