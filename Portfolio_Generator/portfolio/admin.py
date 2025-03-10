from django.contrib import admin
from .models import LaTeXTemplate, UserPortfolio

# Register LaTeXTemplate model to make it available in the admin panel
admin.site.register(LaTeXTemplate)
admin.site.register(UserPortfolio)
