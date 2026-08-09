from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter
from .models import AdmissionRequirement, LanguageRequirement, ApplicationDeadline

@admin.register(AdmissionRequirement)
class AdmissionRequirementAdmin(ImportExportModelAdmin):
    list_display = ('id', 'minimum_gpa', 'minimum_degree_required', 'work_experience_required', 'created_at',)
    search_fields = ('minimum_gpa', 'minimum_degree_required', 'work_experience_required',)
    list_filter = ('program', 'gre_required', 'gmat_required', 'portfolio_required', 'sop_required', 'cv_required', 'research_proposal_required', ('created_at', DateTimeRangeFilter), ('updated_at', DateTimeRangeFilter),)
    list_per_page = 50

@admin.register(LanguageRequirement)
class LanguageRequirementAdmin(ImportExportModelAdmin):
    list_display = ('id', 'test_type', 'minimum_overall_score', 'minimum_subsection_score', 'created_at',)
    search_fields = ('test_type', 'minimum_overall_score', 'minimum_subsection_score',)
    list_filter = ('program', ('created_at', DateTimeRangeFilter), ('updated_at', DateTimeRangeFilter),)
    list_per_page = 50

@admin.register(ApplicationDeadline)
class ApplicationDeadlineAdmin(ImportExportModelAdmin):
    list_display = ('id', 'intake', 'academic_year', 'application_opens', 'priority_deadline',)
    search_fields = ('intake', 'academic_year',)
    list_filter = ('program', ('application_opens', DateTimeRangeFilter), ('priority_deadline', DateTimeRangeFilter), ('regular_deadline', DateTimeRangeFilter), ('final_deadline', DateTimeRangeFilter), ('scholarship_deadline', DateTimeRangeFilter), ('international_deadline', DateTimeRangeFilter), ('created_at', DateTimeRangeFilter), ('updated_at', DateTimeRangeFilter),)
    list_per_page = 50
