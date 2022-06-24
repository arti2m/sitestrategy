from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('header',)}

@admin.register(TypeNews)
class TypeNewsAdmin(admin.ModelAdmin):
    pass

@admin.register(Tags)
class Tags(admin.ModelAdmin):
    pass

@admin.register(TagsChronic)
class TagsChronic(admin.ModelAdmin):
    pass

@admin.register(Chronic)
class Chronic(admin.ModelAdmin):
    pass

@admin.register(TagsArticle)
class TagsArticle(admin.ModelAdmin):
    pass

@admin.register(Article)
class Article(admin.ModelAdmin):
    pass
