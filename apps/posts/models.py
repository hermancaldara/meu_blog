from django.db import models
from datetime import datetime


class Post(models.Model):

    titulo = models.CharField(max_length=100)
    conteudo = models.TextField()
    publicacao = models.DateTimeField(
        default = datetime.now,
        blank = True,
    )
    
    def __unicode__(self):
        return self.titulo
