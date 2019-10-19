from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def patient_index(request):
    context = {
        "greeting"  : "Hello, ",
        "first_name": request.user.first_name
    }
    
    return render(request, 'patient/patient_index.html', context)