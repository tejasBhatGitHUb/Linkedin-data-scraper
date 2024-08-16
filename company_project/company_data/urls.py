from django.urls import path
from .views import CompanyListView, EnrichCompanyDataView

urlpatterns = [
    path('companies/', CompanyListView.as_view(), name='company-list'),
    path('companies/enrich/<int:company_id>/', EnrichCompanyDataView.as_view(), name='enrich-company-data'),
]
