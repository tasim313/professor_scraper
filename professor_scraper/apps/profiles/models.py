from django.db import models
from django.contrib.auth.models import User
import uuid

class UserProfile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    headline = models.CharField(max_length=255, blank=True, null=True, help_text="e.g. PhD Candidate at MIT | AI Researcher")
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.URLField(max_length=500, blank=True, null=True) # Usually an ImageField, using URL for simplicity
    location = models.CharField(max_length=255, blank=True, null=True)
    website = models.URLField(max_length=500, blank=True, null=True)
    github_url = models.URLField(max_length=500, blank=True, null=True)
    linkedin_url = models.URLField(max_length=500, blank=True, null=True)
    google_scholar_url = models.URLField(max_length=500, blank=True, null=True)
    is_public = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Profile: {self.user.username}"

class UserEducation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='education')
    institution = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    field_of_study = models.CharField(max_length=255)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True, null=True)

class UserExperience(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='experience')
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255, blank=True, null=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    is_current = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True)

class UserPublication(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='publications')
    title = models.CharField(max_length=500)
    journal_conference = models.CharField(max_length=255, blank=True, null=True)
    publication_date = models.DateField(null=True, blank=True)
    url = models.URLField(max_length=500, blank=True, null=True)
    abstract = models.TextField(blank=True, null=True)

class UserDocument(models.Model):
    """For uploading CVs, Transcripts, Research Papers, etc."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='documents')
    title = models.CharField(max_length=255)
    document_type = models.CharField(max_length=50, choices=[('CV', 'CV/Resume'), ('TRANSCRIPT', 'Transcript'), ('PAPER', 'Research Paper'), ('OTHER', 'Other')], default='OTHER')
    file = models.FileField(upload_to='user_documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
