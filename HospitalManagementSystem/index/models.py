from django.db import models
from django.contrib.auth.models import User
from accounts.models import MyUsers
# Create your models here.

class Appointments(models.Model):
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=50)
    doctor = models.ForeignKey(User,default= None,on_delete=models.CASCADE,related_name='doctor')
    patients = models.ForeignKey(User,default= None,on_delete=models.CASCADE,related_name='patients')


class Invoice(models.Model):
    document = models.FileField(upload_to='documents/',default=None)
    paid = models.IntegerField()
    date = models.DateField()
    outstanding = models.IntegerField()
    patient = models.ForeignKey(User,default= None,on_delete=models.CASCADE)


class Prescription(models.Model):

    patient = models.ForeignKey(User,default= None,on_delete=models.CASCADE)
    symptom = models.CharField(max_length=100)
    prescription = models.CharField(max_length=250)
    doctor = models.IntegerField()
