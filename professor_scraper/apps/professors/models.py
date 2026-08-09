from django.db import models
import uuid
from apps.universities.models import University
from apps.departments.models import Department, Faculty
from apps.subjects.models import Subject

class Professor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255, blank=True)
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='professors')
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True, related_name='professors')
    faculty = models.ForeignKey(Faculty, on_delete=models.SET_NULL, null=True, blank=True, related_name='professors')
    
    profile_url = models.URLField(max_length=1000, blank=True)
    official_email = models.EmailField(blank=True)
    
    orcid = models.CharField(max_length=255, blank=True)
    google_scholar_url = models.URLField(max_length=1000, blank=True)
    
    verification_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.name} - {self.university.canonical_name}"

class ProfessorSubject(models.Model):
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name='professor_subjects')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='professor_subjects')
    
    class Meta:
        unique_together = ('professor', 'subject')
