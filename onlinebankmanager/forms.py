from django import forms
from django.contrib.auth.models import User
from .models import *
from django.forms.extras.widgets import SelectDateWidget
from phonenumber_field.formfields import PhoneNumberField
from django.utils.translation import ugettext_lazy as _

class AccRegistration(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs=dict(required=True,max_length=30)))
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True,max_length=30)))
    password = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True,max_length=30)))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True,max_length=30)))
    que = forms.CharField(widget=forms.TextInput(attrs=dict(required=True,max_length=30)))
    ans = forms.CharField(widget=forms.TextInput(attrs=dict(required=True,max_length=30)))
    address = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=50)))
    phno = PhoneNumberField()
    account_choise = (('Student', 'Student'), ('Saving', 'Saving'))
    acc_type = forms.ChoiceField(widget=forms.Select(),choices=account_choise)



    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(_('username already exist..'))

    def clean(self):
        try:
            if 'password' in self.cleaned_data and 'password2' in self.cleaned_data:
                if self.cleaned_data['password'] != self.cleaned_data['password2']:
                    raise forms.ValidationError(_("password dosen't match.."))
                return self.cleaned_data
        except:
            raise forms.ValidationError(_("some error occur"))

class DepoAmount(forms.Form):
    amount=forms.FloatField(widget=forms.TextInput(attrs=dict(required=True,max_length=30)))

class WithDraw(forms.Form):
    amount=forms.FloatField(widget=forms.TextInput(attrs=dict(required=True,max_length=30)))





