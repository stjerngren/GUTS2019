from django.conf.urls import url, include
from patient import views

urlpatterns = [
    url(r'^$', views.patient_index, name='patient_index'),
    url(r'^add_doctor/$', views.add_doctor, name='add_doctor'),
    url(r'^my_doctors/$', views.my_doctors, name='my_doctors'),
    url(r'^my_profile/$', views.my_profile, name='my_profile'),
    url(r'^take_pill/$', views.take_pill, name='take_pill'),
    url(r'^put_pill_back/$', views.put_pill_back, name='put_pill_back'),
    url(r'^test/$', views.test, name='test'),
    url(r'^view_doctor/$',views.view_doctor,name='view_doctor')

]