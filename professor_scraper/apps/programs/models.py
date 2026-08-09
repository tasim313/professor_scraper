from django.db import models
import uuid
from apps.universities.models import University
from apps.departments.models import Department, Faculty
from apps.degrees.models import Degree
from apps.subjects.models import Subject

class Program(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='programs')
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True, related_name='programs')
    faculty = models.ForeignKey(Faculty, on_delete=models.SET_NULL, null=True, blank=True, related_name='programs')
    degree = models.ForeignKey(Degree, on_delete=models.PROTECT, related_name='programs')
    
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    
    duration = models.CharField(max_length=100, blank=True, help_text="e.g., 2 years, 4 semesters")
    credits = models.CharField(max_length=100, blank=True)
    study_mode = models.CharField(max_length=100, blank=True, help_text="Online, On-campus, Hybrid")
    attendance_mode = models.CharField(max_length=100, blank=True, help_text="Full-time, Part-time")
    language = models.CharField(max_length=100, blank=True, default='English')
    
    application_fee = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    application_fee_currency = models.CharField(max_length=10, blank=True)
    
    scholarship_availability = models.BooleanField(default=False)
    official_url = models.URLField(max_length=1000, blank=True)
    verification_status = models.CharField(max_length=50, default='PENDING')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('university', 'name', 'degree')

    def __str__(self):
        return f"{self.name} ({self.degree.name}) - {self.university.canonical_name}"

class ProgramSubject(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='program_subjects')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='program_subjects')
    is_primary = models.BooleanField(default=False)

    class Meta:
        unique_together = ('program', 'subject')
