from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSettingsForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'first_name', 'last_name', 'helpful_advice_set', 'site_theme']

