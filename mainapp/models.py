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
    password = models.CharField(max_length=128)
    agreed_info = models.BooleanField(default=False)
    stay_in_loop = models.BooleanField(default=False)
    user_type = models.CharField(max_length=20, choices=USER_TYPES)

    profile_photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)  # <-- Added

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

    # Foreign Keys
    school = models.ForeignKey('School', null=True, blank=True, on_delete=models.SET_NULL)
    college = models.ForeignKey('College', null=True, blank=True, on_delete=models.SET_NULL)
    company = models.ForeignKey('Company', null=True, blank=True, on_delete=models.SET_NULL)

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
    

class School(models.Model):
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    contact_number = models.CharField(max_length=20, blank=True, null=True)  # ✅ Corrected
    email = models.EmailField(blank=True, null=True)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


from django.db import models

class College(models.Model):
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    contact_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    is_approved = models.BooleanField(default=False)
    domains_accepted = models.TextField(blank=True, null=True, help_text="Comma-separated subjects like: Computer Science, Mechanical")
    courses_accepted = models.TextField(blank=True, null=True, help_text="Comma-separated courses like: B.Tech, M.Tech")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

# mainapp/models.py

class Company(models.Model):
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    contact_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



# mainapp/models.py
from django.db import models

class Internship(models.Model):
    MODE_CHOICES = (
        ('Online', 'Online'),
        ('Offline', 'Offline'),
        ('Hybrid', 'Hybrid'),
    )

    CATEGORY_CHOICES = (
        ('Paid', 'Paid'),
        ('Unpaid', 'Unpaid'),
    )

    title = models.CharField(max_length=200)
    company_name = models.CharField(max_length=150)
    domain = models.CharField(max_length=100)
    mode = models.CharField(max_length=10, choices=MODE_CHOICES, default='Online')
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    stipend_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    duration_weeks = models.IntegerField(null=True, blank=True)
    location = models.CharField(max_length=120, null=True, blank=True)
    application_link = models.URLField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

from django.db import models

class Job(models.Model):
    EMPLOYMENT_TYPES = [
    ('Full-time', 'Full-time'),
    ('Part-time', 'Part-time'),
    ('Contract', 'Contract'),
    ('Internship', 'Internship'),
]


    EXPERIENCE_LEVELS = [
        ('Fresher', 'Fresher'),
        ('0‑2 Yrs', '0‑2 Yrs'),
        ('2‑5 Yrs', '2‑5 Yrs'),
        ('5+ Yrs', '5+ Yrs'),
    ]

    CATEGORY_CHOICES = [
        ('Human Resources', 'Human Resources'),
        ('Software Development', 'Software Development'),
        ('Marketing', 'Marketing'),
        ('Operations', 'Operations'),
        ('Finance', 'Finance'),]

    title = models.CharField(max_length=200)
    company_name = models.CharField(max_length=150)
    domain = models.CharField(max_length=100)
    employment_type = models.CharField(max_length=20, choices=EMPLOYMENT_TYPES, default='Full‑time')
    salary_min_lpa = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    salary_max_lpa = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    experience_level = models.CharField(max_length=20, choices=EXPERIENCE_LEVELS, default='Fresher')
    location = models.CharField(max_length=120, null=True, blank=True)
    remote_allowed = models.BooleanField(default=False)
    apply_by = models.DateField(null=True, blank=True)
    job_description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.title
    


    

