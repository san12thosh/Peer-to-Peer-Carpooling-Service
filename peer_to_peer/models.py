from django.db import models
from django.core.exceptions import ValidationError
import re
from django.core.validators import MinValueValidator, MaxValueValidator

# Validation functions
def validate_username(value):
    if not re.search(r'[A-Z]', value):
        raise ValidationError('Username must contain at least one capital letter.')

def validate_password(value):
    if len(value) != 8:
        raise ValidationError('Password must be exactly 8 characters long.')
    if not re.search(r'[A-Z]', value):
        raise ValidationError('Password must contain at least one capital letter.')

def validate_phone(value):
    if not re.fullmatch(r'\d{10}', value):
        raise ValidationError('Phone number must be exactly 10 digits.')

def validate_priority(value):
    if not re.fullmatch(r'\d{10}', value):
        raise ValidationError('Phone number must be exactly 10 digits.')

def validate_aadhaar(value):
    if not re.fullmatch(r'\d{12}', value):
        raise ValidationError('Aadhaar number must be exactly 12 digits.')
    


# Models
class UserProfile(models.Model):
    username = models.CharField(max_length=40, validators=[validate_username])
    password = models.CharField(max_length=15, validators=[validate_password])

class RiderProfile(models.Model):
    username = models.CharField(max_length=40, validators=[validate_username])
    password = models.CharField(max_length=15, validators=[validate_password])

def validate_vehicle_no(value):
    # Example format: ABC 1234
    if not re.fullmatch(r'[A-Z]{3}\d{4}', value):
        raise ValidationError('Vehicle number must follow the format: ABC 1234.')

def validate_license_no(value):
    # Example format: DL-1C-1234
    if not re.fullmatch(r'[A-Z]{2}-\d[A-Z]-\d{4}', value):
        raise ValidationError('License number must follow the format: DL-1C-1234.')

# Create your models here.
class UserProfile(models.Model):
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=15)

class RiderProfile(models.Model):
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=15)

class RiderTrip(models.Model):
    source = models.CharField(max_length=40)
    destination = models.CharField(max_length=40)

class UserTrip(models.Model):
    source = models.CharField(max_length=40)
    destination = models.CharField(max_length=40)

class CreateRide(models.Model):
    Name = models.CharField(max_length=40)
    age = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(120)])
    email = models.EmailField(max_length=254, unique=True)
    phone_no = models.CharField(max_length=10, validators=[validate_phone])
    Gender = models.CharField(max_length=10,default='Not Specified')  
    vehicle_type = models.CharField(max_length=10)# Add choices if there are predefined types
    vehicle_no = models.CharField(max_length=20,validators=[validate_vehicle_no])
    aadhaar_no = models.CharField(max_length=12, validators=[validate_aadhaar])
    license_no = models.CharField(max_length=20,validators=[validate_license_no])
    Username = models.CharField(max_length=30, validators=[validate_username])
    password = models.CharField(max_length=10)
    
class CreateUser(models.Model):
    Name = models.CharField(max_length=40)
    email = models.EmailField(max_length=254, unique=True)
    age = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(120)])
    phone_no = models.CharField(max_length=10, validators=[validate_phone])
    priority_no = models.CharField(max_length=10, validators=[validate_phone],default='DEFAULT_PRIORITY') 
    Gender = models.CharField(max_length=10,default='Not Specified')
    Username = models.CharField(max_length=30, validators=[validate_username])
    password = models.CharField(max_length=10, validators=[validate_password])

# class mapRider(models.Model):
#     source = models.CharField(max_length=40)
#     destination = models.CharField(max_length=40)

# class mapUser(models.Model):
#     source = models.CharField(max_length=40)
#     destination = models.CharField(max_length=40)
