from django import forms
from tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker
from appointment.models import *
from django.forms import *
import datetime
from django.contrib.admin import widgets



class AppointmentForm(ModelForm):
    # booking_date1 = start = DateTimeField(
    #     input_formats = ['%Y-%m-%dT%H:%M'],
    #     widget = DateTimeInput(
    #         attrs={
    #             'type': 'datetime-local',
    #             'class': 'form-control'},
    #         format='%Y-%m-%dT%H:%M')
    # )
    # booking_date1 = DateTimeField(input_formats=['%Y-%m-%dT%H:%M']),
    # booking_date2 = DateTimeField(input_formats=['%d-%m-%YT%H:%M']),
    class Meta:
        fields = '__all__'
        exclude = ['user']
        model = Appointment
        widgets = {
            'tz' : NumberInput({'class':'form-control'}),
            'email' : EmailInput({'class':'form-control'}),
            'phone_number' : TextInput({'class':'form-control'}),
            'booking_date1_date' : DateInput({'class':'form-control','type':'date'}),
            'booking_date1_time':TimeInput({'class':'form-control','type':'time'}),
            'booking_date2_date': DateInput({'class':'form-control','type':'date'}),
            'booking_date2_time':TimeInput({'class':'form-control','type':'time'}),
            'note': TextInput({'class':'form-control'}),
        }



# class MyForm(forms.Form):
#     date_field = forms.DateField(widget=DatePicker())
#     date_field_required_with_min_max_date = forms.DateField(
#         required=True,
#         widget=DatePicker(
#             options={
#                 'minDate': '2009-01-20',
#                 'maxDate': '2017-01-20',
#             },
#         ),
#         initial='2013-01-01',
#     )
#     """
#     In this example, the date portion of `defaultDate` is irrelevant;
#     only the time portion is used. The reason for this is that it has
#     to be passed in a valid MomentJS format. This will default the time
#     to be 14:56:00 (or 2:56pm).
#     """
#     time_field = forms.TimeField(
#         widget=TimePicker(
#             options={
#                 'enabledHours': [9, 10, 11, 12, 13, 14, 15, 16],
#                 'defaultDate': '1970-01-01T14:56:00'
#             },
#             attrs={
#                 'input_toggle': True,
#                 'input_group': False,
#             },
#         ),
#     )
#     datetime_field = forms.DateTimeField(
#         widget=DateTimePicker(
#             options={
#                 'useCurrent': True,
#                 'collapse': False,
#             },
#             attrs={
#                 'append': 'fa fa-calendar',
#                 'icon_toggle': True,
#             }
#         ),
#     )