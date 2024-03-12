from subscriber.models import subscriber
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags
import queue

def sendNewsLetter(object):

    # Building the queue of email address of subscribers
    mailQueue = queue.Queue()
    for obj in subscriber.objects.all():
        mailQueue.put(obj.email)

    while mailQueue.empty() != True:
        from_email = 'justinkoebelephoto@gmail.com'
        to = None
        bcc = [from_email]
        count = 0
        while count < 15 and mailQueue.empty() != True:
            bcc.append(mailQueue.get())
            count += 1

        context = {
            'object': object
            }
        html_message = render_to_string('letter/letter.html', context=context)
        plain_message = strip_tags(html_message)
            
        email = EmailMultiAlternatives(
            subject = object.title,
            from_email=from_email,
            to=None,
            bcc=bcc,
            body=plain_message,
        )
        email.attach_alternative(html_message,'text/html')
        email.send()

def sendTestNewsLetter(object):

    # Send test email to myself
    from_email = 'justinkoebelephoto@gmail.com'
    context = {
        'object': object
        }
    html_message = render_to_string('letter/letter.html', context=context)
    plain_message = strip_tags(html_message)
        
    email = EmailMultiAlternatives(
        subject = object.title,
        from_email=from_email,
        to = [from_email],
        body=plain_message,
    )
    email.attach_alternative(html_message,'text/html')
    email.send()