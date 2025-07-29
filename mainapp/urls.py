from django.urls import path
from . import views
from .views import admin_panel_dashboard_view
from .views import schools_list_view
from .views import add_school_view
from .views import school_detail_view 
from .views import edit_school_view
from .views import delete_school_view
from .views import view_colleges, add_college_view, edit_college_view, delete_college_view ,college_detail_view ,view_companies, add_company, edit_company, delete_company , company_detail_view , view_candidates_by_org, view_candidate, edit_candidate, delete_candidate,view_freshers
from .views import view_freshers, view_fresher, edit_fresher, delete_fresher,login_view
from .views import add_internship
from mainapp.views import jobs_view 
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include


urlpatterns = [

    path('admin/', admin.site.urls),  # Django admin
   
    path('', views.home_view, name='home'),  # 👈 root URL
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('explore/', views.explore_sections_view, name='explore-sections'),
    path('slogan/', views.slogan_view, name='slogan'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('api/internships/', views.get_internships_json, name='get_internships_json'),
    path('college/register/', views.register_college, name='register_college'),
    # urls.py
    path('admin/internship-charts/', views.internship_charts_view, name='internship_charts'),
    path('add-admin-module/', views.add_admin_module_view, name='add-admin-module'),
    path('competition/<int:competition_id>/checkout/', views.competition_checkout, name='competition_checkout'),
    path('our-numbers/', views.our_numbers_view, name='our_numbers'),
    path('add-admin-module/', views.add_admin_module_view, name='add_admin_module'),
    path('jobs/<int:id>/', views.user_job_detail, name='user_job_detail'),
    path('competitions/<int:pk>/', views.competition_detail_user, name='competition_detail_user'),
    path('internship/<int:internship_id>/payment/', views.internship_payment_view, name='internship_payment'),
    path('job/apply/<int:job_id>/', views.apply_for_job_view, name='apply_for_job'),
    path('submit-candidate-form/', views.submit_candidate_form, name='submit_candidate_form'),
    path('adminpaneldashboard/', admin_panel_dashboard_view, name='admin_panel_dashboard'),
    path('adminpaneldashboard/schools/', schools_list_view, name='schools_list'),
    path('adminpaneldashboard/schools/add/', add_school_view, name='add_school'),
    path('adminpaneldashboard/schools/<int:school_id>/', school_detail_view, name='school_detail'),
    path('adminpaneldashboard/schools/edit/<int:school_id>/', edit_school_view, name='edit_school'),
    path('adminpaneldashboard/schools/delete/<int:school_id>/', delete_school_view, name='delete_school'),
    path('adminpaneldashboard/colleges/', view_colleges, name='colleges_list'),
    path('adminpaneldashboard/colleges/add/', add_college_view, name='add_college'),
    path('adminpaneldashboard/colleges/edit/<int:college_id>/', edit_college_view, name='edit_college'),
    path('adminpaneldashboard/colleges/delete/<int:college_id>/', delete_college_view, name='delete_college'),
    path('adminpaneldashboard/colleges/<int:college_id>/', college_detail_view, name='college_detail'),
    path('adminpaneldashboard/companies/', view_companies, name='companies_list'),
    path('adminpaneldashboard/companies/add/', add_company, name='add_company'),
    path('adminpaneldashboard/companies/edit/<int:company_id>/', edit_company, name='edit_company'),
    path('adminpaneldashboard/companies/delete/<int:company_id>/', delete_company, name='delete_company'),
    path('adminpaneldashboard/companies/<int:company_id>/', company_detail_view, name='company_detail'),

    path('fetch-dropdown-data/', views.fetch_dropdown_data, name='fetch_dropdown_data'),
    path('adminpaneldashboard/candidates/', views.candidates_summary, name='candidates_summary'),
    # urls.py
    path('adminpaneldashboard/candidates/<str:org_type>/<int:org_id>/', view_candidates_by_org, name='view_candidates_by_org'),
    # urls.py
    path('adminpaneldashboard/freshers/', view_freshers, name='freshers_list'),
    path('adminpaneldashboard/freshers/<int:pk>/view/', view_fresher, name='view_fresher'),
    path('adminpaneldashboard/freshers/<int:pk>/edit/', edit_fresher, name='edit_fresher'),
    path('adminpaneldashboard/freshers/<int:pk>/delete/', delete_fresher, name='delete_fresher'),
    # mainapp/urls.py

    # urls.py
    path('adminpaneldashboard/view-candidate/<int:candidate_id>/', view_candidate, name='view_candidate'),
    path('adminpaneldashboard/edit-candidate/<int:candidate_id>/', edit_candidate, name='edit_candidate'),
    path('adminpaneldashboard/delete-candidate/<int:candidate_id>/', delete_candidate, name='delete_candidate'),
    path('adminpaneldashboard/add-candidate/', views.add_candidate_view, name='add_candidate'),
        # ... other paths ...
    path('login/', login_view, name='login'),
    path('', views.home_view, name='home'),
    path('logout/', views.logout_view, name='logout'),


    path('internships/', views.internships_page, name='internships'),
    path('internship/<int:id>/', views.user_internship_detail, name='user_internship_detail'),

    path("competitions/", views.competitions_page, name="competitions"),
    path("mentorship/", views.mentorship_page, name="mentorship"),
    path('adminpaneldashboard/add-internship/', add_internship, name='add_internship'),
    path('adminpaneldashboard/internships/', views.internship_list, name='internship_list'),
    path('adminpaneldashboard/internship/<int:internship_id>/', views.view_internship, name='view_internship'),
    path('adminpaneldashboard/internship/<int:internship_id>/edit/', views.edit_internship, name='edit_internship'),
    path('adminpaneldashboard/internship/<int:internship_id>/delete/', views.delete_internship, name='delete_internship'),

    path('adminpaneldashboard/jobs/', views.job_list, name='job_list'),
    path('adminpaneldashboard/add-job/', views.add_job, name='add_job'),
    path('adminpaneldashboard/edit-job/<int:job_id>/', views.edit_job, name='edit_job'),
    path('adminpaneldashboard/delete-job/<int:job_id>/', views.delete_job, name='delete_job'),
    path('adminpaneldashboard/view-job/<int:job_id>/', views.view_job, name='view_job'),
  
    path('jobs/', jobs_view, name='jobs'),
     # Competition URLs
    path('adminpaneldashboard/competitions/', views.competitions_list, name='competitions_list'),
    path('adminpaneldashboard/add-competition/', views.add_competition, name='add_competition'),
    path('adminpaneldashboard/competition/<int:pk>/', views.competition_detail, name='competition_detail'),
    path('adminpaneldashboard/competition/<int:pk>/edit/', views.edit_competition, name='edit_competition'),
    path('adminpaneldashboard/competition/<int:pk>/delete/', views.delete_competition, name='delete_competition'),




# urls.py

    path('college-admin/', views.college_admin_view, name='college_admin_base'),
    path('college-admin/login/', views.college_login_view, name='college_login'),
    path('college-admin/dashboard/', views.college_admin_dashboard, name='college_admin_dashboard'),
    path('college-admin/logout/', views.college_logout, name='college_logout'),
    path('college-admin/register/', views.register_college, name='register_college'),

# Students
    path('college-admin/add-student/', views.add_new_student, name='add_student'),
    path('college-admin/registered-students/', views.view_college_registered_students, name='registered_students'),
    path('college-admin/registered-students/<int:pk>/delete/', views.delete_college_candidate, name='delete_college_candidate'),
    path('college-admin/registered-students/<int:candidate_id>/view/', views.view_college_candidate_detail, name='view_college_candidate_detail'),
    path('college-admin/edit-candidate/<int:candidate_id>/', views.edit_college_candidate, name='edit_college_candidate'),

# Competitions
    path('college-admin/competitions/', views.competitions_list_college, name='competitions_list_college'),
    path('college-admin/add-competition/', views.add_competition_college, name='add_competition_college'),
    path('college-admin/competition/<int:pk>/', views.competition_detail_college, name='competition_detail_college'),
    path('college-admin/competition/<int:pk>/edit/', views.edit_competition_college, name='edit_competition_college'),
    path('college-admin/competition/<int:pk>/delete/', views.delete_competition_college, name='delete_competition_college'),

# Internships
    path('college-admin/add-internship/', views.add_internship_college, name='add_internship_college'),
    path('college-admin/internships/', views.internship_list_college, name='internship_list_college'),
    path('college-admin/internship/<int:internship_id>/', views.view_internship_college, name='view_internship_college'),
    path('college-admin/internship/<int:internship_id>/edit/', views.edit_internship_college, name='edit_internship_college'),
    path('college-admin/internship/<int:internship_id>/delete/', views.delete_internship_college, name='delete_internship_college'),

# Student Applications
    path('college-admin/student/<int:student_id>/internships/', views.view_applied_internships_by_student, name='view_applied_internships_by_student'),
    path('college-admin/student/<int:student_id>/competitions/', views.view_applied_competitions_by_student, name='view_applied_competitions_by_student'),
    path('college-admin/<int:student_id>/applied-jobs/', views.view_applied_jobs_by_student, name='view_applied_jobs_by_student'),
# College Profile
    path('college-admin/edit-profile/', views.edit_college_profile, name='edit_college_profile'),


    path('company-admin/add-company/', views.add_company_home, name='add_company_home'),
    path('company-admin/company-login/', views.company_login_view, name='company_login'),
    path('company-admin/company-dashboard/', views.company_admin_dashboard, name='company_admin_dashboard'),
    path('company-admin/company-logout/', views.company_logout, name='company_logout'),
    path('company-admin/registered-students-college/', views.view_company_registered_students, name='company_registered_students'),
    path('company-admin/view-candidate/<int:candidate_id>/', views.view_candidate_company, name='view_candidate_company'),
    path('company-admin/edit-candidate/<int:candidate_id>/', edit_candidate, name='edit_candidate'),
    path('company-admin/add-candidate/', views.add_new_company_candidate, name='add_company_candidate'),
    path('company-admin/add-job/', views.add_job_company, name='add_job_company'),
    path('company-admin/company-job-list/', views.company_job_list, name='company_job_list'),
    path('company-admin/company-add-internship/', views.add_internship_company, name='add_internship_company'),
    path('company-admin/internships/', views.company_internship_list, name='company_internship_list'),

    path('user-panel/user-login/', views.user_panel_login_view, name='user_login_panel'),
    path('user-panel/user-dashboard/', views.user_panel_dashboard_view, name='user_dashboard_panel'),
    path('user-panel/user-logout/', views.user_panel_logout_view, name='user_logout'),
    path('user-panel/applied-internships/', views.user_applied_internships_view, name='user_applied_internships'),
    path('user-panel/applied-jobs/', views.applied_jobs_list_view, name='applied_jobs_list'),
    path('user-panel/applied-competitions/', views.applied_competitions_list_view, name='applied_competitions_list'),
    path('user-panel/update-information/', views.edit_candidate_user, name='update_information'),
    path('user-panel/delete-applied-internship/<int:pk>/', views.delete_applied_internship, name='delete_applied_internship'),
    path('user-panel/delete-applied-job/<int:pk>/', views.delete_applied_job, name='delete_applied_job'),
    path('user-panel/delete-applied-competition/<int:comp_id>/', views.delete_applied_competition, name='delete_applied_competition'),
    path('about-us/', views.about_us, name='about_us'),
  
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    