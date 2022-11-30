from django.urls import path
from .views import *
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('patient-register/', views.patient_register, name='patient-register'),
    path('doctor-register/', views.register_doctor, name='doctor-register'),
    path('profile/', views.create_profile, name='profile'),
    path('doctor-profile/', views.create_doctor_profile, name='doctor-profile'),
    path('profile-updated/', views.profile_updated, name='profile-updated'),
    path('doctor-profile-updated/', views.doctor_profile_updated, name='doctor-profile-updated'),
    path('disease-autocomplete/', DiseaseAutoComplete.as_view(create_field='description'), name='disease-autocomplete'),
    # path('profile/', views.create_profile, name='profile'),
]

