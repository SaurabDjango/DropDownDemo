from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from django.views.generic import CreateView
from .models import employee,department,company
from app1.forms import EmployeeForm
# Create your views here.


class ModelCreateView(CreateView):
    model = employee
    template_name = "add_form.html"
    form_class = EmployeeForm
    success_url = ("add_form.html")
    
    # def get(self, request, *args, **kwargs):
    #     dep = request.POST.get('depx')
    #     print(">>>>>>>>>>>>>>>>>>>>>>>>",dep)
    #     return render(request,self.template_name)
    def form_valid(self, form):

        return super().form_valid(form)

def load_branches(request):
    # fm = EmployeeForm()
    # dep = request.POST.get('depx')
    # print(">>>>>>>>>>>>>>>>>>>>>>>>",dep)
    
    company_id = request.GET.get('company')
    departmentx = department.objects.filter(company_id=company_id).order_by('name')

    context = {'departmentx':departmentx}
    return render(request,'branch_dropdown_list_options.html',{'departmentx':departmentx})

def formdata(request):
    fm = EmployeeForm()
    dep = request.POST.get('depx')
    print(">>>>>>>>>>>>>>>>>>>>>>>>",dep)

    context = {'fm':fm}
    return render(request,"add_form.html",)