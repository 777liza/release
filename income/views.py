from django.shortcuts import render,  redirect
from django.contrib.auth.decorators import login_required
from .models import Income
from .forms import IncomeForm
from decimal import Decimal, InvalidOperation
from finance.text_constants import INCOME_PAGE, INCOME_MANAGE_PAGE

@login_required
def income_index(request):
    incomes = Income.objects.filter(user=request.user)
    def calculate_total(incomes, field_name):
        total = 0
        for income in incomes:
            for item in getattr(income, field_name):
                total += round(float(item['amount']), 1)
        return total
    
    income_data = []
    for income in incomes:
        income.one_time_incomes.reverse()
        income_data.append({
            'total_income': income.total_income,
            'base_income': income.base_income,
            'base_income_description': income.base_income_description,
            'base_income_start': income.base_income_start_date,
            'base_income_end': income.base_income_end_date,
            'investment_income': income.investment_income,
            'additional_incomes': income.additional_incomes,
            'one_time_incomes': income.one_time_incomes,
            'update_date': income.update_date,
        })

    total_additional_incomes = calculate_total(incomes, 'additional_incomes')
    total_one_time_incomes = calculate_total(incomes, 'one_time_incomes')
    
    context = {
        'total_additional_incomes' : total_additional_incomes,
        'total_one_time_incomes' : total_one_time_incomes,
        'income_data': income_data,
        'total_income': income_data[0]['total_income']  if income_data else 0,
        'income_page' : INCOME_PAGE,
    }
    return render(request, 'income/index.html', context)

@login_required
def income_manage(request):

    income, created = Income.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = IncomeForm(request.POST, instance=income)
        
        if form.is_valid():
            additional_incomes = []
            one_time_incomes = []
            
            additional_amounts = request.POST.getlist('additional_income[]')
            additional_descriptions = request.POST.getlist('additional_income_description[]')
            additional_start_dates = request.POST.getlist('additional_income_start[]')
            additional_end_dates = request.POST.getlist('additional_income_end[]')

            one_time_amounts = request.POST.getlist('one_time_income[]')
            one_time_descriptions = request.POST.getlist('one_time_income_description[]')
            one_time_start_dates = request.POST.getlist('one_time_income_start[]')
            one_time_end_dates = request.POST.getlist('one_time_income_end[]')

            total_income = Decimal('0.00')

            for amount, description, start_date, end_date in zip(additional_amounts, additional_descriptions, additional_start_dates, additional_end_dates):
                if amount:
                    try:
                        amount_decimal = Decimal(amount)
                        additional_incomes.append({
                            'amount': amount,
                            'description': description,
                            'start_date': start_date,
                            'end_date': end_date
                        })
                        total_income += amount_decimal
                    except InvalidOperation:
                        pass

            for amount, description, start_date, end_date in zip(one_time_amounts, one_time_descriptions, one_time_start_dates, one_time_end_dates):
                if amount:
                    try:
                        amount_decimal = Decimal(amount)
                        one_time_incomes.append({
                            'amount': amount,
                            'description': description,
                            'start_date': start_date,
                            'end_date': end_date
                        })
                        total_income += amount_decimal
                    except InvalidOperation:
                        pass

            if income.base_income:
                total_income += income.base_income

            income.additional_incomes = additional_incomes
            income.one_time_incomes = one_time_incomes
            income.total_income = total_income
            income.save() 
            return redirect('income_manage')
    else:
        form = IncomeForm(instance=income)
    
    additional_incomes = income.additional_incomes or [0]
    one_time_incomes = income.one_time_incomes or [0]
    
    context = {
        'income_manage_page' : INCOME_MANAGE_PAGE,
        'form': form, 
        'additional_incomes': additional_incomes, 
        'one_time_incomes': one_time_incomes, 
        'total_income': income.total_income
    }

    return render(request, 'income/income_manage.html', context)