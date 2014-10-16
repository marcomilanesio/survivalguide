from __future__ import absolute_import
from django.conf.urls import patterns, url, include
from . import views


lists_patterns = patterns(
    '',
    url(r'^$', views.EstateListListView.as_view(), name='list'),
    url(r'^d/(?P<slug>[-\w]+)/$', views.EstateListDetailView.as_view(),
    name='detail'),
    url(r'^create/$', views.EstateListCreateView.as_view(),
    name='create'),
    url(r'^update/(?P<slug>[-\w]+)/$', views.EstateListUpdateView.as_view(),
    name='update'),
)

urlpatterns = patterns(
    '',
    url(r'^elists/', include(lists_patterns, namespace='elists')),
)
