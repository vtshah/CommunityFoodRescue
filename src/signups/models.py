from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.utils.encoding import smart_unicode
from phonenumber_field.modelfields import PhoneNumberField
import datetime
from django.contrib.gis.db import models
from django.forms import ModelForm, EmailField, CharField
from django.contrib.auth.forms import UserCreationForm



# Create your models here.

class SignUp(models.Model):
    IDENTITY_CHOICES = (
        ('Donor', 'Donor'),
        ('Recipient', 'Recipient'),
    )
    identity = models.CharField(max_length=9, choices = IDENTITY_CHOICES   , default='Donor')
    first_name = models.CharField(max_length=120, null=True, blank=True)
    last_name = models.CharField(max_length=120, null=True, blank=True)
    phone_number = PhoneNumberField()
    establishment_name = models.CharField(max_length=200, null=True, blank=True)
    establishment_address = models.CharField(max_length=500, null=True, blank=True)
    refrigeration = models.FloatField()
    freezer = models.FloatField()
    dry_storage = models.FloatField()
    loading_docks = models.IntegerField()
    dock_levelers = models.IntegerField()
    scales = models.IntegerField()
    pallet_jacks = models.IntegerField()
    fork_lifts = models.IntegerField()
    refrigerated_trucks = models.IntegerField()
    box_trucks = models.IntegerField()
    vans = models.IntegerField()
    truck_accessible = models.BooleanField(default=True)
    number_of_onsite_parking_spaces = models.IntegerField()
    hours_of_operations_start_time = models.DateTimeField(default=datetime.datetime.now, blank=True)
    hours_of_operations_end_time = models.DateTimeField(default=datetime.datetime.now, blank=True)
    number_of_current_volunteers = models.IntegerField()
    number_of_current_staff_devoted_to_recieving_or_distributing_food = models.IntegerField()
    number_of_current_recipients_per_week = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __unicode__(self):
        return smart_unicode(self.first_name)
    
class MakeADonation(models.Model):
    food_description = models.CharField(max_length=500, null=False, blank=False)
    time_food_available_start_time = models.DateTimeField()
    time_food_available_end_time = models.DateTimeField()
    food_type = models.CharField(max_length=100, null=False, blank=False)
    FOOD_RECIEVING_CHOICES = (
        ('Pickup', 'Pickup'),
        ('Dropoff', 'Dropoff'),
    )
    food_recieving = models.CharField(max_length=7, choices = FOOD_RECIEVING_CHOICES, default='Pickup')
    quantity = models.IntegerField()
    packaging = models.CharField(max_length=120, null=True, blank=True)
    pickup_instructions = models.CharField(max_length=500, null=False, blank=False)
    
    def _unicode_(self):
        return smart_unicode(self.food_description)
    
    
class AccountCreationForm(UserCreationForm):
    
    username = CharField(label=(u'User Name'))
    email = EmailField(label=(u'Email'))
    
    phone_number = PhoneNumberField()

    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name']
