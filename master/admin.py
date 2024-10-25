from django.contrib import admin
from .models import NewsModel, BlogModel

# Register your models here.
class NewsModelAdmin(admin.ModelAdmin):
    readonly_fields = ("id",)

class BlogModelAdmin(admin.ModelAdmin):
    readonly_fields = ("id",)

admin.site.register(NewsModel, NewsModelAdmin)
admin.site.register(BlogModel, BlogModelAdmin)