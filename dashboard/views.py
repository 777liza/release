from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import ContactForm, UserBudgetForm
from .models import ContactMessage, UserBudget, UserDailyFinance
from finance.text_constants import DASHBOARD_PAGE, THANKS_PAGE, CONTACT_US_PAGE, BUDGET_PAGE
from income.models import Income
from expences.models import Expences
from investments.models import Investments

#dashboard page

def index(request):
    if request.user.is_authenticated:
        user = request.user
        incomes = Income.objects.filter(user=user)
        investments = Investments.objects.filter(user=user)
        expences = Expences.objects.filter(user=user)

        income_data = []
        for income in incomes:
            one_time_incomes = income.one_time_incomes if income.one_time_incomes else []
            one_time_incomes.reverse()
            income_data.append({
                'total_income' : income.total_income,
                'investment_income': income.investment_income,
                'additional_incomes': income.additional_incomes[:3] if income.additional_incomes else [],
                'one_time_incomes': one_time_incomes[:3] if one_time_incomes else [],
            })

        expences_data = [] 
        for expence in expences:
            one_time_expences = expence.one_time_expences if expence.one_time_expences else []
            one_time_expences.reverse()
            expences_data.append({
                'total_expences': expence.total_expences,
                'base_expences': expence.base_expences,
                'base_expences_description': expence.base_expences_description,
                'base_expences_start': expence.base_expences_start_date,
                'base_expences_end': expence.base_expences_end_date,
                'investment_expences': expence.investment_expences,
                'additional_expences': expence.additional_expences[:3] if expence.additional_expences else [],
                'one_time_expences': one_time_expences[:3] if one_time_expences else [],
                'update_date': expence.update_date,
            })

        investments_data = []
        investments = Investments.objects.filter(user=request.user).first()
        if investments:
            investments_data.append({
                'bank_deposit': investments.bank_deposit,
                'bank_deposit_start_date': investments.bank_deposit_start_date,
                'bank_deposit_end_date': investments.bank_deposit_end_date,
                'stocks': investments.stocks,
                'stocks_start_date': investments.stocks_start_date,
                'stocks_end_date': investments.stocks_end_date,
                'bonds': investments.bonds,
                'bonds_start_date': investments.bonds_start_date,
                'bonds_end_date': investments.bonds_end_date,
                'real_estate': investments.real_estate,
                'real_estate_start_date': investments.real_estate_start_date,
                'real_estate_end_date': investments.real_estate_end_date,
                'mutual_funds': investments.mutual_funds,
                'mutual_funds_start_date': investments.mutual_funds_start_date,
                'mutual_funds_end_date': investments.mutual_funds_end_date,
            })
        
        context = {
            'income_data' : income_data,
            'total_income': income_data[0]['total_income'] if income_data else 0,
		    'total_expences': expences_data[0]['total_expences'] if expences_data else 0,
            'investments_data' : investments,
            'expences_data' : expences_data,
            'dashboard_page' : DASHBOARD_PAGE,
            }
        return render(request, 'dashboard/dashboard.html',context)
    else:
        return HttpResponseRedirect('home')
    

@login_required
def thanks(request):
    context = {
        'thanks_page' : THANKS_PAGE,
    }
    return render(request, 'pages/thanks.html', context )

# contact us page
@login_required
def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_message = form.save(commit=False)
            contact_message.user_id = 1
            contact_message.save()
            return HttpResponseRedirect('/thanks/')
    else:
        form = ContactForm()
        messages = None
    if request.user.is_staff:
        messages = ContactMessage.objects.all()

    context = {
        'form': form,
        'messages': messages,
        'contact_us_page' : CONTACT_US_PAGE,
    }
    return render(request, 'dashboard/contact_us.html', context)

@login_required
def budget(request):
    user = request.user

    try:
        existing_budget = UserBudget.objects.filter(user=user).first()
    except UserBudget.DoesNotExist:
        existing_budget = None

    if request.method == 'POST':
        form = UserBudgetForm(request.POST, instance=existing_budget)
        if form.is_valid():
            budget_data = form.save(commit=False)
            budget_data.user = user
            budget_data.budget_archive = request.POST.get('budget')
            budget_data.save()

            context = {
                'budget_archive' : existing_budget.budget_archive if existing_budget else None,
                'existing_budget' : budget_data,
                'budget_page': BUDGET_PAGE,
                'form': form
            }
            return render(request, 'dashboard/budget.html', context)
    else:
        form = UserBudgetForm(instance=existing_budget)
    
    # Определение context вне блока if, чтобы он был доступен в любом случае
    context = {
        'budget_archive' : existing_budget.budget_archive if existing_budget else None,
        'existing_budget' : existing_budget,
        'budget_page': BUDGET_PAGE,
        'form': form
    }

    return render(request, 'dashboard/budget.html', context)


