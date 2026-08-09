from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter
from .models import SubscriptionPlan, UserSubscription

@admin.register(SubscriptionPlan)
class SubscriptionPlanAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'currency', 'billing_cycle', 'created_at',)
    search_fields = ('name', 'currency', 'billing_cycle',)
    list_filter = ('is_active', ('created_at', DateTimeRangeFilter),)
    list_per_page = 50

@admin.register(UserSubscription)
class UserSubscriptionAdmin(ImportExportModelAdmin):
    list_display = ('id', 'start_date', 'end_date', 'stripe_subscription_id',)
    search_fields = ('stripe_subscription_id',)
    list_filter = ('user', 'plan', ('start_date', DateTimeRangeFilter), ('end_date', DateTimeRangeFilter), 'is_active',)
    list_per_page = 50
