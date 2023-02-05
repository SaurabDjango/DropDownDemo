from django.contrib import admin
from .models import company,employee,department
# Register your models here.

admin.site.register(company)
admin.site.register(department)
admin.site.register(employee)