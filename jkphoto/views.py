from django.shortcuts import render
from album.models import album

def homeView(request):

    # These are the photo album for the carousel, it gets 3 of the
    # most recently published and hands them to the home page
    sliderObjList = album.objects.filter(publish=True).order_by('-publishDate')[0:3]
    context = {
        'sliderObjList': sliderObjList
    }
    return render(request,'home.html',context=context)

def aboutView(request):
    context = {}
    return render(request,'about.html',context=context)