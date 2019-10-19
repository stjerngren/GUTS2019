from django.contrib import admin
from patient.models import Patient, Prescription

admin.site.register(Patient)
admin.site.register(Prescription)