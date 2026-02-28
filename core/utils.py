from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def send_contact_notification(contact_message):
    """Send email notification for new contact message"""
    subject = f"New Contact Message: {contact_message.subject}"
    
    # Email to admin
    admin_html_message = render_to_string('emails/contact_admin.html', {
        'message': contact_message
    })
    admin_plain_message = strip_tags(admin_html_message)
    
    send_mail(
        subject,
        admin_plain_message,
        settings.DEFAULT_FROM_EMAIL,
        [settings.ADMIN_EMAIL],
        fail_silently=False,
        html_message=admin_html_message
    )
    
    # Auto-reply to user
    user_html_message = render_to_string('emails/contact_user.html', {
        'name': contact_message.name
    })
    user_plain_message = strip_tags(user_html_message)
    
    send_mail(
        "Thank you for contacting me!",
        user_plain_message,
        settings.DEFAULT_FROM_EMAIL,
        [contact_message.email],
        fail_silently=False,
        html_message=user_html_message
    )