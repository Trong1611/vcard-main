from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class QRUserForm(forms.Form):
    DisplayName = forms.CharField(label="Your Full Name", max_length=200)
    Company = forms.CharField(label="Company", max_length=200)
    Position = forms.CharField(label="Position", max_length=200)
    PhoneNumber = forms.CharField(label="Phone Number", max_length=12)
    Address = forms.CharField(label="Address", max_length=200)
    Email = forms.CharField(label="Email", max_length=50)
    Website = forms.CharField(label="Website", max_length=50)


class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username', 'email', 'password1', 'password2']


class UploadIconForm(forms.Form):
    file = forms.FileField(label=False)

    file.widget.attrs.update({"class": "form-control"})
