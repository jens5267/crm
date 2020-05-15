import django_filters
from django_filters import CharFilter, DateFilter
from .models import *

class OrderFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="date_created", lookup_expr="gte", label='after')
    end_date = DateFilter(field_name="date_created", lookup_expr="lte", label='before')
    note = CharFilter(field_name='note', lookup_expr='icontains', label='Notes:')
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['customer', 'date_created']