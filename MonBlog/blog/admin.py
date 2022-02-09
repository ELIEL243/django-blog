from django.contrib import admin
from .models import *


# Register your models here.


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'last_updated', 'published')
    search_fields = ('title',)
    list_per_page = 4
