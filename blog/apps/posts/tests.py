from django.test import TestCase
from apps.posts.models import Post
from should_dsl import should
from utils import pegar_todas_tags


class TesteTags(TestCase):

    def setUp(self):
        self.primeiro_post = Post.objects.create()
        self.segundo_post = Post.objects.create()
        self.terceiro_post = Post.objects.create()
        
    def teste_pegar_todas_tags(self):
        self.primeiro_post.tags.set('python', 'django')
        self.segundo_post.tags.set('ruby', 'rails')
        self.terceiro_post.tags.set('php', 'miolo')
        pegar_todas_tags() |should| equal_to(
            ['django', 'miolo', 'php', 'python', 'rails', 'ruby']
       )
