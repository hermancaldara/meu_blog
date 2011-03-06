from django.db import models
from django.db.models import signals
from django.core.urlresolvers import reverse
from django.conf import settings
from django.template.defaultfilters import slugify

from datetime import datetime
from taggit.managers import TaggableManager


class Post(models.Model):

    class Meta:
        ordering = ('-publicacao',)

    titulo = models.CharField(max_length=100)
    conteudo = models.TextField()
    publicacao = models.DateTimeField(
        default = datetime.now,
        blank = True,
    )
    tags = TaggableManager(blank=True)
    slug = models.SlugField(max_length=100, blank=True, unique=True)

    def __unicode__(self):
        return self.titulo
        
    def get_absolute_url(self):
        return reverse('apps.posts.views.post', kwargs={'slug': self.slug})


def post_pre_save(signal, instance, sender, **kwargs):
    if not instance.slug:
        slug = slugify(instance.titulo)
        novo_slug = slug
        contador = 0
        while Post.objects.filter(slug=novo_slug).exclude(id=instance.id).count() > 0:
            contador += 1
            novo_slug = '%s-%d'%(slug, contador)
        instance.slug = novo_slug


signals.pre_save.connect(post_pre_save, sender=Post)
