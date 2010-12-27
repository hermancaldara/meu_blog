from django.db import models
from datetime import datetime
from taggit.managers import TaggableManager

class Post(models.Model):

    titulo = models.CharField(max_length=100)
    conteudo = models.TextField()
    publicacao = models.DateTimeField(
        default = datetime.now,
        blank = True,
    )
    tags = TaggableManager()

    def __unicode__(self):
        return self.titulo
