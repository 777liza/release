from django.urls import path
from . import views

urlpatterns = [
    path('', views.expences, name='expences'),
    path('manage/', views.expences_manage, name='expences_manage')
]