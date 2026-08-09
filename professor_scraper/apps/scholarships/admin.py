from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter
from .models import Scholarship, ScholarshipCountry, ScholarshipDegree, ScholarshipSubject

@admin.register(Scholarship)
class ScholarshipAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'provider', 'funding_type', 'tuition_coverage',)
    search_fields = ('name', 'provider', 'funding_type', 'tuition_coverage', 'stipend', 'accommodation', 'airfare', 'insurance', 'official_url', 'verification_status',)
    list_filter = (('deadline', DateTimeRangeFilter), ('opening_date', DateTimeRangeFilter), ('created_at', DateTimeRangeFilter), ('updated_at', DateTimeRangeFilter),)
    list_per_page = 50

@admin.register(ScholarshipCountry)
class ScholarshipCountryAdmin(ImportExportModelAdmin):
    list_display = ('id',)
    list_filter = ('scholarship', 'country', 'is_destination',)
    list_per_page = 50

@admin.register(ScholarshipDegree)
class ScholarshipDegreeAdmin(ImportExportModelAdmin):
    list_display = ('id',)
    list_filter = ('scholarship', 'degree',)
    list_per_page = 50

@admin.register(ScholarshipSubject)
class ScholarshipSubjectAdmin(ImportExportModelAdmin):
    list_display = ('id',)
    list_filter = ('scholarship', 'subject',)
    list_per_page = 50
