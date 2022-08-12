from django import template
from django.db.models import Count

from blog.models.post import Post

register = template.Library()


@register.simple_tag
def total_posts():
    return Post.published.count()


@register.inclusion_tag('blog/partials/latest_post.html')
def show_latest_post(count=3):
    latest_post = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_post}


@register.simple_tag
def get_most_commented_posts(count=3):
    return Post.published.annotate(
        total_comments=Count('comments')).order_by('-total_comments')[:count]
