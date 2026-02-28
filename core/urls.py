from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/add-image/<int:project_id>/', views.add_image_url, name='add_image_url'),
]