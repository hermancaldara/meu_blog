from django.conf.urls.defaults import *

urlpatterns = patterns('apps.posts.views',
    (r'^$', 'posts'),
    (r'^post/(?P<slug>[\w_-]+)/$', 'post'),
    (r'^tag/(?P<tag>[\w_-]+)/$', 'posts_por_tag'),
    (r'^busca$', 'busca'),
)
