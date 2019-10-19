from django.db import models
from django.contrib import auth
# Create your models here.



class Patient(models.Model):
    patient_id = models.AutoField(primary_key=True)
    doctor = models.ForeignKey("auth.User", related_name = "doctor", on_delete=models.DO_NOTHING, null=True)
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE)
    pill_today = models.BooleanField()

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