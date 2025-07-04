
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm
from django.contrib import messages

def home_view(request):
    return render(request, 'home.html')


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully!")
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')  # Replace with actual dashboard
        else:
            messages.error(request, "Invalid credentials")
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def explore_sections_view(request):
    return render(request, 'unstop_tabs.html')


def slogan_view(request):
    return render(request, 'slogan.html')

def login_view(request):
    return render(request, 'login_form.html')  # or adjust the path if needed


def register_view(request):
    return render(request, 'register.html')


from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import CandidateProfile, CareerPurpose
from django.contrib.auth.hashers import make_password
import json

@csrf_exempt
def submit_candidate_form(request):
    if request.method == 'POST':
        try:
            # ✅ Parse JSON body
            data = json.loads(request.body)

            # ✅ Create CandidateProfile
            candidate = CandidateProfile.objects.create(
                first_name=data.get('first_name', ''),
                last_name=data.get('last_name', ''),
                email=data.get('email', ''),
                phone=data.get('phone', ''),
                gender=data.get('gender', ''),
                password=make_password(data.get('password', '')),  # ✅ hash password
                agreed_info=data.get('agreed_info', False),
                stay_in_loop=data.get('stay_in_loop', False),
                user_type=data.get('user_type', ''),

                # School
                school_name=data.get('school_name', ''),
                current_class=data.get('current_class') or None,
                school_city=data.get('school_city', ''),

                # College/Fresher
                domain=data.get('domain', ''),
                course_name=data.get('course_name', ''),
                start_year=data.get('start_year', ''),
                end_year=data.get('end_year', ''),
                college_name=data.get('college_name', ''),
                college_city=data.get('college_city', ''),

                # Professional
                experience_years=data.get('experience_years', ''),
                current_job_role=data.get('current_job_role', ''),
                current_company=data.get('current_company', ''),
                job_start_year=data.get('job_start_year', ''),
                job_end_year=data.get('job_end_year', ''),
                job_city=data.get('job_city', ''),
            )

            # ✅ Handle Career Purpose
            purpose_text = data.get('career_purpose', '')
            if purpose_text:
                CareerPurpose.objects.create(candidate=candidate, purpose=purpose_text)

            return JsonResponse({'status': 'success'})

        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
