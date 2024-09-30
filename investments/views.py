from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import InvestmentsForm
from .models import Investments
from finance.text_constants import INVESTMENTS_PAGE, INVESTMENTS_MANAGE_PAGE

@login_required
def investments_index(request):
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
        'investments_page' : INVESTMENTS_PAGE,
        'investments_data': investments
    }
    return render(request, 'investments/invest.html', context )

@login_required
def manage_investments(request):
    investment, created = Investments.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = InvestmentsForm(request.POST, instance=investment)
        if form.is_valid():
            form.save()
            return redirect('invest_manage')
    else:
        form = InvestmentsForm(instance=investment)

    context = {
        'investments_manage_page': INVESTMENTS_MANAGE_PAGE,
        'form': form,
        'investment': investment
    }

    return render(request, 'investments/manage.html', context)

