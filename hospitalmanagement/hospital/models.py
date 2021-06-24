from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Doctor(models.Model):
	name = models.CharField(max_length=60)
	contact = models.CharField(max_length=20)
	specialization = models.CharField(max_length=50)

	def __str__(self):
		return self.name




class Patient(models.Model):
	name = models.CharField(max_length=60)
	gender = models.CharField(max_length=10)
	age    = models.IntegerField(null=True)
	contact = models.CharField(max_length=20)
	address = models.CharField(max_length=200)

	def __str__(self):
		return self.name


class Appointment(models.Model):
	doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
	patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
	date1  = models.DateField()
	time1  = models.TimeField()


	def __str__(self):
		return self.doctor.name+"--"+self.patient.name