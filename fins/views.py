from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Company
from .serializers import CompanySerializer

class CompanyDetailAPIView(APIView):
    def get(self,request, ticker):
        try:
            company = Company.objects.get(ticker=ticker)
        except Company.DoesNotExist:
            return Response(
                {'Error': "Company not found"},
                status=status.HTTP_404_NOT_FOUND
                )

        serializer = CompanySerializer(company)
        return Response(serializer.data)
    
def company_dashboard(request, ticker):
    return render(request, 'company_dashboard.html', {'ticker': ticker})
