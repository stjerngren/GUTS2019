from django.shortcuts import render

def patient_index(request):

    return render(request, 'patient/patient_index.html')