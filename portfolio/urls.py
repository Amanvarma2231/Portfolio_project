from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
]

# Custom Admin Branding
admin.site.site_header = getattr(settings, 'ADMIN_SITE_HEADER', "Aman Varma Admin")
admin.site.site_title = getattr(settings, 'ADMIN_SITE_TITLE', "Portfolio Management")
admin.site.index_title = getattr(settings, 'ADMIN_INDEX_TITLE', "Control Center")

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)