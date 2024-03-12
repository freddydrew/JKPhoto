from django.contrib import admin
from .models import letter
from .utils import sendNewsLetter, sendTestNewsLetter

# Register your models here.
class letterAdmin(admin.ModelAdmin):
    @admin.action(description='Send subscriber email')
    def sendLetter(modelAdmin,request,queryset):
        if queryset.count() != 1:
            warningMsg = 'Only one letter can be sent at a time.'
            modelAdmin.message_user(request,warningMsg)
        else:
            obj = queryset[0]
            sendNewsLetter(obj)
            obj.setSent()
            obj.setDateSent()
            confirmationMsg = 'Message Sent'
            modelAdmin.message_user(request,confirmationMsg)

    @admin.action(description='Send test email')
    def sendTestLetter(modelAdmin,request,queryset):
        if queryset.count() != 1:
            warningMsg = 'Only one test letter can be sent at a time.'
            modelAdmin.message_user(request,warningMsg)
        else:
            obj = queryset[0]
            sendTestNewsLetter(obj)
            obj.setSent()
            obj.setDateSent()
            confirmationMsg = 'Message Sent'
            modelAdmin.message_user(request,confirmationMsg)
    
    list_display = ['title','sent','dateSent']
    readonly_fields = ['sent','dateSent']
    actions = [sendLetter, sendTestLetter]

admin.site.register(letter,letterAdmin)