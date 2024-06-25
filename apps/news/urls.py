from django.urls import include, path
from rest_framework.routers import DefaultRouter
from apps.news import views


router = DefaultRouter()

router.register('category', views.NewsCategoryView,basename='news-categories')
router.register('news', views.NewsCategoryView,basename='news-articles')

urlpatterns = [
    path('',include(router.urls))
]