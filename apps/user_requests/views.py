from .serializers import AttendanceSerializer 
from .models import UserRequest 
from rest_framework import mixins,viewsets,status
from rest_framework.exceptions import NotFound,ValidationError
from rest_framework.permissions import  IsAuthenticated
from apps.users.permissions import IsEmployee
from django.http import JsonResponse
from rest_framework.response import Response
from django.utils.dateparse import parse_datetime
from datetime import datetime,timedelta

# Create your views here.
class ClockInView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = AttendanceSerializer
    # authentication_classes = []  # Allow unauthenticated access
    permission_classes = [IsAuthenticated,IsEmployee,]  # Allow all permissions
    
    def get_queryset(self):
        queryset = UserRequest.objects.filter(user=self.request.user.id)
        from_date = self.request.query_params.get('from_date')
        to_date = self.request.query_params.get('to_date')
        
        if from_date:
            from_date = parse_datetime(from_date)
            if from_date:
                queryset = queryset.filter(clock_in__gte=from_date)
        
        if to_date:
            to_date = parse_datetime(to_date)
            if to_date:
                # Add one day to include the end of the 'to_date'
                queryset = queryset.filter(clock_in__lt=(to_date + timedelta(days=1)))

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

  
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            total_hours = self.calculate_total_hours(page)
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response({
                'total_hours': total_hours,
                'results': serializer.data
            })

        total_hours = self.calculate_total_hours(queryset)
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'total_hours': total_hours,
            'results': serializer.data
        })

    def calculate_total_hours(self, queryset):
        total_duration = timedelta()
        for attendance in queryset:
            if attendance.check_out:
                total_duration += attendance.check_out - attendance.check_in
        total_hours = total_duration.total_seconds() / 3600  # convert seconds to hours
        return round(total_hours, 2)