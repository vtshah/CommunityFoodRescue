from django import forms
from django.contrib.auth.models import User
from .models import SignUp
from .models import MakeADonation

from bootstrap3_datetime.widgets import DateTimePicker

class SignUpForm(forms.ModelForm):
    hours_of_operation_start_time = forms.DateTimeField(
        required=True,
        widget=DateTimePicker(options={"format": "YYYY-MM-DD HH:mm:ss"}))
    hours_of_operation_end_time = forms.DateTimeField(
        required=True,
        widget=DateTimePicker(options={"format": "YYYY-MM-DD HH:mm:ss"}))
    
    class Meta:
        model = SignUp

class MakeADonationForm(forms.ModelForm):
    time_food_available_start_time = forms.DateTimeField(
        required=True,
        widget=DateTimePicker(options={"format": "YYYY-MM-DD HH:mm:ss"}))
    time_food_available_end_time = forms.DateTimeField(
        required=True,
        widget=DateTimePicker(options={"format": "YYYY-MM-DD HH:mm:ss"}))
    class Meta:
        model = MakeADonation
        
class ToDoForm(forms.Form):
    reminder = forms.DateTimeField(
        required=False,
        widget=DateTimePicker(options={"format": "YYYY-MM-DD HH:mm:ss",
                                       "pickSeconds": False}))
        
#class LoginForm(forms.Form):
#        username = forms.CharField(label=(u'User Name'))
#        password = forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False))