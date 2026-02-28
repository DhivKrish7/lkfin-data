from django.contrib import admin
from .models import (
    Company,
    AnnualReport,
    QuarterReport
)

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'ticker', 'sector')
    search_fields = ('name', 'ticker')
    ordering = ('name',)

@admin.register(AnnualReport)
class AnnualReportAdmin(admin.ModelAdmin):
    list_display = ('company', 'year', 'report_date')
    search_fields = ('company__name', 'company__ticker')
    ordering = ('-year',)
    autocomplete_fields = ['company']

@admin.register(QuarterReport)
class QuarterReportAdmin(admin.ModelAdmin):
    list_display = ('company', 'year', 'quarter', 'report_date')
    search_fields = ('company__name', 'company__ticker')
    ordering = ('-year', '-quarter')
    autocomplete_fields = ['company']