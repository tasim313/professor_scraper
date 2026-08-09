from django.db import models
import uuid
from apps.countries.models import Country
from apps.universities.models import University
from apps.degrees.models import Degree
from apps.subjects.models import Subject

class Scholarship(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=500)
    provider = models.CharField(max_length=255, blank=True)
    
    funding_type = models.CharField(max_length=100, blank=True, help_text="Fully Funded, Partially Funded, Tuition Only")
    tuition_coverage = models.CharField(max_length=255, blank=True)
    stipend = models.CharField(max_length=255, blank=True)
    accommodation = models.CharField(max_length=255, blank=True)
    airfare = models.CharField(max_length=255, blank=True)
    insurance = models.CharField(max_length=255, blank=True)
    
    deadline = models.DateTimeField(null=True, blank=True)
    opening_date = models.DateTimeField(null=True, blank=True)
    
    eligibility_requirements = models.TextField(blank=True)
    application_procedure = models.TextField(blank=True)
    official_url = models.URLField(max_length=1000, blank=True)
    verification_status = models.CharField(max_length=50, default='PENDING')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class ScholarshipCountry(models.Model):
    scholarship = models.ForeignKey(Scholarship, on_delete=models.CASCADE, related_name='target_countries')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='scholarships')
    is_destination = models.BooleanField(default=True, help_text="True if studying in this country. False if eligible nationality.")

    class Meta:
        unique_together = ('scholarship', 'country', 'is_destination')

class ScholarshipDegree(models.Model):
    scholarship = models.ForeignKey(Scholarship, on_delete=models.CASCADE, related_name='scholarship_degrees')
    degree = models.ForeignKey(Degree, on_delete=models.CASCADE, related_name='scholarships')

    class Meta:
        unique_together = ('scholarship', 'degree')

class ScholarshipSubject(models.Model):
    scholarship = models.ForeignKey(Scholarship, on_delete=models.CASCADE, related_name='scholarship_subjects')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='scholarships')

    class Meta:
        unique_together = ('scholarship', 'subject')
