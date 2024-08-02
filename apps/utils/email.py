from django.conf import settings
from django.core.mail import BadHeaderError
from django.http import HttpResponse
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

class EmailProcessor:
    
    def __init__(self, subject, message, html_message_template, context) -> None:
        self.subject = subject
        self.message = message 
        self.html_message_template = html_message_template
        self.context = context
        self.email_from = settings.EMAIL_HOST_USER
        
    def send_mail(self,receipient):
        
        recipient_list= [receipient]
        
        # Render the HTML message with context
        html_message = render_to_string(self.html_message_template, self.context)

        print(f"Email from: {self.email_from}")
        print(f"Recipient list: {recipient_list}")
        print(f"Message: {self.message}") 
        
        try: 
            msg = EmailMultiAlternatives(self.subject, self.message, self.email_from, recipient_list)
            msg.attach_alternative(html_message, "text/html")
            msg.send(fail_silently=True) #Fail silently if email not found
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponse('Email sent successfully.')