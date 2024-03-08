from django.contrib import sitemaps
from django.urls import reverse


class staticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = "weekly"

    def items(self):
        return ["home", "about"]

    def location(self, item):
        return reverse(item)