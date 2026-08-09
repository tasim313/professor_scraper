from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter
from .models import Program, ProgramSubject

@admin.register(Program)
class ProgramAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'slug', 'duration', 'credits',)
    search_fields = ('name', 'slug', 'duration', 'credits', 'study_mode', 'attendance_mode', 'language', 'application_fee_currency', 'official_url', 'verification_status',)
    list_filter = ('university', 'department', 'faculty', 'degree', 'scholarship_availability', ('created_at', DateTimeRangeFilter), ('updated_at', DateTimeRangeFilter),)
    list_per_page = 50

@admin.register(ProgramSubject)
class ProgramSubjectAdmin(ImportExportModelAdmin):
    list_display = ('id',)
    list_filter = ('program', 'subject', 'is_primary',)
    list_per_page = 50
