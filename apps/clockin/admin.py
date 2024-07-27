from django.contrib import admin
from .models import NewsArticle, NewsCategory

class NewsCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'date_created', 'date_updated')
    list_filter = ('date_created', 'date_updated')
    search_fields = ('name', 'slug')  # Add 'slug' to search_fields if needed

class NewsArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'news_category', 'created_at', 'date_updated', 'views')
    list_filter = ('created_at', 'date_updated', 'news_category')
    search_fields = ('title', 'body')  # Add 'body' to search_fields if needed

# Register your models with the customized admin classes
admin.site.register(NewsArticle, NewsArticleAdmin)
admin.site.register(NewsCategory, NewsCategoryAdmin)    
