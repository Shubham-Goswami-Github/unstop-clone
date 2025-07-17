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


urlpatterns = [
    path('', views.home_view, name='home'),  # 👈 root URL
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('explore/', views.explore_sections_view, name='explore-sections'),
    path('slogan/', views.slogan_view, name='slogan'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
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

        # ... other paths ...
    path('login/', login_view, name='login'),
    path('', views.home_view, name='home'),
    path('logout/', views.logout_view, name='logout'),


    path('internships/', views.internships_page, name='internships'),

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



    
]
