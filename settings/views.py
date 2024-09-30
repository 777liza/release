from django.shortcuts import render, redirect
# from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import UserSettingsForm
from finance.text_constants import SETTINGS_PAGE

@login_required
def settings_view(request):
		user = request.user
		if request.method == 'POST':
			form = UserSettingsForm(request.POST, request.FILES, instance=user)
			# if form.is_valid():
			form.save()
			return redirect('settings')
		else:
			form = UserSettingsForm(instance=user)

		context = {
			'settings_page' : SETTINGS_PAGE,
			'form': form,
			'username': user.username
		}

		return render(request, 'settings/index.html', context)


# Create your views here.
