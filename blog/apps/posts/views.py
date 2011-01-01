from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Post

def pegar_todas_tags():
    tags = list()
    posts = Post.objects.all()
    for post in posts:
        for tag in post.tags.iterator():
            tags.append(tag.name)
    tags = list(set(tags))

    return tags

def post(request, post_id):
    tags = pegar_todas_tags() 
    post = Post.objects.get(pk=post_id)
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
