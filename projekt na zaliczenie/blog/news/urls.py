from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.news_show_detail, name='news_show_detail'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.DeleteNews.as_view(), name="delete-news"),
    url(r'^search/', views.searching, name='blog_search'),

]