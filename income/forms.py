from django import forms
from .models import Income

class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = [
            'base_income',
            'base_income_description',
            'base_income_start_date', 
            'base_income_end_date',
            'investment_income', 
            'additional_incomes', 
            'one_time_incomes', 
            'update_date'
        ]
        widgets = {
            'base_income': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter income'}),
            'base_income_description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter income description'}),
            'base_income_start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'base_income_end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'investment_income': forms.NumberInput(attrs={'class': 'form-control'}),
            'additional_incomes': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter additional incomes as JSON'}),
            'one_time_incomes': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter one-time incomes as JSON'}),
            'update_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }