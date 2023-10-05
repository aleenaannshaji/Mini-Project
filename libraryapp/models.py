from django.db import models
from django.core.validators import RegexValidator
from datetime import datetime



# Create your models here.


class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    user_type = models.CharField(max_length=10)  # You can use choices for 'admin', 'student', 'staff', etc.

    # Add more fields as needed

    def __str__(self):
        return self.email


class Studentreg(models.Model):
    student_id = models.IntegerField("Student Id", primary_key=True)
    student_name = models.CharField("Student Name", max_length=25)
    dob = models.DateField("Date Of Birth")
    address = models.CharField("Address", max_length=50)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,12}$', message="Phone number must be entered in the format: ' +91 '. Up to 12 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=25, blank=False, default="")
    p_id = models.ForeignKey('Program', on_delete=models.CASCADE)
    d_id = models.ForeignKey('Department', on_delete=models.CASCADE)
    email = models.EmailField("Email", blank=False)
    pwd = models.CharField("Password", max_length=25, blank=False)
    pic = models.ImageField(upload_to='images/')


class Staffreg(models.Model):
    staff_id = models.IntegerField("STAFF ID",primary_key=True)
    staff_name = models.CharField("STAFF NAME",max_length=25)
    dob = models.DateField("DATE OF BIRTH")
    address = models.CharField("ADDRESS",max_length=50)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,12}$', message="Phone number must be entered in the format: ' +91 '. Up to 12 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=25, blank=False, default="")
    des_id = models.ForeignKey('Designation', on_delete=models.CASCADE)
    email = models.EmailField("EMAIL", blank=False)
    pwd = models.CharField("PASSWORD",max_length=25, blank=False)
    pic = models.ImageField(upload_to='images/')    


class Program(models.Model):
   p_id = models.IntegerField("Program id",primary_key = True)
   program = models.CharField("Program", max_length = 50)


class Department(models.Model):
   d_id = models.IntegerField("Department Id",primary_key = True)
   department = models.CharField("Department", max_length = 50)
   

class Designation(models.Model):
    des_id = models.IntegerField("Designation Id",primary_key = True)
    designation = models.CharField("Designation", max_length = 50)