from django import template
from blog.models.post import Post

register = template.Library()


@register.simple_tag
def total_posts():
    return Post.published.count()