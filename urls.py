from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
                        {'document_root': settings.MEDIA_ROOT }),

    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),

    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^phorms/', include('drchrono.phorms.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
