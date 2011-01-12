from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import get_object_or_404
from models import Post
from utils import pegar_todas_tags


def post(request, slug):
    tags = pegar_todas_tags() 
    post = get_object_or_404(Post, slug=slug)

    return render_to_response(
        'post.html',
        {'post': post, 'tags': tags},
        context_instance = RequestContext(request),
    )

def posts(request):
    tags = pegar_todas_tags()
    posts = Post.objects.all()
    
    return render_to_response(
        'posts.html',
        {'posts': posts, 'tags': tags},
        context_instance = RequestContext(request),
    )
    
def posts_por_tag(request, tag):
    posts = Post.objects.filter(tags__name__in=[tag])

    return render_to_response(
        'posts_por_tag.html',
        {'posts': posts},
        context_instance = RequestContext(request),
    )
    
def busca(request):
    todos_posts = Post.objects.all()
    posts = []
    for post in todos_posts:
        try:
            if request.POST['busca'] != '':
                del request.session['busca']
                request.session['busca'] = request.POST['busca']
                if request.POST['busca'].lower() in post.conteudo.lower():
                    posts.append(Post.objects.get(id=post.id))
        except:
            if request.session['busca'].lower() in post.conteudo.lower():
                posts.append(Post.objects.get(id=post.id))

    return render_to_response(
        'busca.html',
        {'posts': posts},
        context_instance = RequestContext(request),
    )
