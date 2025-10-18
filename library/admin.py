from django.contrib import admin
from .models import Category, Book

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'section', 'available_copies', 'total_copies', 'is_available']
    list_filter = ['section', 'category', 'published_year']
    search_fields = ['title', 'author', 'isbn']
    list_editable = ['available_copies', 'total_copies', 'category']