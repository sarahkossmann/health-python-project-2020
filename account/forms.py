from django.forms import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from account.models import *
from django import forms
from dal import autocomplete
from tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

class DoctorRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    key = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'key', 'username', 'email', 'password1', 'password2']


# class DiseaseCreateField(autocomplete.Select2ListCreateChoiceField):
#     def create_value(self, value):
#         return Disease.objects.create(description=value).pk

class CreateProfileForm(ModelForm):

    class Meta:
        fields = ['tz', 'birth_date', 'height', 'weight', 'blood_type', 'medical_history', 'vaccines']
        model = Profile
        widgets = {
            'tz' : NumberInput({'class':'form-control'}),
            'birth_date': DateInput({'class':'form-control','type':'date'}),
            'height' : NumberInput({'class':'form-control'}),
            'weight' : NumberInput({'class':'form-control'}),
            'blood_type' : Select(attrs={'class':'select'}),
            'medical_history': autocomplete.ModelSelect2Multiple(url='disease-autocomplete', attrs={'data-placeholder': 'Search...', 'data-minimum-input-length': 1}),
            'vaccines': CheckboxSelectMultiple(attrs={'class':'checkbox'}, choices=[('Hepatitis A', 'Hepatitis A'), ('Hepatitis B', 'Hepatitis B'), ('Diphtheria - Tetanus - Whooping Cough (pertussis)', 'Diphtheria - Tetanus - Whooping Cough (pertussis)'), ('Polio', 'Polio'), ('Pneumococcal', 'Pneumococcal'), ('Rotavirus', 'Rotavirus'), ('Chickenpox (Varicella)', 'Chickenpox (Varicella)'), ('Measles - Mumps - Rubella', 'Measles - Mumps - Rubella'), ('Human PapillomaVirus vaccine', 'Human PapillomaVirus vaccine'), ('Meningococcal conjugate vaccine', 'Meningococcal conjugate vaccine')]),
        }


class CreateDoctorProfileForm(ModelForm):

    class Meta:
        fields = '__all__'
        exclude = ['user']
        model = DoctorProfile
        widgets = {
            'specialty' : TextInput({'class':'form-control'}),
            'university' : TextInput({'class':'form-control'}),
            'graduation_year': TextInput({'class':'form-control'}),
            'address' : TextInput({'class':'form-control'}),
            'sunday_hours_from' : TimeInput({'class':'form-control','type':'time'}),
            'sunday_hours_to': TimeInput({'class':'form-control','type':'time'}),
            'monday_hours_from': TimeInput({'class':'form-control','type':'time'}),
            'monday_hours_to': TimeInput({'class':'form-control','type':'time'}),
            'tuesday_hours_from': TimeInput({'class':'form-control','type':'time'}),
            'tuesday_hours_to': TimeInput({'class':'form-control','type':'time'}),
            'wednesday_hours_from': TimeInput({'class':'form-control','type':'time'}),
            'wednesday_hours_to': TimeInput({'class':'form-control','type':'time'}),
            'thursday_hours_from': TimeInput({'class':'form-control','type':'time'}),
            'thursday_hours_to': TimeInput({'class':'form-control','type':'time'}),
        }
