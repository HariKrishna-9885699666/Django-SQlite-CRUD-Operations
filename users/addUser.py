from django import forms
from django.forms.widgets import DateInput
from django.core.exceptions import ValidationError
import re
from .models import User  # Assuming you have a User model

class UserForm(forms.Form):
    first_name = forms.CharField(
        min_length=3,
        max_length=10,
        widget=forms.TextInput(attrs={'class': 'form-control w-25'})
    )
    last_name = forms.CharField(
        min_length=3,
        max_length=10,
        widget=forms.TextInput(attrs={'class': 'form-control w-25'})
    )
    phone = forms.CharField(
        max_length=10,
        widget=forms.TextInput(attrs={'class': 'form-control w-25'})
    )
    joined_date = forms.DateField(
        widget=DateInput(
            attrs={
                'type': 'date',
                'class': 'form-control w-25',
            }
        )
    )

    # Custom init method to accept an instance
    def __init__(self, *args, **kwargs):
        instance = kwargs.pop('instance', None)
        super(UserForm, self).__init__(*args, **kwargs)
        
        # If an instance is provided, pre-fill the form fields with its data
        if instance:
            self.fields['first_name'].initial = instance.firstname
            self.fields['last_name'].initial = instance.lastname
            self.fields['phone'].initial = instance.phone
            self.fields['joined_date'].initial = instance.joined_date

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone', 'joined_date']
        widgets = {
            'joined_date': DateInput(attrs={'type': 'date', 'class': 'form-control w-25'})
        }

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if not first_name.isalpha():
            raise ValidationError("First name should only contain letters.")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        if not last_name.isalpha():
            raise ValidationError("Last name should only contain letters.")
        return last_name

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if not re.match(r'^\d{10}$', phone):  # Assumes a 10-digit phone number
            raise ValidationError("Enter a valid 10-digit phone number.")
        return phone
