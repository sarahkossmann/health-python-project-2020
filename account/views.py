from django.shortcuts import render, redirect
from .forms import UserRegisterForm, CreateProfileForm, DoctorRegisterForm, CreateDoctorProfileForm
from django.contrib import messages
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User, Permission
from account.models import Profile, User, Disease, DoctorProfile
from dal import autocomplete
from django.contrib.auth.decorators import login_required



def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')


def patient_register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            permission = Permission.objects.get(codename= 'add_disease')
            user.user_permissions.add(permission)
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in!')
            return redirect('user-login')
    else:
        form = UserRegisterForm()

    return render(request, 'patient-register.html', {'form': form})


def register_doctor(request):
    if request.method == "POST":
        form = DoctorRegisterForm(request.POST)
        if form.is_valid():
            key = form.cleaned_data.get('key')
            if key == 'imadoctor':
                doctor=form.save(commit=False)
                doctor.is_staff=True
                doctor.save()
            messages.success(request, f'Your account has been created! You are now able to log in!')
            return redirect('user-login')
    else:
        form = DoctorRegisterForm()

    return render(request, 'doctor-register.html', {'form': form})


@login_required
def create_profile(request):
    if request.user.is_staff:
        return redirect('doctor-profile')
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = CreateProfileForm(request.POST, instance=profile)
        for field, error in form.errors.items():
            print(field, error)
# first_name = request.user.first_name
# full_name= request.user.get_full_name()
        if form.is_valid():
            form.save()

            for x in form.cleaned_data['medical_history']:
                mh = Disease.objects.get(id=x.id)
                profile.medical_history.add(mh)
            # form.save()
            messages.success(request, f'Your data have been updated')
            return redirect('profile-updated')
    else:
        if created:
            form = CreateProfileForm()
        else:
            form = CreateProfileForm(instance=profile)
    return render(request, 'profile.html', {'form': form})


@login_required
def create_doctor_profile(request):
    if not request.user.is_staff:
        print('user is not a doctor')
        return redirect('profile')
    profile, created = DoctorProfile.objects.get_or_create(user=request.user)
    print(f'{profile.id}, new? {created}')
    if request.method == 'POST':
        print('post')
        form = CreateDoctorProfileForm(request.POST, instance=profile)
        for field, error in form.errors.items():
            print(field, error)

        if form.is_valid():
            form.save()

            messages.success(request, f'Your data have been updated')
            return redirect('doctor-profile-updated')
    else:
        if created:
            form = CreateDoctorProfileForm()
        else:
            form = CreateDoctorProfileForm(instance=profile)
    return render(request, 'doctor-profile.html', {'form': form})


@login_required
def profile_updated(request):
    return render(request, 'profile_updated.html')

@login_required
def doctor_profile_updated(request):
    return render(request, 'doctor-profile-updated.html')


class DiseaseAutoComplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Disease.objects.all()

        if self.q:
            qs = qs.filter(description__istartswith=self.q)
        return qs


# class CreateProfile(LoginRequiredMixin, CreateView):
#     form_class = CreateProfileForm
#     template_name = 'profile.html'
#     success_url = 'home'

# def get_create_option(self, context, q):
#     """Form the correct create_option to append to results."""
#     create_option = []
#     display_create_option = False
#     if self.create_field and q:
#         page_obj = context.get('page_obj', None)
#         if page_obj is None or page_obj.number == 1:
#             display_create_option = True
#
#         # Don't offer to create a new option if a
#         # case-insensitive) identical one already exists
#         existing_options = (self.get_result_label(result).lower()
#                             for result in context['object_list'])
#         if q.lower() in existing_options:
#             display_create_option = False
#
#     if display_create_option and self.has_add_permission(self.request):
#         create_option = [{
#             'id': q,
#             'text': _('Create "%(new_value)s"') % {'new_value': q},
#             'create_id': True,
#         }]
#     return create_option



