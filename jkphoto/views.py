from django.shortcuts import render

def homeView(request):
    context = {}
    return render(request,'home.html',context=context)

def aboutView(request):
    context = {}
    return render(request,'about.html',context=context)