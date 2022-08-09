from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def post_list(request):
    list = Post.published.all()
    paginator = Paginator(list, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request,
                  'blog/pages/list.html',
                  {'posts': posts,
                   'page':page})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                             status='publicado',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    return render(request, 'blog/pages/detail.html', {'post': post})




