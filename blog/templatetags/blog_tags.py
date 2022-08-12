from django import template
from blog.models.post import Post

register = template.Library()


@register.simple_tag
def total_posts():
    return Post.published.count()


@register.inclusion_tag('blog/partials/latest_post.html')
def show_latest_post(count=3):
    latest_post = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_post}