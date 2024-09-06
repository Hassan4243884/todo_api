from rest_framework.views import exception_handler
from rest_framework.exceptions import NotFound, ValidationError, PermissionDenied
from django.http import JsonResponse


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first
    response = exception_handler(exc, context)

    if response is None:
        if isinstance(exc, NotFound):
            return JsonResponse({"error": "Resource not found"}, status=404)
        elif isinstance(exc, ValidationError):
            return JsonResponse(
                {"error": "Validation error", "details": exc.detail}, status=400
            )
        elif isinstance(exc, PermissionDenied):
            return JsonResponse({"error": "Permission denied"}, status=403)
        elif isinstance(exc, Exception):
            return JsonResponse({"error": "Internal Server Error"}, status=500)

    # Return the default response
    return response
