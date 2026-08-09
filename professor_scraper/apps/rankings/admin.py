from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter
from .models import Ranking, Accreditation

@admin.register(Ranking)
class RankingAdmin(ImportExportModelAdmin):
    list_display = ('id', 'ranking_organization', 'position', 'methodology_url', 'created_at',)
    search_fields = ('ranking_organization', 'position', 'methodology_url',)
    list_filter = ('university', 'program', ('created_at', DateTimeRangeFilter), ('updated_at', DateTimeRangeFilter),)
    list_per_page = 50

@admin.register(Accreditation)
class AccreditationAdmin(ImportExportModelAdmin):
    list_display = ('id', 'body', 'status', 'period', 'official_source',)
    search_fields = ('body', 'status', 'period', 'official_source',)
    list_filter = ('university', 'program', 'status',)
    list_per_page = 50
