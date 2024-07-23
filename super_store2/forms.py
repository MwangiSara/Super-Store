from django import forms
from .models import *

class Users_form(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Users
        fields = "__all__"

# class AddCustomers(forms.ModelForm):
#     class Meta:
#         model = Customer
#         fields= "__all__"
#         widgets = {
#             'customer_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter customer name'}),
#             'customer_code': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter customer code'}),
#         }
    
