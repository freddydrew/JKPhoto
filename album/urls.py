from django.urls import path

from .views import (
    oneAlbumView,
    allAlbumsView,
    albumSearchView
)

app_name = 'album'
urlpatterns = [
    path('search/',albumSearchView,name="search"),
    path('',allAlbumsView,name='allAlbums'),
    path('<slug:slug>/',oneAlbumView,name='oneAlbum')
]