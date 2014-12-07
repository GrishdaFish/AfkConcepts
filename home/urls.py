__author__ = 'Mark'
from django.conf.urls import patterns, url
from home import views

urlpatterns = patterns('',
                        url(r'^$', views.index, name='index'),
                        url(r'^index.html', views.index, name='index'),

                       )