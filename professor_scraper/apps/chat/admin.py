from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import ChatRoom, ChatMessage, CallSession

@admin.register(ChatRoom)
class ChatRoomAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'is_group', 'created_at')
    search_fields = ('name',)
    list_filter = ('is_group', 'created_at')

@admin.register(ChatMessage)
class ChatMessageAdmin(ImportExportModelAdmin):
    list_display = ('id', 'room', 'sender', 'is_read', 'created_at')
    search_fields = ('text', 'sender__username')
    list_filter = ('is_read', 'created_at')

@admin.register(CallSession)
class CallSessionAdmin(ImportExportModelAdmin):
    list_display = ('id', 'room', 'caller', 'call_type', 'status', 'started_at')
    list_filter = ('call_type', 'status', 'started_at')
