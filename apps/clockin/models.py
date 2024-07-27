from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from apps.users.models import User

# Create your models here.
class Attendance(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True,required = True)
    check_out = models.DateTimeField(auto_now=True)
    check_out = models.DateTimeField(auto_now=True)
    lat = models.DecimalField(default=0.0,decimal_places=2,)
    long = models.DecimalField(default=0.0,decimal_places=2,)

    class Meta:
        unique_together = ('name',)
        verbose_name = 'Attendance'
        verbose_name_plural = 'Attendances'

    def __str__(self):
        return self.user.email

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.email, allow_unicode=True)
        super(Attendance, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('clockin', kwargs={'slug': self.slug})

 