from django.db import models
import uuid
from apps.universities.models import University
from apps.programs.models import Program
from apps.degrees.models import Degree

class TuitionFee(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='tuition_fees')
    program = models.ForeignKey(Program, on_delete=models.CASCADE, null=True, blank=True, related_name='tuition_fees')
    degree = models.ForeignKey(Degree, on_delete=models.SET_NULL, null=True, blank=True)
    
    student_category = models.CharField(max_length=100, help_text="e.g. Domestic, International")
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    currency = models.CharField(max_length=10)
    billing_period = models.CharField(max_length=50, help_text="per semester, per year, per credit, total")
    academic_year = models.CharField(max_length=20, blank=True)
    
    mandatory_fees = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    
    verification_status = models.CharField(max_length=50, default='PENDING')
    verified_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.amount} {self.currency} {self.billing_period} - {self.university.canonical_name}"
