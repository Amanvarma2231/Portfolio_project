from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from .models import Project, Experience, ContactMessage
from .forms import ContactForm
from .utils import send_contact_notification
from .resume_data import RESUME_DATA, EDUCATION, CERTIFICATES
import logging

logger = logging.getLogger('django')

def home(request):
    """
    Refined Home View: Professional data management and robust error handling.
    """
    contact_form = ContactForm()
    
    if request.method == 'POST':
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            form = ContactForm(request.POST)
            if form.is_valid():
                message = form.save()
                logger.info(f"Contact form submitted by {message.email}")
                
                # Send notifications
                try:
                    send_contact_notification(message)
                except Exception as e:
                    logger.error(f"Email sending failed for contact message from {message.email}: {e}")
                
                return JsonResponse({
                    'success': True, 
                    'message': 'Thank you! Your message has been received securely.'
                })
            else:
                logger.warning(f"Contact form validation failed: {form.errors.as_json()}")
                return JsonResponse({'success': False, 'errors': form.errors}, status=400)
        else: # Non-AJAX POST request
            form = ContactForm(request.POST)
            if form.is_valid():
                contact_message = form.save()
                logger.info(f"Contact form submitted by {contact_message.email} (non-AJAX)")
                try:
                    send_contact_notification(contact_message)
                except Exception as e:
                    logger.error(f"Email sending failed for contact message from {contact_message.email}: {e}")
                messages.success(request, 'Thank you for your message! I will get back to you soon.')
                return redirect('home')
            else:
                logger.warning(f"Contact form validation failed (non-AJAX): {form.errors.as_json()}")
                messages.error(request, 'Please correct the errors below.')
    
    # Process projects for template
    projects_list = []
    projects = Project.objects.all().order_by('-created_at')
    for p in projects:
        # Clean technologies list
        techs = [t.strip().strip(',') for t in p.technologies.replace(',', ' ').split() if t.strip()]
        projects_list.append({
            'title': p.title,
            'description': p.description,
            'technologies_list': techs,
            'image_url': p.image_url,
            'github_link': p.github_link,
            'live_link': p.live_link,
            'duration': p.duration,
        })
    
    # Process experiences for template
    experiences_list = []
    experiences = Experience.objects.all().order_by('-id')
    for exp in experiences:
        skills = [s.strip().strip(',') for s in exp.skills_used.replace(',', ' ').split() if s.strip()]
        experiences_list.append({
            'company': exp.company,
            'position': exp.position,
            'duration': exp.duration,
            'description': exp.description,
            'skills_list': skills,
        })
    
    context = {
        'resume': RESUME_DATA,
        'projects': projects_list,
        'programming_skills': RESUME_DATA['skill_levels']['programming_skills'],
        'database_skills': RESUME_DATA['skill_levels']['database_skills'],
        'education': EDUCATION,
        'certificates': CERTIFICATES,
        'experiences': experiences_list,
        'contact_form': contact_form,
    }
    return render(request, 'home.html', context)

def add_image_url(request, project_id):
    """
    Quickly add an image URL to a project.
    """
    from django.shortcuts import get_object_or_404
    if request.method == 'POST':
        project = get_object_or_404(Project, id=project_id)
        image_url = request.POST.get('image_url')
        if image_url:
            project.image_url = image_url
            project.save()
            return JsonResponse({'success': True, 'message': 'Image updated successfully'})
    return JsonResponse({'success': False, 'message': 'Invalid request'}, status=400)
