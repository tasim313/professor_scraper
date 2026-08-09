from django.db import models
import uuid
from apps.universities.models import University
from apps.departments.models import Department
from apps.professors.models import Professor
from apps.subjects.models import Subject

class ResearchGroup(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=500)
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='research_groups')
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    lead_professor = models.ForeignKey(Professor, on_delete=models.SET_NULL, null=True, blank=True, related_name='led_research_groups')
    website = models.URLField(max_length=1000, blank=True)

class Laboratory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=500)
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='laboratories')
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    director = models.ForeignKey(Professor, on_delete=models.SET_NULL, null=True, blank=True, related_name='directed_labs')
    website = models.URLField(max_length=1000, blank=True)

class ResearchProject(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=500)
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='research_projects')
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=100, blank=True)
