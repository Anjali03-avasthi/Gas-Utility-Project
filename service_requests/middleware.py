from django.shortcuts import redirect
from django.urls import resolve

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        allowed_urls = ['login']
        if not request.session.get('user_id') and resolve(request.path_info).url_name not in allowed_urls:
            return redirect('/login/')
        return self.get_response(request)
