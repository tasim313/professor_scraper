from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter
from .models import Country, City

@admin.register(Country)
class CountryAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'iso_code', 'continent', 'currency',)
    search_fields = ('name', 'iso_code', 'continent', 'currency',)
    list_filter = (('created_at', DateTimeRangeFilter), ('updated_at', DateTimeRangeFilter),)
    list_per_page = 50

@admin.register(City)
class CityAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'region', 'created_at', 'updated_at',)
    search_fields = ('name', 'region',)
    list_filter = ('country', ('created_at', DateTimeRangeFilter), ('updated_at', DateTimeRangeFilter),)
    list_per_page = 50
