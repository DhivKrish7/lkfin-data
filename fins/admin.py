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

    fieldsets = (
        ('Basic Information', {
            'fields': ('company', 'year', 'report_date')
        }),
        ('Income Statement', {
            'fields': (
                'revenue',
                'cost_of_sales',
                'gross_profit',
                'operating_profit',
                'net_profit',
                'eps',
            )
        }),
        ('Balance Sheet', {
            'fields': (
                'total_assets',
                'total_liabilities',
                'equity',
                'current_assets',
                'current_liabilities',
            )
        }),
        ('Cash Flow Statement', {
            'fields': (
                'operating_cashflow',
                'investing_cashflow',
                'financing_cashflow',
                'net_cashflow',
            )
        }),
    )
    
    def save_model(self, request, obj, form, change):
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)

@admin.register(QuarterReport)
class QuarterReportAdmin(admin.ModelAdmin):
    list_display = ('company', 'year', 'quarter', 'report_date')
    search_fields = ('company__name', 'company__ticker')
    ordering = ('-year', '-quarter')
    autocomplete_fields = ['company']

    fieldsets = (
        ('Basic Information', {
            'fields': ('company', 'year', 'quarter', 'report_date')
        }),
        ('Income Statement', {
            'fields': (
                'revenue',
                'cost_of_sales',
                'gross_profit',
                'operating_profit',
                'net_profit',
                'eps',
            )
        }),
        ('Balance Sheet', {
            'fields': (
                'total_assets',
                'total_liabilities',
                'equity',
                'current_assets',
                'current_liabilities',
            )
        }),
        ('Cash Flow Statement', {
            'fields': (
                'operating_cashflow',
                'investing_cashflow',
                'financing_cashflow',
                'net_cashflow',
            )
        }),
    )

    def save_model(self, request, obj, form, change):
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)