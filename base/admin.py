from django.contrib import admin
from . import models




# Register your models here.

@admin.register(models.OnlineBookStore)
class BookStoreAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'publication_date']
    list_per_page = 10
    search_fields = ['title', 'author']
    list_filter = ['title', 'author', 'publication_date' ]