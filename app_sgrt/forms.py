from django import forms
from .models import Customer, Job, Candidate

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'website', 'address', 'phone', 'representative_name']

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['name', 'status', 'customer', 'description', 'location']

class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = ['first_name', 'last_name', 'email', 'skills']