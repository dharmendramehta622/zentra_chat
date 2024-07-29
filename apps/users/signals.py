from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import User
import random
import string

#E4DOJ309#ESF


@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    print("send_welcome_email signal triggered")  # Debug statement
    subject = 'Welcome to Our Platform'
    if created:
        otp = "".join(random.choices(string.digits, k=6))
        context = {
            "otp": otp,
        } 
        # subject = f'OTP for User Account Activation: {otp} | Attendo'
        # recipient =serializer.validated_data["email"]
        # text_content = render_to_string("users/user_verify.html", context)
        message = f'Hi {instance.email},\n\nThank you for signing up on our platform. We are excited to have you on board!'
        print(subject)
        print(message)
        # Uncomment these lines to send an actual email
        # from_email = settings.DEFAULT_FROM_EMAIL
        # recipient_list = [instance.email]
        # send_mail(subject, message, from_email, recipient_list)

@receiver(post_delete, sender=User)
def send_goodbye_email(sender, instance, **kwargs):
    print("send_goodbye_email signal triggered")  # Debug statement
    message = f'Hi {instance.email},\n\nSorry to see you go!'
    print(message)
