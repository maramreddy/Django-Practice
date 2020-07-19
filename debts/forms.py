from django import forms
from .models import Person, UserProfile
from django.contrib.auth.models import User

class NewUserForm(forms.ModelForm):
    class Meta():
        model = Person
        fields = '__all__'

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','email','password')

class UserProfileForm(forms.ModelForm):
    class Meta():
        model = UserProfile
        fields = ('profile_link','profile_pic')
