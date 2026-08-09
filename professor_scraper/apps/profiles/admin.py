from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import UserProfile, UserEducation, UserExperience, UserPublication, UserDocument

@admin.register(UserProfile)
class UserProfileAdmin(ImportExportModelAdmin):
    list_display = ('user', 'headline', 'location', 'is_public', 'created_at')
    search_fields = ('user__username', 'user__email', 'headline', 'location')
    list_filter = ('is_public', 'created_at')

@admin.register(UserEducation)
class UserEducationAdmin(ImportExportModelAdmin):
    list_display = ('profile', 'institution', 'degree', 'field_of_study')

@admin.register(UserExperience)
class UserExperienceAdmin(ImportExportModelAdmin):
    list_display = ('profile', 'title', 'company', 'is_current')

@admin.register(UserPublication)
class UserPublicationAdmin(ImportExportModelAdmin):
    list_display = ('profile', 'title', 'journal_conference', 'publication_date')

@admin.register(UserDocument)
class UserDocumentAdmin(ImportExportModelAdmin):
    list_display = ('profile', 'title', 'document_type', 'is_public')
