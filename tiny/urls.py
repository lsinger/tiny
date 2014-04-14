from django.conf.urls import patterns, include, url
from shorturls.views import LinkCreate

urlpatterns = patterns('',
    url(r'^$', LinkCreate.as_view(), name="home"),
)
