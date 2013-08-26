from django.conf.urls import patterns, include, url
from iw.views import TasksView
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url('^$', 'bda.iw.views.Index'),
                       url(r'^index/$', 'bda.iw.views.Index'),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^register/$', 'bda.iw.views.Register'),
                       url(r'^blog/$', 'bda.iw.views.Blog'),
                       url(r'^control/$', 'bda.iw.views.Control'),
                       url(r'^calendar$', TasksView.as_view(), name='tasks-list'),
                       url(r'^article/$', 'bda.iw.views.Article'))
