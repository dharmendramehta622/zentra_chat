import random
import string
from rest_framework.exceptions import APIException
from django.contrib.auth import login
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from apps.clockin.serializers import AttendanceSerializer
from apps.users.custom_auth.token_auth import MyTokenObtainPairSerializer
from apps.utils.generators import Generator
from rest_framework import generics, mixins, status, viewsets
from rest_framework.exceptions import NotFound, ValidationError
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.response import Response
from apps.users.models import  ResetPassword
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny
from apps.users.permissions import IsEmployee  
from apps.utils.email import EmailProcessor
from apps.users.serializers import (
                                    EmployeeAddSerializer,
                                    EmployeeRegisterSerializer,
                                    LoginSerializer, 
                                    ResetPasswordSerializer,
                                    ResetPasswordVerifySerializer,
                                    UserSerializer,
                                    VerifyOTPSerializer)

User = get_user_model()

def _get_token(user):
    _token = MyTokenObtainPairSerializer.get_token(user)
    return {
        'refresh': str(_token),
        'access': str(_token.access_token),
    }
 
def _get_admin_token(user):
    _token = MyTokenObtainPairSerializer.get_admin_token(user)
    return {
        'refresh': str(_token),
        'access': str(_token.access_token),
    }    
    
    
generator = Generator()

class EmployeeAddView(generics.CreateAPIView):
    serializer_class = EmployeeAddSerializer
    authentication_classes = []  # Allow unauthenticated access
    permission_classes = [AllowAny]  # Allow all permissions

    def get(self, request, *args, **kwargs):
        # Handle GET requests here if needed
        return Response(
            {"message": "GET method is not supported for this endpoint."},
            status=status.HTTP_405_METHOD_NOT_ALLOWED
        )

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid(raise_exception=True): 
                user = serializer.save() 
                
            return Response(
                {
                    "data": f"User added successfully. Email address is {user.email}",
                    "status": "Success",
                },
                status.HTTP_201_CREATED
            )
        except APIException as e:
            return Response({"error": str(e)}, status=e.status_code)

class EmployeeRegisterView(generics.CreateAPIView):
    serializer_class = EmployeeRegisterSerializer
    authentication_classes = []  # Allow unauthenticated access
    permission_classes = [AllowAny]  # Allow all permissions

    def get(self, request, *args, **kwargs):
        # Handle GET requests here if needed
        
        context = {'link': 'https://www.youtube.com/watch?v=8jF5RmI2YNU&list=RD8jF5RmI2YNU&start_radio=1'}
        
        email_processor = EmailProcessor(
            subject='Account Activation',
            message='',
            html_message_template='users/welcome.html',
            context=context
        )
                    
        email_processor.send_mail(
            receipient='dharmendra.mehta@hamrokk.com'
        )
        return Response(
            {"message": "GET method is not supported for this endpoint."},
            status=status.HTTP_405_METHOD_NOT_ALLOWED
        )

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()  
                return Response(
                    {
                        "data": "Please confirm your email to complete the registration.",
                        "status": "Success",
                    },
                    status.HTTP_201_CREATED
                )
        except APIException as e:
            return Response({"error": str(e)}, status=e.status_code)
  
class ResetPasswordAPIView(generics.CreateAPIView):
    serializer_class = ResetPasswordSerializer
    authentication_classes = []  # Allow unauthenticated access
    permission_classes = [AllowAny]  # Allow all permissions

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data["email"].lower()
        try:
            user = User.objects.get(email=email)
            code = "".join(
                random.choices(string.ascii_uppercase + string.digits, k=6)
            )  # randomly_generated 6-digit-code
            user_password_reset = ResetPassword.objects.create(
                pw_reset_user=user, code=code
            )
            context = {
                "user": user.first_name,
                "code": user_password_reset.code
            }
            subject = "Password Reset Code for HamroKK"
            recipient  = user.email
            text_content = render_to_string("users/password_reset.html",
                                            context)
            return Response(
                {"data": "Please check your email to  reset your password.","status":"Success"},
                status=status.HTTP_201_CREATED,
            )
        except User.DoesNotExist:
            return Response(
                {"data": "User does not exist.","status":"Failed"},
                status=status.HTTP_404_NOT_FOUND
            )


class ResetPasswordVerifyAPIView(generics.GenericAPIView):
    serializer_class = ResetPasswordVerifySerializer
    authentication_classes = []  # Allow unauthenticated access
    permission_classes = [AllowAny]  # Allow all permissions

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        reset_code = serializer.validated_data["reset_code"]
        try:
            user_for_pw_reset = ResetPassword.objects.get(code=reset_code)

            if reset_code == user_for_pw_reset.code:
                user_for_pw_reset.pw_reset_user.set_password(
                    serializer.validated_data["new_password"]
                )
                user_for_pw_reset.pw_reset_user.save()
                user_for_pw_reset.delete()
                return Response(
                    {"data": "Password changed successfully.","status":"Success"},
                    status=status.HTTP_201_CREATED,
                )
        except ResetPassword.DoesNotExist as e:
            raise NotFound(
                {"data": "Reset-code is incorrect. Please re-check.","status":"Failed"}
            ) from e


