import graphene
from graphene_django import DjangoObjectType
from .models import NewsCategory, NewsArticle

class NewsCategoryType(DjangoObjectType):
    class Meta:
        model = NewsCategory
        fields = ("id", "name", "slug", "date_created", "date_updated")

class NewsArticleType(DjangoObjectType):
    class Meta:
        model = NewsArticle
        fields = ("id", "news_category", "title", "media", "body", "slug", "created_at", "date_updated", "views")


class Query(graphene.ObjectType):
    news_categories = graphene.List(NewsCategoryType)
    news_articles = graphene.List(NewsArticleType)
    news_article_by_slug = graphene.Field(NewsArticleType, slug=graphene.String(required=True))
    news_articles_by_category = graphene.List(NewsArticleType, category_slug=graphene.String(required=True))

    def resolve_news_categories(root, info):
        return NewsCategory.objects.all()

    def resolve_news_articles(root, info):
        return NewsArticle.objects.all()

    def resolve_news_article_by_slug(root, info, slug):
        try:
            return NewsArticle.objects.get(slug=slug)
        except NewsArticle.DoesNotExist:
            return None

    def resolve_news_articles_by_category(root, info, category_slug):
        try:
            category = NewsCategory.objects.get(slug=category_slug)
            return NewsArticle.objects.filter(news_category=category)
        except NewsCategory.DoesNotExist:
            return []

schema = graphene.Schema(query=Query)
