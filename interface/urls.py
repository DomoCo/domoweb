from django.conf.urls import patterns, url

from interface import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)
