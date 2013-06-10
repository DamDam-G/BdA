from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       url('^$', 'bda.iw.views.Index'),
                       url(r'^index/$', 'bda.iw.views.Index'),
                       url(r'^co/$', 'bda.iw.views.Co'),
                       url(r'^blog/$', 'bda.iw.views.Blog'),
                       url(r'^article/$', 'bda.iw.views.Article'))
