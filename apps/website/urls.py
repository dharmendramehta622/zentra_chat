from django.urls import include, path
from rest_framework.routers import DefaultRouter
from apps.website import views


router = DefaultRouter()

router.register('', views.index, basename='index')

urlpatterns = [
    # path('',include(router.urls)),
     path('', views.index, name='index'),
]