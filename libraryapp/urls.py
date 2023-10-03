from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name="Home"),
    path('login/', views.login, name="Login"),
    path('about/', views.about, name="About"),
    path('admin/', views.admin_homepage, name='admin_homepage'),
    path('student/', views.student_homepage, name='student_homepage'),
    path('staff/', views.staff_homepage, name='staff_homepage'),
    path('studentreg/', views.studentreg, name='student registration'),
    path('staffreg/', views.staffreg, name='staff registration'),

]
#from django.contrib import admin
#from django.urls import path
#from .import views

#urlpatterns = [
 #   path('', views.index, name="Home"),
  #  path('login/',views.login, name="Login"),
   # path('about/',views.about, name="About"),
#    path('admin/', views.admin_homepage, name='admin_homepage'),
 #   path('student/', views.student_homepage, name='student_homepage'),
  #  path('staff/', views.staff_homepage, name='staff_homepage'),
#]