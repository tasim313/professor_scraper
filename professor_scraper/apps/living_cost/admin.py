from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter
from .models import LivingCost

@admin.register(LivingCost)
class LivingCostAdmin(ImportExportModelAdmin):
    list_display = ('id', 'currency', 'verification_status', 'created_at', 'updated_at',)
    search_fields = ('currency', 'verification_status',)
    list_filter = ('country', 'city', ('created_at', DateTimeRangeFilter), ('updated_at', DateTimeRangeFilter),)
    list_per_page = 50
