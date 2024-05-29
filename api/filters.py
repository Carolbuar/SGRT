import django_filters
from app_sgrt.models import Job

class JobFilter(django_filters.FilterSet):
    location = django_filters.CharFilter(field_name='location', lookup_expr='icontains')
    status = django_filters.CharFilter(field_name='status', lookup_expr='exact')
    customer = django_filters.CharFilter(field_name='customer__name', lookup_expr='icontains')

    class Meta:
        model = Job
        fields = ['location', 'status', 'customer']