from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import date

from patient.models import Patient

def get_prescription(patient):
    """ Get amount of pills and when to take precsiption today"""
    
    if date.today().weekday() == 0:
        return patient.prescription.pills_monday_amount, patient.prescription.pills_monday_time
    elif date.today().weekday() == 1:
        return patient.prescription.pills_tuesday_amount, patient.prescription.pills_tuesday_time
    elif date.today().weekday() == 2:
        return patient.prescription.pills_wednesday_amount, patient.prescription.pills_wednesday_time
    elif date.today().weekday() == 3:
        return patient.prescription.pills_thursday_amount, patient.prescription.pills_thursday_time
    elif date.today().weekday() == 4:
        return patient.prescription.pills_friday_amount, patient.prescription.pills_friday_time
    elif date.today().weekday() == 5:
        return patient.prescription.pills_saturday_amount, patient.prescription.pills_saturday_time
    elif date.today().weekday() == 6:
        return patient.prescription.pills_sunday_amount, patient.prescription.pills_sunday_time


@login_required
def patient_index(request):

    if request.user.patient.pill_today:
        pill_today = True
        pill_amount, pill_time = get_prescription(request.user.patient)
        print(pill_amount)
        print(pill_time)
    else:
        pill_today = False
        pill_amount = None
        pill_time = None
    context = {
        "pill"      : pill_today,
        "pill_amount" : pill_amount,
        "pill_time"   :pill_time,
        "greeting"  : "Hello, ",
        "first_name": request.user.first_name
    }

    return render(request, 'patient/patient_index.html', context)

def take_pill(request):
    """Stupid, don't ever ever ever do this
    
    Anyone will be able to request to take the pill with a simpkle get request
    """
    if request.method == 'GET':
        patient_id = request.GET['id']
        patient = Patient.objects.get(id = patient_id)
        patient.pill_today = False
        patient.save()
    return HttpResponse()

def put_pill_back(request):
    """Stupid, don't ever ever ever do this
    
    Anyone will be able to request to put the pill with a simpkle get request
    """
    if request.method == 'GET':
        patient_id = request.GET['id']
        patient = Patient.objects.get(id = patient_id)
        patient.pill_today = True
        patient.save()
    return HttpResponse()


def view_doctor(request):
    return render(request, 'patient/view_doctor.html')


def test(request):
    context = {
        'pill_amount_monday':range(request.user.patient.prescription.pills_monday_amount),
        'pill_amount_tuesday': range(request.user.patient.prescription.pills_tuesday_amount),
        'pill_amount_wednesday': range(request.user.patient.prescription.pills_wednesday_amount),
        'pill_amount_thursday': range(request.user.patient.prescription.pills_thursday_amount),
        'pill_amount_friday': range(request.user.patient.prescription.pills_friday_amount),
        'pill_amount_saturday': range(request.user.patient.prescription.pills_saturday_amount),
        'pill_amount_sunday':range(request.user.patient.prescription.pills_sunday_amount),
        }
    return render(request, 'patient/test.html', context)