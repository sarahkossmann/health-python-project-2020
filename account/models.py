from django.db import models
from django.contrib.auth.models import User
from datetime import date, time


class Disease(models.Model):
    code = models.CharField(default='a code', max_length=10)
    description = models.CharField(default='some disease', max_length=1000, unique=True)

    def __str__(self):
        return self.description


class Profile(models.Model):
    CHOICES = [
        ('A+', 'A+'),('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')
    ]



    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='patient')
    tz = models.IntegerField(default=123456789)
    birth_date = models.DateField(default=date.today)
    height = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)
    blood_type = models.CharField(default='A+', max_length=1000, choices=CHOICES)
    medical_history = models.ManyToManyField(Disease)
    vaccines = models.CharField(default='Hepatitis A', max_length=1000)


    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

class DoctorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doctor')
    specialty = models.CharField(max_length=300)
    university = models.CharField(max_length=300)
    graduation_year = models.CharField(max_length=10)
    address = models.CharField(max_length=300)
    sunday_hours_from = models.TimeField(default='00:00')
    sunday_hours_to = models.TimeField(default='00:00')
    monday_hours_from = models.TimeField(default='00:00')
    monday_hours_to = models.TimeField(default='00:00')
    tuesday_hours_from = models.TimeField(default='00:00')
    tuesday_hours_to = models.TimeField(default='00:00')
    wednesday_hours_from = models.TimeField(default='00:00')
    wednesday_hours_to = models.TimeField(default='00:00')
    thursday_hours_from = models.TimeField(default='00:00')
    thursday_hours_to = models.TimeField(default='00:00')


    def __str__(self):
        return f'Dr {self.user.first_name} {self.user.last_name}'