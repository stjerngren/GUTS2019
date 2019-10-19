from django.db import models
from django.contrib import auth
# Create your models here.

class Doctor(models.Model):
    doctor = models.OneToOneField("auth.User", on_delete=models.CASCADE)


class Patient(models.Model):
    doctor = models.ManyToManyField("doctor", related_name = "patient_doctor")
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE)
    pill_today = models.BooleanField()

    DOB = models.CharField( max_length=10, null = True)
    insurance_number = models.IntegerField(null = True)
    medical_condition = models.CharField( max_length=50, null = True)
    phone_number = models.IntegerField(null = True)
    emergency_contact_first_name = models.CharField( max_length=30, null = True)
    emergency_contact_last_name = models.CharField( max_length=30, null = True)
    emergency_contact_phone_number= models.IntegerField(null = True)
    address = models.CharField(max_length = 200, null = True)


class Prescription(models.Model):

    patient = models.OneToOneField("Patient", on_delete=models.CASCADE)
    pills_monday = models.BooleanField()
    pills_tuesday = models.BooleanField()
    pills_wednesday = models.BooleanField()
    pills_thursday = models.BooleanField()
    pills_friday = models.BooleanField()
    pills_saturday = models.BooleanField()
    pills_sunday = models.BooleanField()

    pills_monday_amount = models.IntegerField()
    pills_tuesday_amount = models.IntegerField()
    pills_wednesday_amount = models.IntegerField()
    pills_thursday_amount = models.IntegerField()
    pills_friday_amount   = models.IntegerField()
    pills_saturday_amount = models.IntegerField()
    pills_sunday_amount   = models.IntegerField()

    pills_monday_time = models.TimeField()
    pills_tuesday_time = models.TimeField()
    pills_wednesday_time = models.TimeField()
    pills_thursday_time = models.IntegerField()
    pills_friday_time   = models.TimeField()
    pills_saturday_time = models.TimeField()
    pills_sunday_time   = models.TimeField()