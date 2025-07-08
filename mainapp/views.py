
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
            data = json.loads(request.body)
            print("✅ Incoming Candidate Data:", data)

            # Foreign key IDs (can be None)
            school_id = data.get('school_id') or None
            college_id = data.get('college_id') or None
            company_id = data.get('company_id') or None

            # Create candidate profile
            candidate = CandidateProfile.objects.create(
                first_name = data.get('first_name', ''),
                last_name = data.get('last_name', ''),
                email = data.get('email', ''),
                phone = data.get('phone', ''),
                gender = data.get('gender', ''),
                password = make_password(data.get('password', '')),
                agreed_info = data.get('agreed_info', False),
                stay_in_loop = data.get('stay_in_loop', False),
                user_type = data.get('user_type', ''),

                # Name fields for easy lookup
                school_name = data.get('school_name', ''),
                college_name = data.get('college_name', ''),
                current_company = data.get('current_company', ''),

                # Foreign Key relations
                school_id = school_id,
                college_id = college_id,
                company_id = company_id,

                # School-specific fields
                current_class = data.get('current_class') or None,
                school_city = data.get('school_city', ''),

                # College/Fresher fields
                domain = data.get('domain', ''),
                course_name = data.get('course_name', ''),
                start_year = data.get('start_year', ''),
                end_year = data.get('end_year', ''),
                college_city = data.get('college_city', ''),

                # Professional fields
                experience_years = data.get('experience_years', ''),
                current_job_role = data.get('current_job_role', ''),
                job_start_year = data.get('job_start_year', ''),
                job_end_year = data.get('job_end_year', ''),
                job_city = data.get('job_city', ''),
            )

            # Career Purpose
            purpose_text = data.get('career_purpose', '')
            if purpose_text:
                CareerPurpose.objects.create(candidate=candidate, purpose=purpose_text)

            print(f"✅ Candidate '{candidate.email}' saved successfully.")
            return JsonResponse({'status': 'success'})

        except Exception as e:
            print("❌ Error while saving candidate:", str(e))
            return JsonResponse({'status': 'error', 'message': str(e)})

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})



from django.shortcuts import render
from .models import School, College, Company, CandidateProfile

def admin_panel_dashboard_view(request):
    context = {
        'school_count': School.objects.count(),
        'college_count': College.objects.count(),
        'company_count': Company.objects.count(),
        'candidate_count': CandidateProfile.objects.count(),
    }
    return render(request, 'admin_panel/admin_dashboard.html', context)


from .models import School  # 👈 model tu bana chuka hai

def schools_list_view(request):
    schools = School.objects.all()
    return render(request, 'admin_panel/schools_list.html', {'schools': schools})



from django.shortcuts import render, redirect
from .models import School

def add_school_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        city = request.POST.get('city')
        contact_number = request.POST.get('contact_number')
        email = request.POST.get('email')
        is_approved = True if request.POST.get('is_approved') == 'on' else False

        School.objects.create(
            name=name,
            address=address,
            city=city,
            contact_number=contact_number,
            email=email,
            is_approved=is_approved
        )
        return redirect('admin_panel/schools_list.html')  # make this view later

    return render(request, 'admin_panel/add_school.html')


from django.shortcuts import render, get_object_or_404
from .models import School

def school_detail_view(request, school_id):
    school = get_object_or_404(School, id=school_id)
    return render(request, 'admin_panel/school_detail.html', {'school': school})


from django.shortcuts import render, get_object_or_404, redirect
from .models import School  # ya jo bhi tera model ka naam ho
from django.contrib import messages

def edit_school_view(request, school_id):
    school = get_object_or_404(School, id=school_id)

    if request.method == 'POST':
        school.name = request.POST.get('name')
        school.address = request.POST.get('address')
        school.city = request.POST.get('city')
        school.contact_number = request.POST.get('contact_number')
        school.email = request.POST.get('email')
        school.is_approved = bool(request.POST.get('is_approved'))
        school.save()
        messages.success(request, 'School updated successfully.')
        return redirect('schools_list')

    return render(request, 'admin_panel/edit_school.html', {'school': school})


def delete_school_view(request, school_id):
    school = get_object_or_404(School, id=school_id)
    school.delete()
    messages.success(request, 'School deleted successfully.')
    return redirect('schools_list')


from django.shortcuts import render, get_object_or_404, redirect
from .models import College
from django.contrib import messages

def view_colleges(request):
    colleges = College.objects.all().order_by('-created_at')
    return render(request, 'admin_panel/view_colleges.html', {'colleges': colleges})

