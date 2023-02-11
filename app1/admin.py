from django.contrib import admin
from .models import company,employee,department
# Register your models here.

#admin.site.register(company)
#admin.site.register(department)
#admin.site.register(employee)

@admin.register(company)
class Company(admin.ModelAdmin):
    list_display = ['id','name',]

@admin.register(department)
class Company(admin.ModelAdmin):
    list_display = ['id','name','company']

@admin.register(employee)
class Company(admin.ModelAdmin):
    list_display = ['id','name','department','company']