class VerifyOTPView(generics.GenericAPIView):
    serializer_class = VerifyOTPSerializer
    authentication_classes = []  # Allow unauthenticated access
    permission_classes = [AllowAny]  # Allow all permissions

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        _otp = serializer.validated_data["otp"]
        try:
            _user = User.objects.get(otp=_otp)
            _user.email_verified = True
            _user.is_active = True
            _user.otp = None
            _user.save()
            login(request, _user)
            return Response({'data': 'Your account has been activated.',"status":"Success"})
        except User.DoesNotExist as e:
            raise ValidationError({'data': "This OTP doesn't exist","status":"Failed"}) from e


class LoginView(generics.CreateAPIView):
    authentication_classes = []  # Allow unauthenticated access
    permission_classes = [AllowAny]  # Allow all permissions    
    serializer_class = LoginSerializer
    model = User
    success_url = reverse_lazy("login")

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            try:
                user = User.objects.get(
                    email=serializer.validated_data["email"])
            except User.DoesNotExist:
                return Response(
                    {
                        "data": "User with this email does not exist.",
                        "status": "Failed"
                    },
                    status=status.HTTP_400_BAD_REQUEST)

            if not user.check_password(serializer.validated_data["password"]):
                return Response(
                    {
                        "data": "Password is incorrect.",
                        "status": "Failed"
                    },
                    status=status.HTTP_400_BAD_REQUEST)
            #admin user token
            if user.is_active and user.is_superuser:
                login(request, user)
                return Response(
                        {
                            "status":"Success",
                            "data":_get_admin_token(user)
                        },
                        status=status.HTTP_200_OK,
                    )    
            # normal user  
            if user.is_active and user.role == 'employee':
                login(request, user)
                return Response(
                        {
                            "status":"Success",
                            "data":_get_token(user)
                        },
                        status=status.HTTP_200_OK,
                    )
            else:
                return Response(
                    {"data": "Please activate your account.","status":"Failed"},
                    status=status.HTTP_401_UNAUTHORIZED,
                )
 
 
class ProfileView( mixins.ListModelMixin,  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,  
                  viewsets.GenericViewSet):
    
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated,IsEmployee]
    
    
    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)
    
    def get_object(self):
        try:
            user_id = self.request.user.id
            return User.objects.get(id=user_id )
        except User.DoesNotExist as e:
            raise NotFound({"message": "Data not found"}) from e

 
def home(request):
    return HttpResponse('You know what to do now!')


def success_msg(request):
    return render(request, template_name="users/welcome.html")








#admin 
from apps.clockin.models import Attendance
from rest_framework.pagination import LimitOffsetPagination
from django.utils.dateparse import parse_date
from django.db.models import Q
from django.utils import timezone

class AdminUsersView(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser,IsAuthenticated]
    pagination_class = LimitOffsetPagination  # Explicitly set pagination class if needed

    def get_queryset(self):
        queryset = super().get_queryset()
        # Include related details for each many-to-many field
        queryset = queryset.prefetch_related()
        return queryset

    def get_object(self):
        try:
            return User.objects.get(id=self.kwargs['pk'])
        except User.DoesNotExist as e:
            raise NotFound({"message": "Data not found"}) from e          
              
class AdminAttendanceView(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [IsAdminUser,IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        # Include related details for each many-to-many field
                # Get the start_date, end_date, and username from query params
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')
        search_query = self.request.query_params.get('search_query')
        
        '''
        Filter the queryset based on the date range.
        
        Django is set to use timezone-aware datetimes, but the parse_date function returns naive 
        datetime objects (datetimes without timezone information).
        
        You should ensure that the datetime objects you create are timezone-aware.
        '''
        if start_date:
            start_date = parse_date(start_date)
            if start_date:
                start_date = timezone.make_aware(timezone.datetime.combine(start_date, timezone.datetime.min.time()))
                queryset = queryset.filter(created_at__gte=start_date)
        if end_date:
            end_date = parse_date(end_date)
            if end_date:
                end_date = timezone.make_aware(timezone.datetime.combine(end_date, timezone.datetime.max.time()))
                queryset = queryset.filter(created_at__lte=end_date)

 
        '''
        Filter the queryset based on partial match for username, first_name, or last_names
        '''
        if search_query:
            queryset = queryset.filter(
                Q(user__username__icontains=search_query) |
                Q(user__first_name__icontains=search_query) |
                Q(user__last_name__icontains=search_query)
            )
        return queryset

    def get_object(self):
        try:
            return User.objects.get(id=self.kwargs['pk'])
        except User.DoesNotExist as e:
            raise NotFound({"message": "Data not found"}) from e                