from django.db import models

# Create your models here.
class Employee(models.Model):
    empno = models.IntegerField()
    ename = models.CharField(max_length=50)
    sal = models.IntegerField()
    deptno = models.IntegerField()
class Dept(models.Model):
    deptno = models.IntegerField()
    dname = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
