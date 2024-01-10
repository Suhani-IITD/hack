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


class appointment(models.Model):
    dt = models.DateField(null=True)
    ti = models.TimeField(null=True)
    desc = models.CharField(max_length = 100)
    category = models.CharField(max_length = 50)
    status = models.CharField(max_length = 20)


class sleephrs(models.Model):
    email=models.EmailField()
    sleephr=models.IntegerField()
    d=models.DateTimeField()
    day=models.CharField(max_length=30)

class lastemail(models.Model):
    email=models.EmailField()