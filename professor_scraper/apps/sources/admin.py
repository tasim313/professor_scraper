from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter
from .models import Source, SourceSnapshot

@admin.register(Source)
class SourceAdmin(ImportExportModelAdmin):
    list_display = ('id', 'url', 'domain', 'organization', 'source_type',)
    search_fields = ('url', 'domain', 'organization', 'source_type', 'content_hash', 'verification_status',)
    list_filter = (('last_checked', DateTimeRangeFilter), ('created_at', DateTimeRangeFilter), ('updated_at', DateTimeRangeFilter),)
    list_per_page = 50

@admin.register(SourceSnapshot)
class SourceSnapshotAdmin(ImportExportModelAdmin):
    list_display = ('id', 's3_location', 'retrieved_date', 'parser_version',)
    search_fields = ('s3_location', 'parser_version',)
    list_filter = ('source', ('retrieved_date', DateTimeRangeFilter),)
    list_per_page = 50
