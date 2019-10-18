from django.conf.urls import url, include
from patient import views

urlpatterns = [
    url(r'^$', views.patient_index, name='patient_index'),
]