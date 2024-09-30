from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils import timezone


class FinanceUser(AbstractUser):
    helpful_advice_set = models.BooleanField(default=False)
    site_theme = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to='avatars/', blank=True)

    def get_avatar_url(self):
        if self.avatar:
            return settings.MEDIA_URL + self.avatar.name
        return settings.STATIC_URL + 'default_avatar.png'
    
class Meta:
			verbose_name = 'Finance User'
			verbose_name_plural = 'Finance Users'

groups = models.ManyToManyField(
			'auth.Group',
			related_name='finance_users',
			blank=True,
			help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
			verbose_name='groups',
		)
user_permissions = models.ManyToManyField(
			'auth.Permission',
			related_name='finance_users',
			blank=True,
			help_text='Specific permissions for this user.',
			verbose_name='user permissions',
		)
		

class ContactMessage(models.Model):
    message_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(null=True, blank=True)
    title = models.CharField(max_length=200)
    message = models.TextField()
    date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.title

class UserInputData(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    income_inputs = models.TextField()  # Consider using JSONField for structured data
    invest_inputs = models.TextField()  # Consider using JSONField for structured data
    expenses_inputs = models.TextField()  # Consider using JSONField for structured data

class UserBudget(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    budget = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    budget_date_start = models.DateField()
    budget_date_end = models.DateField()
    budget_archive = models.TextField()

class UserDailyFinance(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)

    daily_total_income = models.JSONField(default=dict)
    daily_one_time_earnings = models.JSONField(default=dict)
    daily_additional_income = models.JSONField(default=dict)

    daily_total_invest = models.JSONField(default=dict)
    daily_total_actives = models.JSONField(default=dict)
    daily_total_margin = models.JSONField(default=dict)

    daily_total_expenses = models.JSONField(default=dict)
    daily_total_once_expenses = models.JSONField(default=dict)
    daily_total_additional = models.JSONField(default=dict)
