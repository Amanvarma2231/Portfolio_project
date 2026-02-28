from django import forms
from .models import ContactMessage, Project, Experience

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Message', 'rows': 5}),
        }

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'technologies', 'image_url', 'github_link', 'live_link', 'duration']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'technologies': forms.TextInput(attrs={'class': 'form-control'}),
            'image_url': forms.TextInput(attrs={'class': 'form-control'}),
            'github_link': forms.URLInput(attrs={'class': 'form-control'}),
            'live_link': forms.URLInput(attrs={'class': 'form-control'}),
            'duration': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Jan 2026 - Mar 2026'}),
        }

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['company', 'position', 'duration', 'description', 'skills_used']
        widgets = {
            'company': forms.TextInput(attrs={'class': 'form-control bg-dark text-white border-secondary', 'placeholder': 'Company Name'}),
            'position': forms.TextInput(attrs={'class': 'form-control bg-dark text-white border-secondary', 'placeholder': 'Your Role'}),
            'duration': forms.TextInput(attrs={'class': 'form-control bg-dark text-white border-secondary', 'placeholder': 'e.g. Jan 2025 - Present'}),
            'description': forms.Textarea(attrs={'class': 'form-control bg-dark text-white border-secondary', 'placeholder': 'Describe your work...', 'rows': 4}),
            'skills_used': forms.TextInput(attrs={'class': 'form-control bg-dark text-white border-secondary', 'placeholder': 'Python, Flask, etc.'}),
        }
