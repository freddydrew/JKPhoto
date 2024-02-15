from django.db import models

'''
*****GLOSSARY*****

-email:         This is the user submitted email that will be used to 
                send out the newsletter or mass emails. 
-subscribeTime: This is the automatically added time in which some 
                person signs up to be a subscriber
'''
# Create your models here.
class subscriber(models.Model):
    email = models.EmailField(max_length=75,blank=False)
    subscribeTime = models.DateTimeField(auto_now_add=True)