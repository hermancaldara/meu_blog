# -*- coding: utf-8 -*-

from django.contrib.syndication.feeds import Feed
from models import Post


class UltimosPosts(Feed):
    title = 'Últimos posts do blog'
    link = '/'
    
    def items(self):
        return Post.objects.all()
