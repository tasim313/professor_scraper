from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter
from .models import Subscriber, NewsletterCampaign

@admin.register(Subscriber)
class SubscriberAdmin(ImportExportModelAdmin):
    list_display = ('id', 'email', 'first_name', 'subscribed_at',)
    search_fields = ('email', 'first_name',)
    list_filter = ('is_active', ('subscribed_at', DateTimeRangeFilter),)
    list_per_page = 50

@admin.register(NewsletterCampaign)
class NewsletterCampaignAdmin(ImportExportModelAdmin):
    list_display = ('id', 'subject', 'sent_at', 'status', 'created_at',)
    search_fields = ('subject', 'status',)
    list_filter = (('sent_at', DateTimeRangeFilter), 'status', ('created_at', DateTimeRangeFilter),)
    list_per_page = 50
