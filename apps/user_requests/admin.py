from django.contrib import admin
from .models import UserRequest 

from django.contrib import admin

class UserRequestAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'invite_status', 'created_at')
    list_filter = ('invite_status', 'created_at')
    search_fields = ('sender__email', 'sender__username', 'receiver__email', 'receiver__username')  # Searching by sender's and receiver's email and username

# Register the UserRequest model with the customized admin class
admin.site.register(UserRequest, UserRequestAdmin)
