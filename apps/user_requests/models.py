from django.db import models
from django.urls import reverse
from django.utils.text import slugify 
from django.contrib.auth import get_user_model 
from apps.utils.choices import INVITE_STATUS 

User = get_user_model()

# Create your models here.
class UserRequest(models.Model):
    sender = models.ForeignKey(User,on_delete=models.CASCADE,related_name='sent_requests')
    receiver = models.ForeignKey(User,on_delete=models.CASCADE, related_name='received_requests')
    message = models.CharField(max_length=50, default=None,null=True)
    invite_status = models.CharField(max_length=10,choices=INVITE_STATUS,default="pending")
    created_at = models.DateTimeField(auto_now_add=True)  

    class Meta:
        unique_together = ('sender', 'receiver')
        verbose_name = 'User Request'
        verbose_name_plural = 'User Requests'

    def __str__(self):
        return f"{self.sender.first_name} sent request to ${self.receiver.first_name}."

 