from django.conf.urls.defaults import *

urlpatterns = patterns('posts.views',
    (r'^$', 'posts'),
    (r'(?P<post_id>\d+)$', 'post'),
)
