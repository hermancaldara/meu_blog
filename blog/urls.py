from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings
from django.views.generic.simple import direct_to_template


admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^', include('apps.posts.urls')),
    (r'^comentarios/', include('django.contrib.comments.urls')),
    (r'^contato/', include('apps.contato.urls')),
    (r'^sobre/', direct_to_template, {'template': 'sobre.html'}),
    (r'^js/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'templates/js'}),
    (r'^site_media/(.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
)
