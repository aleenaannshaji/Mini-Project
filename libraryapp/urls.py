#from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name="Home"),
    path('login/', views.login_view, name="login"),
    path('about/', views.about, name="About"),
    path('adminpage/', views.adminhomepage, name='adminpage'),
    path('student/', views.student_homepage, name='student'),
    path('staff/', views.staff_homepage, name='staff'),
    path('studentreg/', views.student_registration, name='student_registration'),
    path('staffreg/', views.staff_registration, name='staff_registration'),
    path('registration_success/', views.registration_success, name='registration_success'),
  #  path('user/', views.user_homepage, name='user_homepage'),
    path('logout/', views.logout_view, name='logout'),
]