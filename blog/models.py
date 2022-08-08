from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    STATUS = (
        ('não-publicado', 'Não-publicado'),
        ('publicado', 'Publicado')
    )
    title = models.CharField(max_length=60)
    slug = models.SlugField(max_length=60, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=15, choices=STATUS, default='não-publicado')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title