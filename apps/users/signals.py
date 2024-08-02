from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import User
from apps.utils.email import EmailProcessor 



@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    
    if created:
        print("send_welcome_email signal triggered")  # Debug statement
        context = {'link': f'https://api.hamrokk.com/onboard/{instance.id}/'}
        
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
