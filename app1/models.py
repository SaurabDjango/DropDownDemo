from django.db import models

# Create your models here.

class company(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name
    
class department(models.Model):
        id = models.AutoField(primary_key=True)
        company = models.ForeignKey(company, on_delete=models.CASCADE,default="")
        name = models.CharField(max_length=25)
        def __str__(self):
            return self.name

class employee(models.Model):
         id = models.AutoField(primary_key=True)
         company = models.ForeignKey(company, on_delete=models.CASCADE)
         department = models.ForeignKey(department, on_delete=models.CASCADE)
         name = models.CharField(max_length=25)
         def __str__(self):
             return self.name