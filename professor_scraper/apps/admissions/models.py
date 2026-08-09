from django.db import models
import uuid
from apps.programs.models import Program

class AdmissionRequirement(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='admission_requirements')
    minimum_gpa = models.CharField(max_length=50, blank=True)
    minimum_degree_required = models.CharField(max_length=255, blank=True)
    prerequisite_courses = models.TextField(blank=True)
    work_experience_required = models.CharField(max_length=255, blank=True)
    gre_required = models.BooleanField(default=False, null=True)
    gmat_required = models.BooleanField(default=False, null=True)
    portfolio_required = models.BooleanField(default=False, null=True)
    sop_required = models.BooleanField(default=False, null=True)
    cv_required = models.BooleanField(default=False, null=True)
    recommendation_letters = models.IntegerField(default=0)
    research_proposal_required = models.BooleanField(default=False, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class LanguageRequirement(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='language_requirements')
    test_type = models.CharField(max_length=100, help_text="e.g. IELTS, TOEFL, PTE")
    minimum_overall_score = models.CharField(max_length=50)
    minimum_subsection_score = models.CharField(max_length=50, blank=True)
    waiver_conditions = models.TextField(blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ApplicationDeadline(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='deadlines')
    intake = models.CharField(max_length=100, help_text="e.g. Fall, Spring, Summer")
    academic_year = models.CharField(max_length=50, blank=True)
    
    application_opens = models.DateTimeField(null=True, blank=True)
    priority_deadline = models.DateTimeField(null=True, blank=True)
    regular_deadline = models.DateTimeField(null=True, blank=True)
    final_deadline = models.DateTimeField(null=True, blank=True)
    scholarship_deadline = models.DateTimeField(null=True, blank=True)
    international_deadline = models.DateTimeField(null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
