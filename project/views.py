from django.shortcuts import render
from app1.models import company,department,employee
from .models import project
# Create your views here.

def table(request,pk=id):
    com = company.objects.all()
    dep = department.objects.all()
    emp = employee.objects.all()
    pro = project.objects.all()

    comname = request.POST.get('comx')
    print(">>>>>>>>>>>>>>",comname)

    depame = request.POST.get('depx')
    print(">>>>>>>>>>>>>>",depame)

    empname = request.POST.get('empx')
    print(">>>>>>>>>>>>>>",empname)
    
    #prox = project.objects.filter(company__id=comname)

    prox = project.objects.filter(company__id=comname,employee__id__in=emp)
    print(">>>>>>>>>>>>>>>>>>>>>>",prox)
    context = {

        'com':com,
        'dep':dep,
        'emp':emp,
        'pro':pro,
        'prox':prox,
    }
    return render(request,'table.html',context) 