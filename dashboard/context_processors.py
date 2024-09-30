from .models import UserBudget, FinanceUser

def budget_balance(request):
    if request.user.is_authenticated:
        try:
            user_budget = UserBudget.objects.get(user=request.user)
            budget_balance = user_budget.budget
            budget = user_budget.budget_archive
        except UserBudget.DoesNotExist:
            budget_balance = 0
            budget = 0
    else:
        budget_balance = None
        budget = 0

    return {'budget_balance': budget_balance, 'budget': budget}

def site_theme(request):
    if request.user.is_authenticated:
        user = request.user
        theme_class = 'dark-theme' if user.site_theme else 'light-theme'
    else:
        theme_class = 'light-theme'

    return {
        'theme_class': theme_class
    }
    return {
        'theme_class': 'dark-theme'
    }