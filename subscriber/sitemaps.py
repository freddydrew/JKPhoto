from django.contrib import sitemaps

class subscriberSiteMap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = "weekly"

    def items(self):
        return ["/subscribe/","/unsubscribe/"]

    def location(self, item):
        return item