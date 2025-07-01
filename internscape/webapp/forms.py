from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
from .models import Job,Application,Blog

from django import forms

from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

#register a user

class CandidateRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# Company Registration Form
class CompanyRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

#Login a user

class LoginForm(AuthenticationForm):

    username = forms.CharField(widget= TextInput())
    password = forms.CharField(widget=PasswordInput())



class JobForm(forms.ModelForm):
    class Meta:

        model = Job
        fields = [
            'company_name', 'title', 'description', 'salary_package', 
            'location', 'experience_required', 'skills_required'
        ]
    

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['name', 'phone_number', 'email', 'cover_letter_file']


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'description']