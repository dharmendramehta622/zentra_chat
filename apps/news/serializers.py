from rest_framework import serializers
from apps.news.models import NewsCategory,NewsArticle
 

class NewsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsCategory
        fields = "__all__"


class NewsArticleSerializer(serializers.ModelSerializer):
    blog_category = NewsCategorySerializer(required=True)
    class Meta:
        model = NewsArticle
        fields = [
            "id",
            "title",
            "slug",
            "featured_image",
            "body",
            "created_at",
            "date_updated",
            "blog_category",
            'views'
        ]


 