from django.shortcuts import render, redirect 
from django.http import JsonResponse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
from django.views.decorators.http import require_POST
from decimal import Decimal
from django.utils import timezone
from income.models import Income
from expences.models import Expences
from dashboard.models import UserBudget
from django.contrib.auth import logout


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    
def custom_logout(request):
    if request.method == 'POST':
        import requests
        try:
            requests.post('/accounts/logout/', data={'user_id': request.user.id})
        except requests.RequestException:
            pass
    logout(request)
    return redirect(reverse_lazy('home_page'))

def policy(request):
    return render(request, 'pages/policy.html')

def about(request):
    return render(request, 'pages/about.html')


def contact(request):
    return render(request, 'pages/contact_us.html')

def terms(request):
    return render(request, 'pages/terms.html')

def home(request):
    return render(request, 'pages/home_page.html')

	
@login_required
@require_POST
def espress_add(request):
    income_once = request.POST.get('income_once')
    income_description = request.POST.get('income_description')
    expences_once = request.POST.get('expences_once')
    expences_description = request.POST.get('expences_description')

    try:
        income_once = float(income_once)
        expences_once = float(expences_once)
    except ValueError:
        return JsonResponse({'error': 'Invalid income or expenses value'}, status=400)

    try:
        user_budget = UserBudget.objects.filter(user=request.user).first()
    except UserBudget.DoesNotExist:
        return JsonResponse({'error': 'User budget not found'}, status=400)

    income, created = Income.objects.get_or_create(user=request.user)
    expense, created = Expences.objects.get_or_create(user=request.user)

    user_budget.budget += Decimal(income_once)
    user_budget.budget -= Decimal(expences_once)

    existing_incomes = income.one_time_incomes or []
    existing_expense = expense.one_time_expences or []

    new_income = {
        "amount": str(Decimal(request.POST.get('income_once'))),  # Преобразование в строку
        "description": request.POST.get('income_description'),
        "end_date": timezone.now().strftime("%Y-%m-%d"),
        "start_date": timezone.now().strftime("%Y-%m-%d")
    }

    new_expense = {
        "amount": str(Decimal(request.POST.get('expences_once'))),  # Преобразование в строку
        "description": request.POST.get('expences_description'),
        "end_date": timezone.now().strftime("%Y-%m-%d"),
        "start_date": timezone.now().strftime("%Y-%m-%d")
    }

    existing_incomes.append(new_income)
    existing_expense.append(new_expense)

    income.one_time_incomes = existing_incomes
    expense.one_time_expences = existing_expense

    income.save()
    expense.save()
    user_budget.save()

    return JsonResponse({'success': 'Budget updated', 'budget_balance': user_budget.budget})


def custom_404(request, exception):
    return render(request, '404.html', status=404)
    
