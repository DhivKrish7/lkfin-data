from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError

class Company(models.Model):
    name = models.CharField(max_length=200, unique=True)
    ticker = models.CharField(max_length=10, unique=True)
    sector = models.CharField(max_length=50, blank=True, null=True)
    industry = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.ticker})"

class AnnualReport(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    year = models.IntegerField()
    report_date = models.DateField()

#incomeestatement
    revenue = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    cost_of_sales = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    gross_profit = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    operating_profit = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    net_profit = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    eps = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

#balancesheet
    total_assets = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    total_liabilities = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    equity = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    current_assets = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    current_liabilities = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)

#cashflow
    operating_cashflow = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    investing_cashflow = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    financing_cashflow = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    net_cashflow = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)

    class Meta:
        unique_together = ('company', 'year')
        ordering = ['-year']
        indexes = [
            models.Index(fields=['company']),
            models.Index(fields=['year']),
        ]

    def clean(self):
        if AnnualReport.objects.filter(company=self.company, year=self.year).exclude(pk=self.pk).exists():
            raise ValidationError('Annual report for this company and year already exists')
        if self.net_profit and self.revenue:
            if self.net_profit > self.revenue:
                raise ValidationError('Net profit cant bigger than Revenue')
        if self.total_assets and self.total_liabilities and self.equity:
            if self.total_liabilities + self.equity != self.total_assets:
                raise ValidationError('Assets must equal to liabilities + equity')
            
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(
        'auth.User',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.company.ticker} - Annual {self.year}"
    
class QuarterReport(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    year = models.IntegerField()
    quarter = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(4)]
    )
    report_date = models.DateField()

#incomestatement
    revenue = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    cost_of_sales = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    gross_profit = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    operating_profit = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    net_profit = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    eps = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

#balancesheet
    total_assets = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    total_liabilities = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    equity = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    current_assets = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    current_liabilities = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)

#cashflow
    operating_cashflow = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    investing_cashflow = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    financing_cashflow = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    net_cashflow = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)

    class Meta:
        unique_together = ('company', 'year', 'quarter')
        ordering = ['-company','-year', '-quarter']
        indexes = [
            models.Index(fields=['company']),
            models.Index(fields=['year']),
            models.Index(fields=['quarter']),
        ]

    def clean(self):
        if QuarterReport.objects.filter(
            company=self.company,
            year=self.year,
            quarter=self.quarter
        ).exclude(pk=self.pk).exists():
            raise ValidationError('Quarter report for this company, year and quarter already exists')
        
        if self.net_profit and self.revenue:
            if self.net_profit > self.revenue:
                raise ValidationError('Net profit cant bigger than Revenue')
        if self.total_assets and self.total_liabilities and self.equity:
            if self.total_liabilities + self.equity != self.total_assets:
                raise ValidationError('Assets must equal to liabilities + equity')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(
        'auth.User',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.company.ticker} - Q{self.quarter} {self.year}"