from django import forms
from django.contrib.auth.models import User
from .models import UserPortfolio, Skill, AcademicBackground, WorkExperience, Project
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class UserPortfolioForm(forms.ModelForm):
    class Meta:
        model = UserPortfolio
        fields = ["name", "designation", "email", "phone", "profile_photo", "short_bio"]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'designation': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'short_bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ["skill_name"]
        widgets = {'skill_name': forms.TextInput(attrs={'class': 'form-control'})}

class AcademicBackgroundForm(forms.ModelForm):
    class Meta:
        model = AcademicBackground
        fields = ["institute", "degree", "year_of_graduation", "grade"]
        widgets = {
            'institute': forms.TextInput(attrs={'class': 'form-control'}),
            'degree': forms.TextInput(attrs={'class': 'form-control'}),
            'year_of_graduation': forms.TextInput(attrs={'class': 'form-control'}),
            'grade': forms.TextInput(attrs={'class': 'form-control'}),
        }

class WorkExperienceForm(forms.ModelForm):
    class Meta:
        model = WorkExperience
        fields = ["company_name", "job_duration", "job_responsibilities"]
        widgets = {
            'company_name': forms.TextInput(attrs={'class': 'form-control'}),
            'job_duration': forms.TextInput(attrs={'class': 'form-control'}),
            'job_responsibilities': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["project_name", "project_description"]
        widgets = {
            'project_name': forms.TextInput(attrs={'class': 'form-control'}),
            'project_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class PortfolioForm(forms.ModelForm):
    class Meta:
        model = UserPortfolio
        fields = ['name', 'designation', 'email', 'phone', 'profile_photo', 'short_bio']