"""blog URL Configuration

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
#import view
from django.contrib import admin
from django.urls import include
from django.conf.urls import url
from news.views import author
from news.views import add_news


urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^news/', include('news.urls'), name='news-page'),
    url(r'^autor=(?P<name>[0-9]+)$', author, name='concrete_author'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^accounts/profile/', include('news.urls')),
    url(r'^/?$', include('users.urls')),
    url(r'^news/add/$', add_news,name='add_news'),



]
