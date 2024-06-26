"""
URL configuration for jkphoto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import (
    homeView,
    aboutView
)
from django.contrib.sitemaps.views import sitemap
from .sitemaps import staticViewSitemap
from album.sitemaps import albumSiteMap
from subscriber.sitemaps import subscriberSiteMap

sitemaps = {
    'static': staticViewSitemap,
    'albums': albumSiteMap,
    'subscribe': subscriberSiteMap
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homeView,name='home'),
    path('about/',aboutView,name='about'),
    path('albums/',include('album.urls')),
    path('',include('subscriber.urls')),
    path("sitemap.xml",sitemap,{"sitemaps": sitemaps},
    name="django.contrib.sitemaps.views.sitemap")
]
