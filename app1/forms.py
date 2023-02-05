from django import forms
from .models import employee,company,department

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = employee
        fields = ('company','department','name')

        def __init__(self, *args, **kwargs):
            super().__init__( *args, **kwargs)
            self.fields['department'].queryset = department.objects.none()

            if 'company' in self.data:
                try:
                    company_id = int(self.data.get('company'))
                    self.fields['department'].queryset = department.objects.filter(company_id = company_id)
                except(ValueError, TypeError):
                    pass
            elif self.instance.pk:
                self.fields['department'].queryset = self.instance.company.department_set.order_by('name')
                