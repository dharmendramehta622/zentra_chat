from django.urls import include, path,re_path
from rest_framework.routers import DefaultRouter
from apps.website.views import UserViewSet,OnboardView


router = DefaultRouter()

router = DefaultRouter()
router.register('', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path('onboard/<uuid:user_id>/', OnboardView.as_view(), name='onboard'),
]