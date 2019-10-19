from django.conf.urls import url, include
from patient import views

urlpatterns = [
    url(r'^$', views.patient_index, name='patient_index'),
    url(r'^take_pill/$', views.take_pill, name='take_pill'),
    url(r'^put_pill_back/$', views.put_pill_back, name='put_pill_back'),
    url(r'^test/$', views.test, name='test'),

]