
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required


from django.contrib.auth.decorators import login_required


from .models import Internship, Job, Competition

def home_view(request):
    internships = Internship.objects.all()
    jobs = Job.objects.all()
    competitions = Competition.objects.all()
    return render(request, 'home.html', {
        'internships': internships,
        'jobs': jobs,
        'competitions': competitions,
    })



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
    request.session.flush()  # This clears all session data
    return redirect('home')  # ya jahan bhi redirect karna ho


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
            # If multipart, use request.POST and request.FILES
            if request.content_type.startswith('multipart/form-data'):
                data = request.POST
                files = request.FILES
            else:
                data = json.loads(request.body)
                files = None
            print("✅ Incoming Candidate Data:", data)

            # Foreign key IDs (can be None)
            school_id = data.get('school_id') or None
            college_id = data.get('college_id') or None
            company_id = data.get('company_id') or None

            # Handle checkboxes (may come as 'on', 'true', True, or '1')
            def parse_bool(val):
                return str(val).lower() in ['true', 'on', '1']

            # Create candidate profile
            candidate = CandidateProfile(
                first_name = data.get('first_name', ''),
                last_name = data.get('last_name', ''),
                email = data.get('email', ''),
                phone = data.get('phone', ''),
                gender = data.get('gender', ''),
                password = make_password(data.get('password', '')),
                agreed_info = parse_bool(data.get('agreed_info', False)),
                stay_in_loop = parse_bool(data.get('stay_in_loop', False)),
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
            # Handle profile photo
            if files and files.get('profile_photo'):
                candidate.profile_photo = files['profile_photo']
            candidate.save()

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


from mainapp.models import School, College, Company, CandidateProfile, Internship, Job, Competition
from django.contrib.admin.views.decorators import staff_member_required

from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Count
from django.db.models.functions import TruncDate
from django.shortcuts import render
from .models import School, College, Company, CandidateProfile, Internship, Job, Competition
from django.db.models.functions import TruncMonth
from django.db.models import Count


from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from django.db.models.functions import TruncMonth
from django.db.models import Count
from django.utils.dateformat import DateFormat
from .models import School, College, Company, CandidateProfile, Internship, Job, Competition
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Count
from django.db.models.functions import TruncDay
from django.shortcuts import render
from mainapp.models import (
    School, College, Company,
    CandidateProfile, Internship, Job, Competition
)


def admin_panel_dashboard_view(request):
    # Total organization counts
    total_schools = School.objects.count()
    total_colleges = College.objects.count()
    total_companies = Company.objects.count()

    # Total candidate count
    total_candidates = CandidateProfile.objects.count()

    # Candidate type-wise counts
    school_candidates_count = CandidateProfile.objects.filter(user_type='school').count()
    college_candidates_count = CandidateProfile.objects.filter(user_type='college').count()
    experienced_candidates_count = CandidateProfile.objects.filter(user_type='professional').count()
    fresher_candidates_count = CandidateProfile.objects.filter(user_type='fresher').count()

    # Total opportunities
    total_internships = Internship.objects.count()
    total_jobs = Job.objects.count()
    total_competitions = Competition.objects.count()

    # Recent internships list for table (limit 80)
    internships = list(
        Internship.objects.all().order_by('-created_at')[:80].values(
            'id',
            'title',
            'company_name',
            'created_at',
            'category',
            'mode',
            'domain',
            'stipend_amount',
            'duration_weeks',
            'location',
        )
    )

    # Internship creation count per day (for line chart)
    internships_daily_data = (
        Internship.objects
        .annotate(day=TruncDay('created_at'))
        .values('day')
        .annotate(count=Count('id'))
        .order_by('day')
    )
    internships_by_day = [
        {
            'date': entry['day'].strftime('%Y-%m-%d'),
            'count': entry['count']
        }
        for entry in internships_daily_data
    ]

    # Jobs data list (full set)
    jobs = list(
        Job.objects.all().order_by('-created_at').values(
            'id',
            'title',
            'company_name',
            'created_at',
            'category',
            'employment_type',
            'experience_level',
            'domain',
        )
    )

    # Job creation count per day (for line chart)
    jobs_daily_data = (
        Job.objects
        .annotate(day=TruncDay('created_at'))
        .values('day')
        .annotate(count=Count('id'))
        .order_by('day')
    )
    jobs_by_day = [
        {
            'date': entry['day'].strftime('%Y-%m-%d'),
            'count': entry['count']
        }
        for entry in jobs_daily_data
    ]
     # ✅ Competitions
    competitions = list(
        Competition.objects.all().order_by('-created_at').values(
            'id', 'title', 'host_org', 'category', 'mode',
            'competition_type', 'created_at'
        )
    )

    competitions_daily_data = (
        Competition.objects.annotate(day=TruncDay('created_at'))
        .values('day').annotate(count=Count('id')).order_by('day')
    )
    competitions_by_day = [{'date': entry['day'].strftime('%Y-%m-%d'), 'count': entry['count']} for entry in competitions_daily_data]


    # Candidate count per organization
    schools = School.objects.all()
    for school in schools:
        school.candidate_count = CandidateProfile.objects.filter(school_id=school.id).count()

    colleges = College.objects.all()
    for college in colleges:
        college.candidate_count = CandidateProfile.objects.filter(college_id=college.id).count()

    companies = Company.objects.all()
    for company in companies:
        company.candidate_count = CandidateProfile.objects.filter(company_id=company.id).count()

    # Final context passed to dashboard template
    context = {
        'school_count': total_schools,
        'college_count': total_colleges,
        'company_count': total_companies,

        'candidate_count': total_candidates,
        'school_candidates_count': school_candidates_count,
        'college_candidates_count': college_candidates_count,
        'experienced_count': experienced_candidates_count,
        'fresher_count': fresher_candidates_count,

        'internship_count': total_internships,
        'job_count': total_jobs,
        'competition_count': total_competitions,

        'schools': schools,
        'colleges': colleges,
        'companies': companies,

        'internships': internships,
        'internships_by_day': internships_by_day,

        'jobs': jobs,
        'jobs_by_day': jobs_by_day,

         # ✅ Send competitions to template
        'competitions': competitions,
        'competitions_by_day': competitions_by_day,
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
        return redirect("schools_list")  # make this view later

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



from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from .models import Company  # import your model


def add_company(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        city = request.POST.get('city')
        contact_number = request.POST.get('contact_number')
        email = request.POST.get('email')
        password = request.POST.get('password')
        is_approved = request.POST.get('is_approved') == 'on'

        # hash password before saving
        hashed_password = make_password(password)

        Company.objects.create(
            name=name,
            address=address,
            city=city,
            contact_number=contact_number,
            email=email,
            password=hashed_password,
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

from .models import CandidateProfile, School, College, Company

def candidates_summary(request):
    school_count = CandidateProfile.objects.filter(user_type='school').count()
    college_count = CandidateProfile.objects.filter(user_type='college').count()
    experienced_count = CandidateProfile.objects.filter(user_type='professional').count()

    # Annotate each with count of registered candidates
    schools = School.objects.all()
    for school in schools:
        school.candidate_count = CandidateProfile.objects.filter(user_type='school', school_id=school.id).count()

    colleges = College.objects.all()
    for college in colleges:
        college.candidate_count = CandidateProfile.objects.filter(user_type='college', college_id=college.id).count()

    companies = Company.objects.all()
    for company in companies:
        company.candidate_count = CandidateProfile.objects.filter(user_type='professional', company_id=company.id).count()

    return render(request, 'admin_panel/candidates_summary.html', {
        'school_count': school_count,
        'college_count': college_count,
        'experienced_count': experienced_count,
        'schools': schools,
        'colleges': colleges,
        'companies': companies
    })


# views.py
from django.shortcuts import get_object_or_404

def view_candidates_by_org(request, org_type, org_id):
    org_model = {'school': School, 'college': College, 'company': Company}.get(org_type)
    if not org_model:
        return HttpResponse("Invalid organization type", status=400)

    organization = get_object_or_404(org_model, id=org_id)
    if org_type == 'school':
        candidates = CandidateProfile.objects.filter(user_type='school', school_id=org_id)
    elif org_type == 'college':
        candidates = CandidateProfile.objects.filter(user_type='college', college_id=org_id)
    elif org_type == 'company':
        candidates = CandidateProfile.objects.filter(user_type='professional', company_id=org_id)

    return render(request, 'admin_panel/view_candidates.html', {
        'organization': organization,
        'org_type': org_type,
        'candidates': candidates,
    })



from django.shortcuts import render, get_object_or_404, redirect
from .models import CandidateProfile
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

def view_candidate(request, candidate_id):
    candidate = get_object_or_404(CandidateProfile, id=candidate_id)
    return render(request, 'admin_panel/view_candidate_detail.html', {'candidate': candidate})
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import CandidateProfile


def edit_candidate(request, candidate_id):
    candidate = get_object_or_404(CandidateProfile, pk=candidate_id)
    org_type = candidate.user_type  # 'school' | 'college' | 'professional' | 'fresher'

    if request.method == 'POST':
        candidate.first_name = request.POST.get('first_name')
        candidate.last_name = request.POST.get('last_name')
        candidate.email = request.POST.get('email')
        candidate.phone = request.POST.get('phone')
        candidate.gender = request.POST.get('gender')

        if request.FILES.get('profile_photo'):
            candidate.profile_photo = request.FILES['profile_photo']

        if org_type == 'school':
            candidate.school_name = request.POST.get('school_name')
            candidate.current_class = request.POST.get('current_class')
            candidate.school_city = request.POST.get('school_city')

        elif org_type == 'college':
            candidate.college_name = request.POST.get('college_name')
            candidate.domain = request.POST.get('domain')
            candidate.course_name = request.POST.get('course_name')
            candidate.start_year = request.POST.get('start_year')
            candidate.end_year = request.POST.get('end_year')
            candidate.college_city = request.POST.get('college_city')

        elif org_type == 'professional' or org_type == 'fresher':
            candidate.current_company = request.POST.get('current_company')
            candidate.experience_years = request.POST.get('experience_years')
            candidate.current_job_role = request.POST.get('current_job_role')
            candidate.job_start_year = request.POST.get('job_start_year')
            candidate.job_end_year = request.POST.get('job_end_year')
            candidate.job_city = request.POST.get('job_city')

        candidate.save()
        return redirect('candidates_summary')

    return render(request, 'admin_panel/edit_candidate.html', {
        'candidate': candidate,
        'org_type': org_type
    })


@csrf_exempt
def delete_candidate(request, candidate_id):
    candidate = get_object_or_404(CandidateProfile, id=candidate_id)
    org_type = candidate.user_type
    org_id = getattr(candidate, f"{org_type}_id")
    candidate.delete()
    messages.success(request, "Candidate deleted successfully.")
    return redirect('view_candidates_by_org', org_type=org_type, org_id=org_id)


from django.shortcuts import render, get_object_or_404, redirect
from .models import CandidateProfile

def view_freshers(request):
    freshers = CandidateProfile.objects.filter(user_type='fresher')
    return render(request, 'admin_panel/freshers_list.html', {'freshers': freshers})

def view_fresher(request, pk):
    fresher = get_object_or_404(CandidateProfile, pk=pk)
    return render(request, 'admin_panel/fresher_detail.html', {'fresher': fresher})

def edit_fresher(request, pk):
    fresher = get_object_or_404(CandidateProfile, pk=pk)
    if request.method == 'POST':
        # Update logic (simple example)
        fresher.first_name = request.POST.get('first_name')
        fresher.last_name = request.POST.get('last_name')
        fresher.email = request.POST.get('email')
        fresher.save()
        return redirect('freshers_list')
    return render(request, 'admin_panel/edit_fresher.html', {'fresher': fresher})

def delete_fresher(request, pk):
    fresher = get_object_or_404(CandidateProfile, pk=pk)
    fresher.delete()
    return redirect('freshers_list')



from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from mainapp.models import CandidateProfile

def login_view(request):
    if request.method == "POST":
        identifier = request.POST.get('username_or_email')
        password = request.POST.get('password')

        try:
            candidate = CandidateProfile.objects.get(email=identifier)
        except CandidateProfile.DoesNotExist:
            try:
                candidate = CandidateProfile.objects.get(phone=identifier)
            except CandidateProfile.DoesNotExist:
                candidate = None

        if candidate and check_password(password, candidate.password):
            # ✅ Login successful: Set required session values
            request.session['candidate_id'] = candidate.id
            request.session['candidate_name'] = candidate.first_name
            request.session['candidate_email'] = candidate.email
            request.session['candidate_phone'] = candidate.phone

            # ✅ Handle profile photo if it exists
            if candidate.profile_photo:
                request.session['candidate_photo'] = candidate.profile_photo.url
            else:
                request.session['candidate_photo'] = '/static/images/default-user.png'  # fallback default

            return redirect('home')
        else:
            messages.error(request, "Invalid credentials. Please try again.")

    return render(request, "login_form.html")

def logout_view(request):
    request.session.flush()
    return redirect('home')

def logout_view(request):
    request.session.flush()
    return redirect('home')  # or any page you want



from django.shortcuts import render
from .models import Internship

def internships_page(request):
    internships = Internship.objects.all()  # ya filter conditions bhi ho sakti hain
    return render(request, 'internships.html', {'internships': internships})

from django.shortcuts import render

from django.shortcuts import render
from django.template.loader import get_template
from .models import Job


# views.py
from django.shortcuts import render
from .models import Competition

def competitions_page(request):
    competitions = Competition.objects.all()
    COMPETITION_TYPE_CHOICES = [
        ('Hackathons', 'Hackathons'),
        ('Quizzes', 'Quizzes'),
        ('Scholarships', 'Scholarships'),
        ('Workshops', 'Workshops'),
        ('Conferences', 'Conferences'),
        ('Cultural Events', 'Cultural Events'),
    ]
    return render(request, 'competitions.html', {
        'competitions': competitions,
        'competition_type_choices': COMPETITION_TYPE_CHOICES,
    })

def mentorship_page(request):
    return render(request, 'mentorship.html')



# mainapp/views.py
from django.shortcuts import render, redirect
from .forms import InternshipForm

def add_internship(request):
    if request.method == 'POST':
        form = InternshipForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('internship_list')  # update this to your internship list view
    else:
        form = InternshipForm()
    return render(request, 'admin_panel/add_internship.html', {'form': form})

from django.shortcuts import render, get_object_or_404
from .models import Internship
from .forms import InternshipForm
from django.urls import reverse
from django.http import HttpResponseRedirect


def internship_list(request):
    internships = Internship.objects.all()
    return render(request, 'admin_panel/internship_list.html', {'internships': internships})


def view_internship(request, internship_id):
    internship = get_object_or_404(Internship, id=internship_id)
    return render(request, 'admin_panel/view_internship.html', {'internship': internship})


def edit_internship(request, internship_id):
    internship = get_object_or_404(Internship, id=internship_id)
    if request.method == 'POST':
        form = InternshipForm(request.POST, instance=internship)
        if form.is_valid():
            form.save()
            return redirect('internship_list')
    else:
        form = InternshipForm(instance=internship)
    return render(request, 'admin_panel/edit_internship.html', {'form': form})


def delete_internship(request, internship_id):
    internship = get_object_or_404(Internship, id=internship_id)
    internship.delete()
    return redirect('internship_list')



from django.shortcuts import render, get_object_or_404, redirect
from .models import Job
from .forms import JobForm

def job_list(request):
    jobs = Job.objects.all().order_by('-created_at')
    return render(request, 'admin_panel/job_list.html', {'jobs': jobs})
from datetime import date
from django.shortcuts import render, redirect
from .models import Job

def add_job(request):
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        company_name = request.POST.get('company_name', '').strip()
        domain = request.POST.get('domain', '').strip()
        employment_type = request.POST.get('employment_type', '')
        experience_level = request.POST.get('experience_level', '')
        location = request.POST.get('location', '').strip()
        apply_by = request.POST.get('apply_by') or None
        job_description = request.POST.get('job_description', '').strip()
        category = request.POST.get('category', '')

        # Handle optional fields
        salary_min = request.POST.get('salary_min_lpa')
        salary_max = request.POST.get('salary_max_lpa')

        salary_min = float(salary_min) if salary_min else None
        salary_max = float(salary_max) if salary_max else None

        remote_allowed = 'remote_allowed' in request.POST  # checkbox handling

        Job.objects.create(
            title=title,
            company_name=company_name,
            domain=domain,
            employment_type=employment_type,
            salary_min_lpa=salary_min,
            salary_max_lpa=salary_max,
            experience_level=experience_level,
            location=location,
            remote_allowed=remote_allowed,
            apply_by=apply_by,
            job_description=job_description,
            category=category
        )
        return redirect('job_list')

    # For GET request, pass today's date to template
    return render(request, 'admin_panel/add_job.html', {
        'today_date': date.today().isoformat()
    })

from django.shortcuts import render, get_object_or_404, redirect
from .models import Job

def edit_job(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    if request.method == 'POST':
        job.title = request.POST.get('title')
        job.company_name = request.POST.get('company_name')
        job.domain = request.POST.get('domain')
        job.employment_type = request.POST.get('employment_type')
        job.salary_min_lpa = request.POST.get('salary_min_lpa') or None
        job.salary_max_lpa = request.POST.get('salary_max_lpa') or None
        job.experience_level = request.POST.get('experience_level')
        job.location = request.POST.get('location')
        job.remote_allowed = bool(request.POST.get('remote_allowed'))
        job.apply_by = request.POST.get('apply_by') or None
        job.job_description = request.POST.get('job_description')
        job.category = request.POST.get('category')
        job.save()
        return redirect('job_list')

    return render(request, 'admin_panel/edit_job.html', {'job': job})

def delete_job(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    job.delete()
    return redirect('job_list')

def view_job(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    return render(request, 'admin_panel/job_detail.html', {'job': job})

from django.shortcuts import render
from .models import Job


def jobs_view(request):
    jobs = Job.objects.all()
    template = get_template('jobs.html')
    print("Template path being used:", template.origin)
    print("Debug:", jobs.count(), "jobs loaded")
    return render(request, 'jobs.html', {'jobs': jobs})


from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Competition
from .forms import CompetitionForm

def competitions_list(request):
    comps = Competition.objects.order_by('-created_at')
    print("COMPETITIONS:", comps)  # ye line rakho debugging ke liye
    return render(request, 'admin_panel/competitions_list.html', {'competitions': comps})

def competition_detail(request, pk):
    comp = get_object_or_404(Competition, pk=pk)
    return render(request, 'admin_panel/view_competition.html', {'comp': comp})

def add_competition(request):
    if request.method == 'POST':
        form = CompetitionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Competition added!')
            return redirect('competitions_list')
    else:
        form = CompetitionForm()
    return render(request, 'admin_panel/add_competition.html', {'form': form})

def edit_competition(request, pk):
    comp = get_object_or_404(Competition, pk=pk)
    if request.method == 'POST':
        form = CompetitionForm(request.POST, instance=comp)
        if form.is_valid():
            form.save()
            messages.success(request, 'Competition updated!')
            return redirect('competitions_list')
    else:
        form = CompetitionForm(instance=comp)
    return render(request, 'admin_panel/edit_competition.html', {'form': form, 'comp': comp})

def delete_competition(request, pk):
    comp = get_object_or_404(Competition, pk=pk)
    if request.method == 'POST':
        comp.delete()
        messages.success(request, 'Competition deleted successfully.')
        return redirect('competitions_list')
    return render(request, 'admin_panel/delete_competition.html', {'comp': comp})




def user_internship_detail(request, id):
    internship = get_object_or_404(Internship, pk=id)
    return render(request, 'internship_detail.html', {'internship': internship})

def user_job_detail(request, id):
    job = get_object_or_404(Job, pk=id)
    return render(request, 'job_detail.html', {'job': job})
# views.py
from django.shortcuts import render, get_object_or_404
from .models import Competition

def competition_detail_user(request, pk):
    comp = get_object_or_404(Competition, pk=pk)
    return render(request, 'competition_detail.html', {'comp': comp})



from mainapp.models import CandidateProfile, Internship
from django.shortcuts import render, redirect

from django.shortcuts import render, redirect, get_object_or_404
from .models import Internship, CandidateProfile

from django.shortcuts import render, redirect, get_object_or_404
from .models import Internship, CandidateProfile, AppliedInternship
# views.py

def internship_payment_view(request, internship_id):
    if 'candidate_id' not in request.session:
        return redirect('login')

    internship = get_object_or_404(Internship, id=internship_id)
    profile = get_object_or_404(CandidateProfile, id=request.session['candidate_id'])

    success_message = None

    if request.method == 'POST':
        full_name = f"{profile.first_name} {profile.last_name}"
        email = profile.email
        phone = profile.phone

        payment_status = 'Not Applicable' if internship.category == 'Unpaid' else 'Success'

        # Save application
        _, created = AppliedInternship.objects.get_or_create(
            candidate=profile,
            internship=internship,
            defaults={
                'payment_status': payment_status,
                'name': full_name,
                'email': email,
                'phone': phone,
                'internship_title': internship.title,
                'internship_company_name': internship.company_name,
                'mode': internship.mode,
                'category': internship.category,
                'stipend_amount': internship.stipend_amount
            }
        )

        if created:
            success_message = "Application Submitted Successfully!"
        else:
            success_message = "You have already applied for this internship."

    return render(request, 'internship_payment.html', {
        'internship': internship,
        'profile': profile,
        'success_message': success_message,
    })



from django.shortcuts import render, get_object_or_404
from .models import Job, CandidateProfile, AppliedForJob

def apply_for_job_view(request, job_id):
    if 'candidate_id' not in request.session:
        return redirect('login')

    job = get_object_or_404(Job, id=job_id)
    profile = get_object_or_404(CandidateProfile, id=request.session['candidate_id'])

    success_message = None
    info_message = None
    already_applied = AppliedForJob.objects.filter(candidate=profile, job=job).exists()

    if already_applied:
        info_message = "You have already applied for this job."
    elif request.method == "POST":
        AppliedForJob.objects.create(
            candidate=profile,
            job=job,
            title=job.title,
            company_name=job.company_name,
            domain=job.domain,
            employment_type=job.employment_type,
            location=job.location,
            name=f"{profile.first_name} {profile.last_name}",
            email=profile.email,
            phone=profile.phone
        )
        success_message = "Application submitted successfully!"
        already_applied = True  # update for frontend to hide button if needed

    return render(request, 'job_apply.html', {
        'job': job,
        'profile': profile,
        'success_message': success_message,
        'info_message': info_message,
        'already_applied': already_applied
    })

from django.shortcuts import render, get_object_or_404, redirect
from mainapp.models import CandidateProfile, Competition, CompetitionsApplied

def competition_checkout(request, competition_id):
    if 'candidate_id' not in request.session:
        return redirect('login')

    competition = get_object_or_404(Competition, id=competition_id)
    profile = get_object_or_404(CandidateProfile, id=request.session['candidate_id'])

    success_message = None
    info_message = None
    already_applied = CompetitionsApplied.objects.filter(candidate=profile, competition=competition).exists()

    if already_applied:
        info_message = "You have already registered for this competition."
    elif request.method == "POST":
        CompetitionsApplied.objects.create(
            candidate=profile,
            competition=competition,
            title=competition.title,
            host_org=competition.host_org,
            category=competition.category,
            fee_amount=competition.fee_amount,
            competition_type=competition.competition_type,
            mode=competition.mode,
            start_date=competition.start_date,
            end_date=competition.end_date,
            team_size=competition.team_size,
            prize_pool=competition.prize_pool,
            name=f"{profile.first_name} {profile.last_name}",
            phone=profile.phone,
            email=profile.email
        )
        success_message = "Successfully registered for the competition!"
        already_applied = True

    return render(request, 'competition_checkout.html', {
        'competition': competition,
        'profile': profile,
        'success_message': success_message,
        'info_message': info_message,
        'already_applied': already_applied
    })





from django.shortcuts import render
from mainapp.models import Internship
from collections import Counter

def internship_charts_view(request):
    internships = Internship.objects.all()

    # Paid vs Unpaid
    paid_count = internships.filter(is_paid=True).count()
    unpaid_count = internships.filter(is_paid=False).count()

    # Paid/Unpaid split by mode
    mode_payment = {
        'Paid-Online': internships.filter(is_paid=True, mode='Online').count(),
        'Paid-Offline': internships.filter(is_paid=True, mode='Offline').count(),
        'Unpaid-Online': internships.filter(is_paid=False, mode='Online').count(),
        'Unpaid-Offline': internships.filter(is_paid=False, mode='Offline').count(),
    }

    # Domain Distribution
    domain_counts = dict(Counter([intern.domain for intern in internships]))

    context = {
        'paid_count': paid_count,
        'unpaid_count': unpaid_count,
        'mode_payment': mode_payment,
        'domain_labels': list(domain_counts.keys()),
        'domain_data': list(domain_counts.values()),
    }
    return render(request, 'admin_panel/charts_internship.html', context)



# views.py
from django.http import JsonResponse
from .models import Internship

def get_internships_json(request):
    internships = Internship.objects.all().order_by('-created_at').values(
        'id', 'title', 'company_name', 'created_at', 'category', 'domain'
    )
    return JsonResponse({'internships': list(internships)})

from django.shortcuts import render

def add_candidate_view(request):
    return render(request, 'admin_panel/add_candidate.html')


from django.shortcuts import render, redirect
from .forms import AdminModuleForm

def add_admin_module_view(request):
    if request.method == 'POST':
        form = AdminModuleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_panel_dashboard')  # Update with your desired redirect
    else:
        form = AdminModuleForm()
    return render(request, 'admin_panel/add_adminmodule.html', {'form': form})





# views.py
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from .models import College, CandidateProfile


def college_admin_view(request):
    college_id = request.session.get('college_id')
    if not college_id:
        return redirect('college_login')

    college = College.objects.get(id=college_id)
    student_count = CandidateProfile.objects.filter(user_type='college', college_id=college_id).count()

    context = {
        'college': college,
        'student_count': student_count,
    }

    return render(request, 'college_admin_panel/college_admin_base.html', context)




# views.py
from django.shortcuts import render, redirect
from mainapp.models import College
from django.contrib.auth.hashers import make_password

def register_college(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        city = request.POST.get('city')
        address = request.POST.get('address')
        contact_number = request.POST.get('contact_number')
        email = request.POST.get('email')
        domains_accepted = request.POST.get('domains_accepted')
        courses_accepted = request.POST.get('courses_accepted')
        is_approved = True if request.POST.get('is_approved') == 'on' else False
        password = make_password(request.POST.get('password'))  # Hashing

        College.objects.create(
            name=name,
            city=city,
            address=address,
            contact_number=contact_number,
            email=email,
            domains_accepted=domains_accepted,
            courses_accepted=courses_accepted,
            is_approved=is_approved,
            password=password,
        )
        return redirect('home')  # ya koi success page

    return render(request, 'register_college.html')

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from .models import College

def college_login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            college = College.objects.get(email=email)
            if check_password(password, college.password):
                if college.is_approved:
                    request.session['college_id'] = college.id
                    request.session['college_name'] = college.name
                    return redirect('college_admin_dashboard')
                else:
                    messages.error(request, "Your college is not approved yet.")
            else:
                messages.error(request, "Invalid email or password.")
        except College.DoesNotExist:
            messages.error(request, "Invalid email or password.")
    
    return render(request, 'college_admin_panel/college_login.html')

def college_admin_dashboard(request):
    college_id = request.session.get('college_id')
    if not college_id:
        return redirect('college_login')

    college = College.objects.get(id=college_id)

    student_count = CandidateProfile.objects.filter(user_type='college', college_id=college_id).count()

    context = {
        'college': college,
        'student_count': student_count,
    }

    return render(request, 'college_admin_panel/college_admin_dashboard.html', context)

from django.shortcuts import render, redirect, get_object_or_404
from .models import College
from django.contrib import messages

def edit_college_profile(request):
    college_id = request.session.get('college_id')
    if not college_id:
        return redirect('college_login')

    college = get_object_or_404(College, id=college_id)

    if request.method == 'POST':
        college.name = request.POST.get('name')
        college.email = request.POST.get('email')
        college.phone = request.POST.get('phone')
        college.city = request.POST.get('city')
        college.state = request.POST.get('state')
        college.courses_accepted = request.POST.get('courses_accepted')
        college.website = request.POST.get('website')
        college.logo = request.FILES.get('logo') or college.logo
        college.save()

        messages.success(request, "College profile updated successfully.")
        return redirect('college_admin_dashboard')

    return render(request, 'college_admin_panel/edit_college_profile.html', {
        'college': college
    })


def college_logout(request):
    request.session.flush()
    return redirect('college_login')


from .models import CandidateProfile, CareerPurpose, College
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.contrib import messages

def add_new_student(request):
    college_id = request.session.get('college_id')
    if not college_id:
        return redirect('college_login')

    college = College.objects.get(id=college_id)
    courses = [course.strip() for course in (college.courses_accepted or "").split(',') if course.strip()]

    if request.method == 'POST':
        # Extracting student fields
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        gender = request.POST.get('gender')
        password = request.POST.get('password')
        domain = request.POST.get('domain')
        course_name = request.POST.get('course_name')
        start_year = request.POST.get('start_year')
        end_year = request.POST.get('end_year')
        career_purpose = request.POST.get('career_purpose')
        agreed_info = bool(request.POST.get('agreed_info'))
        stay_in_loop = bool(request.POST.get('stay_in_loop'))
        profile_photo = request.FILES.get('profile_photo')

        # ✅ Hashing password
        hashed_password = make_password(password)

        # Saving student
        student = CandidateProfile(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            gender=gender,
            password=hashed_password,  # ✅ Save hashed password
            domain=domain,
            course_name=course_name,
            start_year=start_year,
            end_year=end_year,
            agreed_info=agreed_info,
            stay_in_loop=stay_in_loop,
            user_type='college',
            college=college,
            college_name=college.name,
            college_city=college.city,
            profile_photo=profile_photo if profile_photo else None,
        )
        student.save()

        # ✅ Saving Career Purpose
        if career_purpose:
            CareerPurpose.objects.create(candidate=student, purpose=career_purpose)

        messages.success(request, "Student added successfully.")
        return redirect('college_admin_dashboard')

    return render(request, 'college_admin_panel/add_new_student.html', {
        'college': college,
        'courses': courses,
    })


from .models import CandidateProfile

def view_college_registered_students(request):
    college_id = request.session.get('college_id')
    if not college_id:
        return redirect('college_login')

    students = CandidateProfile.objects.filter(college_id=college_id)
    return render(request, 'college_admin_panel/registered_students.html', {'students': students})


from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .models import CandidateProfile

def delete_college_candidate(request, pk):
    student = get_object_or_404(CandidateProfile, pk=pk)
    student.delete()
    messages.success(request, "Student deleted successfully.")
    return redirect('registered_students')

def view_college_candidate_detail(request, candidate_id):
    candidate = get_object_or_404(CandidateProfile, id=candidate_id)
    return render(request, 'college_admin_panel/view_candidate_detail_college.html', {'candidate': candidate})

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import CandidateProfile, CareerPurpose, College

def edit_college_candidate(request, candidate_id):
    college_id = request.session.get('college_id')
    if not college_id:
        return redirect('college_login')

    candidate = get_object_or_404(CandidateProfile, id=candidate_id, college_id=college_id)
    try:
        career_obj = CareerPurpose.objects.get(candidate=candidate)
        career_purpose = career_obj.purpose
    except CareerPurpose.DoesNotExist:
        career_purpose = ""

    if request.method == 'POST':
        # Update fields
        candidate.first_name = request.POST.get('first_name')
        candidate.last_name = request.POST.get('last_name')
        candidate.email = request.POST.get('email')
        candidate.phone = request.POST.get('phone')
        candidate.gender = request.POST.get('gender')
        candidate.domain = request.POST.get('domain')
        candidate.course_name = request.POST.get('course_name')
        candidate.start_year = request.POST.get('start_year')
        candidate.end_year = request.POST.get('end_year')

        if request.FILES.get('profile_photo'):
            candidate.profile_photo = request.FILES.get('profile_photo')

        candidate.save()

        # Update CareerPurpose
        new_purpose = request.POST.get('career_purpose')
        if new_purpose:
            if career_obj:
                career_obj.purpose = new_purpose
                career_obj.save()
            else:
                CareerPurpose.objects.create(candidate=candidate, purpose=new_purpose)

        messages.success(request, "Candidate updated successfully.")
        return redirect('registered_students')
    return render(request, 'college_admin_panel/edit_college_candidate.html', {
        'candidate': candidate,
        'career_purpose': career_purpose,
    })




def add_competition_college(request):
    if request.method == 'POST':
        form = CompetitionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Competition added!')
            return redirect('competitions_list_college')
    else:
        form = CompetitionForm()
    return render(request, 'college_admin_panel/add_competition_college.html', {'form': form})


    
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Competition
from .forms import CompetitionForm

def competitions_list_college(request):
    comps = Competition.objects.order_by('-created_at')
    print("COMPETITIONS:", comps)  # ye line rakho debugging ke liye
    return render(request, 'college_admin_panel/competitions_list_college.html', {'competitions': comps})




def competition_detail_college(request, pk):
    comp = get_object_or_404(Competition, pk=pk)
    return render(request, 'college_admin_panel/view_competition_college.html', {'comp': comp})


def edit_competition_college(request, pk):
    comp = get_object_or_404(Competition, pk=pk)
    if request.method == 'POST':
        form = CompetitionForm(request.POST, instance=comp)
        if form.is_valid():
            form.save()
            messages.success(request, 'Competition updated!')
            return redirect('competitions_list_college')
    else:
        form = CompetitionForm(instance=comp)
    return render(request, 'college_admin_panel/edit_competition_college.html', {'form': form, 'comp': comp})



def delete_competition_college(request, pk):
    comp = get_object_or_404(Competition, pk=pk)
    if request.method == 'POST':
        comp.delete()
        messages.success(request, 'Competition deleted successfully.')
        return redirect('competitions_list')
    return render(request, 'college_admin_panel/delete_competition_college.html', {'comp': comp})




# mainapp/views.py
from django.shortcuts import render, redirect
from .forms import InternshipForm

def add_internship_college(request):
    if request.method == 'POST':
        form = InternshipForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('internship_list')  # update this to your internship list view
    else:
        form = InternshipForm()
    return render(request, 'college_admin_panel/add_internship_college.html', {'form': form})



from django.shortcuts import render, get_object_or_404
from .models import Internship
from .forms import InternshipForm
from django.urls import reverse
from django.http import HttpResponseRedirect


def internship_list_college(request):
    internships = Internship.objects.all()
    return render(request, 'college_admin_panel/internship_list_college.html', {'internships': internships})


def view_internship_college(request, internship_id):
    internship = get_object_or_404(Internship, id=internship_id)
    return render(request, 'college_admin_panel/view_internship_college.html', {'internship': internship})


def edit_internship_college(request, internship_id):
    internship = get_object_or_404(Internship, id=internship_id)
    if request.method == 'POST':
        form = InternshipForm(request.POST, instance=internship)
        if form.is_valid():
            form.save()
            return redirect('internship_list_college')
    else:
        form = InternshipForm(instance=internship)
    return render(request, 'college_admin_panel/edit_internship_college.html', {'form': form})


def delete_internship_college(request, internship_id):
    internship = get_object_or_404(Internship, id=internship_id)
    internship.delete()
    return redirect('internship_list_college')




from django.shortcuts import render, get_object_or_404
from .models import CandidateProfile, AppliedInternship, CompetitionsApplied

def view_applied_internships_by_student(request, student_id):
    student = get_object_or_404(CandidateProfile, id=student_id)
    internships = AppliedInternship.objects.filter(candidate=student)
    return render(request, 'college_admin_panel/student_internships_applied.html', {
        'student': student,
        'internships': internships
    })

def view_applied_competitions_by_student(request, student_id):
    student = get_object_or_404(CandidateProfile, id=student_id)
    competitions = CompetitionsApplied.objects.filter(candidate=student)
    return render(request, 'college_admin_panel/student_competitions_applied.html', {
        'student': student,
        'competitions': competitions
    })




from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from .models import Company  # import your model


def add_company_home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        city = request.POST.get('city')
        contact_number = request.POST.get('contact_number')
        email = request.POST.get('email')
        password = request.POST.get('password')
        is_approved = request.POST.get('is_approved') == 'on'

        # hash password before saving
        hashed_password = make_password(password)

        Company.objects.create(
            name=name,
            address=address,
            city=city,
            contact_number=contact_number,
            email=email,
            password=hashed_password,
            is_approved=is_approved
        )
        messages.success(request, "Company added successfully.")
        return redirect('home')

    return render(request, 'add_company_home.html')



from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Company
from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Company
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Company

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Company

def company_login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            company = Company.objects.get(email=email)

            if company.check_password(password):
                if company.is_approved:
                    request.session['company_id'] = company.id
                    request.session['company_name'] = company.name
                    request.session['company_city'] = company.city

                    return redirect('company_admin_dashboard')
                else:
                    messages.error(request, "Company not approved.")
            else:
                messages.error(request, "Incorrect password.")
        except Company.DoesNotExist:
            messages.error(request, "Company not found.")

    return render(request, 'company_admin_panel/company_login.html')

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Company, CandidateProfile  # ✅ Import candidate model

def company_admin_dashboard(request):
    company_id = request.session.get('company_id')

    if not company_id:
        messages.error(request, "Please login first.")
        return redirect('company_login')

    company = Company.objects.get(id=company_id)

    # Count candidates registered under this company
    total_registered = CandidateProfile.objects.filter(company=company).count()

    context = {
        'company': company,
        'total_applied': total_registered  # this will be shown on the card
    }

    return render(request, 'company_admin_panel/company_admin_dashboard.html', context)

def company_logout(request):
    request.session.flush()
    return redirect('company_login')
    
# views.py (for company admin panel)
from django.shortcuts import render, redirect
from mainapp.models import CandidateProfile

# views.py
from django.shortcuts import render, redirect
from mainapp.models import CandidateProfile

def view_company_registered_students(request):
    company_id = request.session.get('company_id')
    if not company_id:
        return redirect('company_login')

    # Filter candidates for this company
    students = CandidateProfile.objects.filter(company_id=company_id)
    return render(request, 'company_admin_panel/registered_students_2.html', {'students': students})


from django.shortcuts import render, get_object_or_404, redirect
from .models import CandidateProfile
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

def view_candidate_company(request, candidate_id):
    candidate = get_object_or_404(CandidateProfile, id=candidate_id)
    return render(request, 'company_admin_panel/view_candidate_company.html', {'candidate': candidate})



from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import CandidateProfile


def edit_candidate_company(request, candidate_id):
    candidate = get_object_or_404(CandidateProfile, pk=candidate_id)
    org_type = candidate.user_type  # 'school' | 'college' | 'professional' | 'fresher'

    if request.method == 'POST':
        candidate.first_name = request.POST.get('first_name')
        candidate.last_name = request.POST.get('last_name')
        candidate.email = request.POST.get('email')
        candidate.phone = request.POST.get('phone')
        candidate.gender = request.POST.get('gender')

        if request.FILES.get('profile_photo'):
            candidate.profile_photo = request.FILES['profile_photo']

        if org_type == 'school':
            candidate.school_name = request.POST.get('school_name')
            candidate.current_class = request.POST.get('current_class')
            candidate.school_city = request.POST.get('school_city')

        elif org_type == 'college':
            candidate.college_name = request.POST.get('college_name')
            candidate.domain = request.POST.get('domain')
            candidate.course_name = request.POST.get('course_name')
            candidate.start_year = request.POST.get('start_year')
            candidate.end_year = request.POST.get('end_year')
            candidate.college_city = request.POST.get('college_city')

        elif org_type == 'professional' or org_type == 'fresher':
            candidate.current_company = request.POST.get('current_company')
            candidate.experience_years = request.POST.get('experience_years')
            candidate.current_job_role = request.POST.get('current_job_role')
            candidate.job_start_year = request.POST.get('job_start_year')
            candidate.job_end_year = request.POST.get('job_end_year')
            candidate.job_city = request.POST.get('job_city')

        candidate.save()
        return redirect('candidates_summary')

    return render(request, 'company_admin_panel/edit_candidate_company.html', {
        'candidate': candidate,
        'org_type': org_type
    })


def add_new_company_candidate(request):
    company_id = request.session.get('company_id')
    if not company_id:
        return redirect('company_login')

    company = Company.objects.get(id=company_id)

    if request.method == 'POST':
        # Basic
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        gender = request.POST.get('gender')
        password = make_password(request.POST.get('password'))
        user_type = 'professional'

        # Professional fields
        current_job_role = request.POST.get('current_job_role')
        experience_years = request.POST.get('experience_years')
        job_start_year = request.POST.get('job_start_year')
        job_end_year = request.POST.get('job_end_year')

        agreed_info = bool(request.POST.get('agreed_info'))
        stay_in_loop = bool(request.POST.get('stay_in_loop'))
        profile_photo = request.FILES.get('profile_photo')

        candidate = CandidateProfile.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            gender=gender,
            password=password,
            agreed_info=agreed_info,
            stay_in_loop=stay_in_loop,
            user_type=user_type,
            company=company,
            current_company=company.name,
            job_city=company.city,
            current_job_role=current_job_role,
            experience_years=experience_years,
            job_start_year=job_start_year,
            job_end_year=job_end_year,
            profile_photo=profile_photo
        )

        messages.success(request, "Candidate added successfully.")
        return redirect('company_admin_dashboard')

    return render(request, 'company_admin_panel/add_new_candidate.html', {'company': company})
from django.shortcuts import render, redirect
from .models import Job

from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Job, Company  # Import your Company model


def add_job_company(request):
    if request.method == 'POST':
        company_id = request.session.get('company_id')
        if not company_id:
            return redirect('company_admin_dashboard')

        company = get_object_or_404(Company, id=company_id)

        Job.objects.create(
            title=request.POST.get('title'),
            company_name=company.name,
            domain=request.POST.get('domain'),
            employment_type=request.POST.get('employment_type'),
            salary_min_lpa=request.POST.get('salary_min_lpa') or None,
            salary_max_lpa=request.POST.get('salary_max_lpa') or None,
            experience_level=request.POST.get('experience_level'),
            location=company.city,  # ✅ FIXED LINE
            remote_allowed=bool(request.POST.get('remote_allowed')),
            apply_by=request.POST.get('apply_by') or None,
            job_description=request.POST.get('job_description'),
            category=request.POST.get('category')
        )
        return redirect('company_admin_dashboard')

    return render(request, 'company_admin_panel/company_add_job.html')



from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, get_object_or_404
from .models import Job, Company


def company_job_list(request):
    company_id = request.session.get('company_id')
    if not company_id:
        return redirect('company_admin_dashboard')

    company = get_object_or_404(Company, id=company_id)
    jobs = Job.objects.filter(company_name=company.name).order_by('-id')  # latest first

    return render(request, 'company_admin_panel/company_job_list.html', {'jobs': jobs})

from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Internship, Company


def add_internship_company(request):
    if request.method == 'POST':
        company_id = request.session.get('company_id')
        if not company_id:
            return redirect('company_admin_dashboard')

        company = get_object_or_404(Company, id=company_id)

        Internship.objects.create(
            title=request.POST.get('title'),
            company_name=company.name,  # ✅ auto set
            domain=request.POST.get('domain'),
            mode=request.POST.get('mode'),
            category=request.POST.get('category'),
            stipend_amount=request.POST.get('stipend_amount') or None,
            start_date=request.POST.get('start_date') or None,
            end_date=request.POST.get('end_date') or None,
            duration_weeks=request.POST.get('duration_weeks') or None,
            location=company.city,  # ✅ auto set
            application_link=request.POST.get('application_link')
        )

        return redirect('company_admin_dashboard')  # ✅ update this URL if needed

    return render(request, 'company_admin_panel/add_company_internships.html')

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from mainapp.models import Internship, Company

def company_internship_list(request):
    company_id = request.session.get('company_id')
    if not company_id:
        return redirect('company_login')  # change if your login url is different

    company = get_object_or_404(Company, id=company_id)

    # ✅ Match using company.name instead of company.company_name
    internships = Internship.objects.filter(company_name=company.name)

    return render(request, 'company_admin_panel/company_internship_list.html', {
        'internships': internships,
        'today': timezone.now().date(),
        'company': company
    })


from django.shortcuts import render, redirect
from django.contrib import messages
from .models import CandidateProfile
from django.contrib.auth.hashers import check_password

def user_panel_login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = CandidateProfile.objects.get(email=email)

            # If passwords are hashed, use this:
            if check_password(password, user.password):
                request.session['user_id'] = user.id
                request.session['user_name'] = user.first_name
                messages.success(request, "Login successful!")
                return redirect('user_dashboard_panel')
            else:
                messages.error(request, "Invalid email or password.")
        except CandidateProfile.DoesNotExist:
            messages.error(request, "Invalid email or password.")

    return render(request, 'user_dashboard_panel/login.html')

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import CandidateProfile, AppliedInternship, AppliedForJob, CompetitionsApplied

def user_panel_dashboard_view(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('user_login_panel')

    try:
        user = CandidateProfile.objects.get(id=user_id)
    except CandidateProfile.DoesNotExist:
        messages.error(request, "User not found.")
        return redirect('user_login_panel')

    internship_count = AppliedInternship.objects.filter(candidate=user).count()
    job_count = AppliedForJob.objects.filter(candidate=user).count()
    competition_count = CompetitionsApplied.objects.filter(candidate=user).count()

    context = {
        'user': user,
        'internship_count': internship_count,
        'job_count': job_count,
        'competition_count': competition_count,
    }

    return render(request, 'user_dashboard_panel/user_admin_dashboard.html', context)

def user_panel_logout_view(request):
    request.session.flush()
    return redirect('user_login_panel')


def user_applied_internships_view(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('user_login_panel')

    try:
        user = CandidateProfile.objects.get(id=user_id)
    except CandidateProfile.DoesNotExist:
        messages.error(request, "User not found.")
        return redirect('user_login_panel')

    internships = AppliedInternship.objects.filter(candidate=user).order_by('-applied_at')

    return render(request, 'user_dashboard_panel/user_applied_internships.html', {
        'internships': internships,
        'user': user,
    })


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import AppliedForJob, CompetitionsApplied, CandidateProfile


def applied_jobs_list_view(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('user_login')

    try:
        candidate = CandidateProfile.objects.get(id=user_id)
        applied_jobs = AppliedForJob.objects.filter(candidate=candidate).order_by('-applied_at')
    except CandidateProfile.DoesNotExist:
        applied_jobs = []

    return render(request, 'user_dashboard_panel/applied_jobs_list.html', {
        'applied_jobs': applied_jobs,
    })


def applied_competitions_list_view(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('user_login')

    try:
        candidate = CandidateProfile.objects.get(id=user_id)
        applied_competitions = CompetitionsApplied.objects.filter(candidate=candidate).order_by('-applied_at')
    except CandidateProfile.DoesNotExist:
        applied_competitions = []

    return render(request, 'user_dashboard_panel/applied_competitions_list.html', {
        'applied_competitions': applied_competitions,
    })


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import CandidateProfile

def edit_candidate_user(request):
    user_id = request.session.get('user_id')
    if not user_id:
        messages.error(request, "Please log in first.")
        return redirect('user_login_panel')

    candidate = get_object_or_404(CandidateProfile, id=user_id)
    org_type = candidate.user_type  # 'school' | 'college' | 'professional' | 'fresher'

    if request.method == 'POST':
        candidate.first_name = request.POST.get('first_name')
        candidate.last_name = request.POST.get('last_name')
        candidate.email = request.POST.get('email')
        candidate.phone = request.POST.get('phone')
        candidate.gender = request.POST.get('gender')

        if request.FILES.get('profile_photo'):
            candidate.profile_photo = request.FILES['profile_photo']

        if org_type == 'school':
            candidate.school_name = request.POST.get('school_name')
            candidate.current_class = request.POST.get('current_class')
            candidate.school_city = request.POST.get('school_city')

        elif org_type == 'college':
            candidate.college_name = request.POST.get('college_name')
            candidate.domain = request.POST.get('domain')
            candidate.course_name = request.POST.get('course_name')
            candidate.start_year = request.POST.get('start_year')
            candidate.end_year = request.POST.get('end_year')
            candidate.college_city = request.POST.get('college_city')

        elif org_type in ['professional', 'fresher']:
            candidate.current_company = request.POST.get('current_company')
            candidate.experience_years = request.POST.get('experience_years')
            candidate.current_job_role = request.POST.get('current_job_role')
            candidate.job_start_year = request.POST.get('job_start_year')
            candidate.job_end_year = request.POST.get('job_end_year')
            candidate.job_city = request.POST.get('job_city')

        candidate.save()
        messages.success(request, "Profile updated successfully!")
        return redirect('user_dashboard_panel')

    return render(request, 'user_dashboard_panel/update_information.html', {
        'candidate': candidate,
        'org_type': org_type
    })


from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .models import AppliedInternship  # Import your model

def delete_applied_internship(request, pk):
    if request.method == 'POST':
        app = get_object_or_404(AppliedInternship, pk=pk)
        app.delete()
        messages.success(request, 'Application deleted successfully.')
    else:
        messages.error(request, 'Invalid request.')
    return redirect('applied_internships_list')  # Update this name to your internships list view


def delete_applied_job(request, pk):
    job = get_object_or_404(AppliedForJob, pk=pk)
    job.delete()
    return redirect('applied_jobs_list')

def delete_applied_competition(request, pk):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('user_login')

    try:
        candidate = CandidateProfile.objects.get(id=user_id)
        comp = get_object_or_404(CompetitionsApplied, application_id=pk, candidate=candidate)
        comp.delete()
        messages.success(request, "Applied competition deleted successfully.")
    except CandidateProfile.DoesNotExist:
        messages.error(request, "Candidate not found.")

    return redirect('applied_competitions_list')



from django.shortcuts import render, get_object_or_404
from .models import CandidateProfile, AppliedForJob

def view_applied_jobs_by_student(request, student_id):
    student = get_object_or_404(CandidateProfile, id=student_id)
    applied_jobs = AppliedForJob.objects.filter(candidate=student).order_by('-applied_at')

    return render(request, 'college_admin_panel/view_applied_jobs_by_student.html', {
        'student': student,
        'applied_jobs': applied_jobs,
    })
# views.py
from django.shortcuts import render
from .models import CandidateProfile, Competition, Job, College, Company

def our_numbers_view(request):
    context = {
        'user_count': CandidateProfile.objects.count(),
        'competition_count': Competition.objects.count(),
        'job_count': Job.objects.count(),
        'college_count': College.objects.count(),
        'company_count': Company.objects.count(),
    }
    return render(request, 'our_numbers.html', context)
from django.shortcuts import render

def about_us(request):
    return render(request, 'about_us.html')

from django.shortcuts import render, redirect
from django.contrib import messages
from mainapp.models import CandidateProfile

def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email', '').strip().lower()

        try:
            candidate = CandidateProfile.objects.get(email=email)
            request.session['reset_email'] = email  # Temporarily store email
            return redirect('reset_password')
        except CandidateProfile.DoesNotExist:
            messages.error(request, "Email not found. Please enter a registered email.")

    return render(request, 'forgot_password.html')
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from mainapp.models import CandidateProfile

def reset_password(request):
    email = request.session.get('reset_email')
    if not email:
        messages.error(request, "Session expired or invalid access.")
        return redirect('forgot_password')

    try:
        candidate = CandidateProfile.objects.get(email=email)
    except CandidateProfile.DoesNotExist:
        messages.error(request, "User not found.")
        return redirect('forgot_password')

    if request.method == 'POST':
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        if new_password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('reset_password')

        candidate.password = make_password(new_password)
        candidate.save()

        messages.success(request, "Password reset successful. You can now log in.")
        return redirect('login')

    return render(request, 'reset_password.html')


from django.shortcuts import render, get_object_or_404
from .models import CompetitionsApplied, CandidateProfile

def view_applied_competition_user(request, pk):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('user_login')

    candidate = get_object_or_404(CandidateProfile, id=user_id)
    comp = get_object_or_404(CompetitionsApplied, application_id=pk, candidate=candidate)

    return render(request, 'user_dashboard_panel/view_applied_competition.html', {
        'comp': comp
    })
