from django.db import models
from django.contrib.auth.models import AbstractUser,Group,Permission
from django.urls import reverse
from apps.users.managers import UserManager
import uuid 

# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    role = models.CharField(max_length=12, error_messages={
        'required': "Role must be provided"
    })
    email = models.EmailField(unique=True, blank=False, error_messages={
        'unique': "This email already exists in our system."
    })
    phone_no = models.CharField(max_length=16, blank=True)
    user_image = models.ImageField(upload_to="user_image",)
    is_active = models.BooleanField(default=False)
    dob = models.DateField(auto_now=True)
    date_joined = models.DateTimeField(auto_now=True)
    email_verified = models.BooleanField(default=False)
    otp = models.CharField(max_length=6, blank=True, null=True)
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        related_name='custom_group_set',  # This is the key change
        blank=True,
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        related_name='custom_user_set',  # This is the key change
        blank=True,
    )
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    def __unicode__(self):
        return self.email

    def get_absolute_url(self):
        return reverse('user-details', kwargs={'slug': self.role})

    objects = UserManager()


class ResetPassword(models.Model):
    pw_reset_user = models.ForeignKey(User, related_name="pw_reset_user",
                                      on_delete=models.CASCADE)
    code = models.CharField(max_length=64, unique=True, default=None)

    def __str__(self):
        return str(self.pw_reset_user)

    class Meta:
        verbose_name = "Reset Password"
        verbose_name_plural = "Reset Password"



 