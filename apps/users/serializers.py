from django.contrib.auth import get_user_model, password_validation
from rest_framework import serializers, status
from validate_email_address import validate_email
from apps.utils.mailbox_validation import MailboxValidation
User = get_user_model()


class EmployeeRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={"input_type": "password"})
    confirm_password = serializers.CharField(
        style={"input_type": "password"}, write_only=True
    )

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name", 
            "email",
            "password",
            "confirm_password",
        ]

    # def validate_email(self, attrs):
    #     _result = validate_email(email=attrs, verify=True)
    #     if _result is True:
    #         return attrs
    #     raise MailboxValidation("This mailbox doesn't exist. Please input a valid one.",
    #                             'email', status_code=status.HTTP_404_NOT_FOUND)

    def validate(self, data):
        """Validate user password."""
        try:
            password = data["password"]
            password_c = data["confirm_password"]
        except KeyError as e:
            print(e)
        else:
            if password != password_c:
                raise serializers.ValidationError(
                    "Password don't match. Please confirm your password."
                )
            password_validation.validate_password(password)
            return data

    def create(self, validated_data):
        """Create user w/ `employee` role."""
        validated_data.pop("confirm_password")
        user = User.objects.create_user(**validated_data)
        user.role = "employee"
        # user.is_active =True
        # user.email_verified =True
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    model = User
    email = serializers.EmailField()
    password = serializers.CharField(style={"input_type": "password"},
                                     write_only=True)


class LoginSendOTPSerializer(serializers.Serializer):
    model = User
    email = serializers.EmailField() 
class LoginVerifyOTPSerializer(serializers.Serializer):
    model = User
    otp = serializers.CharField() 


class LoginSerializer(serializers.Serializer):
    model = User
    email = serializers.EmailField()
    password = serializers.CharField(style={"input_type": "password"},
                                     write_only=True)


class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()


class ResetPasswordVerifySerializer(serializers.Serializer):
    reset_code = serializers.CharField()
    new_password = serializers.CharField(style={"input_type": "password"})


class EmployeeProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            "id", "role", "email",  "phone_no",
           "first_name", "last_name", 
           "user_image",
           "is_active",
           "date_joined",
           "email_verified"
        ]

        read_only_field = [
               "id", "role", "email",  "phone_no",
           "first_name", "last_name", 
           "user_image",
           "is_active",
           "date_joined",
           "email_verified"
        ]

    def to_representation(self, instance):
        """Convert `fields` to different cases."""
        ret = super().to_representation(instance)
        ret['first_name'] = ret['first_name'].title()
        ret['last_name'] = ret['last_name'].title()
        ret['role'] = ret['role'].upper()
        return ret


class VerifyOTPSerializer(serializers.Serializer):
    otp = serializers.CharField()
 
 
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id", "role", "email",  "phone_no",
           "first_name", "last_name", 
           "user_image",
           "is_active",
           "date_joined",
           "last_login",
           "email_verified"
        ]

        read_only_field = [
               "id", "role", "email",  "phone_no",
           "first_name", "last_name", 
           "user_image", 
             "last_login",
           "date_joined",
           "email_verified"
        ]