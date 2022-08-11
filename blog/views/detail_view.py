from django.shortcuts import render, get_object_or_404
from blog.models.post import Post
from blog.models.comment import Comment
from blog.forms.comment_form import CommentForm


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
    return render(request, 'blog/pages/detail.html', {'post': post,
                                                          'comments':comments,
                                                          'new_comment': new_comment,
                                                          'comment_form': comment_form})