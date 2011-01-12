from models import Post


def pegar_todas_tags():
    tags = list()
    posts = Post.objects.all()
    for post in posts:
        for tag in post.tags.iterator():
            tags.append(tag.name)
    tags = list(set(tags))
    tags.sort()
    return tags
