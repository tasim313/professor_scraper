from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter
from .models import Professor, ProfessorSubject

@admin.register(Professor)
class ProfessorAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'title', 'profile_url', 'official_email',)
    search_fields = ('name', 'title', 'profile_url', 'official_email', 'orcid', 'google_scholar_url',)
    list_filter = ('university', 'department', 'faculty', ('verification_date', DateTimeRangeFilter), ('created_at', DateTimeRangeFilter), ('updated_at', DateTimeRangeFilter),)
    list_per_page = 50

@admin.register(ProfessorSubject)
class ProfessorSubjectAdmin(ImportExportModelAdmin):
    list_display = ('id',)
    list_filter = ('professor', 'subject',)
    list_per_page = 50
