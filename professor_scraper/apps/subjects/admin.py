from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter
from .models import Subject, SubjectAlias

@admin.register(Subject)
class SubjectAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'slug', 'created_at', 'updated_at',)
    search_fields = ('name', 'slug',)
    list_filter = ('parent', ('created_at', DateTimeRangeFilter), ('updated_at', DateTimeRangeFilter),)
    list_per_page = 50

@admin.register(SubjectAlias)
class SubjectAliasAdmin(ImportExportModelAdmin):
    list_display = ('id', 'alias',)
    search_fields = ('alias',)
    list_filter = ('subject',)
    list_per_page = 50
