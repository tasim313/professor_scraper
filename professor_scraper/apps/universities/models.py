from django.db import models
import uuid
from apps.countries.models import Country, City

class University(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    canonical_name = models.CharField(max_length=255, unique=True)
    official_name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=100, blank=True)
    slug = models.SlugField(max_length=255, unique=True)
    country = models.ForeignKey(Country, on_delete=models.PROTECT, related_name='universities')
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True, related_name='universities')
    official_domain = models.CharField(max_length=255, blank=True)
    official_website = models.URLField(max_length=500, blank=True)
    admissions_url = models.URLField(max_length=500, blank=True)
    international_student_url = models.URLField(max_length=500, blank=True)
    founded_year = models.IntegerField(null=True, blank=True)
    institution_type = models.CharField(max_length=100, blank=True) # Public/Private
    accreditation_status = models.CharField(max_length=255, blank=True)
    student_population = models.IntegerField(null=True, blank=True)
    international_student_population = models.IntegerField(null=True, blank=True)
    description = models.TextField(blank=True)
    logo_url = models.URLField(max_length=500, blank=True)
    verification_status = models.CharField(max_length=50, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Universities"
        ordering = ['canonical_name']

    def __str__(self):
        return self.canonical_name

class Campus(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='campuses')
    name = models.CharField(max_length=255)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return f"{self.university.canonical_name} - {self.name}"

class UniversityAlias(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='aliases')
    alias = models.CharField(max_length=255)

    def __str__(self):
        return self.alias
