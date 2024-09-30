from django import forms
from .models import Expences

class expencesForm(forms.ModelForm):
    class Meta:
        model = Expences
        fields = [
            'base_expences',
            'base_expences_description',
            'base_expences_start_date', 
            'base_expences_end_date',
            'investment_expences', 
            'additional_expences', 
            'one_time_expences', 
            'update_date'
        ]
        widgets = {
            'base_expences': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter expences'}),
            'base_expences_description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter expences description'}),
            'base_expences_start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'base_expences_end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'investment_expences': forms.NumberInput(attrs={'class': 'form-control'}),
            'additional_expences': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter additional expences as JSON'}),
            'one_time_expences': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter one-time expences as JSON'}),
            'update_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }