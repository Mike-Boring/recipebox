"""recipebox URL Configuration
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
from django.urls import path

from homepage.views import index, author_detail, recipe_detail, recipe_form_view, author_form_view

from homepage import views

urlpatterns = [
    path('', index, name="homepage"),
    path('recipe/<int:recipe_id>/', views.recipe_detail, name="recipeview"),
    path('newrecipe/', views.recipe_form_view, name="newrecipe"),
    path('newauthor/', views.author_form_view, name="newauthor"),
    path('author/<int:author_id>/', views.author_detail, name="authorview"),
    path('login/', views.login_view, name="loginview"),
    path('signup/', views.signup_view, name="signupview"),
    path('logout/', views.logout_view, name="logoutview"),
    path('admin/', admin.site.urls),
]
