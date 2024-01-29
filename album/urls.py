from django.urls import path

from .views import (
    oneAlbumView,
    allAlbumsView
)

app_name = 'album'
urlpatterns = [
    path('',allAlbumsView,name='allAlbums'),
    path('<slug:slug>/',oneAlbumView,name='oneAlbum')
]