import json
from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin
import traceback

class CustomExceptionMiddleware(MiddlewareMixin):
    def process_exception(self, request, exception):
       
        traceback.print_exc()
        data = {
            "detail": str(exception)
        }
        return JsonResponse(data, status=500)
