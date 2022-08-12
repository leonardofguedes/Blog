from django.contrib.sitemaps import Sitemap
from blog.models.post import Post


class PostSitemap(Sitemap):
    changefreq = 'weekly'
    pririty = 0.9

    def items(self):
        return Post.published.all()

    def lastmod(self, obj):
        return obj.update
