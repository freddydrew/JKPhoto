from django.shortcuts import render
from album.models import album
from subscriber.models import subscriber
from subscriber.forms import (
    subscribeForm, 
    recaptchaV3
)

def homeView(request):

    # These are the photo album for the carousel, it gets 3 of the
    # most recently published and hands them to the home page
    sliderObjList = album.objects.filter(publish=True).order_by('-publishDate')[0:3]
    robotForm = recaptchaV3(request.POST or None)
    form = subscribeForm(request.POST or None)
    context = {
        'sliderObjList': sliderObjList,
        "form": form,
        "robotForm": robotForm
    }

    if request.method == 'POST':
        if form.is_valid() and robotForm.is_valid():
            
            if subscriber.objects.filter(email=form.cleaned_data['email'].lower()).exists():
                context['status'] = False
            else:
                newSubscriber = subscriber(
                    email=form.cleaned_data['email'].lower()                
                    )
                newSubscriber.save()
                context['status'] = True
            return render(request,'home.html',context=context)
    return render(request,'home.html',context=context)

def aboutView(request):
    context = {}
    return render(request,'about.html',context=context)