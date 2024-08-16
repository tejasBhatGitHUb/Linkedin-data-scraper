from django.db import models
from django.db import models

class Company(models.Model):
    company_id = models.IntegerField(primary_key=True)
    company_linkedin_url = models.URLField(unique=True)

class EnrichedCompany(models.Model):
    company= models.OneToOneField(Company, on_delete=models.CASCADE)
    company_name=models.CharField(max_length=200,null=True,blank=True)
    employee_count=models.IntegerField(null=True,blank=True)
    specialities=models.TextField(blank=True,null=True)
    tagline=models.CharField(max_length=500,blank=True,null=True)
    logo_resolution_result=models.URLField(blank=True,null=True)
    industry=models.CharField(max_length=200,blank=True,null=True)
    description=models.TextField(blank=True,null=True)
    website_url=models.URLField(blank=True,null=True)
    founded_on=models.JSONField(blank=True,null=True)
    universal_name=models.CharField(max_length=200,null=True,blank=True)
    linkedin_url=models.URLField(null=True,blank=True)
    headquarter=models.JSONField(null=True,blank=True)