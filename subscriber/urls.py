from django.urls import path

from .views import (
    subscribeView,
    unsubscribeView,
)

app_name = 'subscriber'
urlpatterns = [
    path('subscribe/',subscribeView,name="subscribe"),
    path('unsubscribe/',unsubscribeView,name='unsubscribe')
]