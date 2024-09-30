from django.urls import path
from . import views

urlpatterns = [
    path('', views.income_index, name='income'),
    path('manage/', views.income_manage, name='income_manage'),

]
