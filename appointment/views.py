from django.shortcuts import render, redirect
from .forms import AppointmentForm
from .models import Appointment
from account.models import DoctorProfile, Profile
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import connection
# print(connection.queries)  see what db query are

@login_required
def appointment(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.save()
            # messages.success(request, f'Your request has been submitted')
            return redirect('appointment-set')
        for field, error in form.errors.items():
            print(field, error)
    else:
        form = AppointmentForm()
        form.fields['doctor'].queryset = DoctorProfile.objects.all()

    return render(request, 'appointment.html', {'form': form})

def appointment_set(request):
    return render(request, 'appointment-set.html')


def our_practitioners(request):
    practitioners = DoctorProfile.objects.all()
    return render(request, 'our-practitioners.html',{'practitioners': practitioners})


@login_required
def appointment_list(request):
    agenda = Appointment.objects.filter(user=request.user).order_by('booking_date2_date')
    return render(request, 'appointment-list.html', {'appointments': agenda})

@login_required
def doctor_appointment(request):
    agenda = Appointment.objects.filter(doctor=request.user.doctor).order_by('booking_date2_date')
    return render(request, 'doctor-appointment.html', {'appointments': agenda})


def confirm_cancel_appointment(request, key):
    appointment_to_cancel = Appointment.objects.get(pk=key)
    # print(connection.queries)
    return render(request, 'confirm-cancel-appointment.html', {'a': appointment_to_cancel})

def confirm_cancel_appointment_doctor(request, key):
    appointment_to_cancel = Appointment.objects.get(pk=key)
    # print(connection.queries)
    return render(request, 'confirm-cancel-appointment-doctor.html', {'a': appointment_to_cancel})

def consultation_hours(request, key):
    hours_to_show = DoctorProfile.objects.get(pk=key)
    print(connection.queries)
    return render(request, 'consultation-hours.html', {'hours': hours_to_show})


def cancel_appointment(request, key):
    appointment_to_cancel = Appointment.objects.get(pk=key)
    appointment_to_cancel.delete()
    return redirect('appointment-list')

def cancel_appointment_doctor(request, key):
    appointment_to_cancel = Appointment.objects.get(pk=key)
    appointment_to_cancel.delete()
    return redirect('doctor-appointment')
