from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']




from django.db import models

class CandidateProfile(models.Model):
    GENDER_CHOICES = [('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')]
    USER_TYPES = [
        ('school', 'School'),
        ('college', 'College Student'),
        ('fresher', 'Fresher'),
        ('professional', 'Professional'),
    ]

    # Common Fields
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    password = models.CharField(max_length=128)  # store hashed passwords
    agreed_info = models.BooleanField(default=False)
    stay_in_loop = models.BooleanField(default=False)
    user_type = models.CharField(max_length=20, choices=USER_TYPES)

    # School Fields
    school_name = models.CharField(max_length=150, blank=True, null=True)
    current_class = models.IntegerField(blank=True, null=True)
    school_city = models.CharField(max_length=100, blank=True, null=True)

    # College/Fresher Fields
    domain = models.CharField(max_length=100, blank=True, null=True)
    course_name = models.CharField(max_length=150, blank=True, null=True)
    start_year = models.CharField(max_length=10, blank=True, null=True)
    end_year = models.CharField(max_length=10, blank=True, null=True)
    college_name = models.CharField(max_length=150, blank=True, null=True)
    college_city = models.CharField(max_length=100, blank=True, null=True)

    # Professional Fields
    experience_years = models.CharField(max_length=10, blank=True, null=True)
    current_job_role = models.CharField(max_length=100, blank=True, null=True)
    current_company = models.CharField(max_length=150, blank=True, null=True)
    job_start_year = models.CharField(max_length=10, blank=True, null=True)
    job_end_year = models.CharField(max_length=10, blank=True, null=True)
    job_city = models.CharField(max_length=100, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} ({self.email})"


class CareerPurpose(models.Model):
    PURPOSE_CHOICES = [
        ('job', 'To find a Job'),
        ('compete', 'Compete & Upskill'),
        ('host', 'To Host an Event'),
        ('mentor', 'To be a Mentor'),
    ]

    candidate = models.ForeignKey('CandidateProfile', on_delete=models.CASCADE)
    purpose = models.CharField(max_length=50, choices=PURPOSE_CHOICES)

    def __str__(self):
        return f"{self.candidate.email} - {self.purpose}"