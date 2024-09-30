from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from dashboard.models import FinanceUser
class CustomUserCreationForm(UserCreationForm):
	class Meta:
		model = FinanceUser
		fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):
	class Meta:
		model = FinanceUser
		fields = ('username', 'email')



