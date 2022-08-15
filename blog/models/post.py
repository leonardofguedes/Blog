from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='publicado')


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
    objects = models.Manager()
    published = PublishedManager()
    cover = models.ImageField(upload_to='blog/photos/%Y/%m/%d/', blank=True, default='')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', args=[self.publish.year,
                                       self.publish.month,
                                       self.publish.day,
                                       self.slug])

    tags = TaggableManager()
