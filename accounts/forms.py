from django import forms
from accounts.models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['User_Name','Email','Password']