from django.db import models

# Create your models here.
class account(models.Model):
    name= models.CharField(max_length=30)
    email=models.EmailField()
    phone=models.CharField(max_length=10)
    password=models.CharField(max_length=30)
    dob = models.DateField(null=True)
    gender = models.CharField(max_length=30,null=True)
    def _str_(self):
        return self.name