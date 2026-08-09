from django.db import models
import uuid
from apps.sources.models import Source

class ScraperSource(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    adapter_class = models.CharField(max_length=255, help_text="e.g. scrapers.university.example.ExampleScraper")
    is_active = models.BooleanField(default=True)
    priority = models.IntegerField(default=1)

class ScraperJob(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    scraper_source = models.ForeignKey(ScraperSource, on_delete=models.CASCADE, related_name='jobs')
    status = models.CharField(max_length=50, default='QUEUED') # QUEUED, RUNNING, COMPLETED, FAILED
    started_at = models.DateTimeField(null=True, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    records_processed = models.IntegerField(default=0)
    error_message = models.TextField(blank=True)

class ScraperResult(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    job = models.ForeignKey(ScraperJob, on_delete=models.CASCADE, related_name='results')
    source = models.ForeignKey(Source, on_delete=models.SET_NULL, null=True, blank=True)
    raw_data = models.JSONField(blank=True, null=True)
    is_processed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
