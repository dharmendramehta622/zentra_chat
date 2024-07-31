import random
import string
from rest_framework.exceptions import APIException
from django.contrib.auth import login
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from apps.users.custom_auth.token_auth import MyTokenObtainPairSerializer
from apps.utils.generators import Generator
from playground.settings import EMAIL_HOST_USER,EMAIL_PORT,EMAIL_HOST_PASSWORD,EMAIL_BACKEND
from rest_framework import generics, mixins, status, viewsets
from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound, ValidationError
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.response import Response
from apps.users.models import  ResetPassword, User
from rest_framework.permissions import AllowAny
from apps.users.permissions import IsEmployee  
from apps.utils.email import EmailProcessor
from apps.users.serializers import (
                                    EmployeeAddSerializer,
                                    EmployeeRegisterSerializer,
                                    LoginSerializer,
                                    LoginSendOTPSerializer,
                                    LoginVerifyOTPSerializer,
                                    EmployeeProfileSerializer,
                                    ResetPasswordSerializer,
                                    ResetPasswordVerifySerializer,
                                    UserSerializer,
                                    VerifyOTPSerializer)


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
                print(serializer.validated_data)
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
class LoginSendOTPView(generics.CreateAPIView):
    serializer_class = LoginSendOTPSerializer
    authentication_classes = []  # Allow unauthenticated access
    permission_classes = [AllowAny]  # Allow all permissions
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
                        "data": "User with this email does not exist."  ,"status":"Failed"
                    },
                    status=status.HTTP_400_BAD_REQUEST)
            
            if user.is_active and user.role == 'employee':
                login(request, user)
                otp = "".join(random.choices(string.digits, k=6))
                user.otp = otp
                user.save()
                context = {
                    "otp": otp
                }
                subject = f'OTP for User Login: {otp} | HamroKK'
                recipient  =serializer.validated_data["email"]
                text_content = render_to_string("users/user_verify.html", context)
                return Response(
                        {
                            "status":"Success",
                            "data":"Please check you email for OTP."
                        },
                        status=status.HTTP_200_OK,
                    )
            else:
                return Response(
                    {"data": "Please activate your account.","status":"Success"},
                    status=status.HTTP_401_UNAUTHORIZED,
                )
                
class LoginVerifyOTPView(generics.CreateAPIView):
    serializer_class = LoginVerifyOTPSerializer
    authentication_classes = []  # Allow unauthenticated access
    permission_classes = [AllowAny]  # Allow all permissions
    model = User
    success_url = reverse_lazy("login")

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            try:
                user = User.objects.get(
                otp=serializer.validated_data["otp"])
                user.otp = None 
                user.save()
                print(user)
                login(request, user)
                subject = f'Account Login: | HamroKK'
                recipient  = user.email
                text_content = render_to_string("users/login_info.html")
                return Response(
                        {
                            "status":"Success",
                            "data":{"token":_get_token(user)}
                        },
                        status=status.HTTP_200_OK,
                    )
            except User.DoesNotExist:
                return Response(
                    {
                        "data": "Incorrect OTP."
                     ,"status":"Failed"
                    },
                    status=status.HTTP_400_BAD_REQUEST)

class EmployeeProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = EmployeeProfileSerializer
    permission_classes = [IsAuthenticated, IsEmployee]

    def get_object(self): 
        return User.objects.get(id=self.kwargs['pk'])

    def retrieve(self, request, *args, **kwargs):
        try:
            profile = User.objects.get(id=self.kwargs['pk'])
            if profile.role == 'employee':
                user_data = self.serializer_class(
                    profile, context={"request": request}).data
                return Response(user_data, status=status.HTTP_200_OK)
            else:
                return Response({'data': "You are not allowed to access "
                                "recruiter's profile in this way.","status":"Failed"},
                                status=status.HTTP_405_METHOD_NOT_ALLOWED)
        except User.DoesNotExist as e:
            raise NotFound({"data": "User does not exist.","status":"Failed"}) from e

    def patch(self, request, *args, **kwargs):
        serializer = EmployeeProfileSerializer(
            self.get_object(), data=request.data,
            partial=True, context={"request": request})
        if serializer.is_valid(raise_exception=True):
            if self.request.user.id == self.kwargs['pk']:
                _user = serializer.save()
                if _user.profile_is_set is False:
                    _user.profile_is_set = True
                    _user.save()
                return Response(serializer.data)
            raise ValidationError({"data": "You do not have permission to update the profile of other users.","status":"Failed"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfileView( mixins.ListModelMixin,  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,  
                  viewsets.GenericViewSet):
    # queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    
    
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

    def get_queryset(self):
        queryset = super().get_queryset()
        # Include related details for each many-to-many field
        queryset = queryset.prefetch_related(   )
        return queryset

    def get_object(self):
        try:
            return User.objects.get(id=self.kwargs['pk'])
        except User.DoesNotExist as e:
            raise NotFound({"message": "Data not found"}) from e                