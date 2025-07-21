
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


from mainapp.models import School, College, Company, CandidateProfile, Internship, Job, Competition
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def admin_panel_dashboard_view(request):
    # Total organizations count
    total_schools = School.objects.count()
    total_colleges = College.objects.count()
    total_companies = Company.objects.count()

    # Total candidate count
    total_candidates = CandidateProfile.objects.count()

    # Candidate type-wise count
    school_candidates_count = CandidateProfile.objects.filter(user_type='school').count()
    college_candidates_count = CandidateProfile.objects.filter(user_type='college').count()
    experienced_candidates_count = CandidateProfile.objects.filter(user_type='professional').count()
    fresher_candidates_count = CandidateProfile.objects.filter(user_type='fresher').count()

    # Internships, Jobs, Competitions
    total_internships = Internship.objects.count()
    total_jobs = Job.objects.count()
    total_competitions = Competition.objects.count()

    # ✅ Add actual internship queryset
    internships = list(
    Internship.objects.all().order_by('-created_at')[:50].values(
        'id', 'title', 'company_name', 'created_at', 'category', 'mode', 'domain'
    )
)

  # Or any number

    # Organizations with candidate count
    schools = School.objects.all()
    for school in schools:
        school.candidate_count = CandidateProfile.objects.filter(school_id=school.id).count()

    colleges = College.objects.all()
    for college in colleges:
        college.candidate_count = CandidateProfile.objects.filter(college_id=college.id).count()

    companies = Company.objects.all()
    for company in companies:
        company.candidate_count = CandidateProfile.objects.filter(company_id=company.id).count()

    context = {
        # Total registered orgs
        'school_count': total_schools,
        'college_count': total_colleges,
        'company_count': total_companies,

        # Total candidates overall
        'candidate_count': total_candidates,

        # Candidates by user type
        'school_candidates_count': school_candidates_count,
        'college_candidates_count': college_candidates_count,
        'experienced_count': experienced_candidates_count,
        'fresher_count': fresher_candidates_count,

        # Lists for detail view
        'schools': schools,
        'colleges': colleges,
        'companies': companies,

        # New counts
        'internship_count': total_internships,
        'job_count': total_jobs,
        'competition_count': total_competitions,

        # ✅ Internship data for template
        'internships': internships,
    }

    return render(request, 'admin_panel/admin_dashboard.html', context)




from .models import School  # 👈 model tu bana chuka hai
@staff_member_required
def schools_list_view(request):
    schools = School.objects.all()
    return render(request, 'admin_panel/schools_list.html', {'schools': schools})



from django.shortcuts import render, redirect
from .models import School
@staff_member_required
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
@staff_member_required
def school_detail_view(request, school_id):
    school = get_object_or_404(School, id=school_id)
    return render(request, 'admin_panel/school_detail.html', {'school': school})


from django.shortcuts import render, get_object_or_404, redirect
from .models import School  # ya jo bhi tera model ka naam ho
from django.contrib import messages
@staff_member_required
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

@staff_member_required
def delete_school_view(request, school_id):
    school = get_object_or_404(School, id=school_id)
    school.delete()
    messages.success(request, 'School deleted successfully.')
    return redirect('schools_list')


from django.shortcuts import render, get_object_or_404, redirect
from .models import College
from django.contrib import messages
@staff_member_required
def view_colleges(request):
    colleges = College.objects.all().order_by('-created_at')
    return render(request, 'admin_panel/view_colleges.html', {'colleges': colleges})
@staff_member_required
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

@staff_member_required
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
@staff_member_required
def delete_college_view(request, college_id):
    college = get_object_or_404(College, id=college_id)
    college.delete()
    messages.success(request, 'College deleted successfully.')
    return redirect('colleges_list')

from django.shortcuts import render, get_object_or_404
from .models import College
@staff_member_required
def college_detail_view(request, college_id):
    college = get_object_or_404(College, id=college_id)
    return render(request, 'admin_panel/college_detail.html', {'college': college})


