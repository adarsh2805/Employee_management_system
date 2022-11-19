from distutils.archive_util import make_zipfile
from pyexpat import model
from statistics import mode
from django.db import models

# Create your models here.
class Department(models.Model):
    name=models.CharField(max_length=30,null=False)
    location=models.CharField(max_length=30)


    def __str__(self):
        return self.name


class Role(models.Model):
    name=models.CharField(max_length=100,null=False)
    def __str__(self) -> str:
        return self.name


class Employee(models.Model):
    firstname=models.CharField(max_length=30,null=False)
    lastname=models.CharField(max_length=30)
    salary=models.IntegerField(max_length=30)
    bonus=models.IntegerField(max_length=20)
    phone=models.CharField(max_length=11)
    role=models.ForeignKey(Role,on_delete=models.CASCADE)
    dapt=models.ForeignKey(Department,on_delete=models.CASCADE)   
    location=models.CharField(max_length=60)
    hire_date=models.DateField()
    def __str__(self) :
        return "%s %s %s"%(self.firstname,self.lastname,self.phone) 
