import os
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, render
from blog.forms.email_post_form import EmailPostForm
from blog.models.post import Post


def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id, status='publicado')
    sent = False

    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} recommendes you read {post.title}"
            message = f"Read {post.title} at {post_url}\n\n {cd['name']}\ 's comments: {cd['comments']}"
            send_mail(subject, message, os.environ.get('EMAIL'), [cd['to']])
            sent = True
    else:
        form = EmailPostForm()
    return render(request, 'blog/pages/share.html', {'post': post, 'form': form, 'sent': sent})