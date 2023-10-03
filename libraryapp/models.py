from django.db import models
from django.core.validators import RegexValidator
from datetime import date

# Create your models here.

class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    user_type = models.CharField(max_length=10)  # You can use choices for 'admin', 'student', 'staff', etc.

    # Add more fields as needed

    def __str__(self):
        return self.email

class Studentreg(models.Model):
    student_id = models.IntegerField("STUDENT ID",primary_key=True)
    student_name = models.CharField("STUDENT NAME",max_length=25)
    dob = models.DateField("DATE OF BIRTH")
    address = models.CharField("ADDRESS",max_length=50)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,12}$', message="Phone number must be entered in the format: ' +91 '. Up to 12 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=25, blank=False)
    program = models.CharField("PROGRAM",max_length=25)
    department = models.Model("DEPARTMENT",max_length=25)
    email = models.EmailField("EMAIL", blank=False)
    pwd = models.CharField("PASSWORD",max_length=25, blank=False)
    pic = models.ImageField(upload_to='images/')

class Staffreg(models.Model):
    staff_id = models.IntegerField("STAFF ID",primary_key=True)
    staff_name = models.CharField("STAFF NAME",max_length=25)
    dob = models.DateField("DATE OF BIRTH")
    address = models.CharField("ADDRESS",max_length=50)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,12}$', message="Phone number must be entered in the format: ' +91 '. Up to 12 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=25, blank=False)
    designation = models.Model("DESIGNATION",max_length=25)
    email = models.EmailField("EMAIL", blank=False)
    pwd = models.CharField("PASSWORD",max_length=25, blank=False)
    pic = models.ImageField(upload_to='images/')    

class Designation(models.Model):
    did = models.IntegerField("ID", primary_key=True)
    designation = models.CharField("DESIGNATION", max_length=25)   

class Program(models.Model):
    pid = models.IntegerField("Program Id", primary_key=True)
    program = models.CharField("PROGRAM", max_length=25)

class Department(models.Model):
    deptid = models.IntegerField("DEPARTMENT ID", primary_key=True)
    Department = models.CharField("DEPARTMENT", max_length=25)