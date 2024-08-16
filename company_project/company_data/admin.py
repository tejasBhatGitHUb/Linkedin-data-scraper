from django.contrib import admin
from .models import Company,EnrichedCompany

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display=["company_id","company_linkedin_url"]
 
@admin.register(EnrichedCompany)       
class EnrichedCompanyAdmin(admin.ModelAdmin):
    list_display=["company_id","company_name","website_url"]