from django.conf.urls import patterns, url, include
from django.contrib.auth.decorators import login_required
from zadanie import views

urlpatterns = patterns('',
    url(r'^index/$', views.index, name='index'),
)