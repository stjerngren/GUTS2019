from django.conf.urls import url, include
from main import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]