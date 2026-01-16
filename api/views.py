"""
API views for the application.
"""
from django.http import JsonResponse


def health_check(request):
    """
    Health check endpoint to verify the API is running.
    """
    return JsonResponse({
        'status': 'healthy',
        'service': 'django-api'
    })

