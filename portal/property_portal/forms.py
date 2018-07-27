from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import Buy, Rent, UserProfile


# Registration form
class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'password1', 'password2']

# edit profile
class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']

# login form
class LoginForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'password']

# let to Rent form
class RentPropertyForm(forms.ModelForm):
    class Meta:
        model = Rent
        exclude= ['id']

# sell form
class SellPropertyForm(forms.ModelForm):
    class Meta:
        model = Buy
        exclude= ['id']
