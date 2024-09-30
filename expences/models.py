from django.db import models
from django.core.exceptions import ValidationError
from django.conf import settings

class Expences(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    total_expences = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    base_expences = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    base_expences_description = models.CharField(max_length=100)
    base_expences_start_date = models.DateField(blank=True, null=True)
    base_expences_end_date = models.DateField(blank=True, null=True)
    investment_expences = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    additional_expences = models.JSONField(blank=True, null=True)
    one_time_expences = models.JSONField(blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)
