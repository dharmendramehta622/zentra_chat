from django.shortcuts import render
from .serializers import AttendanceSerializer 
from .models import Attendance 
from rest_framework import mixins,viewsets
from rest_framework.exceptions import NotFound
from rest_framework.permissions import  AllowAny

# Create your views here.
class NewsCategoryView(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = AttendanceSerializer
    authentication_classes = []  # Allow unauthenticated access
    permission_classes = [AllowAny]  # Allow all permissions
    
    def get_queryset(self):
        return Attendance.objects.filter(user=self.user.id)

    def get_object(self):
        try:
            return Attendance.objects.get(id=self.kwargs['pk'])
        except Attendance.DoesNotExist as e:
            raise NotFound({"message": "Data not found"}) from e

 