from .models import Post
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage

def get_posts(query_params=None):
    qs = Post.objects.select_related("author").all()
    if not query_params:
        return qs
    
    author_id = query_params.get("author_id")
    if author_id:
        qs = qs.filter(author_id=author_id)
    
    search = query_params.get("search")
    if search:
        qs = qs.filter(title__icontains=search) | qs.filter(content__icontains=search)
   
    ordering = query_params.get("ordering")
    if ordering:
        qs = qs.order_by(ordering)
    return qs

def get_post_by_id(pk):
    return get_object_or_404(Post, pk=pk)

def create_post(**kwargs):
    return Post.objects.create(**kwargs)

def update_post(instance, **kwargs):
    for k, v in kwargs.items():
        if k in ("title", "content"):
            setattr(instance, k, v)
    instance.save()
    return instance

def delete_post(instance):
    instance.delete()
