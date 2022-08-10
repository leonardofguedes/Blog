from django.shortcuts import render, get_object_or_404
from blog.models import Post


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                             status='publicado',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    return render(request, 'blog/pages/detail.html', {'post': post})