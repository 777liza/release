from django.urls import path
from . import views

urlpatterns = [
    path('', views.banking_index, name='banking'),
    path('manage/', views.banking_manage, name='banking_manage'),

]
