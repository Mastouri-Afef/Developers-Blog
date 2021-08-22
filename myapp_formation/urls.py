"""projectweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from .views import (
     PostListView,
     PostDetailView,
     PostCreateView,
     PostUpdateView,
     PostDeleteView
     )
from . import views

urlpatterns = [
#as_view it's a method transform the class to a view we can see it
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    #if i want to see the blog one or two by details (pl hiya primary key (1,2..) 
    #after that we need a template to show all our posts details
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),#here we should know the"pk" because we gona know hwich id of post we gone modifie
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),

    #path('about/', views.AboutPageView.as_view(), name='about'),
]
#template with naming convention
#<app>/<model> <viewtype>.html
#donc myapp_foormation POst(model eli testena fih) and the view type is List
