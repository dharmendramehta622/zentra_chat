from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import ( 
                                            TokenRefreshView)
from apps.users import views
from apps.users.views import ( UserRegisterView ,
                              LoginView, ResetPasswordAPIView, ResetPasswordVerifyAPIView,
                              )

router = DefaultRouter()
router.register('info', views.ProfileView,
                basename="user-profile") 
router.register('users/list', views.UserListView, basename="users-list")



urlpatterns = [
    path('', include(router.urls)),

    path('register/', UserRegisterView .as_view(),
         name='add'),  
    path('reset-password/', ResetPasswordAPIView.as_view(),
         name='reset-password'),
    path('reset-password-verify/', ResetPasswordVerifyAPIView.as_view(),
         name='reset-password-verify'),
    path('login/', LoginView.as_view(), name='login'), 
    path('', views.home, name='home'),
    path('success/', views.success_msg, name='success_msg'), 
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
