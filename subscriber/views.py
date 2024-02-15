from django.shortcuts import render
from .models import subscriber
from .forms import (
    subscribeForm, 
    unsubscribeForm, 
    recaptchaV3
)

# Create your views here.
def subscribeView(request):
    robotForm = recaptchaV3(request.POST or None)
    form = subscribeForm(request.POST or None)
    context = {
        "form": form,
        "robotForm": robotForm
    }

    if request.method == 'POST':
        if form.is_valid() and robotForm.is_valid():
            
            if subscriber.objects.filter(email=form.cleaned_data['email'].lower()).exists():
                pass
            else:
                newSubscriber = subscriber(
                    email=form.cleaned_data['email'].lower()                
                    )
                newSubscriber.save()
            return render(request,'subscriber/success.html')
    return render(request,'subscriber/subscribe.html',context=context)

def unsubscribeView(request):
    robotForm = recaptchaV3(request.POST or None)
    form = unsubscribeForm(request.POST or None)
    context = {
        "form": form,
        "robotForm": robotForm
    }

    if request.method == 'POST':
        if form.is_valid() and robotForm.is_valid():
            
            if subscriber.objects.filter(email=form.cleaned_data['email'].lower()).exists():
                subscriber.objects.filter(email=form.cleaned_data['email'].lower()).delete()
            else:
                pass
            return render(request,'subscriber/successUnsub.html')
    return render(request,'subscriber/unsubscribe.html',context=context)