from django.db import models
import uuid
from apps.countries.models import Country
from apps.universities.models import University
from apps.degrees.models import Degree
from apps.subjects.models import Subject

class FundingOpportunity(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=500)
    funding_type = models.CharField(max_length=200, help_text="Fellowship, Research Grant, Teaching Assistantship, etc.")
    university = models.ForeignKey(University, on_delete=models.CASCADE, null=True, blank=True, related_name='funding_opportunities')
    
    amount = models.CharField(max_length=255, blank=True)
    duration = models.CharField(max_length=100, blank=True)
    deadline = models.DateTimeField(null=True, blank=True)
    official_url = models.URLField(max_length=1000, blank=True)
    description = models.TextField(blank=True)
    
    verification_status = models.CharField(max_length=50, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class FundingSubject(models.Model):
    funding = models.ForeignKey(FundingOpportunity, on_delete=models.CASCADE, related_name='funding_subjects')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='funding_opportunities')

class FundingEligibility(models.Model):
    funding = models.ForeignKey(FundingOpportunity, on_delete=models.CASCADE, related_name='eligibilities')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True)
    degree = models.ForeignKey(Degree, on_delete=models.CASCADE, null=True, blank=True)
