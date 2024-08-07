from .serializers import UserRequestSerializer 
from .models import UserRequest 
from rest_framework import mixins,viewsets,status
from rest_framework.exceptions import NotFound,ValidationError
from rest_framework.permissions import  IsAuthenticated
from apps.users.permissions import IsEmployee
from rest_framework.response import Response

# Create your views here.
class UserRequestView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = UserRequestSerializer
    # authentication_classes = []  # Allow unauthenticated access
    permission_classes = [IsAuthenticated,IsEmployee,]  # Allow all permissions
    
    def get_queryset(self):
        queryset = UserRequest.objects.filter(receiver=self.request.user.id)
        return queryset

    def get_object(self):
        try:
            return UserRequest.objects.get(id=self.kwargs['pk'])
        except UserRequest.DoesNotExist as e:
            raise NotFound({"message": "Data not found"}) from e
        
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        except ValidationError as e:
            error_message = e.detail.get('non_field_errors', ['An error occurred'])[0]
            return Response({"status": "Failed", "message": error_message}, status=status.HTTP_400_BAD_REQUEST)

  
 
 
 