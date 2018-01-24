"""biblioteka2 URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from shelf.views import AutorListView, AutorDetailView
from contact.views import MessageAddView

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^autor/$', AutorListView.as_view(), name='autor-list'),
    url(r'^autor/(?P<pk>\d+)/$', AutorDetailView.as_view(), name= 'autor-detail'),
    url(r'^contact$', MessageAddView.as_view()),
]
