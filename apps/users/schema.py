import graphene
from graphene_django import DjangoObjectType
from .models import User
 
class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ("username","role","email","phone_no","user_image","is_active","date_joined","email_verified",)
        
        
class Query(graphene.ObjectType):
    user = graphene.List(UserType)   
    
    def resolve_user(root,info):
        return User.objects.all()
    

schema = graphene.Schema(query=Query)
         