from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter
from .models import SearchQueryLog

@admin.register(SearchQueryLog)
class SearchQueryLogAdmin(ImportExportModelAdmin):
    list_display = ('id', 'query', 'created_at',)
    search_fields = ('query',)
    list_filter = (('created_at', DateTimeRangeFilter),)
    list_per_page = 50
