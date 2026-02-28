import logging
import traceback
from django.http import JsonResponse
from django.conf import settings

logger = logging.getLogger('django')

class StrongBackendMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            response = self.get_response(request)
            return response
        except Exception as e:
            # Log the error with full traceback
            logger.error(f"Global Exception caught: {str(e)}\n{traceback.format_exc()}")
            
            if settings.DEBUG:
                # In debug mode, let Django show the error
                raise e
            
            # In production, return a clean JSON or a friendly message
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest' or 'api' in request.path:
                return JsonResponse({
                    'success': False,
                    'message': 'A critical system error occurred. Our engineers have been notified.'
                }, status=500)
            
            # For standard requests, let it fall back to 500.html (which we should create)
            raise e
