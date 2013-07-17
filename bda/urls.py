from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       url('^$', 'bda.iw.views.Index'),
                       url(r'^index/$', 'bda.iw.views.Index'),
                       url(r'^index2/$', 'bda.iw.views.Index2'),
                       url(r'^co/$', 'bda.iw.views.Co'),
                       url(r'^register/$', 'bda.iw.views.Register'),
                       url(r'^blog/$', 'bda.iw.views.Blog'),
                       url(r'^control/$', 'bda.iw.views.Control'),
                       url(r'^article/$', 'bda.iw.views.Article'))
