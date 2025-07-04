from django.urls import path
from . import views

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
]
