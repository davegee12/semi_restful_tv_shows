from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^shows$', views.index),
    url(r'^shows/new$', views.add_show),
    url(r'^shows/(?P<id>\d+)$', views.view_show),
    url(r'^shows/(?P<id>\d+)/edit$', views.edit_show),
    url(r'^create_show$', views.create_show),
    url(r'^update_show$', views.update_show),
    url(r'^shows/(?P<id>\d+)/destroy$', views.destroy_show),
]