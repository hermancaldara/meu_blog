from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings


admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^', include('posts.urls')),
    (r'^site_media/(.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
)
