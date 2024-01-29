from django.shortcuts import render
from .models import album
from django.core.paginator import (
    Paginator,
    EmptyPage,
    PageNotAnInteger,
)

# Create your views here.

def allAlbumsView(request):
    defaultPage = 1
    page = request.GET.get('page', defaultPage)
    objList = album.objects.filter(publish=True)

    objPerPage = 1
    paginator = Paginator(objList, objPerPage)

    try:
        objPage = paginator.page(page)
    except PageNotAnInteger:
        objPage = paginator.page(defaultPage)
    except EmptyPage:
        objPage = paginator.page(paginator.num_pages)

    context={
        'objList': objList,
        'objPage': objPage
    }
    return render(request,"album/allAlbums.html",context=context)

def oneAlbumView(request,slug=None):

    # getting the unique slug for the article in question
    obj = album.objects.get(slug=slug)

    # put the fetched object into dict that is given to page
    context={
        'obj': obj
    }
    return render(request,"album/oneAlbum.html",context=context)