from rest_framework import serializers
from .models import Company, EnrichedCompany

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['company_id', 'company_linkedin_url']

class EnrichedCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = EnrichedCompany
        fields=["company_name","company","universal_name","website_url","description","industry","specialities",
                "employee_count","tagline","founded_on","logo_resolution_result","headquarter","linkedin_url"]