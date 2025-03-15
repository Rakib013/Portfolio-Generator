from django.db import models
from django.contrib.auth.models import User

class LaTeXTemplate(models.Model):
    name = models.CharField(max_length=255)
    template_file = models.TextField(blank=True)
    preview_image = models.ImageField(upload_to="template_previews/", null=True, blank=True)

    def __str__(self):
        return self.name

class UserPortfolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    profile_photo = models.ImageField(upload_to="portfolio_photos/", null=True, blank=True)
    short_bio = models.TextField(blank=True)
    pdf_file = models.FileField(upload_to="generated_pdfs/", null=True, blank=True)  # PDF Storage

    def __str__(self):
        return f"{self.user.username}"
        
class Templates(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    template = models.ForeignKey(LaTeXTemplate, on_delete=models.SET_NULL, null=True, blank=True)
    selected_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.template.name if self.template else 'No Template'}"

class Skill(models.Model):
    portfolio = models.ForeignKey(UserPortfolio, on_delete=models.CASCADE, related_name="skills")
    skill_name = models.CharField(max_length=255)

    def __str__(self):
        return self.skill_name

class AcademicBackground(models.Model):
    portfolio = models.ForeignKey(UserPortfolio, on_delete=models.CASCADE, related_name="academic_background")
    institute = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    year_of_graduation = models.CharField(max_length=10)
    grade = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.degree} - {self.institute}"

class WorkExperience(models.Model):
    portfolio = models.ForeignKey(UserPortfolio, on_delete=models.CASCADE, related_name="work_experience")
    company_name = models.CharField(max_length=255)
    job_duration = models.CharField(max_length=100)
    job_responsibilities = models.TextField()

    def __str__(self):
        return f"{self.company_name} ({self.job_duration})"

class Project(models.Model):
    portfolio = models.ForeignKey(UserPortfolio, on_delete=models.CASCADE, related_name="projects")
    project_name = models.CharField(max_length=255)
    project_description = models.TextField()

    def __str__(self):
        return self.project_name
