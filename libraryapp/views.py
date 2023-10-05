from django.shortcuts import render, redirect
from .forms import StudentRegistrationForm, StaffRegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages


#from django.views.generic import UpdateView


def logout_view(request):
    # Log the user out by calling the logout() function
    logout(request)
    # Redirect the user to a login page or any other page you prefer
    return redirect('login.html')  # Replace 'login' with the name of your login page URL pattern



def student_registration(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # Add logic to send success alert
            return redirect('registration_success')  # Redirect to success page
    else:
        form = StudentRegistrationForm()
    return render(request, 'studentreg.html', {'form': form})


def staff_registration(request):
    if request.method == 'POST':
        form = StaffRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # Add logic to send success alert
            return redirect('registration_success')  # Redirect to success page
    else:
        form = StaffRegistrationForm()
    return render(request, 'staffreg.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        # Validate email format
        valid_email_formats = ['@mca.ajce.in', '@intmca.ajce.in', '@cs.ajce.in', 'admin@amaljyothi.ac.in']
        if not any(email.endswith(format) for format in valid_email_formats):
            messages.error(request, 'Invalid email format')
            return redirect('login')
        
        # Validate password complexity (minimum 8 characters, one special character, one digit, one alphabet)
        if len(password) < 8 or not any(char.isalpha() for char in password) \
            or not any(char.isdigit() for char in password) \
            or not any(char in '!@#$%^&*()-_+=<>?' for char in password):
            messages.error(request, 'Invalid password format')
            return redirect('login')
        
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            # Redirect to the respective homepage based on email format
            if email == 'admin@amaljyothi.ac.in':
                print("Admin login successful")  # Debug print
                return redirect('adminhomepage')  # Assuming you have a 'admin_homepage' URL pattern
            elif email.endswith('@amaljyothi.ac.in'):
                print("Staff login successful")  # Debug print
                return redirect('staff_homepage')  # Assuming you have a 'staff_homepage' URL pattern
            else:
                print("Student login successful")  # Debug print
                return redirect('student_homepage')  # Assuming you have a 'student_homepage' URL pattern
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    
    return render(request, 'login.html')



def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def about(request):
    return render(request, 'about.html')    

def adminhomepage(request):
    return render(request, 'adminhomepage.html')  

def student_homepage(request):
    return render(request, 'studenthome.html')  

def staff_homepage(request):
    return render(request, 'staffhome.html')  

def registration_success(request):
    return render(request, 'regsuccess.html')

def studentreg(request):
   return render(request, 'studentreg.html')         

def staffreg(request):
    return render(request, 'staffreg.html') 


#def user_homepage(request):
#    user = request.user
#    if user.user_type == "admin":
#        return redirect('admin_homepage')
#    elif user.user_type == "student":
#        return redirect('student_homepage')
#    elif user.user_type == "staff":
#        return redirect('staff_homepage')
#    else:
        # Handle invalid user types
#        return HttpResponse("Invalid user type")




#class EditProfile(UpdateView):
#    model = Studentreg
#    fields = ['name','pic','address','phone_number','email']
#    success_url = '/'

#def student_profile(request):
#    studrec = Studentreg.objects.filter(id=request.session['id'])
#    return render(request, 'Student_profile.html', {'studrec':studrec})

#class EditProfile(UpdateView):
#    model = Staffreg
#    fields = ['name','pic','address','phone_number','email']
#    success_url = '/'

#def staff_profile(request):
#    staffrec = Staffreg.objects.filter(sid=request.session['id'])
#    return render(request, 'Staff_profile.html', {'staffrec':staffrec})   