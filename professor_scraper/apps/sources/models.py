from django.db import models
import uuid

class Source(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    url = models.URLField(max_length=1000, unique=True)
    domain = models.CharField(max_length=255)
    organization = models.CharField(max_length=255, blank=True)
    source_type = models.CharField(max_length=100, help_text="Official University, Government, Secondary")
    source_authority = models.IntegerField(default=1, help_text="1 (Highest) to 6 (Lowest)")
    
    last_checked = models.DateTimeField(null=True, blank=True)
    http_status = models.IntegerField(null=True, blank=True)
    content_hash = models.CharField(max_length=255, blank=True)
    verification_status = models.CharField(max_length=50, default='PENDING')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.url

class SourceSnapshot(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    source = models.ForeignKey(Source, on_delete=models.CASCADE, related_name='snapshots')
    s3_location = models.CharField(max_length=1000, blank=True)
    retrieved_date = models.DateTimeField(auto_now_add=True)
    parser_version = models.CharField(max_length=50, blank=True)
