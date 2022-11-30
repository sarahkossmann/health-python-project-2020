from django.urls import path
from .views import *
from . import views


urlpatterns = [
    path('appointment/', views.appointment, name='appointment'),
    path('appointment-set/', views.appointment_set, name='appointment-set'),
    path('appointment-list/', views.appointment_list, name='appointment-list'),
    path('doctor-appointment/', views.doctor_appointment, name='doctor-appointment'),
    path('confirm-cancel-appointment/<int:key>/', views.confirm_cancel_appointment, name='confirm-cancel-appointment'),
    path('confirm-cancel-appointment-doctor/<int:key>/', views.confirm_cancel_appointment_doctor, name='confirm-cancel-appointment-doctor'),
    path('cancel/<int:key>/', views.cancel_appointment, name='cancel'),
    path('cancel-doctor/<int:key>/', views.cancel_appointment_doctor, name='cancel-doctor'),
    path('our-practitioners/', views.our_practitioners, name='our-practitioners'),
    path('consultation/<int:key>/', views.consultation_hours, name='consultation-hours'),
]