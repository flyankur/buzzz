from django.conf.urls import patterns, include, url
from django.conf.urls import handler404

import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('buzzz.views',
    # Examples:
    # url(r'^$', 'fingowebapp.views.home', name='home'),
    # url(r'^fingowebapp/', include('fingowebapp.foo.urls')),
    # url('^$', landing),
    url('^recorded/$', 'recorded'),
	)
