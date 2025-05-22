import django_filters
from .models import Employee


class EmployeeFilter(django_filters.FilterSet):
    emp_name = django_filters.CharFilter(lookup_expr='icontains') # infers the field name from the model by 
    designation = django_filters.CharFilter(field_name='designation',lookup_expr='icontains')
    # emp_id = django_filters.UUIDFilter(field_name='emp_id',lookup_expr='exact')
    # age = django_filters.RangeFilter(field_name='age',lookup_expr='exact') # age from - to 

    class Meta:
        model = Employee
        fields = ['emp_name', 'designation'] #, 'age'