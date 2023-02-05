from django.shortcuts import render
from django.views.generic import CreateView
from .models import employee,department,company
from app1.forms import EmployeeForm
# Create your views here.


class ModelCreateView(CreateView):
    model = employee
    template_name = "add_form.html"
    form_class = EmployeeForm


def load_branches(request):
    company_id = request.GET.get('company')
    departmentx = department.objects.filter(company_id=company_id).order_by('name')
    return render(request,'branch_dropdown_list_options.html',{'departmentx':departmentx})