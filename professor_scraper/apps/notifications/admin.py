from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter
from .models import Notification

@admin.register(Notification)
class NotificationAdmin(ImportExportModelAdmin):
    list_display = ('id', 'title', 'link', 'created_at',)
    search_fields = ('title', 'link',)
    list_filter = ('user', 'is_read', ('created_at', DateTimeRangeFilter),)
    list_per_page = 50
