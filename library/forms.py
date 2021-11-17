from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

class AddBookForm(forms.ModelForm):
    class Meta:
        model = AddBook
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    group = forms.ModelChoiceField(queryset=Group.objects.all(),required=True)
    class Meta:
        model = User
        fields = ['username','email','password1','password2','first_name','last_name','group']
