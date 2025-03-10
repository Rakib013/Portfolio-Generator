from django.urls import path
from . import views

app_name = 'portfolio' 

urlpatterns = [
    path('login/', views.user_login, name='user_login'),
    path('register/', views.user_register, name='user_register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('templates/', views.template_list, name='template_list'),
    path('choose_template/<int:template_id>/', views.choose_template, name='choose_template'),
    path('download/<int:template_id>/', views.generate_portfolio_tex, name='generate_pdf'),
]