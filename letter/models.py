from django.db import models
import datetime as dt

# Create your models here.
class letter(models.Model):
    title = models.CharField(max_length=75,blank=False)
    message = models.TextField()
    sent = models.BooleanField(default=False,editable=False)
    dateSent = models.DateField(null=True,editable=False)

    def setSent(self):
        letter.objects.filter(id=self.id).update(sent=True)
    
    def setDateSent(self):
        letter.objects.filter(id=self.id).update(dateSent=dt.date.today())
    


