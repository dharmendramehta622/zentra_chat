from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import User
from apps.utils.email import EmailProcessor 



@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    
    if created:
        print(''' Start of send email.''')  # Debug statement
        ''' Handle welcome email send sample code.'''
        # context = {'link': f'https://api.zenchat.com/onboard/{instance.id}/'}
        
        # email_processor = EmailProcessor(
        #     subject='Account Activation',
        #     message='',
        #     html_message_template='users/welcome.html',
        #     context=context
        # )
                    
        # email_processor.send_mail(
        #     receipient=instance.email
        # )
        print('''Email sent successfully.''')  # Debug statement

@receiver(post_delete, sender=User)
def send_goodbye_email(sender, instance, **kwargs):
    print(''' Start of send email.''')  # Debug statement
    ''' Handle good bye email send sample code.'''
    message = f'Hi {instance.email},\n\nSorry to see you go!'
    print(message)
    print('''Email sent successfully.''')  # Debug statement
