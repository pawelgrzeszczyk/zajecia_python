from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.template, name='template'),
    url(r'^hello/page(?P<num>[0-9]+)/$', views.page, name='page'),

]