from django.db import models
from django.core.validators import URLValidator

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technologies = models.CharField(max_length=300)
    image_url = models.CharField(max_length=500, blank=True, null=True)
    github_link = models.URLField(validators=[URLValidator()], blank=True, null=True)
    live_link = models.URLField(validators=[URLValidator()], blank=True, null=True)
    duration = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class Experience(models.Model):
    company = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    duration = models.CharField(max_length=100)
    description = models.TextField()
    skills_used = models.CharField(max_length=300)
    
    class Meta:
        verbose_name_plural = "Experiences"
        ordering = ['-duration'] # Fallback ordering

    def __str__(self):
        return f"{self.position} at {self.company}"

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Message from {self.name} - {self.subject}"