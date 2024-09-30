from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import Expences
from .forms import expencesForm
from decimal import Decimal, InvalidOperation
from finance.text_constants import EXPENSES_PAGE, EXPENSES_MANAGE_PAGE

@login_required
def expences(request):
    expences = Expences.objects.filter(user=request.user)

    expences_data = []
    for expences in expences:
        expences.one_time_expences.reverse()
        expences_data.append({
            'total_expences': expences.total_expences,
            'base_expences': expences.base_expences,
            'base_expences_description': expences.base_expences_description,
            'base_expences_start': expences.base_expences_start_date,
            'base_expences_end': expences.base_expences_end_date,
            'investment_expences': expences.investment_expences,
            'additional_expences': expences.additional_expences,
            'one_time_expences': expences.one_time_expences,
            'update_date': expences.update_date,
        })

    context = {
        'total_expences': expences_data[0]['total_expences']  if expences_data else 0,
        'expences_page' : EXPENSES_PAGE,
        'expences_data': expences_data
    }
    return render(request, 'expences/expences.html', context)

@login_required
def expences_manage(request):

    expences, created = Expences.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = expencesForm(request.POST, instance=expences)
        
        if form.is_valid():
            additional_expences = []
            one_time_expences = []
            
            additional_amounts = request.POST.getlist('additional_expences[]')
            additional_descriptions = request.POST.getlist('additional_expences_description[]')
            additional_start_dates = request.POST.getlist('additional_expences_start[]')
            additional_end_dates = request.POST.getlist('additional_expences_end[]')

            one_time_amounts = request.POST.getlist('one_time_expences[]')
            one_time_descriptions = request.POST.getlist('one_time_expences_description[]')
            one_time_start_dates = request.POST.getlist('one_time_expences_start[]')
            one_time_end_dates = request.POST.getlist('one_time_expences_end[]')

            total_expences = Decimal('0.00')

            for amount, description, start_date, end_date in zip(additional_amounts, additional_descriptions, additional_start_dates, additional_end_dates):
                if amount:
                    try:
                        amount_decimal = Decimal(amount)
                        additional_expences.append({
                            'amount': amount,
                            'description': description,
                            'start_date': start_date,
                            'end_date': end_date
                        })
                        total_expences += amount_decimal
                    except InvalidOperation:
                        pass

            for amount, description, start_date, end_date in zip(one_time_amounts, one_time_descriptions, one_time_start_dates, one_time_end_dates):
                if amount:
                    try:
                        amount_decimal = Decimal(amount)
                        one_time_expences.append({
                            'amount': amount,
                            'description': description,
                            'start_date': start_date,
                            'end_date': end_date
                        })
                        total_expences += amount_decimal
                    except InvalidOperation:
                        pass

            if expences.base_expences:
                total_expences += expences.base_expences

            expences.additional_expences = additional_expences
            expences.one_time_expences = one_time_expences
            expences.total_expences = total_expences
            expences.save()
            return redirect('expences_manage')
    else:
        form = expencesForm(instance=expences)
    
    additional_expences = expences.additional_expences or [0]
    one_time_expences = expences.one_time_expences or [0]
    
    context = {
        'expences_manage_page' : EXPENSES_MANAGE_PAGE,
        'form': form, 
        'additional_expences': additional_expences, 
        'one_time_expences': one_time_expences, 
        'total_expences': expences.total_expences
    }

    return render(request, 'expences/expences_manage.html', context)
