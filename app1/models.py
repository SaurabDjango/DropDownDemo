from django.db import models

# Create your models here.

class company(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name
    
class department(models.Model):
        company = models.ForeignKey(company, on_delete=models.CASCADE,default="")
        name = models.CharField(max_length=25)
        def __str__(self):
            return self.name
        

class employee(models.Model):
         company = models.ForeignKey(company, on_delete=models.CASCADE)
         department = models.ForeignKey(department, on_delete=models.CASCADE)
         name = models.CharField(max_length=25)
         def __str__(self):
             return self.name