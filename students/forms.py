from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model  = Student
        fields = ['name', 'email', 'course_interest', 'status']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Full Name',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email Address',
            }),
            'course_interest': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. Python, Data Science, Web Dev',
            }),
            'status': forms.Select(attrs={
                'class': 'form-select',
            }),
        }
        labels = {
            'course_interest': 'Course Interest',
        }
