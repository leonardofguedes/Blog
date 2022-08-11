from django.shortcuts import render, get_object_or_404
from blog.models.post import Post
from blog.forms.comment_form import CommentForm
from django.db.models import Count


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                             status='publicado',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    comments = post.comments.filter(active=True)
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()
    posts_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(tags__in=posts_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags', '-publish')[:4]
    return render(request, 'blog/pages/detail.html', {'post': post,
                                                          'comments':comments,
                                                          'new_comment': new_comment,
                                                          'comment_form': comment_form,
                                                          'similar_posts': similar_posts})