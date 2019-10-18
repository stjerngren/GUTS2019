from django.shortcuts import render

def patient_index(request):

    return render(request, 'templates/patient/patient_index.html')