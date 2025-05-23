# streamapp/middleware.py
from django.conf import settings
from django.utils.deprecation import MiddlewareMixin

class MediaCORSHeadersMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        if request.path.startswith(settings.MEDIA_URL):
            response["Access-Control-Allow-Origin"] = "*"  # aap yahan frontend ka URL bhi de sakte ho, "*" sabko allow karta hai
            response["Access-Control-Allow-Methods"] = "GET, OPTIONS"
            response["Access-Control-Allow-Headers"] = "Origin, Content-Type, Accept"
        return response