def add_college_view(request):
    if request.method == 'POST':
        College.objects.create(
            name=request.POST.get('name'),
            address=request.POST.get('address'),
            city=request.POST.get('city'),
            contact_number=request.POST.get('contact_number'),
            email=request.POST.get('email'),
            is_approved=bool(request.POST.get('is_approved')),
            domains_accepted=request.POST.get('domains_accepted'),
            courses_accepted=request.POST.get('courses_accepted'),
        )
        messages.success(request, 'College added successfully.')
        return redirect('colleges_list')
    return render(request, 'admin_panel/add_college.html')


def edit_college_view(request, college_id):
    college = get_object_or_404(College, id=college_id)
    if request.method == 'POST':
        college.name = request.POST.get('name')
        college.address = request.POST.get('address')
        college.city = request.POST.get('city')
        college.contact_number = request.POST.get('contact_number')
        college.email = request.POST.get('email')
        college.is_approved = bool(request.POST.get('is_approved'))
        college.domains_accepted = request.POST.get('domains_accepted')
        college.courses_accepted = request.POST.get('courses_accepted')
        college.save()
        messages.success(request, 'College updated successfully.')
        return redirect('colleges_list')
    return render(request, 'admin_panel/edit_college.html', {'college': college})

def delete_college_view(request, college_id):
    college = get_object_or_404(College, id=college_id)
    college.delete()
    messages.success(request, 'College deleted successfully.')
    return redirect('colleges_list')

from django.shortcuts import render, get_object_or_404
from .models import College

def college_detail_view(request, college_id):
    college = get_object_or_404(College, id=college_id)
    return render(request, 'admin_panel/college_detail.html', {'college': college})


# mainapp/views.py

from .models import Company
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

def view_companies(request):
    companies = Company.objects.all().order_by('-created_at')
    return render(request, 'admin_panel/view_companies.html', {'companies': companies})

def add_company(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        city = request.POST.get('city')
        contact_number = request.POST.get('contact_number')
        email = request.POST.get('email')
        is_approved = request.POST.get('is_approved') == 'on'

        Company.objects.create(
            name=name,
            address=address,
            city=city,
            contact_number=contact_number,
            email=email,
            is_approved=is_approved
        )
        messages.success(request, "Company added successfully.")
        return redirect('companies_list')
    
    return render(request, 'admin_panel/add_company.html')

def edit_company(request, company_id):
    company = get_object_or_404(Company, pk=company_id)
    if request.method == 'POST':
        company.name = request.POST.get('name')
        company.address = request.POST.get('address')
        company.city = request.POST.get('city')
        company.contact_number = request.POST.get('contact_number')
        company.email = request.POST.get('email')
        company.is_approved = request.POST.get('is_approved') == 'on'
        company.save()
        messages.success(request, "Company updated successfully.")
        return redirect('companies_list')

    return render(request, 'admin_panel/edit_company.html', {'company': company})

def delete_company(request, company_id):
    company = get_object_or_404(Company, pk=company_id)
    company.delete()
    messages.success(request, "Company deleted successfully.")
    return redirect('companies_list')

from django.shortcuts import get_object_or_404, render
from .models import Company

def company_detail_view(request, company_id):
    company = get_object_or_404(Company, id=company_id)
    return render(request, 'admin_panel/company_detail.html', {'company': company})


from django.http import JsonResponse
from mainapp.models import School, College, Company
import json

# views.py
def fetch_dropdown_data(request):
    schools = list(School.objects.filter(is_approved=True).values('id', 'name', 'city'))
    colleges = list(College.objects.filter(is_approved=True).values('id', 'name', 'city', 'domains_accepted', 'courses_accepted'))
    companies = list(Company.objects.filter(is_approved=True).values('id', 'name', 'city'))

    # Extract domains/courses as before
    domains = set()
    courses = set()
    for college in colleges:
        try:
            domain_list = json.loads(college['domains_accepted']) if college['domains_accepted'] else []
            domains.update(domain_list)
        except json.JSONDecodeError:
            pass

        try:
            course_list = json.loads(college['courses_accepted']) if college['courses_accepted'] else []
            courses.update(course_list)
        except json.JSONDecodeError:
            pass

    return JsonResponse({
        'schools': schools,  # ✅ Not just name
        'colleges': colleges,
        'companies': companies,
        'domains': sorted([d.strip() for d in domains if d.strip()]),
        'courses': sorted([c.strip() for c in courses if c.strip()])
    })
