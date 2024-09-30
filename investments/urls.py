from django.urls import path
from . import views

urlpatterns = [
    path('', views.investments_index, name='investments'),
    path('manage/', views.manage_investments, name='invest_manage'),
]

