from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter
from .models import TuitionFee

@admin.register(TuitionFee)
class TuitionFeeAdmin(ImportExportModelAdmin):
    list_display = ('id', 'student_category', 'currency', 'billing_period', 'academic_year',)
    search_fields = ('student_category', 'currency', 'billing_period', 'academic_year', 'verification_status',)
    list_filter = ('university', 'program', 'degree', ('verified_date', DateTimeRangeFilter), ('created_at', DateTimeRangeFilter), ('updated_at', DateTimeRangeFilter),)
    list_per_page = 50
