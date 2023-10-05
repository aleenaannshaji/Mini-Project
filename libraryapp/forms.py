
from django import forms
from .models import Studentreg, Staffreg

class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = Studentreg
        fields = '__all__'  # You can customize this as needed

class StaffRegistrationForm(forms.ModelForm):
    class Meta:
        model = Staffreg
        fields = '__all__'  # You can customize this as needed
