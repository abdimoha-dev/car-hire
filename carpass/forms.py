from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CarForm(forms.Form):
    car_model = forms.CharField(label='Car model', max_length= 50)
    car_numberplate = forms.CharField(label='Car Number Plate', max_length=10)
    car_image = forms.FileField()
    car_sits = forms.IntegerField()
    price_per_day = forms.IntegerField()

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1','password2']