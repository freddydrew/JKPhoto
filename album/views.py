from django.shortcuts import render

# Create your views here.
def oneAlbumView(request):
    context={}
    return render(request,"album/oneAlbum.html",context=context)

def allAlbumsView(request):
    context={}
    return render(request,"album/allAlbums.html",context=context)