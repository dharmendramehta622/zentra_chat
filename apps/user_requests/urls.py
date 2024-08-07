from django.urls import include, path
from rest_framework.routers import DefaultRouter
from apps.user_requests import views


router = DefaultRouter()

router.register('', views.UserRequestView,basename='user-requests')

urlpatterns = [
    path('',include(router.urls))
]