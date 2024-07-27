from django.urls import include, path
from rest_framework.routers import DefaultRouter
from apps.clockin import views


router = DefaultRouter()

router.register('clockin', views.ClockInView,basename='clockin')

urlpatterns = [
    path('',include(router.urls))
]