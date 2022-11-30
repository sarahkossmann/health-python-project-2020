from django.db import models
from datetime import datetime, date, time
from django.contrib.auth.models import User
from account.models import DoctorProfile

class Appointment(models.Model):
    CHOICES = [
        ('Dr Levy', 'Dr Levy'), ('Dr Rozenthal', 'Dr Rozenthal'), ('Dr Golan', 'Dr Golan'), ('Dr Ben Sussan', 'Dr Ben Sussan'), ('Dr Shapira', 'Dr Shapira'), ('Dr Rotem', 'Dr Rotem')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='my_appointments')
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE, related_name='my_meetings')
    phone_number = models.CharField(max_length=15, default='972551234574')
    booking_date1_date = models.DateField(default=date.today)
    booking_date1_time = models.TimeField(default='00:00')
    booking_date2_date = models.DateField(default=date.today)
    booking_date2_time = models.TimeField(default='00:00')
    note = models.TextField(max_length=500)



# request.user.my_appointments.all()=appointment.objects.filter(user=request.user)
# request.user.my_meetings.all()=appointment.objects.filter(doctor=request.user)


