import os
import subprocess
import tempfile
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse, FileResponse
from .models import UserPortfolio, Skill, AcademicBackground, WorkExperience, Project, LaTeXTemplate, Templates
from .forms import UserPortfolioForm, SkillForm, AcademicBackgroundForm, WorkExperienceForm, ProjectForm, RegisterForm, LoginForm

def landing(request):
    return render(request, "landing.html")

def user_register(request):
    if request.user.is_authenticated:
        return redirect("portfolio:dashboard")
    
    if request.method == "POST":
        form = RegisterForm(request.POST)
        print("Checking..", form.is_valid())
        if form.is_valid():
            user = form.save()
            login(request, user)  
            messages.success(request, "Account created successfully!")
            return redirect("portfolio:dashboard")
        else:
            print(form.errors)
    else:
        form = RegisterForm()

    return render(request, "login.html", {"form": form})

def user_login(request):
    if request.user.is_authenticated: 
        return redirect("portfolio:dashboard")

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
    templates = LaTeXTemplate.objects.all()
    profile, created = UserPortfolio.objects.get_or_create(user=request.user)
    return render(request, "dashboard.html", {"user_templates": user_templates, "templates": templates, "profile": profile})

@login_required
def profile(request):
    user_portfolio, created = UserPortfolio.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        portfolio_form = UserPortfolioForm(request.POST, request.FILES, instance=user_portfolio)
        
        skill_form = SkillForm(request.POST)
        if skill_form.is_valid():
            skill = skill_form.save(commit=False)
            skill.portfolio = user_portfolio
            skill.save()

        academic_form = AcademicBackgroundForm(request.POST)
        if academic_form.is_valid():
            academic = academic_form.save(commit=False)
            academic.portfolio = user_portfolio
            academic.save()

        work_experience_form = WorkExperienceForm(request.POST)
        if work_experience_form.is_valid():
            work_experience = work_experience_form.save(commit=False)
            work_experience.portfolio = user_portfolio
            work_experience.save()

        project_form = ProjectForm(request.POST)
        if project_form.is_valid():
            project = project_form.save(commit=False)
            project.portfolio = user_portfolio
            project.save()

        if portfolio_form.is_valid():
            portfolio_form.save()
        
        return redirect('portfolio:profile')
    else:
        portfolio_form = UserPortfolioForm(instance=user_portfolio)
        skill_form = SkillForm()
        academic_form = AcademicBackgroundForm()
        work_experience_form = WorkExperienceForm()
        project_form = ProjectForm()

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
        'projects': projects,
        'user_info': request.user
    })

def delete_portfolio(request, template_id):
    Templates.objects.filter(user=request.user, template=template_id).delete()
    return redirect('portfolio:dashboard')

@login_required
def choose_template(request, template_id):
    template = LaTeXTemplate.objects.get(id=template_id)
    existing_portfolio = Templates.objects.filter(user=request.user, template=template).first()
    
    if existing_portfolio:
        return redirect('portfolio:dashboard')
    new_portfolio = Templates(
        user=request.user,
        template=template,
    )
    new_portfolio.save()
    
    messages.success(request, f"Portfolio created with template: {template.name}")
    return redirect('portfolio:dashboard')

def generate_pdf_from_latex(latex_content, output_filename="output.pdf"):
    # Create a temporary working directory
    with tempfile.TemporaryDirectory() as working_dir:
        # Create the tex file
        base_name = os.path.splitext(output_filename)[0]
        tex_file = os.path.join(working_dir, f"{base_name}.tex")
        
        with open(tex_file, 'w', encoding='utf-8') as f:
            f.write(latex_content)
        
        # Run pdflatex (twice to resolve references)
        for _ in range(2):
            process = subprocess.Popen(
                ['pdflatex', '-interaction=nonstopmode', tex_file],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                cwd=working_dir
            )
            stdout, stderr = process.communicate()
            
            if process.returncode != 0:
                # Log the full output for debugging
                print("LaTeX compilation failed with the following output:")
                print(stdout.decode('utf-8'))
                print(stderr.decode('utf-8'))
                raise Exception(f"LaTeX compilation failed: {stdout.decode('utf-8')}\n{stderr.decode('utf-8')}")
        
        # Return the path to the generated PDF
        pdf_path = os.path.join(working_dir, f"{base_name}.pdf")
        
        if not os.path.exists(pdf_path):
            raise Exception("PDF generation failed")
            
        # Copy the PDF to a permanent location
        final_path = os.path.join(os.getcwd(), output_filename)
        with open(pdf_path, 'rb') as src, open(final_path, 'wb') as dst:
            dst.write(src.read())
            
        return final_path
    
