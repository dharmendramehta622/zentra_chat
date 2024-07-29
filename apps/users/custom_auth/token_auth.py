from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        _groups = user.groups.all()
        last_index = len(_groups)-1
        token['user-info'] = {
            "user_id":user.id,
            "role": user.role,
            "is_superuser": user.is_superuser,
            "is_active": user.is_active,
            "email_verified": user.email_verified,
        }
        return token
    
    @classmethod
    def get_admin_token(cls, user):
        token = super().get_token(user)
        _groups = user.groups.all()
        last_index = len(_groups)-1
        token['user-info'] = {
            "user_id":user.id,
            "role": 'admin',
            "is_superuser": user.is_superuser,
            "is_active": user.is_active,
            "email_verified": user.email_verified,
        }
        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
