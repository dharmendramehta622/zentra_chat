from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)
from apps.users import views
from apps.users.views import (EmployeeRegisterView,
                              LoginView, EmployeeProfileView,
                              ResetPasswordAPIView, ResetPasswordVerifyAPIView,
                              EmployeeProfileView, VerifyOTPView, LoginSendOTPView,LoginVerifyOTPView,GoogleSigninView
                              )

router = DefaultRouter()
router.register('', views.ProfileView,
                basename="user-profile") 
router.register('admin/users', views.AdminUsersView, basename="admin-users-list")



urlpatterns = [
    path('register/', EmployeeRegisterView.as_view(),
         name='register'),
        path('user/google-sign-in/', GoogleSigninView.as_view(), 
         name='user-register'),
   path('profile/<int:pk>/', EmployeeProfileView.as_view(),
         name='user-profile'), 
    path('profile/', include(router.urls)),
    path('reset-password/', ResetPasswordAPIView.as_view(),
         name='reset-password'),
    path('reset-password-verify/', ResetPasswordVerifyAPIView.as_view(),
         name='reset-password-verify'),
    path('verify-otp/', VerifyOTPView.as_view(), name='verify-otp'),
    path('login/', LoginView.as_view(), name='login'),
    path('login-send-otp/', LoginSendOTPView.as_view(), name='login'),
    path('login-verify-otp/', LoginVerifyOTPView.as_view(), name='login'),
    path('', views.home, name='home'),
    path('success/', views.success_msg, name='success_msg'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
