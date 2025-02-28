from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from finance.text_constants import BANKING_PAGE

@login_required
def banking_index(request):
    context = {
        'banking_page' : BANKING_PAGE
    }
    return render(request, 'banking/banking.html', context)
    
@login_required
def banking_manage(request):

    return render(request, 'banking/banking_manage.html')
