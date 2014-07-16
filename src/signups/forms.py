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
    
    username = forms.CharField(label=(u'User Name'))
    email = forms.EmailField(label=(u'Email Address'))
    password = forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False))
    password1 = forms.CharField(label=(u'Verify Password'), widget=forms.PasswordInput(render_value=False))
    
    class Meta:
        model = SignUp
        
    def clean_username(self):
                username = self.cleaned_data['username']
                try:
                        User.objects.get(username=username)
                except User.DoesNotExist:
                        return username
                raise forms.ValidationError("That username is already taken, please select another.")

    def clean(self):
                if self.cleaned_data['password'] != self.cleaned_data['password1']:
                        raise forms.ValidationError("The passwords did not match.  Please try again.")
                return self.cleaned_data

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
        
class LoginForm(forms.Form):
        username = forms.CharField(label=(u'User Name'))
        password = forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False))