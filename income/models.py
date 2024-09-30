from django.db import models
from django.conf import settings

class Income(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    total_income = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    base_income = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    base_income_description = models.CharField(max_length=100)
    base_income_start_date = models.DateField(blank=True, null=True)
    base_income_end_date = models.DateField(blank=True, null=True)
    investment_income = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    additional_incomes = models.JSONField(blank=True, null=True)
    one_time_incomes = models.JSONField(blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)