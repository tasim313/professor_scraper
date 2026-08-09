from django.db import models
import uuid

class Degree(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True) # e.g., Master's, PhD, Bachelor's
    slug = models.SlugField(max_length=255, unique=True)
    level = models.IntegerField(help_text="Numeric level for sorting, e.g. 1 for Certificate, 4 for Bachelor's, 5 for Master's, 6 for PhD", default=0)

    class Meta:
        ordering = ['level']

    def __str__(self):
        return self.name
