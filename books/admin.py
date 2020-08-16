from django.contrib import admin
from .models import Book, Category


class BookAdmin(admin.ModelAdmin):
    list_display = (
        'isbn13',
        'isbn10',
        'title',
        'author',
        'category',
        'price',
        'book_format',
        'rating',
        'image',
    )

    ordering = ('isbn13',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Book, BookAdmin)
admin.site.register(Category, CategoryAdmin)