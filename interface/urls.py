from django.conf.urls import patterns, url

from interface import views, ajax_views

urlpatterns = patterns('',
    url(r'^$', views.login),
    url(r'^tests/$', views.tests, name='tests'),
    url(r'^editor/$', views.editor, name='editor'),
    url(r'^play/$', views.index, name='index'),
    # Ajax network calls
    url(r'^info/cell/$', ajax_views.get_cells),
    url(r'^info/responses/([\w\d]+)/$', ajax_views.get_response_templates),
    url(r'^login/$', ajax_views.login),
)
