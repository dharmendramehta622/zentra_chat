from django.shortcuts import render
from .serializers import NewsCategorySerializer,NewsArticleSerializer
from .models import NewsCategory,NewsArticle
from rest_framework import mixins,viewsets
from rest_framework.exceptions import NotFound
from rest_framework.permissions import  AllowAny

# Create your views here.
class NewsCategoryView(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = NewsCategorySerializer
    authentication_classes = []  # Allow unauthenticated access
    permission_classes = [AllowAny]  # Allow all permissions
    
    def get_queryset(self):
        return NewsCategory.objects.all()

    def get_object(self):
        try:
            return NewsCategory.objects.get(id=self.kwargs['pk'])
        except NewsCategory.DoesNotExist as e:
            raise NotFound({"message": "Data not found"}) from e


class NewsArticleView(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = NewsArticleSerializer
    authentication_classes = []  # Allow unauthenticated access
    permission_classes = [AllowAny]  # Allow all permissions
    
    def get_queryset(self):
        return NewsArticle.objects.all()

    def get_object(self):
        try:
            blog_article = NewsArticle.objects.get(id=self.kwargs['pk'])
            blog_article.views = blog_article.views + 1
            blog_article.save()
            return blog_article
        except NewsArticle.DoesNotExist as e:
            raise NotFound({"message": "Data not found"}) from e