from django.db import models
class Competition(models.Model):
    CATEGORY_CHOICES = [
        ('Free', 'Free'),
        ('Paid', 'Paid'),
    ]

    COMPETITION_TYPE_CHOICES = [
        ('Competitions', 'Competitions'),
        ('Hackathons', 'Hackathons'),
        ('Quizzes', 'Quizzes'),
        ('Scholarships', 'Scholarships'),
        ('Workshops', 'Workshops'),
        ('Conferences', 'Conferences'),
        ('Cultural Events', 'Cultural Events'),
    ]

    MODE_CHOICES = [
        ('Online', 'Online'),
        ('Offline', 'Offline'),
        ('Hybrid', 'Hybrid'),
    ]

    title                 = models.CharField(max_length=200)
    host_org              = models.CharField(max_length=150)
    category              = models.CharField(max_length=4,  choices=CATEGORY_CHOICES, default='Free')
    fee_amount            = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    competition_type      = models.CharField(max_length=20, choices=COMPETITION_TYPE_CHOICES)  # updated max_length & choices
    mode                  = models.CharField(max_length=7,  choices=MODE_CHOICES, default='Online')
    start_date            = models.DateField(null=True, blank=True)
    end_date              = models.DateField(null=True, blank=True)
    prize_pool            = models.CharField(max_length=120, null=True, blank=True)
    team_size             = models.CharField(max_length=20, default='Individual')
    registration_deadline = models.DateField(null=True, blank=True)
    created_at            = models.DateTimeField(auto_now_add=True)
    updated_at            = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



# models.py

class AppliedInternship(models.Model):
    PAYMENT_CHOICES = [
        ('Success', 'Success'),
        ('Unsuccess', 'Unsuccess'),
        ('Not Applicable', 'Not Applicable'),
    ]

    candidate = models.ForeignKey(
        CandidateProfile,
        on_delete=models.CASCADE,
        related_name='applied_internships',
        db_column='candidate_id'
    )

    internship = models.ForeignKey(
        Internship,
        on_delete=models.CASCADE,
        related_name='applications',
        db_column='internship_id'
    )

    applied_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(
        max_length=20,
        choices=PAYMENT_CHOICES,
        default='Not Applicable'
    )

    # Candidate details
    name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)

    # Internship extra details (copied for record keeping)
    internship_title = models.CharField(max_length=200, blank=True)
    internship_company_name = models.CharField(max_length=150, blank=True)
    mode = models.CharField(max_length=10, blank=True)
    category = models.CharField(max_length=10, blank=True)
    stipend_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    class Meta:
        unique_together = ('candidate', 'internship')
        db_table = 'mainapp_appliedinternship'

    def __str__(self):
        return f"{self.candidate.first_name} -> {self.internship.title}"



# models.py

from django.db import models
from .models import CandidateProfile, Job  # Adjust the import path if needed

class AppliedForJob(models.Model):
    application_id = models.AutoField(primary_key=True)

    candidate = models.ForeignKey(
        CandidateProfile,
        on_delete=models.CASCADE,
        related_name='job_applications'
    )

    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE,
        related_name='job_applicants'
    )

    applied_at = models.DateTimeField(auto_now_add=True)

    # Job Snapshot Fields (Stored as redundancy in case original job changes)
    title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    domain = models.CharField(max_length=100)
    employment_type = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    # User Snapshot Fields
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    class Meta:
        unique_together = ('candidate', 'job')  # Prevent duplicate applications
        db_table = 'mainapp_appliedforjob'

    def __str__(self):
        return f"{self.candidate.first_name} -> {self.job.title}"





from django.db import models
from .models import CandidateProfile, Competition  # adjust if paths differ

class CompetitionsApplied(models.Model):
    application_id = models.AutoField(primary_key=True)

    # Foreign Keys
    candidate = models.ForeignKey(
        CandidateProfile,
        on_delete=models.CASCADE,
        related_name='competition_applications'
    )

    competition = models.ForeignKey(
        Competition,
        on_delete=models.CASCADE,
        related_name='applicants'
    )

    applied_at = models.DateTimeField(auto_now_add=True)

    # Competition Snapshot
    title = models.CharField(max_length=255)
    host_org = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    fee_amount = models.DecimalField(max_digits=10, decimal_places=2)
    competition_type = models.CharField(max_length=100)
    mode = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    team_size = models.CharField(max_length=50)  # instead of IntegerField

    prize_pool = models.CharField(max_length=100)

    # Candidate Snapshot
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    class Meta:
        unique_together = ('candidate', 'competition')  # prevents duplicate entries
        db_table = 'mainapp_competitions_applied'

    def __str__(self):
        return f"{self.candidate.first_name} -> {self.competition.title}"
