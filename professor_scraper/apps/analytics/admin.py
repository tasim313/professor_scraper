from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter
from .models import PageView

@admin.register(PageView)
class PageViewAdmin(ImportExportModelAdmin):
    list_display = ('id', 'path', 'user_agent', 'timestamp',)
    search_fields = ('path', 'user_agent',)
    list_filter = (('timestamp', DateTimeRangeFilter),)
    list_per_page = 50
