from django.db import models
import uuid

class DataChange(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    model_name = models.CharField(max_length=255)
    record_id = models.CharField(max_length=255)
    field_name = models.CharField(max_length=255)
    old_value = models.TextField(null=True, blank=True)
    new_value = models.TextField(null=True, blank=True)
    
    source_url = models.URLField(max_length=1000, blank=True)
    change_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default='PENDING_REVIEW') # PENDING_REVIEW, APPROVED, REJECTED

class VerificationRecord(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    model_name = models.CharField(max_length=255)
    record_id = models.CharField(max_length=255)
    verified_by = models.CharField(max_length=255, blank=True) # Typically a User ID, keep soft link
    verification_date = models.DateTimeField(auto_now_add=True)
    confidence_score = models.CharField(max_length=50, default='HIGH')
    notes = models.TextField(blank=True)
