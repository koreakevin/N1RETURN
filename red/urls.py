"""red URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
import velvet.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',velvet.views.layout, name="layout"),
    path('velvet/home/', velvet.views.home, name='home'),
    path('velvet/new/', velvet.views.new, name='new'),
    path('velvet/new/', velvet.views.create, name='create'),
    path('velvet/newblog/', velvet.views.blogform, name='newblog'),
    path('velvet/<int:pk>/edit/', velvet.views.edit, name='edit'),
    path('velvet/<int:pk>/remove/', velvet.views.remove, name='remove'),
    path('velvet/<int:blog_id>/comment_new/', velvet.views.comment_new, name='comment_new'),
    path('velvet/<int:comment_id>/comment_edit/', velvet.views.comment_edit, name='comment_edit'),
    path('velvet/<int:comment_id>/comment_delete/', velvet.views.comment_delete, name='comment_delete'),
]

