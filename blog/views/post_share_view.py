from django.shortcuts import get_object_or_404, render
from blog.forms.email_post_form import EmailPostForm
from blog.models import Post


def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id, status='publicado')

    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
        else:
            form = EmailPostForm()
    return render(request, 'blog/partials/share', {'post':post, 'form':form})