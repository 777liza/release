from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='dashboard'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('thanks/',views.thanks, name='thanks'),
    path('budget', views.budget, name='budget')
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
