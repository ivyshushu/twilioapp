from django.conf.urls import patterns, url

from sms import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^send/$', views.send, name='send')
)