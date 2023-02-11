from django.db import models
from app1.models import company,department,employee
# Create your models here.
class project(models.Model):
         id = models.AutoField(primary_key=True)
         company = models.ForeignKey(company, on_delete=models.CASCADE)
         department = models.ForeignKey(department, on_delete=models.CASCADE)
         employee = models.ForeignKey(employee, on_delete=models.CASCADE)
         name = models.CharField(max_length=25)
         def __str__(self):
             return self.name