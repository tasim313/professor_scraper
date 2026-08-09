from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter
from .models import ResearchGroup, Laboratory, ResearchProject

@admin.register(ResearchGroup)
class ResearchGroupAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'website',)
    search_fields = ('name', 'website',)
    list_filter = ('university', 'department', 'lead_professor',)
    list_per_page = 50

@admin.register(Laboratory)
class LaboratoryAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'website',)
    search_fields = ('name', 'website',)
    list_filter = ('university', 'department', 'director',)
    list_per_page = 50

@admin.register(ResearchProject)
class ResearchProjectAdmin(ImportExportModelAdmin):
    list_display = ('id', 'title', 'start_date', 'end_date', 'status',)
    search_fields = ('title', 'status',)
    list_filter = ('university', ('start_date', DateRangeFilter), ('end_date', DateRangeFilter), 'status',)
    list_per_page = 50
