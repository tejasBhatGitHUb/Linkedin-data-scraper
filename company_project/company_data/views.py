
import os
import requests
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Company, EnrichedCompany
from .serializers import CompanySerializer, EnrichedCompanySerializer 
from rest_framework.pagination import PageNumberPagination
from dotenv import load_dotenv
load_dotenv()

class CustomPagination(PageNumberPagination):
    page_size=2
    page_query_param="page"
    
class CompanyListView(CustomPagination,APIView):
    def get(self, request):
        companies =Company.objects.all()
        # return Response(CompanySerializer(companies,many=True).data)
        
        page=self.paginate_queryset(companies,request,view=self)
        serializer = CompanySerializer(page, many=True)
        return self.get_paginated_response(serializer.data)

class EnrichCompanyDataView(APIView):
    def get(self, request, company_id):        
        try:
            enriched_data=EnrichedCompany.objects.get(company_id=company_id)
            enriched_serializer = EnrichedCompanySerializer(enriched_data)
            return Response(enriched_serializer.data)
                  
        except EnrichedCompany.DoesNotExist:
            try:
                company=Company.objects.get(company_id=company_id)
                payload={"links":[company.company_linkedin_url]}
                headers = {
                    "x-rapidapi-key": os.getenv('API_KEY'),
                    "x-rapidapi-host": os.getenv("host"),
                    "Content-Type": os.getenv('type'),
                    "x-rapidapi-user": os.getenv('user')
                }

                response = requests.post(os.getenv('url'), json=payload, headers=headers)
                if response.status_code == 200:
                    data = response.json()["data"][0]["data"]
                
                    # Selecting wanted fields
                    include=["specialities","tagline","logoResolutionResult","industry","description",
                            "websiteUrl","headquarter","foundedOn","universalName","url","companyName","employeeCount"]
                    filtered_data = {k: v for k, v in data.items() if  any(sub in k for sub in include)}

                    # Stor enriched data
                    enriched_company = EnrichedCompany.objects.create(company_name=filtered_data["companyName"],
                        company=company, specialities=filtered_data["specialities"],tagline=filtered_data["tagline"],
                        logo_resolution_result=filtered_data["logoResolutionResult"],industry=filtered_data["industry"],
                        description=filtered_data["description"],website_url=filtered_data["websiteUrl"],
                        headquarter=filtered_data["headquarter"],founded_on=filtered_data["foundedOn"],
                        universal_name=filtered_data["universalName"],linkedin_url=filtered_data["url"],employee_count=filtered_data["employeeCount"])

                    enriched_serializer = EnrichedCompanySerializer(enriched_company)
                    return Response(enriched_serializer.data, status=status.HTTP_201_CREATED)
                else:
                    return Response({'error': 'Failed to fetch data from LinkedIn API'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            except Company.DoesNotExist:
                return Response({'error': 'Company not found in our database'}, status=status.HTTP_404_NOT_FOUND)
            
            