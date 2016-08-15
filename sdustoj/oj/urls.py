from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^ojlist/','oj.views.state',name='adminform'),
    url(r'^info/(\d+)/','oj.views.info',name='info'),
]