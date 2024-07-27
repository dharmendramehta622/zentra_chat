from rest_framework import serializers
from apps.clockin.models import Attendance
 

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = "__all__"
 
 