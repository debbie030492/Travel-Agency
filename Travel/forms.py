from django import forms
from django.contrib.admin.widgets import AdminSplitDateTime, AdminDateWidget
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Order
from .models import Package


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('First_name', 'Last_name', 'Date_of_departure', 'Number_of_travelers', 'Package', 'Departing_city', 'Notes')

        widgets = {
            'Date_of_departure': forms.DateTimeInput(attrs={'class': 'datetime-input'})
        }