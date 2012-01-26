from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^login/$', 'phorms.views.login_user'),
    url(r'^create/$', 'phorms.views.create_form'),
    url(r'^list/$', 'phorms.views.list_form'),
    url(r'^survey/(?P<survey_id>\d+)/$', 'phorms.views.detail'),                                            
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)
