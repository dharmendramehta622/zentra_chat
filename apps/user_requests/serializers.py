from rest_framework import serializers
from apps.user_requests.models import UserRequest
from apps.users.serializers import UserSerializer

class AttendanceSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = UserRequest
        fields = '__all__'
        read_only_fields = [ 'user', 'created_at']

    def validate(self, data):
        user = self.context['request'].user

        # Only apply the check during creation
        if self.instance is None:
            # Check if there's an existing attendance without check_out
            ongoing_attendance = UserRequest.objects.filter(user=user, check_out__isnull=True).exists()
            if ongoing_attendance:
                raise serializers.ValidationError("You already have a running check-in. Please check out before creating a new one.")

        return data
