from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
class NewsCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('name',)
        verbose_name = 'news category'
        verbose_name_plural = 'news categories'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, allow_unicode=True)
        super(NewsCategory, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('news-categories', kwargs={'slug': self.slug})


class NewsArticle(models.Model):
    news_category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    media = models.FileField(upload_to='news/')
    body =models.TextField(   max_length=50000,null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now=True)
    views = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ("title",)
        ordering = ('-created_at',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news-articles', kwargs={'slug': self.slug})

