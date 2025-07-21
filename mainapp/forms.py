from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
# mainapp/forms.py
from django import forms
from .models import Internship

class InternshipForm(forms.ModelForm):
    class Meta:
        model = Internship
        fields = '__all__'
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

from django import forms
from .models import Job

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'

from django import forms
from mainapp.models import Competition

class CompetitionForm(forms.ModelForm):
    class Meta:
        model  = Competition
        fields = '__all__'
        widgets = {
            # quick Bootstrap styling
            'start_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'end_date':   forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'registration_deadline': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }
