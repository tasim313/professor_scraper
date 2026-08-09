from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter
from .models import Faculty, Department

@admin.register(Faculty)
class FacultyAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'dean', 'website', 'created_at',)
    search_fields = ('name', 'dean', 'website',)
    list_filter = ('university', ('created_at', DateTimeRangeFilter), ('updated_at', DateTimeRangeFilter),)
    list_per_page = 50

@admin.register(Department)
class DepartmentAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'website', 'created_at', 'updated_at',)
    search_fields = ('name', 'website',)
    list_filter = ('university', 'faculty', ('created_at', DateTimeRangeFilter), ('updated_at', DateTimeRangeFilter),)
    list_per_page = 50
