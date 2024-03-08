from django.shortcuts import render
from .models import album
from django.core.paginator import (
    Paginator,
    EmptyPage,
    PageNotAnInteger,
)
from django.contrib.postgres.search import (
    SearchQuery, 
    SearchVector, 
    SearchRank 
)

# Create your views here.

def allAlbumsView(request):

    sortbtn = request.GET.get('sortbtn')

    if sortbtn == 'observations':
        objList = album.objects.filter(publish=True,postType='observations')
    elif sortbtn == 'portraits':
        objList = album.objects.filter(publish=True,postType='portraits')
    elif sortbtn == 'landscapes':
        objList = album.objects.filter(publish=True,postType='landscapes')
    elif sortbtn == 'bmx':
        objList = album.objects.filter(publish=True,postType='bmx')
    elif sortbtn == 'family':
        objList = album.objects.filter(publish=True,postType='family')
    else:
        objList = album.objects.filter(publish=True).order_by('-publishDate')

    objList = objList.order_by('-publishDate')

    defaultPage = 1
    page = request.GET.get('page', defaultPage)
    objPerPage = 4

    paginator = Paginator(objList, objPerPage)

    try:
        objPage = paginator.page(page)
    except PageNotAnInteger:
        objPage = paginator.page(defaultPage)
    except EmptyPage:
        objPage = paginator.page(paginator.num_pages)

    context={
        'objPage': objPage,
        'sortbtn': sortbtn
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

def albumSearchView(request):
    q = request.GET.get('q')
    query = SearchQuery(q)
        
    vector = SearchVector('title',
                          'content',
                          'slug',
                          'updated',
                          'publishDate',
                          )
    
    # Full text search with postgresql
    object_list = album.objects.annotate(
        rank=SearchRank(vector,query)).filter(publish=True,rank__gte=0.001).order_by('-rank')
    
    # Setting up paginator 
    defaultPage = 1
    page = request.GET.get('page', defaultPage)
    objPerPage = 4
    paginator = Paginator(object_list, objPerPage)

    try:
        objPage = paginator.page(page)
    except PageNotAnInteger:
        objPage = paginator.page(defaultPage)
    except EmptyPage:
        objPage = paginator.page(paginator.num_pages)


    context={
        'query': q,
        'objPage': objPage
    }

    return render(request,"album/search.html",context=context)