from django import forms
from .models import ContactMessage, UserBudget



class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['title', 'message']


class UserBudgetForm(forms.ModelForm):
    class Meta:
        model = UserBudget
        fields = ['budget', 'budget_date_start', 'budget_date_end']

    def init(self, args, **kwargs):
        super(UserBudgetForm, self).init(args, **kwargs)
        # You can add custom validation or widget customization here (optional)
