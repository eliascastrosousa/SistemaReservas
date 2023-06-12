from . import views
from django.urls import path

urlpatterns = [
    path('', views.schedulinglist, name='schedulinglist'),    
    path('schedulinglist', views.schedulinglist, name='schedulinglist'),
    path('schedulingregister', views.schedulingregister, name='schedulingregister'),
    path('schedulingsearch', views.schedulingsearch, name='schedulingsearch'),
    path('schedulingregistersearchpatient', views.schedulingregistersearchpatient, name='schedulingregistersearchpatient'),
    path('saveconsulting', views.saveconsulting, name='saveconsulting')
    
]