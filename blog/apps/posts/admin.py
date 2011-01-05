from django.contrib import admin
from models import Post, Imagem


class PostAdmin(admin.ModelAdmin):

    class Media:
        
        js = ('/js/tiny_mce/tiny_mce.js', '/js/textareas.js')

admin.site.register(Post, PostAdmin)
admin.site.register(Imagem)
