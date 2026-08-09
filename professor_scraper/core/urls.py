from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('pricing/', views.PricingView.as_view(), name='pricing'),
    path('chat/', views.ChatView.as_view(), name='chat'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    
    path('universities/', views.UniversityListView.as_view(), name='university_list'),
    path('universities/<uuid:pk>/', views.UniversityDetailView.as_view(), name='university_detail'),
    
    path('programs/', views.ProgramListView.as_view(), name='program_list'),
    path('programs/<uuid:pk>/', views.ProgramDetailView.as_view(), name='program_detail'),
    
    path('scholarships/', views.ScholarshipListView.as_view(), name='scholarship_list'),
    path('scholarships/<uuid:pk>/', views.ScholarshipDetailView.as_view(), name='scholarship_detail'),
    
    path('professors/', views.ProfessorListView.as_view(), name='professor_list'),
    path('professors/<uuid:pk>/', views.ProfessorDetailView.as_view(), name='professor_detail'),
    
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('register/', views.register, name='register'),
]