def escape_latex(text):
    # Escape special LaTeX characters
    special_chars = {
        '&': r'\&',
        '%': r'\%',
        '$': r'\$',
        '#': r'\#',
        '_': r'\_',
        '{': r'\{',
        '}': r'\}',
        '~': r'\textasciitilde{}',
        '^': r'\textasciicircum{}',
        '\\': r'\textbackslash{}',
    }
    for char, escaped_char in special_chars.items():
        text = text.replace(char, escaped_char)
    return text

# Testing the templates
@login_required
def generate_portfolio_pdf(request, template_id):
    """Generate a PDF from the user's portfolio and selected template and download it"""
    portfolio = get_object_or_404(UserPortfolio, user=request.user)
    
    # Get the selected template
    user_template = get_object_or_404(LaTeXTemplate, id=template_id)
    
    latex_template = user_template
    
    # Replace placeholders with user data
    def escape_latex(text):
        return text.replace('&', '\\&').replace('%', '\\%').replace('_', '\\_')
    
    template_content = latex_template.template_file
    template_content = template_content.replace('$name$', escape_latex(portfolio.name))
    template_content = template_content.replace('$designation$', escape_latex(portfolio.designation))
    template_content = template_content.replace('$email$', escape_latex(portfolio.email))
    template_content = template_content.replace('$phone$', escape_latex(portfolio.phone))
    template_content = template_content.replace('$short_bio$', escape_latex(portfolio.short_bio))
    
    # Handle profile photo
    if portfolio.profile_photo:
        profile_photo_path = portfolio.profile_photo.path
        template_content = template_content.replace('$profile_photo_path$', profile_photo_path)
    else:
        template_content = template_content.replace('$profile_photo_path$', "placeholder.jpg")
    
    # Handle skills
    skills_list = " \\\\ \n".join(escape_latex(skill.skill_name) for skill in portfolio.skills.all())
    template_content = template_content.replace('$skills_list$', skills_list)
    
    # Handle education
    education_list = "\n".join(f"\\subsection*{{{escape_latex(edu.institute)}}}\n{escape_latex(edu.degree)} | {edu.year_of_graduation} | GPA: {edu.grade if edu.grade else ''}" for edu in portfolio.academic_background.all())
    template_content = template_content.replace('$education_list$', education_list)
    
    # Handle work experience
    work_experience_list = "\n".join(f"\\subsection*{{{escape_latex(exp.company_name)}}}\n{exp.job_duration}\n\n{escape_latex(exp.job_responsibilities)}" for exp in portfolio.work_experience.all())
    template_content = template_content.replace('$work_experience_list$', work_experience_list)
    
    # Handle projects
    projects_list = "\n".join(f"\\subsection*{{{escape_latex(project.project_name)}}}\n{escape_latex(project.project_description)}" for project in portfolio.projects.all())
    template_content = template_content.replace('$projects_list$', projects_list)
    
    print("\n\n\nGoing to generate")
    # Generate PDF
    try:
        pdf_path = generate_pdf_from_latex(template_content, f"portfolio_{portfolio.id}.pdf")
        print("Generated\n\n")
        pdf_filename = f"{portfolio.name}_portfolio.pdf"
        # Return the PDF as a downloadable file
        response = FileResponse(open(pdf_path, 'rb'), content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{pdf_filename}"'

        # Clean up the temporary PDF file
        os.remove(pdf_path)
        return response
    except Exception as e:
        return HttpResponse(f"Error generating PDF: {str(e)}", status=500)
