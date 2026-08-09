from django.db import models
import uuid

class Subscriber(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)
    interests = models.JSONField(default=list, help_text="e.g., ['PhD', 'Computer Science', 'Canada']")
    
    def __str__(self):
        return self.email

class NewsletterCampaign(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    subject = models.CharField(max_length=255)
    content = models.TextField()
    sent_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=50, choices=[('DRAFT', 'Draft'), ('SCHEDULED', 'Scheduled'), ('SENT', 'Sent')], default='DRAFT')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.subject
