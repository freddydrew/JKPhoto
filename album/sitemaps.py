from django.contrib import sitemaps

class albumSiteMap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = "weekly"

    def items(self):
        return ["/albums/"]

    def location(self, item):
        return item