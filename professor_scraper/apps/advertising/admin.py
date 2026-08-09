from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter
from .models import Sponsor, AdPlacement

@admin.register(Sponsor)
class SponsorAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'contact_email', 'website', 'created_at',)
    search_fields = ('name', 'contact_email', 'website',)
    list_filter = ('is_active', ('created_at', DateTimeRangeFilter),)
    list_per_page = 50

@admin.register(AdPlacement)
class AdPlacementAdmin(ImportExportModelAdmin):
    list_display = ('id', 'title', 'image_url', 'target_url', 'placement_zone',)
    search_fields = ('title', 'image_url', 'target_url', 'placement_zone',)
    list_filter = ('sponsor', ('start_date', DateRangeFilter), ('end_date', DateRangeFilter), 'is_active',)
    list_per_page = 50
