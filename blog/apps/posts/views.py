from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Post

def post(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render_to_response(
        'post.html',
        {'post': post},
        context_instance = RequestContext(request),
    )

def posts(request):
    posts = Post.objects.all()
    return render_to_response(
        'posts.html',
        {'posts': posts},
        context_instance = RequestContext(request),
    )
