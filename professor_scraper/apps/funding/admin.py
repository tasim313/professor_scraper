from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter
from .models import FundingOpportunity, FundingSubject, FundingEligibility

@admin.register(FundingOpportunity)
class FundingOpportunityAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'funding_type', 'amount', 'duration',)
    search_fields = ('name', 'funding_type', 'amount', 'duration', 'official_url', 'verification_status',)
    list_filter = ('university', ('deadline', DateTimeRangeFilter), ('created_at', DateTimeRangeFilter), ('updated_at', DateTimeRangeFilter),)
    list_per_page = 50

@admin.register(FundingSubject)
class FundingSubjectAdmin(ImportExportModelAdmin):
    list_display = ('id',)
    list_filter = ('funding', 'subject',)
    list_per_page = 50

@admin.register(FundingEligibility)
class FundingEligibilityAdmin(ImportExportModelAdmin):
    list_display = ('id',)
    list_filter = ('funding', 'country', 'degree',)
    list_per_page = 50
