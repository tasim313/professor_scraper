from django.db import models
import uuid
from apps.universities.models import University
from apps.programs.models import Program

class Ranking(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='rankings', null=True, blank=True)
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='rankings', null=True, blank=True)
    
    ranking_organization = models.CharField(max_length=255)
    year = models.IntegerField()
    position = models.CharField(max_length=50)
    methodology_url = models.URLField(max_length=1000, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Accreditation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='accreditations', null=True, blank=True)
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='accreditations', null=True, blank=True)
    
    body = models.CharField(max_length=255)
    status = models.CharField(max_length=100)
    period = models.CharField(max_length=255, blank=True)
    official_source = models.URLField(max_length=1000, blank=True)
