from django.contrib import admin
from .models import Attendance 

from django.contrib import admin

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at','check_out', 'check_in', 'lat', 'long')
    list_filter = ('created_at', 'check_out','check_in','lat', 'long')
    search_fields = ('user__email', 'user__username')  # Searching by user's email and username

# Register the Attendance model with the customized admin class
admin.site.register(Attendance, AttendanceAdmin)
