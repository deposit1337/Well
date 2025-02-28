from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Item 


class StaticViewSitemap(Sitemap):
    priority = 1.0
    changefreq = 'daily'

    def items(self):
        return ['home_page']

    def location(self, item):
        return reverse(item)


class ProductSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Item.objects.all()

    def lastmod(self, obj):
        return obj.updated_at