from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group 
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomUserAdmin(UserAdmin):
    model = User

    list_display = ('id', 'email', 'is_staff', 'is_active', 'is_superuser',)
    list_filter = ('is_staff', 'is_active', 'is_superuser', 'role'
                )
    fieldsets = (
        (None, {'fields': (
            'email',
            "first_name",
            "last_name",
            "role",
            "phone_no",
            "user_image",
            "otp",
            "email_verified",
        )}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser')}),
        (('Login Info'), {'fields': ('last_login',)}),
        # (('Addresses'), {'fields': ('add_type_id','address_line','to_name','contact_num','alt_contact_num','city','state','country','landmark','pincode')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff',
                       'is_active')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)



# Register your models here. 
admin.site.unregister(Group)
admin.site.register(User,CustomUserAdmin)
