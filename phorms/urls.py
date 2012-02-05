from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
                       
    url(r'^login/$', 'drchrono.phorms.views.login_user'),
    url(r'^accounts/', 'django.contrib.auth.views.login'),

    url(r'^create/$', 'drchrono.phorms.views.create_form'),
    url(r'^list/$', 'drchrono.phorms.views.list_form'),
    url(r'^survey/(?P<survey_id>\d+)/$', 'drchrono.phorms.views.detail'),
    url(r'^preview/survey/(?P<survey_id>\d+)/$',
        'drchrono.phorms.views.preview'),                       

    url(r'^results/(?P<survey_id>\d+)/$', 'drchrono.phorms.views.results'),
)
