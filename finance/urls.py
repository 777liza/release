from django.contrib import admin
from django.urls import path, include
from .views import SignUpView
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('settings/', include('settings.urls')),
    path('', include('dashboard.urls')),
    path('income/', include('income.urls')),
    path('investments/', include('investments.urls')),
    path('about/', views.about, name='about'),
    path('contact/',views.contact, name='contact'),
    path('policy/', views.policy, name='policy'),
    path('terms/',views.terms, name='terms'),
    path('expences/', include('expences.urls')),
    path('home/', views.home, name='home_page'),
    path('exspress-add/', views.espress_add, name='espress_add'),
    # path('logout/', views.custom_logout, name='logout'),
    path('logout/', views.custom_logout, name='logout'),
    path('404/', views.custom_404, name='404')


    
    
    
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)