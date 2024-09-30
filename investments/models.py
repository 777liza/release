from django.db import models
from django.conf import settings

class Investments(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    total_margin = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_actives = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    bank_deposit = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    bank_deposit_type = models.BooleanField(default=True)
    bank_deposit_start_date = models.DateField(blank=True, null=True)
    bank_deposit_end_date = models.DateField(blank=True, null=True)

    stocks = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    stocks_type = models.BooleanField(default=True)
    stocks_start_date = models.DateField(blank=True, null=True)
    stocks_end_date = models.DateField(blank=True, null=True)

    bonds = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    bonds_type = models.BooleanField(default=True)
    bonds_start_date = models.DateField(blank=True, null=True)
    bonds_end_date = models.DateField(blank=True, null=True)

    real_estate  = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    real_estate_type = models.BooleanField(default=True)
    real_estate_start_date = models.DateField(blank=True, null=True)
    real_estate_end_date = models.DateField(blank=True, null=True)

    mutual_funds = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    mutual_funds_type = models.BooleanField(default=True)
    mutual_funds_start_date = models.DateField(blank=True, null=True)
    mutual_funds_end_date = models.DateField(blank=True, null=True)
   