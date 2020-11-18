from django.contrib import admin
from .models import Category, Tasks

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display= ['name', 'description', 'owner']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Tasks)
    