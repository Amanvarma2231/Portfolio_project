from django.contrib import admin
from .models import Project, Experience, ContactMessage

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'duration', 'created_at', 'has_image')
    list_filter = ('created_at',)
    search_fields = ('title', 'description', 'technologies')
    ordering = ('-created_at',)
    
    @admin.display(boolean=True, description='Has Image')
    def has_image(self, obj):
        return bool(obj.image_url)

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('position', 'company', 'duration')
    search_fields = ('position', 'company', 'description')

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at', 'is_read')
    list_filter = ('is_read', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('created_at',)
    actions = ['mark_as_read', 'mark_as_unread']
    
    @admin.action(description="Mark selected messages as read")
    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)
    
    @admin.action(description="Mark selected messages as unread")
    def mark_as_unread(self, request, queryset):
        queryset.update(is_read=False)