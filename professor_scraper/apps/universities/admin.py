from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter
from .models import University, Campus, UniversityAlias

@admin.register(University)
class UniversityAdmin(ImportExportModelAdmin):
    list_display = ('id', 'canonical_name', 'official_name', 'short_name', 'slug',)
    search_fields = ('canonical_name', 'official_name', 'short_name', 'slug', 'official_domain', 'official_website', 'admissions_url', 'international_student_url', 'institution_type', 'accreditation_status', 'logo_url', 'verification_status',)
    list_filter = ('country', 'city', ('created_at', DateTimeRangeFilter), ('updated_at', DateTimeRangeFilter),)
    list_per_page = 50

@admin.register(Campus)
class CampusAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('name',)
    list_filter = ('university', 'city',)
    list_per_page = 50

@admin.register(UniversityAlias)
class UniversityAliasAdmin(ImportExportModelAdmin):
    list_display = ('id', 'alias',)
    search_fields = ('alias',)
    list_filter = ('university',)
    list_per_page = 50
