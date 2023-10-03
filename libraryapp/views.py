from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.views.generic import UpdateView

# Create your views here.
def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def about(request):
    return render(request, 'about.html')    

def admin_homepage(request):
    return render(request, 'admin_homepage.html')  

def student_homepage(request):
    return render(request, 'studenthome.html')  

def staff_homepage(request):
    return render(request, 'staffhome.html')  

def user_homepage(request):
    user = request.user
    if user.user_type == "admin":
        return redirect('admin_homepage')
    elif user.user_type == "student":
        return redirect('student_homepage')
    elif user.user_type == "staff":
        return redirect('staff_homepage')
    else:
        # Handle invalid user types
        return HttpResponse("Invalid user type")


def studentreg(request):
    return render(request, 'studentreg.html')         

def staffreg(request):
    return render(request, 'staffreg.html')    




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