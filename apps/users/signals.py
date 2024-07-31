from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import User
from apps.utils.email import EmailProcessor
import random
import string

#E4DOJ309#ESF


@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    print("send_welcome_email signal triggered")  # Debug statement
    if created:
        print(instance.email)
        context = {'link': f'https://www.hamrokk.com/onboard/{instance.id}'}
        
        email_processor = EmailProcessor(
            subject='Account Activation',
            message='',
            html_message_template='users/welcome.html',
            context=context
        )
                    
        email_processor.send_mail(
            receipient=instance.email
        )

@receiver(post_delete, sender=User)
def send_goodbye_email(sender, instance, **kwargs):
    print("send_goodbye_email signal triggered")  # Debug statement
    message = f'Hi {instance.email},\n\nSorry to see you go!'
    print(message)
