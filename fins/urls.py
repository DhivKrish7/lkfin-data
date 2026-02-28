from django.urls import path
from .views import CompanyDetailAPIView, company_dashboard

urlpatterns = [
    path('company/<str:ticker>/', company_dashboard, name='company-dashboard'),
    path('api/company/<str:ticker>/', CompanyDetailAPIView.as_view(), name='company-detail'),
]