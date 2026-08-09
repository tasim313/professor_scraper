from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter
from .models import ScraperSource, ScraperJob, ScraperResult

@admin.register(ScraperSource)
class ScraperSourceAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'adapter_class',)
    search_fields = ('name', 'adapter_class',)
    list_filter = ('is_active',)
    list_per_page = 50

@admin.register(ScraperJob)
class ScraperJobAdmin(ImportExportModelAdmin):
    list_display = ('id', 'status', 'started_at', 'completed_at',)
    search_fields = ('status',)
    list_filter = ('scraper_source', 'status', ('started_at', DateTimeRangeFilter), ('completed_at', DateTimeRangeFilter),)
    list_per_page = 50

@admin.register(ScraperResult)
class ScraperResultAdmin(ImportExportModelAdmin):
    list_display = ('id', 'created_at',)
    list_filter = ('job', 'source', 'is_processed', ('created_at', DateTimeRangeFilter),)
    list_per_page = 50
