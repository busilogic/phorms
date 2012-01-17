from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                        {'document_root': settings.MEDIA_ROOT }),
    
    # Examples:
    # url(r'^$', 'drchrono.views.home', name='home'),
    url(r'^phorms/', include('drchrono.phorms.urls')),
    # url(r'^login/$', 'phorms.views.login_user'),
    # url(r'^create/$', 'phorms.views.create_form'),                       

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
