# Generated by Django 3.2.9 on 2024-07-29 08:00

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('username', models.CharField(max_length=150, unique=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('role', models.CharField(error_messages={'required': 'Role must be provided'}, max_length=12)),
                ('email', models.EmailField(error_messages={'unique': 'This email already exists in our system.'}, max_length=254, unique=True)),
                ('phone_no', models.CharField(max_length=16)),
                ('user_image', models.ImageField(upload_to='user_image')),
                ('is_active', models.BooleanField(default=False)),
                ('dob', models.DateField(auto_now=True)),
                ('date_joined', models.DateTimeField(auto_now=True)),
                ('email_verified', models.BooleanField(default=False)),
                ('otp', models.CharField(blank=True, max_length=6, null=True)),
                ('groups', models.ManyToManyField(blank=True, related_name='custom_group_set', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='custom_user_set', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ResetPassword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default=None, max_length=64, unique=True)),
                ('pw_reset_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pw_reset_user', to='users.user')),
            ],
            options={
                'verbose_name': 'Reset Password',
                'verbose_name_plural': 'Reset Password',
            },
        ),
    ]
