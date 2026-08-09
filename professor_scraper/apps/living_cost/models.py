from django.db import models
import uuid
from apps.countries.models import Country, City

class LivingCost(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='living_costs')
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True, blank=True, related_name='living_costs')
    
    currency = models.CharField(max_length=10)
    
    # Costs are typically stored as a range or a specific estimated average
    accommodation_min = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    accommodation_max = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    food_min = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    food_max = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    transport_estimate = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    utilities_estimate = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    internet_estimate = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    healthcare_estimate = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    misc_estimate = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    student_monthly_min = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    student_monthly_max = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    methodology = models.TextField(blank=True)
    verification_status = models.CharField(max_length=50, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.city:
            return f"Living Cost for {self.city.name}, {self.country.name}"
        return f"Living Cost for {self.country.name}"
