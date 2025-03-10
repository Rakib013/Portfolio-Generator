from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from .models import UserPortfolio, Skill, AcademicBackground, WorkExperience, Project, LaTeXTemplate, Templates
from .forms import UserPortfolioForm, SkillForm, AcademicBackgroundForm, WorkExperienceForm, ProjectForm, RegisterForm, LoginForm


def user_register(request):
    if request.user.is_authenticated:
        return redirect("portfolio:dashboard")
    
    if request.method == "POST":
        form = RegisterForm(request.POST)
        print("Checking..", form.is_valid())
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto-login after signup
            messages.success(request, "Account created successfully!")
            return redirect("portfolio:dashboard")
        else:
            print(form.errors)
    else:
        form = RegisterForm()

    return render(request, "register.html", {"form": form})

def user_login(request):
    if request.user.is_authenticated: 
        redirect("portfolio:dashboard")

    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Logged in successfully!")
            return redirect("portfolio:dashboard")
        else:
            print(form.errors)
    else:
        form = LoginForm()

    return render(request, "login.html", {"form": form})

def user_logout(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("portfolio:user_login")

@login_required
def dashboard(request):
    user_templates = Templates.objects.filter(user=request.user).select_related("template") 
    return render(request, "dashboard.html", {"templates": user_templates})

@login_required
def template_list(request):
    # Display all available LaTeX templates
    templates = LaTeXTemplate.objects.all()
    return render(request, 'template_list.html', {'templates': templates})

@login_required
def profile(request):
    user_portfolio, created = UserPortfolio.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        # Update UserPortfolio details
        portfolio_form = UserPortfolioForm(request.POST, request.FILES, instance=user_portfolio)
        
        # Process Skill Form
        skill_form = SkillForm(request.POST)
        if skill_form.is_valid():
            skill = skill_form.save(commit=False)
            skill.portfolio = user_portfolio
            skill.save()

        # Process Academic Background Form
        academic_form = AcademicBackgroundForm(request.POST)
        if academic_form.is_valid():
            academic = academic_form.save(commit=False)
            academic.portfolio = user_portfolio
            academic.save()

        # Process Work Experience Form
        work_experience_form = WorkExperienceForm(request.POST)
        if work_experience_form.is_valid():
            work_experience = work_experience_form.save(commit=False)
            work_experience.portfolio = user_portfolio
            work_experience.save()

        # Process Project Form
        project_form = ProjectForm(request.POST)
        if project_form.is_valid():
            project = project_form.save(commit=False)
            project.portfolio = user_portfolio
            project.save()

        # Save portfolio form
        if portfolio_form.is_valid():
            portfolio_form.save()
        
        return redirect('portfolio:profile')
    else:
        portfolio_form = UserPortfolioForm(instance=user_portfolio)
        skill_form = SkillForm()
        academic_form = AcademicBackgroundForm()
        work_experience_form = WorkExperienceForm()
        project_form = ProjectForm()

    # Get all related data to display
    skills = Skill.objects.filter(portfolio=user_portfolio)
    academic_background = AcademicBackground.objects.filter(portfolio=user_portfolio)
    work_experience = WorkExperience.objects.filter(portfolio=user_portfolio)
    projects = Project.objects.filter(portfolio=user_portfolio)
    
    return render(request, 'profile.html', {
        'portfolio_form': portfolio_form,
        'skill_form': skill_form,
        'academic_form': academic_form,
        'work_experience_form': work_experience_form,
        'project_form': project_form,
        'skills': skills,
        'academic_background': academic_background,
        'work_experience': work_experience,
        'projects': projects
    })

@login_required
def choose_template(request, template_id):
    template = LaTeXTemplate.objects.get(id=template_id)
    existing_portfolio = Templates.objects.filter(user=request.user, template=template).first()
    
    if existing_portfolio:
        messages.info(request, "You already have a portfolio with this template!")
        return redirect('portfolio:dashboard')
    # Create a new portfolio with the selected template
    new_portfolio = Templates(
        user=request.user,
        template=template,
    )
    new_portfolio.save()
    
    messages.success(request, f"Portfolio created with template: {template.name}")
    return redirect('portfolio:dashboard')

@login_required
def generate_portfolio_tex(request, template_id):
    portfolio = get_object_or_404(UserPortfolio, user=request.user)
    template = get_object_or_404(LaTeXTemplate, id=template_id)

    # Read the LaTeX content from the template file
    with open(template.template_file.path, 'r') as file:
        latex_code = file.read()

    # Replace placeholders in the LaTeX code with actual user data
    latex_code = latex_code.replace('{{name}}', portfolio.name)
    latex_code = latex_code.replace('{{designation}}', portfolio.designation)
    latex_code = latex_code.replace('{{email}}', portfolio.email)
    latex_code = latex_code.replace('{{phone}}', portfolio.phone)
    latex_code = latex_code.replace('{{short_bio}}', portfolio.short_bio)

    # Create an HTTP response with the LaTeX file
    response = HttpResponse(latex_code, content_type="application/x-latex")
    response['Content-Disposition'] = f'attachment; filename="{portfolio.name}_portfolio.tex"'

    return response
