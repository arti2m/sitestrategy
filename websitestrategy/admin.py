from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    pass

@admin.register(TypeNews)
class TypeNewsAdmin(admin.ModelAdmin):
    pass

@admin.register(Tags)
class Tags(admin.ModelAdmin):
    pass
