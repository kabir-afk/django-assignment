from django_filters import rest_framework as filters
from .models import Branch

class BranchFilter(filters.FilterSet):
    bank_name = filters.CharFilter(field_name='bank_name', lookup_expr='iexact')
    branch_name = filters.CharFilter(field_name='branch_name', lookup_expr='iexact')
    state = filters.CharFilter(field_name='state', lookup_expr='iexact')
    city = filters.CharFilter(field_name='city', lookup_expr='iexact')
    district = filters.CharFilter(field_name='district', lookup_expr='iexact')
    
    class Meta:
        model = Branch
        fields = ['bank_name','branch_name','state', 'city','district']