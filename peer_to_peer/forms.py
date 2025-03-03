from django import forms
from .models import UserProfile, RiderProfile,RiderTrip,UserTrip,CreateUser,CreateRide

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'password']

class RiderProfileForm(forms.ModelForm):
    class Meta:
        model = RiderProfile
        fields = ['username', 'password']

class RiderTripForm(forms.ModelForm):
    class Meta:
        model = RiderTrip
        fields = ['source','destination']

class UserTripForm(forms.ModelForm):
    class Meta:
        model = UserTrip
        fields = ['source','destination']

class CreateUserForm(forms.ModelForm):
    class Meta:
        model = CreateUser
        fields = ['Name','email','phone_no','priority_no','Gender','age','Username','password']

class CreateRideForm(forms.ModelForm):
    class Meta:
        model = CreateRide
        fields = ['Name','age','email','phone_no','Gender','vehicle_type','vehicle_no','aadhaar_no','license_no','Username','password']

# class mapRiderForm(forms.ModelForm):
#     class Meta:
#         model = mapRider
#         fields = ['source','destination']

# class mapUserForm(forms.ModelForm):
#     class Meta:
#         model = mapUser
#         fields = ['source','destination']