from django.views.generic import TemplateView, ListView, DetailView
from apps.universities.models import University
from apps.programs.models import Program
from apps.scholarships.models import Scholarship
from apps.professors.models import Professor

class HomeView(TemplateView):
    template_name = 'core/home.html'

class PricingView(TemplateView):
    template_name = 'core/pricing.html'

class ChatView(TemplateView):
    template_name = 'core/chat.html'

class ProfileView(TemplateView):
    template_name = 'core/profile.html'

class UniversityListView(ListView):
    model = University
    template_name = 'core/universities.html'
    context_object_name = 'universities'

class UniversityDetailView(DetailView):
    model = University
    template_name = 'core/university_detail.html'
    context_object_name = 'university'

class ProgramListView(ListView):
    model = Program
    template_name = 'core/programs.html'
    context_object_name = 'programs'

class ProgramDetailView(DetailView):
    model = Program
    template_name = 'core/program_detail.html'
    context_object_name = 'program'

class ScholarshipListView(ListView):
    model = Scholarship
    template_name = 'core/scholarships.html'
    context_object_name = 'scholarships'

class ScholarshipDetailView(DetailView):
    model = Scholarship
    template_name = 'core/scholarship_detail.html'
    context_object_name = 'scholarship'

class ProfessorListView(ListView):
    model = Professor
    template_name = 'core/professors.html'
    context_object_name = 'professors'

class ProfessorDetailView(DetailView):
    model = Professor
    template_name = 'core/professor_detail.html'
    context_object_name = 'professor'

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'core/register.html', {'form': form})
