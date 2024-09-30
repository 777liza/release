from django import forms
from .models import Investments

class InvestmentsForm(forms.ModelForm):
    class Meta:
        model = Investments
        fields = [
            'bank_deposit', 'bank_deposit_type', 
            'bank_deposit_start_date', 'bank_deposit_end_date', 'stocks', 
            'stocks_type', 'stocks_start_date', 'stocks_end_date', 'bonds', 
            'bonds_type', 'bonds_start_date', 'bonds_end_date', 'real_estate', 
            'real_estate_type', 'real_estate_start_date', 'real_estate_end_date', 
            'mutual_funds', 'mutual_funds_type', 'mutual_funds_start_date', 
            'mutual_funds_end_date'
        ]
        widgets = {
            'bank_deposit': forms.NumberInput(attrs={'class': 'form-control'}),
            'bank_deposit_type': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'bank_deposit_start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'bank_deposit_end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'stocks': forms.NumberInput(attrs={'class': 'form-control'}),
            'stocks_type': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'stocks_start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'stocks_end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'bonds': forms.NumberInput(attrs={'class': 'form-control'}),
            'bonds_type': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'bonds_start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'bonds_end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'real_estate': forms.NumberInput(attrs={'class': 'form-control'}),
            'real_estate_type': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'real_estate_start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'real_estate_end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'mutual_funds': forms.NumberInput(attrs={'class': 'form-control'}),
            'mutual_funds_type': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'mutual_funds_start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'mutual_funds_end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }