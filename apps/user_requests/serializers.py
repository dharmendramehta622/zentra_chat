from rest_framework import serializers
from apps.user_requests.models import UserRequest
from apps.users.serializers import UserSerializer

class UserRequestSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    
    class Meta:
        model = UserRequest
        fields = '__all__'
        read_only_fields = [ 'sender','invite_status' 'created_at']

    def validate(self, data):
        sender = self.context['request'].user
        receiver = data['receiver']
        
        if sender == receiver:
            raise serializers.ValidationError("You cannot send request to yourself.")
            
        # Only apply the check during creation
        if self.instance is None:
            # Check if there's an existing attendance without check_out
            existing_request = UserRequest.objects.filter(sender=sender,receiver=receiver).exists()
            if existing_request:
                raise serializers.ValidationError("You already have a request sent to this user.")
        return data
    
    def create(self, validated_data):
        validated_data.pop('user', None)
        print(validated_data)  # Debugging line
        # Set the sender to the current user from the request context
        validated_data['sender'] = self.context['request'].user
        return super().create(validated_data)