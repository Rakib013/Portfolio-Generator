from django.urls import path
from . import views

app_name = 'portfolio' 

urlpatterns = [
    path('', views.landing, name='landing'),
    path('login/', views.user_login, name='user_login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('choose_template/<int:template_id>/', views.choose_template, name='choose_template'),
    path('download/<int:template_id>/', views.generate_portfolio_pdf, name='generate_pdf'),
    path('delete/<int:template_id>/', views.delete_portfolio, name='delete_portfolio'),
]