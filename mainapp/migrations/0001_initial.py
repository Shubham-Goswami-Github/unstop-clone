# Generated by Django 5.2.3 on 2025-07-01 06:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CandidateProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=15)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10)),
                ('password', models.CharField(max_length=128)),
                ('agreed_info', models.BooleanField(default=False)),
                ('stay_in_loop', models.BooleanField(default=False)),
                ('user_type', models.CharField(choices=[('school', 'School'), ('college', 'College Student'), ('fresher', 'Fresher'), ('professional', 'Professional')], max_length=20)),
                ('school_name', models.CharField(blank=True, max_length=150, null=True)),
                ('current_class', models.IntegerField(blank=True, null=True)),
                ('school_city', models.CharField(blank=True, max_length=100, null=True)),
                ('domain', models.CharField(blank=True, max_length=100, null=True)),
                ('course_name', models.CharField(blank=True, max_length=150, null=True)),
                ('start_year', models.CharField(blank=True, max_length=10, null=True)),
                ('end_year', models.CharField(blank=True, max_length=10, null=True)),
                ('college_name', models.CharField(blank=True, max_length=150, null=True)),
                ('college_city', models.CharField(blank=True, max_length=100, null=True)),
                ('experience_years', models.CharField(blank=True, max_length=10, null=True)),
                ('current_job_role', models.CharField(blank=True, max_length=100, null=True)),
                ('current_company', models.CharField(blank=True, max_length=150, null=True)),
                ('job_start_year', models.CharField(blank=True, max_length=10, null=True)),
                ('job_end_year', models.CharField(blank=True, max_length=10, null=True)),
                ('job_city', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CareerPurpose',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purpose', models.CharField(choices=[('job', 'To find a Job'), ('compete', 'Compete & Upskill'), ('host', 'To Host an Event'), ('mentor', 'To be a Mentor')], max_length=50)),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.candidateprofile')),
            ],
        ),
    ]
