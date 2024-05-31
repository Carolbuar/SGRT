import django_filters
from app_sgrt.models import Job

class JobFilterLocation(django_filters.FilterSet):
    location = django_filters.CharFilter(field_name='location', lookup_expr='icontains')
   
    class Meta:
        model = Job
        fields = ['location']

class JobFilterStatus(django_filters.FilterSet):
    status = django_filters.CharFilter(field_name='status', lookup_expr='exact')
    
    class Meta:
        model = Job
        fields = ['status']

class JobFilterCustomer(django_filters.FilterSet):
    customer = django_filters.CharFilter(field_name='customer__name', lookup_expr='icontains')

    class Meta:
        model = Job
        fields = ['customer']