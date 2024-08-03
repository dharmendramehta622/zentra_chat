from django.db import models
from django.urls import reverse
from django.utils.text import slugify 
from django.contrib.auth import get_user_model 

User = get_user_model()

# Create your models here.
class Attendance(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    check_in = models.DateTimeField(auto_now_add=True)
    check_out = models.DateTimeField(auto_now_add=False,null=True)
    lat = models.DecimalField(default=0.0, decimal_places=6, max_digits=9)   
    long = models.DecimalField(default=0.0, decimal_places=6, max_digits=9)  

    class Meta:
        unique_together = ('created_at', 'user')
        verbose_name = 'Attendance'
        verbose_name_plural = 'Attendances'

    def __str__(self):
        return self.user.username

 