# mainapp/views.py

from .models import Company
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
@staff_member_required
def view_companies(request):
    companies = Company.objects.all().order_by('-created_at')
    return render(request, 'admin_panel/view_companies.html', {'companies': companies})
@staff_member_required
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
@staff_member_required
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
@staff_member_required
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
@staff_member_required
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
@staff_member_required
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
@staff_member_required
def view_candidate(request, candidate_id):
    candidate = get_object_or_404(CandidateProfile, id=candidate_id)
    return render(request, 'admin_panel/view_candidate_detail.html', {'candidate': candidate})
@staff_member_required
def edit_candidate(request, candidate_id):
    candidate = get_object_or_404(CandidateProfile, id=candidate_id)
    if request.method == 'POST':
        candidate.first_name = request.POST.get('first_name')
        candidate.last_name = request.POST.get('last_name')
        candidate.email = request.POST.get('email')
        candidate.phone_number = request.POST.get('phone_number')
        candidate.gender = request.POST.get('gender')
        candidate.save()
        messages.success(request, "Candidate updated successfully!")
        return redirect('view_candidates_by_org', org_type=candidate.user_type, org_id=getattr(candidate, f"{candidate.user_type}_id"))
    return render(request, 'admin_panel/edit_candidate.html', {'candidate': candidate})
@staff_member_required
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
@staff_member_required
def view_freshers(request):
    freshers = CandidateProfile.objects.filter(user_type='fresher')
    return render(request, 'admin_panel/freshers_list.html', {'freshers': freshers})
@staff_member_required
def view_fresher(request, pk):
    fresher = get_object_or_404(CandidateProfile, pk=pk)
    return render(request, 'admin_panel/fresher_detail.html', {'fresher': fresher})
@staff_member_required
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
@staff_member_required
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
            # Try email first, fallback to phone
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

            return redirect('home')  # Redirect to home page
        else:
            messages.error(request, "Invalid credentials. Please try again.")

    return render(request, "login_form.html")


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
@staff_member_required
def job_list(request):
    jobs = Job.objects.all().order_by('-created_at')
    return render(request, 'admin_panel/job_list.html', {'jobs': jobs})
@staff_member_required
def add_job(request):
    if request.method == 'POST':
        Job.objects.create(
            title=request.POST.get('title'),
            company_name=request.POST.get('company_name'),
            domain=request.POST.get('domain'),
            employment_type=request.POST.get('employment_type'),
            salary_min_lpa=request.POST.get('salary_min_lpa') or None,
            salary_max_lpa=request.POST.get('salary_max_lpa') or None,
            experience_level=request.POST.get('experience_level'),
            location=request.POST.get('location'),
            remote_allowed=bool(request.POST.get('remote_allowed')),
            apply_by=request.POST.get('apply_by') or None,
            job_description=request.POST.get('job_description'),
            category=request.POST.get('category')
        )
        return redirect('job_list')
    return render(request, 'admin_panel/add_job.html')
from django.shortcuts import render, get_object_or_404, redirect
from .models import Job
@staff_member_required
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
@staff_member_required
def delete_job(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    job.delete()
    return redirect('job_list')
@staff_member_required
def view_job(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    return render(request, 'admin_panel/job_detail.html', {'job': job})

from django.shortcuts import render
from .models import Job

@staff_member_required
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
@staff_member_required
def competitions_list(request):
    comps = Competition.objects.order_by('-created_at')
    print("COMPETITIONS:", comps)  # ye line rakho debugging ke liye
    return render(request, 'admin_panel/competitions_list.html', {'competitions': comps})
@staff_member_required
def competition_detail(request, pk):
    comp = get_object_or_404(Competition, pk=pk)
    return render(request, 'admin_panel/view_competition.html', {'comp': comp})
@staff_member_required
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
@staff_member_required
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
@staff_member_required
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
