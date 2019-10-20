from django.contrib import admin
from patient.models import Patient, Prescription, Doctor

admin.site.register(Patient)
admin.site.register(Prescription)
admin.site.register(Doctor)