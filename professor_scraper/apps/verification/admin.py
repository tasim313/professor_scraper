from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter
from .models import DataChange, VerificationRecord

@admin.register(DataChange)
class DataChangeAdmin(ImportExportModelAdmin):
    list_display = ('id', 'model_name', 'record_id', 'field_name', 'source_url',)
    search_fields = ('model_name', 'record_id', 'field_name', 'source_url', 'status',)
    list_filter = (('change_date', DateTimeRangeFilter), 'status',)
    list_per_page = 50

@admin.register(VerificationRecord)
class VerificationRecordAdmin(ImportExportModelAdmin):
    list_display = ('id', 'model_name', 'record_id', 'verified_by', 'verification_date',)
    search_fields = ('model_name', 'record_id', 'verified_by', 'confidence_score',)
    list_filter = (('verification_date', DateTimeRangeFilter),)
    list_per_page = 50
