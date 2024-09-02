from django.contrib import admin
from .models import Contact
from .models import Book

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message', 'created_at')
    search_fields = ('name', 'email', 'subject')

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_added')
    ordering = ('-date_added',)