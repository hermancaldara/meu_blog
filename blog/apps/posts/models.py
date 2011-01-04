import markdown

from django.db import models
from django.conf import settings

from datetime import datetime
from taggit.managers import TaggableManager


def markdown_to_html( markdownText, images ):    
    image_ref = ""

    for image in images:
        image_url = settings.MEDIA_URL + image.imagem.url
        image_ref = "%s\n[%s]: %s" % ( image_ref, image, image_url )

    md = "%s\n%s" % ( markdownText, image_ref )
    html = markdown.markdown( md )
    return html


class Imagem(models.Model):

    class Meta:
        
        verbose_name_plural = 'Imagens'

    nome = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='imagens')
    
    def __unicode__(self):
        return self.nome
        

class Post(models.Model):

    class Meta:
        ordering = ('-publicacao',)

    titulo = models.CharField(max_length=100)
    conteudo = models.TextField()
    publicacao = models.DateTimeField(
        default = datetime.now,
        blank = True,
    )
    imagens = models.ManyToManyField(Imagem, blank=True)
    tags = TaggableManager()

    def __unicode__(self):
        return self.titulo
        
    def get_absolute_url(self):
        return '/%d' % self.id
        
    def body_html( self ):
        return markdown_to_html( self.conteudo, self.imagens.all() )  
