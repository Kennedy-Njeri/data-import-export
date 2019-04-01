from django.contrib import admin
from .models import Book
from .models import Author, Category
from import_export.admin import ImportExportModelAdmin



# Register your models here.
@admin.register(Book)
class BookAdmin(ImportExportModelAdmin):
    pass
