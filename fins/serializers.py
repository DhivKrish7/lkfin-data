from rest_framework import serializers
from .models import Company, AnnualReport, QuarterReport

class AnnualReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnnualReport
        fields = '__all__'

class QuarterReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuarterReport
        fields = '__all__'

class CompanySerializer(serializers.ModelSerializer):
    annual_reports = AnnualReportSerializer(many=True, source='annualreport_set', read_only=True)
    quarter_reports = QuarterReportSerializer(many=True, source='quarterreport_set', read_only=True)

    class Meta:
        model = Company
        fields = [
            'id',
            'name',
            'ticker',
            'sector',
            'industry',
            'annual_reports',
            'quarter_reports',
        ]